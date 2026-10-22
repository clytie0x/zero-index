"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/23-greedy/01-coin-machine   (รันที่รากของโปรเจกต์)

ชุดที่ไม่ได้ขึ้นต้นด้วย big ใช้ยอดเงินเล็ก ให้วิธีลบทีละเหรียญใน naive.cpp ตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big ใช้ยอดเงินถึง 10^18 ซึ่งวิธีลบทีละเหรียญไม่ทัน
big2 กับ big3 มีคำตอบเกิน int ทุกชุดให้เหรียญมาไม่เรียง ยกเว้น sample2 กับ one-coin
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2301)


def chain(k):
    """เหรียญ k ชนิด เริ่มที่ 1 ชนิดถัดไปเป็นจำนวนเท่าของชนิดก่อนหน้า ค่าไม่เกิน 10^9"""
    coins = [1]
    while len(coins) < k:
        factor = random.choice([2, 2, 3, 5, 10])
        if coins[-1] * factor > 10**9:
            break
        coins.append(coins[-1] * factor)
    return coins


def build(coins, amounts, shuffle=True):
    coins = list(coins)
    if shuffle:
        while len(coins) > 1 and coins == sorted(coins, reverse=True):
            random.shuffle(coins)
    rows = [f"{len(coins)} {len(amounts)}", " ".join(map(str, coins))] + [str(a) for a in amounts]
    return "\n".join(rows)


def cases():
    yield "sample1", "4 3\n10 1 50 2\n38\n87\n100"
    yield "sample2", "1 2\n1\n5\n1"
    # เรียงจากน้อยไปมาก ถ้าไม่เรียงใหม่จะใช้เหรียญ 1 บาทหมด
    yield "ascending", build([1, 5, 10, 100, 1000], [1, 4, 9, 99, 1234, 99999], shuffle=False)
    yield "one-coin", build([1], [1, 7, 100000], shuffle=False)
    # เหรียญเกือบทุกชนิดถูกใช้ เพื่อจับการใช้เศษผิดชนิด
    yield "all-used", build([1, 2, 4, 8, 16, 32, 64, 128], [255, 254, 129, 128, 127, 1])
    yield "exact", build([1, 3, 15, 30, 300], [300, 30000, 15, 3, 45, 90000])
    coins = chain(8)
    yield "rand1", build(coins, [random.randint(1, 10**5) for _ in range(100)])
    coins = chain(30)
    yield "rand2", build(coins, [random.randint(1, 10**5) for _ in range(200)])
    coins = chain(30)
    yield "big1", build(coins, [random.randint(1, 10**18) for _ in range(100000)])
    # มีแต่เหรียญ 1 บาท คำตอบคือ A เอง ถึง 10^18
    yield "big2", build([1], [10**18, 999999999999999999, 123456789012345678], shuffle=False)
    yield "big3", build([2, 1], [10**18 - 1, 3 * 10**17 + 1])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
