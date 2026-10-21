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
random.seed(108)


def cases():
    yield "sample1", "3 7"
    yield "sample2", "1 100"
    yield "min", "1 1"
    yield "same", "1000000000 1000000000"
    yield "max", "1 1000000000"
    yield "upper-half", "500000000 1000000000"
    for i in range(1, 4):
        a = random.randint(1, 10**9)
        yield f"rand{i}", f"{a} {random.randint(a, 10**9)}"


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
