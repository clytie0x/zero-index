"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/12-math/02-triangle-land   (รันที่รากของโปรเจกต์)

ชุดที่ไล่หมุดตามเข็มนาฬิกาทำให้สูตรได้ค่าติดลบ ชุดที่ชื่อมีคำว่า half มีพื้นที่ลงท้ายด้วย .5
ชุด int-trap กับชุดที่พิกัดใหญ่จับโปรแกรมที่คูณด้วย int ส่วนชุด big-half จับโปรแกรมที่ใช้ double
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1202)

LIMIT = 10**9


def twice_area(points):
    (x1, y1), (x2, y2), (x3, y3) = points
    return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)


def line(points):
    return " ".join(f"{x} {y}" for x, y in points)


def random_points(low, high, want_odd):
    # สุ่มจนได้สามเหลี่ยมที่สองเท่าของพื้นที่เป็นเลขคี่หรือคู่ตามที่ต้องการ
    while True:
        points = [(random.randint(low, high), random.randint(low, high)) for _ in range(3)]
        t = twice_area(points)
        if t != 0 and (t % 2 == 1) == want_odd:
            return points


def cases():
    yield "sample1", "1 1 5 1 1 4"
    yield "sample2", "0 0 3 1 1 2"
    yield "on-line", "0 0 1 1 3 3"
    yield "same-point", "7 7 7 7 7 7"
    yield "clockwise", "0 0 0 3 4 0"
    yield "clockwise-half", "0 0 1 2 3 1"
    yield "int-trap", "0 0 100000 0 0 100000"
    yield "max", f"{-LIMIT} {-LIMIT} {LIMIT} {-LIMIT} {-LIMIT} {LIMIT}"
    yield "big-half", f"{-LIMIT} {-LIMIT} {LIMIT} {-LIMIT + 1} {-LIMIT + 2} {LIMIT}"
    yield "far-line", f"{-LIMIT} {-LIMIT + 3} 0 3 {LIMIT - 3} {LIMIT}"
    yield "rand-half", line(random_points(-LIMIT, LIMIT, True))
    yield "rand-even", line(random_points(-LIMIT, LIMIT, False))
    yield "rand-small", line(random_points(-20, 20, True))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
