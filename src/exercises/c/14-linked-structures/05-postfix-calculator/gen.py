"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/05-postfix-calculator   (รันที่รากของโปรเจกต์)

ตัวสร้างคำนวณค่าไปพร้อมกัน เพื่อเลือกเครื่องหมายที่ไม่หารด้วยศูนย์และไม่ทำให้ค่าเกิน 10^18
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1405)
LIMIT = 10**18


def c_div(a, b):
    """หารแบบภาษา C ตัดเศษทิ้งไปทาง 0 (// ของ Python ปัดลง ใช้ตรงๆ ไม่ได้)"""
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b > 0) else -q


def apply(op, a, b):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    return None if b == 0 else c_div(a, b)


def build(tokens):
    return f"{len(tokens)}\n{' '.join(tokens)}"


def random_expression(numbers, max_value, push_rate):
    """สุ่มนิพจน์ postfix ที่มีตัวเลข numbers ตัว แล้วคืนรายการของ token"""
    tokens, values, left = [], [], numbers
    while left > 0 or len(values) > 1:
        if left > 0 and (len(values) < 2 or random.random() < push_rate):
            v = random.randint(0, max_value)
            tokens.append(str(v))
            values.append(v)
            left -= 1
            continue
        b = values.pop()
        a = values.pop()
        ops = ["+", "-", "*", "/"]
        random.shuffle(ops)
        for op in ops:
            r = apply(op, a, b)
            if r is not None and abs(r) <= LIMIT:
                break
        tokens.append(op)
        values.append(r)
    return tokens


def cases():
    yield "sample1", build("8 3 - 4 *".split())
    yield "sample2", build("2 7 - 2 /".split())
    yield "single", build(["1000000000"])
    # ผลรวมสามตัวเกิน int
    yield "over-int", build("1000000000 1000000000 + 1000000000 +".split())
    yield "zero", build("0 5 /".split())
    # ลบกับหารสลับข้างไม่ได้ จับคนที่ pop ตัวซ้ายก่อน
    yield "order", build("100 1 - 9 / 1000 10 / -".split())
    # หารจำนวนลบ ต้องตัดไปทาง 0 ได้ -3 ไม่ใช่ -4
    yield "negative-div", build("3 10 - 2 / 0 7 - 2 / *".split())
    # ผลรวมห้าหมื่นตัวของ 10^9 เกิน int
    yield "big-long-sum", build(["1000000000"] + ["1000000000", "+"] * 49999)
    # ตัวเลขมาก่อนทั้งหมด stack สูงห้าหมื่น
    nums = [str(random.randint(0, 9)) for _ in range(50000)]
    yield "big-deep", build(nums + ["+"] * 49999)
    # ผลคูณใกล้ 10^18
    yield "large-product", build("1000000000 999999999 * 7 - 3 /".split())
    yield "rand1", build(random_expression(8, 20, 0.5))
    yield "rand2", build(random_expression(2000, 1000, 0.5))
    yield "big-rand", build(random_expression(50000, 10**9, 0.45))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
