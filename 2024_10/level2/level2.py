import os
import sys

ROOT_FOLDER = "/home/ldulling/events/Cloudflight_Coding_Contest/2024_10"
# from CCC import ROOT_FOLDER
sys.path.append(ROOT_FOLDER)
from file_handler import FileHandler, File  # type: ignore


def algorithm(input: str) -> str:
    x, y, amount = (int(i) for i in input.split())
    t_in_row = x // 3

    res = ""



    for i in range(1, amount + 1, t_in_row):
        line = []
        for j in range(t_in_row):
            line += [str(i + j)] * 3
        res += " ".join(line) + "\n"


    return res

handler = FileHandler("/home/ldulling/events/Cloudflight_Coding_Contest/2024_10/level2", skip_lines=1)
# handler.test(algorithm)
handler.process_all_files(algorithm, test=False)
