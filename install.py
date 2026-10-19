"""install.py"""

import os
from pathlib import Path

with (
    Path(__file__)
    .parent.joinpath("requirements.txt")
    .open("r", encoding="utf-8") as file
):
    for line in file:
        line: str = line.strip()

        if line and not line.startswith("pip"):
            print(f"Trying to install {line} ...")

            res: int = os.system(f"uv tool install {line}")

            print(f"{res=}")
