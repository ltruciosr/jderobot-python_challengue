import random


class Cell:
    def __init__(self, is_alive=False):
        if is_alive:
            self.status = 1
        else:
            self.status = 0

    def set_dead(self):
        self.status = 0

    def set_alive(self):
        self.status = 1

    def is_alive(self):
        """
        returns True if it is alive, False if not.
        """
        if self.status == 1:
            return True
        else:
            return False

    def character(self):
        """
        method returning a status character of our choice to print on the board
        """
        if self.is_alive():
            return "[*]"
        return "[ ]"


class Board:
    def __init__(self, rows, columns, live_probability=0.3, seed=0):
        """
        class Board
        constructor holding rows, cols, live probability and random seed
        constructor generates a grid board filled by Cells.
        """
        self.live_probability = live_probability
        self.seed = seed
        self.rows = rows
        self.columns = columns
        self.grid = [
            [Cell() for column_cells in range(self.columns)]
            for row_cells in range(self.rows)
        ]

        self.generate_board()

    def draw_board(self):
        """
        method to draw a board in CLI, the symbol is defined in class Cell
        """
        print("\n" * 10)
        print("-PRINTING BOARD-")
        for row in self.grid:
            for column in row:
                print(column.character(), end="")
            print()  # to create a new line

    def generate_board(self):
        """
        method which initialize board cells to either alive or dead
        """
        random.seed(self.seed)
        for row in self.grid:
            for column in row:
                probability = random.random()
                if self.live_probability > probability:
                    column.set_alive()

    def get_alives_count(self):
        alives_count = 0
        for row in self.grid:
            for column in row:
                if column.is_alive():
                    alives_count += 1

        return alives_count

    def is_valid_cell(self, row, column):
        valid_cell = True

        if (row) < 0 or (row) >= self.rows:
            valid_cell = False
        if (column) < 0 or (column) >= self.columns:
            valid_cell = False

        return valid_cell

    def check_neighbour(self, check_row, check_column, kernel=3):
        # define search kernel
        search_min = (int)((1 - kernel) / 2)
        search_max = (int)((kernel - 1) / 2 + 1)

        # append valid cells
        neighbour_list = []
        for row in range(search_min, search_max):
            for column in range(search_min, search_max):
                if row == column == 0:
                    continue

                neighbour_row = check_row + row
                neighbour_column = check_column + column

                if self.is_valid_cell(neighbour_row, neighbour_column):
                    neighbour_list.append(self.grid[neighbour_row][neighbour_column])

        return neighbour_list

    def update_board(self):
        # print("-UPDATING BOARD-")
        goes_alive = []
        gets_killed = []

        for row in range(len(self.grid)):
            for column in range(len(self.grid[row])):
                # check neighbour:
                kernel = 3
                check_neighbour = self.check_neighbour(row, column, kernel)

                living_neighbours_count = 0

                for neighbour_cell in check_neighbour:
                    # check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count += 1

                main_cell = self.grid[row][column]

                # If the cell is alive, check the neighbour status.
                if main_cell.is_alive():
                    if living_neighbours_count < 2 or living_neighbours_count > 3:
                        gets_killed.append(main_cell)

                    else:
                        goes_alive.append(main_cell)

                else:
                    if living_neighbours_count == 3:
                        goes_alive.append(main_cell)

        # update board status
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()