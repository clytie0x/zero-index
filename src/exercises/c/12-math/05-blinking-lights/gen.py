"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/05-blinking-lights   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อมีคำว่า trap มี ค.ร.น. สะสมใหญ่ระดับ 10^17 ถึง 10^18 แล้วตามด้วยเลขที่หารมันลงตัว
โปรแกรมที่คูณก่อนหารจะล้น long long ทั้งที่คำตอบไม่เปลี่ยน
"""

import math
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1205)

TOP = 10**9
ANSWER_LIMIT = 10**18
SMALL_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def lcm_all(values):
    answer = 1
    for v in values:
        answer = answer // math.gcd(answer, v) * v
    return answer


def build(values):
    assert 1 <= len(values) <= 100
    assert all(1 <= v <= TOP for v in values)
    assert lcm_all(values) <= ANSWER_LIMIT
    return f"{len(values)}\n" + " ".join(map(str, values))


def random_smooth(n):
    # สุ่มเลขที่เป็นผลคูณของจำนวนเฉพาะเล็กๆ ทีละตัว ทิ้งตัวที่ทำให้คำตอบเกิน 10^18
    values = []
    while len(values) < n:
        v = 1
        for _ in range(random.randint(1, 8)):
            p = random.choice(SMALL_PRIMES)
            if v * p <= TOP:
                v *= p
        if lcm_all(values + [v]) <= ANSWER_LIMIT:
            values.append(v)
    return values


def cases():
    yield "sample1", "3\n4 6 10"
    yield "sample2", "2\n12 18"
    yield "single", "1\n1000000000"
    yield "all-one", "4\n1 1 1 1"
    yield "same", "5\n7 7 7 7 7"
    yield "int-trap", build([100000, 100000])
    yield "coprime-max", build([TOP, TOP - 1])
    yield "trap-repeat", build([TOP, TOP - 1, TOP, TOP - 1, 3, 2])
    yield "trap-divisor", build([999999937, 999999929, 999999937])
    yield "trap-powers", build([2**29, 3**18, 4, 9, 2**10 * 3**5, 2**29])
    yield "rand1", build(random_smooth(10))
    yield "rand2", build(random_smooth(100))
    values = random_smooth(60)
    values.sort()
    yield "rand3", build(values[::-1])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
