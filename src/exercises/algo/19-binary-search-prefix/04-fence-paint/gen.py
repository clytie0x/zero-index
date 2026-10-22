"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/04-fence-paint   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีไม้สองแสนแผ่นและสองแสนกลุ่ม แต่ละกลุ่มทาเกือบทั้งรั้ว
ตั้งใจให้วิธีวนทาทีละแผ่นใน naive.cpp ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1904)


def build(n, k, groups):
    rows = [f"{n} {len(groups)} {k}"] + [f"{l} {r} {c}" for l, r, c in groups]
    return "\n".join(rows)


def random_group(n, top):
    l, r = sorted((random.randint(1, n), random.randint(1, n)))
    return l, r, random.randint(1, top)


def cases():
    yield "sample1", "8 4 3\n1 4 1\n3 8 2\n5 5 1\n2 3 1"
    yield "single", build(1, 2, [(1, 1, 1), (1, 1, 1)])
    yield "never-painted", build(10, 1, [(4, 6, 1000000000)])
    # กลุ่มที่ทาแผ่นเดียว และกลุ่มที่ทาถึงแผ่นสุดท้าย
    yield "edges", build(6, 2, [(1, 1, 2), (6, 6, 2), (2, 6, 1), (3, 3, 1), (5, 6, 1)])
    # จำนวนชั้นเกิน int และ K เกิน int
    yield "over-int", build(5, 3000000000, [(1, 5, 1000000000), (1, 4, 1000000000), (2, 5, 1000000000), (3, 3, 1)])
    yield "huge-k", build(4, 10**15, [(1, 4, 10**9)] * 5)
    groups = [random_group(30, 5) for _ in range(30)]
    yield "rand1", build(30, 8, groups)
    groups = [random_group(2000, 1000) for _ in range(2000)]
    yield "rand2", build(2000, 330000, groups)
    n = 200000
    groups = [(random.randint(1, 1000), random.randint(n - 1000, n), random.randint(1, 10**9)) for _ in range(n)]
    yield "big1", build(n, 99 * 10**12, groups)
    groups = [random_group(n, 10) for _ in range(n)]
    yield "big2", build(n, 330000, groups)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
