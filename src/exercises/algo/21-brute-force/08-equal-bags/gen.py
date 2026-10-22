"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/08-equal-bags   (รันที่รากของโปรเจกต์)

ชุดเล็กมี N ไม่เกิน 10 ให้ naive.cpp ที่ลองใส่ทุกห่อลงทุกถุงตรวจได้
ชุดที่ชื่อขึ้นต้นด้วย big มี N = 20 ลองครบ K^N แบบไม่ทัน
big-hard เป็นชุดที่คำตอบเป็น NO และวิธีที่ตัดแค่ถุงหนักเกินต้องค้นราว 6 × 10^9 โหนด
big-dups มีห่อหนักเท่ากันเกือบหมด จับคนที่ไม่ข้ามน้ำหนักซ้ำ
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2108)


def build(k, weights):
    return f"{len(weights)} {k}\n" + " ".join(map(str, weights))


def make_divisible(weights, k):
    weights[-1] += (-sum(weights)) % k
    return weights


def constructed_yes(n, k, target):
    sizes = [n // k + (1 if i < n % k else 0) for i in range(k)]
    weights = []
    for size in sizes:
        cuts = sorted(random.sample(range(1, target), size - 1))
        weights += [b - a for a, b in zip([0] + cuts, cuts + [target])]
    random.shuffle(weights)
    return weights


def cases():
    yield "sample1", build(3, [5, 4, 3, 3, 2, 1])
    yield "sample2", build(2, [3, 3, 3, 5])
    yield "not-divisible", build(3, [4, 4, 4, 4, 4])
    yield "too-heavy", build(2, [1, 1, 1, 9])
    yield "one-pack", build(2, [10])
    yield "all-same", build(5, [7] * 10)
    yield "small-yes", build(4, constructed_yes(10, 4, 500))
    yield "small-rand", build(3, make_divisible([random.randint(1, 100) for _ in range(10)], 3))
    yield "big-yes", build(5, constructed_yes(20, 5, 1000000))
    yield "big-yes4", build(4, constructed_yes(20, 4, 999999))
    yield "big-no", build(5, make_divisible([random.randint(1, 10**6) for _ in range(20)], 5))
    yield "big-hard", build(4, [789, 809, 327, 1016, 651, 1111, 375, 568, 1153, 1085,
                                414, 1188, 1092, 395, 564, 973, 413, 784, 1150, 1091])
    # ทุกถุงต้องหนัก 39 กรัม ต้องมีห่อ 3 กรัมทุกถุง แต่มีห่อนั้นห่อเดียว
    yield "big-dups", build(3, [6] * 19 + [3])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
