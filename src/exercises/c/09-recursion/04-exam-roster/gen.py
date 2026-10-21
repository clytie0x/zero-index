"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/09-recursion/04-exam-roster   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีรายชื่อแสนคนและคำถามแสนข้อ
ตั้งใจให้วิธีไล่ดูทีละคนทุกคำถามใน naive.c ไม่ทัน
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(904)

TOP = 1000000000


def build(ids, queries):
    rows = [f"{len(ids)} {len(queries)}", " ".join(map(str, ids))] + [str(x) for x in queries]
    return "\n".join(rows)


def roster(n, low=1, high=TOP):
    return sorted(random.sample(range(low, high + 1), n))


def mixed_queries(ids, count):
    """ครึ่งหนึ่งเป็นเลขที่มีในรายชื่อ อีกครึ่งสุ่มทั้งช่วง ซึ่งส่วนใหญ่ไม่มี"""
    out = []
    for _ in range(count):
        if random.random() < 0.5:
            out.append(random.choice(ids))
        else:
            out.append(random.randint(1, TOP))
    return out


def cases():
    yield "sample1", build([1012, 1047, 1105, 1188, 1230, 1302, 1377, 1419, 1460, 1525],
                           [1460, 1200, 1012, 1525, 1000, 2000])
    yield "single", build([500], [500, 499, 501, 1, TOP])
    # ตัวแรก ตัวสุดท้าย น้อยกว่าทุกตัว มากกว่าทุกตัว และค่าขอบของโจทย์
    yield "ends", build([1, 3, 5, 7, TOP], [1, TOP, 2, 6, TOP - 1, 4, 7])
    ids = roster(64, 1, 1000)
    queries = ids[:]
    random.shuffle(queries)
    yield "all-present", build(ids, queries)
    ids = [2 * i for i in range(1, 51)]
    yield "none-present", build(ids, [2 * i + 1 for i in range(0, 51)])
    ids = roster(50, 1, 200)
    yield "rand1", build(ids, [random.randint(1, 200) for _ in range(50)])
    ids = roster(2000)
    yield "rand2", build(ids, mixed_queries(ids, 2000))
    ids = roster(100000)
    yield "big1", build(ids, mixed_queries(ids, 100000))
    # เลขประจำตัวติดกันเป็นช่วงที่ปลายบนสุด ถามแต่ตัวท้ายๆ ซึ่งวิธีไล่ต้องเดินเกือบสุดแถวทุกครั้ง
    ids = list(range(TOP - 99999, TOP + 1))
    yield "big2", build(ids, [random.randint(TOP - 10000, TOP) for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
