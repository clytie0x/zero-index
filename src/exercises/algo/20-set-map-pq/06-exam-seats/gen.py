"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/06-exam-seats   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big ทำให้แถวที่นั่งที่ถูกจองต่อกันยาวเป็นแสน ตั้งใจให้การไล่หาทีละที่ใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2006)


def case(n, events):
    return f"{n} {len(events)}\n" + "\n".join(events)


def simulate(n, count, leave_chance, low_x=1):
    """สุ่มคำสั่งที่ถูกเงื่อนไข L ใช้กับที่นั่งที่มีคนนั่งอยู่เท่านั้น จำลองตามกติกาเพื่อรู้ว่าใครนั่งที่ไหน"""
    events = []
    seated = []
    taken = [False] * (n + 2)
    for _ in range(count):
        if seated and random.random() < leave_chance:
            k = random.randrange(len(seated))
            x = seated[k]
            seated[k] = seated[-1]
            seated.pop()
            taken[x] = False
            events.append(f"L {x}")
        else:
            x = random.randint(low_x, n)
            events.append(f"B {x}")
            seat = x
            while seat <= n and taken[seat]:
                seat += 1
            if seat <= n:
                taken[seat] = True
                seated.append(seat)
    return events


def cases():
    yield "sample1", case(5, ["B 2", "B 2", "B 5", "B 4", "B 4", "L 2", "B 1", "B 1", "B 1"])
    yield "sample2", case(1, ["B 1", "B 1", "L 1", "B 1"])
    # ที่นั่งสุดท้ายเต็มแล้ว ต้องตอบ 0 ไม่วนกลับไปหาที่นั่งข้างหน้า
    yield "no-wrap", case(4, ["B 4", "B 4", "B 3", "B 3", "B 1"])
    yield "fill-all", case(6, ["B 1"] * 8 + ["L 3", "B 1", "L 6", "B 6"])
    yield "leave-return", case(3, ["B 2", "L 2", "B 2", "L 2", "B 1", "B 1", "B 1"])
    yield "rand1", case(50, simulate(50, 3000, 0.4))
    yield "rand2", case(5000, simulate(5000, 8000, 0.3))
    yield "rand3", case(200000, simulate(200000, 8000, 0.2))
    yield "big1", case(200000, ["B 1"] * 200000)
    events = ["B 1"] * 100000
    for _ in range(50000):
        x = random.randint(1, 100000)
        events += [f"L {x}", "B 1"]
    yield "big2", case(200000, events)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
