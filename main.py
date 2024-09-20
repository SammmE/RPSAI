import os
from typing import List, Tuple

data_key = {"s": 1, "x": 2, "p": 3}


def read_data() -> List[List[List[str]]]:
    """Return the data from the initial data file as a list of lists of lists of strings (dataframes would not be useful here)"""

    # data is stored with: 's' -> rock, 'x' ->, 'p' -> paper and '-' the end of a game.
    # for our purposes, we will convert this to 1, 2, and 3 respectively. We will also remove the '-' characters. and store them in an array

    data: List[List[Tuple[int, int]]] = []

    game: List[Tuple[int, int]] = []
    for i, line in enumerate(open("data/initial_data.txt", "r")):
        if line == "-\n":
            data.append(game)
            game = []
        else:
            game.append((data_key[line[0]], data_key[line[1]]))

    return data


if __name__ == "__main__":
    if not os.path.exists("data/initial_data.txt"):
        print("Data file not found")
        os._exit(1)

    print(read_data())
