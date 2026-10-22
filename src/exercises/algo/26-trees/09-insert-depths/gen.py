"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/26-trees/09-insert-depths   (รันที่รากของโปรเจกต์)

naive.cpp จำลอง BST ตรงๆ ช้าเมื่อต้นไม้ลึก
ชุดที่ชื่อขึ้นต้นด้วย big มีสองแสนคน big1 เรียงจากน้อยไปมาก big2 เรียงจากมากไปน้อย
big3 สลับเล็กใหญ่ 1, N, 2, N - 1, ... ซึ่งก็ลึกเป็นเส้นตรงเหมือนกัน
ตั้งใจให้ naive.cpp ไม่ทัน big4 สุ่มลำดับ ต้นไม้ไม่ลึก มีไว้เพราะไฟล์ใหญ่เกินจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2609)


def text(keys):
    return f"{len(keys)}\n" + " ".join(map(str, keys))


def zigzag(keys):
    """น้อยสุด มากสุด น้อยรองลงมา มากรองลงมา ไปเรื่อยๆ"""
    keys = sorted(keys)
    out = []
    lo, hi = 0, len(keys) - 1
    while lo <= hi:
        out.append(keys[lo])
        lo += 1
        if lo <= hi:
            out.append(keys[hi])
            hi -= 1
    return out


def balanced(keys):
    """ลำดับที่ให้ต้นไม้เตี้ยที่สุด ใส่ตัวกลางก่อนแล้วไล่ทีละชั้น"""
    keys = sorted(keys)
    out, ranges = [], [(0, len(keys) - 1)]
    while ranges:
        next_ranges = []
        for lo, hi in ranges:
            if lo > hi:
                continue
            mid = (lo + hi) // 2
            out.append(keys[mid])
            next_ranges += [(lo, mid - 1), (mid + 1, hi)]
        ranges = next_ranges
    return out


def distinct(count, top):
    return random.sample(range(1, top + 1), count)


def cases():
    yield "sample1", "7\n165 152 176 149 158 171 180"
    yield "sample2", "5\n10 20 30 25 5"
    yield "single", "1\n1000000000"
    yield "ascending", text(sorted(distinct(2000, 10**9)))
    yield "descending", text(sorted(distinct(2000, 10**9), reverse=True))
    yield "zigzag", text(zigzag(distinct(2000, 10**9)))
    yield "balanced", text(balanced(distinct(2047, 10**9)))
    yield "rand1", text(distinct(12, 50))
    yield "rand2", text(distinct(2000, 10**9))
    n = 200000
    yield "big1", text(sorted(distinct(n, 10**9)))
    yield "big2", text(sorted(distinct(n, 10**9), reverse=True))
    yield "big3", text(zigzag(distinct(n, 10**9)))
    yield "big4", text(distinct(n, 10**9))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
