import os
import sys
import pprint

ROOT_FOLDER = "/home/ldulling/events/Cloudflight_Coding_Contest/2024_10"
# from CCC import ROOT_FOLDER
sys.path.append(ROOT_FOLDER)
from file_handler import FileHandler, File  # type: ignore


def algorithm(input: str) -> str:
    x, y, amount = (int(i) for i in input.split())
    t_in_row = x // 3
    leftover_col_idx = x - x % 3

    res = ""

    room = [["." for _ in range(x)] for _ in range(y)]

    row = 0
    while (row + 2) < y:
        col = 0
        while col < x:
            room[row][col] = "X"
            room[row + 1][col] = "X"
            room[row + 2][col] = "X"
            col += 2
        row += 4

    while row < y:
        col = 0
        while (col + 2) < x:
            room[row][col] = "X"
            room[row][col + 1] = "X"
            room[row][col + 2] = "X"
            col += 4
        row += 2


    for line in room:
        res += "".join(line) + "\n"

    # for i in range(1, amount + 1, t_in_row):
    #     for j in range(t_in_row):
    #         room[i][j] =
    #         line += [str(i + j)] * 3
    #     res += " ".join(line) + "\n"

    # pprint.pprint(room)
    return res

handler = FileHandler("/home/ldulling/events/Cloudflight_Coding_Contest/2024_10/level4", skip_lines=1)
# handler.test(algorithm)
handler.process_all_files(algorithm, test=False)
