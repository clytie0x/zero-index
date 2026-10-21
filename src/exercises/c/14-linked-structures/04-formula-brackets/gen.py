"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/04-formula-brackets   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1404)

PAIRS = ["()", "[]", "{}"]
FILLER = "abcxyz0123456789+-*/"


def build(formulas):
    return "\n".join([str(len(formulas))] + formulas)


def balanced(length):
    """สูตรที่วงเล็บถูกต้องยาว length ตัวพอดี มีตัวอักษรอื่นแทรก"""
    out, stack = [], []
    while len(out) + len(stack) < length:
        r = random.random()
        if r < 0.3 and len(out) + len(stack) + 1 < length:
            pair = random.choice(PAIRS)
            out.append(pair[0])
            stack.append(pair[1])
        elif r < 0.6 and stack:
            out.append(stack.pop())
        else:
            out.append(random.choice(FILLER))
    while stack:
        out.append(stack.pop())
    return "".join(out)


def broken(length):
    """ทำสูตรที่ถูกให้ผิดหนึ่งจุด แบบใดแบบหนึ่งในสามแบบ ยาวไม่เกิน length ตัว"""
    s = list(balanced(length - 1))
    spots = [i for i, c in enumerate(s) if c in ")]}"]
    kind = random.randint(0, 2)
    if kind == 0 and spots:
        i = random.choice(spots)
        s[i] = random.choice([c for c in ")]}" if c != s[i]])
    elif kind == 1:
        s.insert(random.randint(0, len(s)), random.choice(")]}"))
    else:
        s.insert(random.randint(0, len(s)), random.choice("([{"))
    return "".join(s)


def cases():
    yield "sample1", build(["{a+[b*(c-d)]}", "(a+b]*c", "((a)+b", "a+b)", "x*(y+(z)"])
    # ไม่มีวงเล็บเลย ตัวเดียว และวงเล็บปิดตัวแรก
    yield "tiny", build(["7", "(", ")", "x", "}", "[]"])
    # มีวงเล็บเปิดค้าง ตัวซ้ายสุดที่ค้างไม่ได้อยู่ตำแหน่ง 1
    yield "left-open", build(["()((", "[]{}(a)[b", "(()", "a{b(c)d"])
    # จำนวนวงเล็บเปิดปิดเท่ากัน แต่ผิดลำดับหรือผิดชนิด
    yield "same-count", build([")(", "([)]", "{(})", "][", "(]"])
    # ซ้อนลึกแสนชั้น stack ต้องสูงได้ถึงแสน
    yield "big-deep-ok", build(["(" * 50000 + ")" * 50000, "[" * 100000])
    yield "big-deep-wrong", build(["{" * 49999 + "(" + ")" + "]" + "}" * 49998])
    yield "rand1", build([random.choice([balanced, broken])(random.randint(1, 20)) for _ in range(30)])
    yield "rand2", build([random.choice([balanced, broken])(random.randint(50, 1000)) for _ in range(100)])
    yield "big-rand", build([broken(100000) for _ in range(5)] + [balanced(99000) for _ in range(5)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
