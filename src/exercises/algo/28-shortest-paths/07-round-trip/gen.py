"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/07-round-trip   (รันที่รากของโปรเจกต์)

naive.cpp รัน Dijkstra จากทุกบ้านเพื่อหาขากลับ ผ่านชุดเล็กทุกชุด
ชุดที่ชื่อขึ้นต้นด้วย big มีแสนจุด ตั้งใจให้วิธีนั้นไม่ทัน
one-way ดักคนที่ใส่ถนนเป็นสองทาง no-return กับ big3 มีบ้านที่กลับไม่ได้
ทุกชุดตั้งแต่ rand2 มีเวลารวมเกิน int
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2807)


def build(n, edges):
    return f"{n} {len(edges)}\n" + "\n".join(f"{u} {v} {w}" for u, v, w in edges)


def strongly_connected(n, m, top):
    """วงใหญ่ผ่านทุกจุดทำให้ทุกจุดไปถึงกันได้ แล้วเติมถนนสุ่มทางเดียว"""
    order = list(range(2, n + 1))
    random.shuffle(order)
    cycle = [1] + order
    edges = [(cycle[i], cycle[(i + 1) % n], random.randint(1, top)) for i in range(n)]
    while len(edges) < m:
        u, v = random.randint(1, n), random.randint(1, n)
        if u != v:
            edges.append((u, v, random.randint(1, top)))
    random.shuffle(edges)
    return edges


def cases():
    yield "sample1", "4 6\n1 2 5\n2 3 2\n3 1 4\n1 3 10\n3 4 1\n4 1 3"
    yield "sample2", "3 3\n1 2 4\n2 1 4\n1 3 1"
    yield "min", "2 2\n1 2 1000000\n2 1 1"
    # ถนนสั้นเป็นทางเดียวผิดทิศ ถ้าใส่สองทางจะได้คำตอบน้อยเกินไป
    yield "one-way", build(3, [(1, 2, 1), (2, 3, 1), (3, 1, 1), (2, 1, 100), (3, 2, 100)])
    # บ้าน 4 ไปถึงได้แต่ไม่มีถนนออก
    yield "no-return", build(4, [(1, 2, 3), (2, 1, 3), (2, 3, 3), (3, 1, 3), (3, 4, 3)])
    yield "rand1", build(20, strongly_connected(20, 50, 100))
    yield "rand2", build(2000, strongly_connected(2000, 5000, 10**6))
    yield "big1", build(100000, strongly_connected(100000, 200000, 10**6))
    # วงใหญ่วงเดียว ถนนยาวเกือบ 10^6 ทุกเส้น ทุกเที่ยวต้องวนครบวง
    n = 100000
    yield "big2", build(n, strongly_connected(n, n, 10**6))
    edges = strongly_connected(n, 200000, 10**6)
    stuck = random.randint(2, n)
    edges = [(u, v, w) for u, v, w in edges if u != stuck]
    yield "big3", build(n, edges)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
