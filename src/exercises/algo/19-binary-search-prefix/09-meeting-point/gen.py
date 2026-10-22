"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/09-meeting-point   (รันที่รากของโปรเจกต์)

คำตอบจริงคือ (x_j - x_i) / (v_i + v_j) ของคู่ที่ต้องใช้เวลามากที่สุด gen.py หาคู่นั้นแล้วตรวจด้วยเลขจำนวนเต็มแบบแม่นยำ
และสุ่มใหม่ถ้าคำตอบอยู่ใกล้กึ่งกลางของการปัดทศนิยม 4 ตำแหน่งเกิน 10^-6
เพราะตัวตรวจเทียบทุกตัวอักษร และ Windows กับ Linux ปัดค่าที่ตกตรงครึ่งต่างกัน
naive.cpp ลองทุกคู่ ชุดที่ชื่อขึ้นต้นด้วย big มีแสนคน ซึ่งวิธีลองทุกคู่ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1909)

TOP = 10**9


def exact_answer(xs, vs):
    """คืน (num, den) ของคำตอบจริง หาคู่ที่ผูกคำตอบด้วยทศนิยมก่อน แล้วยืนยันด้วยจำนวนเต็ม"""
    lo, hi = 0.0, 1e9
    for _ in range(100):
        mid = (lo + hi) / 2
        if max(x - v * mid for x, v in zip(xs, vs)) <= min(x + v * mid for x, v in zip(xs, vs)):
            hi = mid
        else:
            lo = mid
    i = max(range(len(xs)), key=lambda k: xs[k] - vs[k] * hi)
    j = min(range(len(xs)), key=lambda k: xs[k] + vs[k] * hi)
    num, den = xs[i] - xs[j], vs[i] + vs[j]
    if num <= 0:
        assert max(xs) == min(xs)
        return 0, 1
    left = max(x * den - v * num for x, v in zip(xs, vs))
    right = min(x * den + v * num for x, v in zip(xs, vs))
    assert left <= right, "คู่ที่หาได้ไม่ใช่คำตอบจริง"
    return num, den


def safe(xs, vs):
    num, den = exact_answer(xs, vs)
    remainder = num * 10000 % den
    return abs(2 * remainder - den) > den // 50


def build(xs, vs):
    assert safe(xs, vs), "คำตอบใกล้กึ่งกลางของการปัดเกินไป"
    return f"{len(xs)}\n" + " ".join(map(str, xs)) + "\n" + " ".join(map(str, vs))


def random_case(n, top_x, top_v):
    while True:
        xs = [random.randint(0, top_x) for _ in range(n)]
        vs = [random.randint(1, top_v) for _ in range(n)]
        if safe(xs, vs):
            return build(xs, vs)


def cases():
    yield "sample1", "3\n0 10 40\n2 3 1"
    yield "sample2", "2\n5 5\n7 9"
    yield "single", build([123456789], [1000])
    yield "two-far", build([0, TOP], [1, 2])
    yield "slow-in-middle", build([0, 500, 1000], [1000, 1, 1000])
    yield "same-speed", build([3, 30, 17, 8, 26], [7, 7, 7, 7, 7])
    yield "rand1", random_case(10, 100, 5)
    yield "rand2", random_case(1000, TOP, 1000)
    yield "big1", random_case(100000, TOP, 1000)
    yield "big2", random_case(100000, 10**6, 3)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
