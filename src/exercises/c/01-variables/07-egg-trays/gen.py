"""สร้างชุดทดสอบของข้อนี้ แล้วรันเฉลยเพื่อเขียนคำตอบ

    python gen.py

ใช้ gcc ใน PATH หรือกำหนดเองด้วยตัวแปร ZI_GCC
"""

import os
import random
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(107)


def cases():
    yield "sample1", "65 30"
    yield "sample2", "60 30"
    yield "min", "1 1"
    yield "one-big-tray", "1 1000000000"
    yield "many-trays", "1000000000 1"
    yield "equal-max", "1000000000 1000000000"
    yield "just-under", "999999999 1000000000"
    yield "just-over", "1000000000 999999999"
    for i in range(1, 4):
        yield f"rand{i}", f"{random.randint(1, 10**9)} {random.randint(1, 1000)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        exe = Path(tmp) / "solution.exe"
        gcc = os.environ.get("ZI_GCC", "gcc")
        subprocess.run([gcc, "-std=c17", "-O2", str(HERE / "solution.c"), "-o", str(exe)], check=True)
        for name, text in cases():
            data = (text + "\n").encode()
            (tests / f"{name}.in").write_bytes(data)
            out = subprocess.run([str(exe)], input=data, capture_output=True, check=True).stdout
            (tests / f"{name}.out").write_bytes(out.replace(b"\r\n", b"\n"))


if __name__ == "__main__":
    main()
