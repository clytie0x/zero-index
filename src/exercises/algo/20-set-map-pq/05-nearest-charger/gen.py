"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/algo/20-set-map-pq/05-nearest-charger   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มีหัวชาร์จเปิดค้างเป็นแสนแล้วถามอีกเป็นแสน ตั้งใจให้การไล่ดูทุกสถานีใน naive.cpp ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2005)

TOP = 10**9


def case(events):
    return f"{len(events)}\n" + "\n".join(events)


def simulate(count, low, high, weights):
    """สุ่มเหตุการณ์ที่ถูกเงื่อนไขโจทย์ เปิดซ้ำจุดเดิมได้ ปิดเฉพาะหัวที่เปิดอยู่"""
    events = []
    opened = []
    for _ in range(count):
        kind = random.choices("+-?", weights=weights)[0]
        if kind == "-" and opened:
            k = random.randrange(len(opened))
            x = opened[k]
            opened[k] = opened[-1]
            opened.pop()
            events.append(f"- {x}")
        elif kind == "+":
            # ครึ่งหนึ่งเปิดเพิ่มที่จุดที่มีหัวอยู่แล้ว ให้มีจุดที่มีหลายหัวเยอะๆ
            if opened and random.random() < 0.5:
                x = random.choice(opened)
            else:
                x = random.randint(low, high)
            opened.append(x)
            events.append(f"+ {x}")
        else:
            events.append(f"? {random.randint(low, high)}")
    return events


def cases():
    yield "sample1", case(["? 500", "+ 1200", "+ 300", "? 500", "? 1200", "+ 900", "? 1000", "- 900", "? 1000"])
    yield "sample2", case(["+ 0", "+ 0", "? 1000000000", "- 0", "? 7", "- 0", "? 7"])
    yield "never-open", case(["? 5", "? 0", "? 1000000000"])
    # คำถามอยู่ตรงกลางพอดี และอยู่นอกสถานีทั้งหมดทั้งสองฝั่ง
    yield "both-sides", case(["+ 100", "+ 200", "? 150", "? 99", "? 201", "? 0", "? 1000000000", "? 100"])
    yield "extremes", case(["+ 0", "+ 1000000000", "? 500000000", "? 499999999", "- 0", "? 1", "+ 0", "- 1000000000", "? 1000000000"])
    # ปิดตัวที่อยู่ติดคำตอบ ต้องไม่ตอบระยะไปยังสถานีที่ปิดแล้ว
    yield "close-nearest", case(["+ 10", "+ 20", "+ 30", "? 21", "- 20", "? 21", "- 30", "? 21", "- 10", "? 21"])
    # สองหัวที่จุดเดียวกัน ปิดหัวเดียวแล้วจุดนั้นต้องยังอยู่ จับคนที่ใช้ set หรือ erase(x)
    yield "same-point", case(["+ 50", "+ 50", "? 60", "- 50", "? 60", "+ 80", "- 50", "? 60", "- 80", "? 60"])
    # หัวซ้อนกันหลายชั้นสองจุด ปิดทีละหัวแล้วถามคั่น
    yield "stacked", case(["+ 300"] * 3 + ["+ 700"] * 2 + ["? 450", "- 300", "? 450", "- 300", "? 450", "- 300", "? 450", "- 700", "? 450", "+ 300", "? 450", "- 700", "? 450"])
    yield "rand1", case(simulate(3000, 0, 100, [4, 2, 4]))
    yield "rand2", case(simulate(10000, 0, TOP, [4, 1, 5]))
    events = [f"+ {x}" for x in random.sample(range(0, TOP + 1), 100000)]
    events += [f"? {random.randint(0, TOP)}" for _ in range(100000)]
    yield "big1", case(events)
    yield "big2", case(simulate(200000, 0, TOP, [6, 1, 3]))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
