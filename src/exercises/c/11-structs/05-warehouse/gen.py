"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/11-structs/05-warehouse/gen.py
    python tools/make_outputs.py src/exercises/c/11-structs/05-warehouse
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1105)
BIG = 10**6


def codes(n):
    result = []
    while len(result) < n:
        code = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(1, 10)))
        if code not in result:
            result.append(code)
    return result


def warehouse(items, orders):
    lines = [f"{len(items)} {len(orders)}"]
    lines += [f"{c} {q} {p}" for c, q, p in items]
    lines += [f"{t} {c} {k}" for t, c, k in orders]
    return "\n".join(lines)


def random_orders(items, q, max_k, out_ratio=0.5):
    return [("OUT" if random.random() < out_ratio else "IN", random.choice(items)[0], random.randint(1, max_k))
            for _ in range(q)]


def cases():
    yield "sample1", warehouse([("PEN01", 50, 12), ("ERASER", 20, 5), ("RULER30", 0, 25)],
                               [("OUT", "PEN01", 30), ("OUT", "RULER30", 1), ("IN", "RULER30", 10),
                                ("OUT", "PEN01", 25), ("OUT", "ERASER", 20)])
    yield "sample2", warehouse([("A", 5, 100)], [("IN", "A", 3), ("OUT", "A", 9)])
    # เบิกพอดีกับที่มี ต้องเบิกได้ และเหลือ 0
    yield "exact", warehouse([("BOOK", 7, 30), ("BAG", 1, 450)],
                             [("OUT", "BOOK", 7), ("OUT", "BAG", 1), ("OUT", "BOOK", 1)])
    yield "all-rejected", warehouse([("X1", 0, 9), ("X2", 3, 9)],
                                    [("OUT", "X1", 1), ("OUT", "X2", 4), ("OUT", "X1", 1000000)])
    # รหัสที่เป็นส่วนต้นของรหัสอื่น เทียบผิดวิธีจะหาผิดชนิด
    yield "prefix-codes", warehouse([("A10", 10, 1), ("A1", 1, 10), ("A100", 100, 100), ("A", 0, 1000)],
                                    [("IN", "A1", 5), ("OUT", "A10", 10), ("IN", "A", 2), ("OUT", "A100", 50),
                                     ("OUT", "A1", 7), ("OUT", "A", 1)])
    # จำนวนและราคาใหญ่สุด มูลค่ารวมเกิน int ไปมาก
    items = [(c, BIG, BIG) for c in codes(100)]
    yield "max-value", warehouse(items, [("IN", items[i % 100][0], BIG) for i in range(1000)])
    yield "only-in", warehouse([("SOLO", BIG, BIG)], [("IN", "SOLO", BIG) for _ in range(1000)])
    items = [(c, random.randint(0, 100), random.randint(1, 500)) for c in codes(20)]
    yield "rand1", warehouse(items, random_orders(items, 300, 60))
    items = [(c, random.randint(0, BIG), random.randint(1, BIG)) for c in codes(100)]
    yield "rand2", warehouse(items, random_orders(items, 1000, BIG, 0.7))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for case_name, text in cases():
        (tests / f"{case_name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
