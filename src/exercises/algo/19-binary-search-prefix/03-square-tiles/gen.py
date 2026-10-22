"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/19-binary-search-prefix/03-square-tiles   (รันที่รากของโปรเจกต์)

ชุดทดสอบเน้นค่าที่ติดขอบของกำลังสองพอดี ทั้งเลขเล็กและเลขใกล้ 10^18
ซึ่ง sqrt ของ double ปัดผิด และ mid * mid ล้นถ้า hi เริ่มที่ n
ชุด big1 มีงานแสนงาน ใหญ่เกินจะเก็บใน git จึงตั้งชื่อขึ้นต้นด้วย big ให้ CI สร้างใหม่
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1903)

TOP = 10**18


def build(values):
    return "\n".join([str(len(values))] + [str(v) for v in values])


def cases():
    yield "sample1", "5\n10\n16\n0\n99\n1000000000000000000"
    yield "tiny", build(list(range(0, 30)))
    # กำลังสองพอดี กับน้อยกว่ากำลังสองไปหนึ่ง ใกล้ 10^18 ที่ double แยกไม่ออก
    near = []
    for k in [10**9, 10**9 - 1, 999999937, 3037000499, 2**30, 123456789]:
        if k * k <= TOP:
            near += [k * k, k * k - 1, k * k + 1]
    yield "near-max", build([v for v in near if 0 <= v <= TOP])
    yield "max", build([TOP, TOP - 1, TOP - 2])
    yield "squares", build([k * k for k in range(1, 2001)] + [k * k - 1 for k in range(1, 2001)])
    values = [random.randint(0, 10**6) for _ in range(500)]
    yield "rand1", build(values)
    values = []
    for _ in range(3000):
        k = random.randint(1, 10**9)
        values.append(random.choice([k * k - 1, k * k, min(k * k + random.randint(0, 2 * k), TOP)]))
    yield "rand2", build(values)
    yield "big1", build([random.randint(0, TOP) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
