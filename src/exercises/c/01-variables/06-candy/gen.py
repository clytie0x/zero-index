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
random.seed(106)


def cases():
    yield "sample1", "3 20 15"
    yield "min", "1 1 0"
    yield "none-left", "1 1 1"
    yield "over-int", "100000 100000 1"
    yield "max", "1000000000 1000000000 0"
    yield "max-all-given", "1000000000 1000000000 1000000000000000000"
    for i in range(1, 4):
        n = random.randint(1, 10**9)
        m = random.randint(1, 10**9)
        yield f"rand{i}", f"{n} {m} {random.randint(0, n * m)}"


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
