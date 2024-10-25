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

    room = [["0" for _ in range(x)] for _ in range(y)]

    i = 1
    for row in range(y):
        for col in range(0, x, 3):
            if col + 3 <= x and i <= amount:
                for _ in range(3):
                    room[row][col + _] = str(i)
                i += 1

    if leftover_col_idx != x:
        for col in range(leftover_col_idx, x):
            for row in range(0, y, 3):
                if row + 3 <= y and i <= amount:
                    for _ in range(3):
                        room[row + _][col] = str(i)
                    i += 1


    for line in room:
        res += " ".join(line) + "\n"

    # for i in range(1, amount + 1, t_in_row):
    #     for j in range(t_in_row):
    #         room[i][j] =
    #         line += [str(i + j)] * 3
    #     res += " ".join(line) + "\n"


    return res

handler = FileHandler("/home/ldulling/events/Cloudflight_Coding_Contest/2024_10/level3", skip_lines=1)
# handler.test(algorithm)
handler.process_all_files(algorithm, test=False)
