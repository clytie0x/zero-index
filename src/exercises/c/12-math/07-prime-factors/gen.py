"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/07-prime-factors   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีเลขที่มีตัวประกอบเฉพาะใหญ่เกือบ 10^12 วิธีลองหารไปจนถึง n ใน naive.c ไม่ทัน
ชุดอื่นมีตัวประกอบเฉพาะที่ใหญ่สุดไม่เกินราวล้าน ให้ naive.c ผ่านได้
ชุด leftover จับโปรแกรมที่ลืมพิมพ์ตัวประกอบที่เหลือหลังลูป ชุด prime-square จับเงื่อนไข p * p < n
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1207)

TOP = 10**12


def is_prime(n):
    if n < 2:
        return False
    p = 2
    while p * p <= n:
        if n % p == 0:
            return False
        p += 1
    return True


def prime_below(n):
    while not is_prime(n):
        n -= 1
    return n


def build(numbers):
    assert 1 <= len(numbers) <= 10
    assert all(2 <= n <= TOP for n in numbers)
    return f"{len(numbers)}\n" + "\n".join(map(str, numbers))


def cases():
    yield "sample1", build([360, 97, 1024])
    yield "sample2", build([2])
    yield "small", build([3, 4, 6, 12, 30, 49, 64, 81, 99, 100])
    yield "leftover", build([2000006, 3 * 1000003, 2 * 3 * 5 * 999983])
    yield "prime-square", build([999983 * 999983, 1009 * 1009, 4, 9])
    yield "two-primes", build([999983 * 999979, 1000003 * 999979])
    yield "powers", build([2**39, 3**25, 10**12, 7**14])
    yield "many-primes", build([2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31, 963761198400])
    yield "rand-smooth", build([random.randint(2, 10**6) * random.randint(1, 10**6) for _ in range(10)])
    big_prime = prime_below(TOP)
    yield "big1", build([big_prime])
    yield "big2", build([2 * prime_below(TOP // 2), 3 * prime_below(TOP // 3), big_prime])
    yield "big3", build([prime_below(random.randint(TOP // 2, TOP)) for _ in range(10)])
    yield "big4", build([random.randint(TOP // 2, TOP) for _ in range(10)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
