"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/21-brute-force/02-light-switches   (รันที่รากของโปรเจกต์)

ลองทุกเซตย่อยของสวิตช์ 2^20 แบบทันในเวลา ข้อนี้ไม่มีชุด big
ชุด or-trap ใช้ OR แทน XOR แล้วจะได้คำตอบผิด ชุด need-all ต้องกดครบทุกตัว
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2102)


def build(m, switches):
    lines = [f"{len(switches)} {m}"]
    for lamps in switches:
        lines.append(" ".join(map(str, [len(lamps)] + lamps)))
    return "\n".join(lines)


def random_switch(m, low, high):
    return sorted(random.sample(range(1, m + 1), random.randint(low, high)))


def lamps_of(switches, chosen):
    state = set()
    for i in chosen:
        state ^= set(switches[i])
    return state


def cases():
    yield "sample1", build(4, [[1, 2], [2, 3], [3, 4]])
    yield "sample2", build(3, [[1, 2], [2, 3]])
    yield "min", build(1, [[1]])
    yield "one-does-all", build(5, [[1, 2], [1, 2, 3, 4, 5], [3, 5]])
    # กด 1 กับ 2 แบบ OR ได้ครบทุกดวง แต่หลอด 2 โดนสลับสองครั้งจึงดับ ต้องกด 3 ตัว
    yield "or-trap", build(3, [[1, 2], [2, 3], [2]])
    # สวิตช์ตัวที่ i สลับหลอด i ดวงเดียว ต้องกดครบ 20 ตัว
    yield "need-all", build(20, [[i] for i in range(1, 21)])
    # ทุกสวิตช์สลับหลอดจำนวนคู่ ผลรวมจึงติดจำนวนคู่ดวงเสมอ แต่มี 19 ดวง ทำไม่ได้
    yield "parity", build(19, [sorted(random.sample(range(1, 20), random.choice([2, 4, 6]))) for _ in range(20)])
    # สุ่ม 19 ตัว แล้วสร้างตัวที่ 20 ให้รวมกับเซตย่อยลับแล้วติดครบ รับประกันว่ามีคำตอบ
    switches = [random_switch(20, 1, 8) for _ in range(19)]
    secret = random.sample(range(19), 9)
    missing = sorted(set(range(1, 21)) - lamps_of(switches, secret))
    switches.append(missing if missing else [1])
    yield "rand-solvable", build(20, switches)
    yield "rand1", build(12, [random_switch(12, 1, 6) for _ in range(15)])
    yield "rand2", build(20, [random_switch(20, 3, 10) for _ in range(20)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
