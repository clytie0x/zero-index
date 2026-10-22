"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/03-delivery-route   (รันที่รากของโปรเจกต์)

N ไม่เกิน 9 ลองทุกลำดับทันทุกชุด ข้อนี้ไม่มีชุด big
ชุด one-way ระยะไปกับกลับต่างกันมาก จับคนที่อ่านตารางกลับด้าน
ชุด greedy ถ้าไปบ้านที่ใกล้ที่สุดก่อนทุกครั้งจะได้คำตอบไม่ดีที่สุด
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2103)


def build(dist):
    n = len(dist) - 1
    return f"{n}\n" + "\n".join(" ".join(map(str, row)) for row in dist)


def random_dist(n, low, high, symmetric):
    dist = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(n + 1):
            if i < j:
                dist[i][j] = random.randint(low, high)
                dist[j][i] = dist[i][j] if symmetric else random.randint(low, high)
    return dist


def cases():
    yield "sample1", build([[0, 4, 9, 7], [4, 0, 3, 8], [9, 3, 0, 2], [7, 8, 2, 0]])
    yield "sample2", build([[0, 5, 1], [5, 0, 10], [1, 1, 0]])
    yield "one-house", build([[0, 37], [12, 0]])
    yield "two-houses", build([[0, 6, 2], [9, 0, 1], [3, 100, 0]])
    yield "all-same", build([[0 if i == j else 5 for j in range(10)] for i in range(10)])
    # ไปทางเดียวได้ระยะ 1 ทางกลับยาว 1000 ต้องอ่าน d[i][j] เป็นจากแถว i ไปคอลัมน์ j
    dist = [[0 if i == j else 1000 for j in range(7)] for i in range(7)]
    for i in range(6):
        dist[i][i + 1] = 1
    yield "one-way", build(dist)
    # บ้านอยู่บนถนนเส้นตรงที่ตำแหน่ง -3 2 5 ร้านอยู่ที่ 0 ไปบ้านที่ใกล้สุดก่อนทุกครั้งได้ 13 แต่คำตอบคือ 11
    yield "greedy", build([[0, 3, 2, 5], [3, 0, 5, 8], [2, 5, 0, 3], [5, 8, 3, 0]])
    yield "max-sym", build(random_dist(9, 1, 1000, True))
    yield "max-oneway", build(random_dist(9, 1, 1000, False))
    yield "rand1", build(random_dist(6, 1, 50, False))
    yield "rand2", build(random_dist(8, 900, 1000, True))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
