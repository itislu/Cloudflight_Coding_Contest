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
    i = 0

    res = ""
    while s:
        res += "S"
        s -= 1
        i += 1
    if i % 2 and p:
        res += "P"
        p -= 1
        i += 1
    while i % 4:
        if p:
            res += "P"
            p -= 1
            i += 1
        if r:
            res += "R"
            r -= 1
            i += 1
    while r >= 3 and p > 1:
        res += "RRRP"
        r -= 3
        p -= 1
    while p > 1:
        res += "P"
        p -= 1
    while r:
        res += "R"
        r -= 1
    if p:
        res += "P"
        p -= 1

    return res


handler = FileHandler(f"{os.path.dirname(__file__)}", skip_lines=1)
# handler.test(algorithm)
handler.process_all_files(algorithm, test=False)
