"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/06-strings/07-caesar-decode

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(607)


def encrypt(key, plain):
    out = []
    for c in plain:
        if c.islower():
            c = chr((ord(c) - ord("a") + key) % 26 + ord("a"))
        elif c.isupper():
            c = chr((ord(c) - ord("A") + key) % 26 + ord("A"))
        out.append(c)
    return "".join(out)


def secret(key, plain):
    return f"{key}\n{encrypt(key, plain)}"


def text(length, pool):
    return "".join(random.choice(pool) for _ in range(length))


def cases():
    yield "sample1", secret(3, "See you at the gate at 7 pm.")
    yield "sample2", secret(29, "Zebra and yak")
    yield "zero", secret(0, "Nothing changes here!")
    yield "full-turn", secret(26, "Twenty six is a full turn")
    yield "back-one", secret(25, "abcxyz ABCXYZ")
    # 10^9 mod 26 = 12 ถ้าไม่ mod หรือบวกใน char จะผิด
    yield "max-key", secret(1000000000, "Meet me by the old banyan tree")
    yield "edge-spaces", secret(13, "   Lead and trail   ")
    pool = string.ascii_letters + string.digits + " " * 10 + ".,!?'-"
    yield "max-len", secret(999999999, text(1000, pool))
    yield "max-upper", secret(random.randint(0, 10**9), text(1000, string.ascii_uppercase))
    yield "rand1", secret(random.randint(0, 10**9), text(random.randint(20, 500), pool))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_bytes((data + "\n").encode())


if __name__ == "__main__":
    main()
