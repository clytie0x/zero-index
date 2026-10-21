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
random.seed(105)


def cases():
    yield "sample1", "472"
    yield "sample2", "120"
    yield "min", "100"
    yield "max", "999"
    yield "zero-middle", "101"
    yield "two-zeros", "900"
    yield "palindrome", "353"
    for i in range(1, 3):
        yield f"rand{i}", str(random.randint(100, 999))


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
