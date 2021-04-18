import yaml
from board.tools import Board


def life_game():
    with open("board_setup.yaml", "r") as stream:
        try:
            board_param = yaml.safe_load(stream)
            print(board_param)
        except yaml.YAMLError as exc:
            print(exc)

    # set size
    rows = board_param["rows"]
    columns = board_param["columns"]

    # create a board:
    live_probability = board_param["live_probability"]
    random_seed = board_param["random_seed"]

    BoardObj = Board(rows, columns, live_probability, random_seed)

    # print board initialization
    BoardObj.draw_board()

    action = ""
    while action != "q":
        action = input("Press enter to add generation or q to quit:")

        if action == "":
            BoardObj.update_board()
            BoardObj.draw_board()


if __name__ == "__main__":
    life_game()