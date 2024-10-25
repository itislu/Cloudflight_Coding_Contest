import os
import sys

ROOT_FOLDER = "/home/ldulling/events/Cloudflight_Coding_Contest/2024_10"
# from CCC import ROOT_FOLDER
sys.path.append(ROOT_FOLDER)
from file_handler import FileHandler, File  # type: ignore


def algorithm(input: str):
    x, y = input.split()
    return str(int(x) * int(y) // 3)

handler = FileHandler("/home/ldulling/events/Cloudflight_Coding_Contest/2024_10/level1", skip_lines=1)
# handler.test(algorithm)
handler.process_all_files(algorithm, test=False)
