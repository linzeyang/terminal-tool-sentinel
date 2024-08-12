import os
from pathlib import Path


with (Path(__file__).parent / "requirements.txt").open("r") as file:
    for line in file:
        line = line.strip()

        if line and not line.startswith("pip"):
            print(f"Trying to install {line} ...")

            res = os.system(f"pipx install {line}")

            print(f"{res=}")
