import os
import sys

ROOT_FOLDER = os.path.dirname(os.path.abspath(f"{__file__}/../.."))
# from CCC import ROOT_FOLDER
sys.path.append(ROOT_FOLDER)
from file_handler import FileHandler, File  # type: ignore


WIN = {
    "R": "S",
    "S": "P",
    "P": "R",
}


def winner(l: str, r: str) -> str:
    return l if WIN[l] == r else r


def algorithm(input: str) -> str:
    round = input
    for _ in range(2):
        tmp = ""
        i = 0
        while i < len(round):
            tmp += winner(round[i], round[i + 1])
            i += 2
        round = str(tmp)
    return round


handler = FileHandler(f"{os.path.dirname(__file__)}", skip_lines=1)
# handler.test(algorithm)
handler.process_all_files(algorithm)
