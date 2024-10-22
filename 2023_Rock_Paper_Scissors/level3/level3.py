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
    r, p, s = (int(x[:-1]) for x in input.split())

    res = ""
    while r >= 3 and p:
        res += "RRRP"
        r -= 3
        p -= 1
    # RRPS should be RSRP
    while r and p:
        res += "RP"
        r -= 1
        p -= 1
    while r:
        res += "R"
        r -= 1
    while p:
        res += "P"
        p -= 1
    while s:
        res += "S"
        s -= 1

    return res


handler = FileHandler(f"{os.path.dirname(__file__)}", skip_lines=1)
# handler.test(algorithm)
handler.process_all_files(algorithm, test=False)
