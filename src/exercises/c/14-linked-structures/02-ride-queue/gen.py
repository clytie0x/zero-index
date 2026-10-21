"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/02-ride-queue   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1402)


def build(commands):
    return "\n".join([str(len(commands))] + commands)


def random_commands(q, join_rate, max_seats):
    commands = []
    for _ in range(q):
        r = random.random()
        if r < join_rate:
            commands.append(f"JOIN {random.randint(1, 10**9)}")
        elif r < join_rate + (1 - join_rate) * 0.7:
            commands.append(f"RIDE {random.randint(1, max_seats)}")
        else:
            commands.append("COUNT")
    commands[-1] = "COUNT"
    return commands


def cases():
    yield "sample1", build(["JOIN 101", "JOIN 102", "JOIN 103", "JOIN 104", "RIDE 3", "COUNT", "JOIN 105", "RIDE 4", "RIDE 2", "COUNT"])
    yield "sample2", build(["RIDE 5", "JOIN 7", "COUNT", "RIDE 1", "COUNT"])
    # ที่นั่งมากกว่าคนในแถวมาก ถ้าวนครบ k รอบจะได้หมายเลขขยะ
    yield "many-seats", build(["JOIN 8", "JOIN 9", "RIDE 100000", "RIDE 100000", "COUNT"])
    yield "one-seat", build([f"JOIN {i}" for i in range(1, 11)] + ["RIDE 1"] * 12 + ["COUNT"])
    yield "only-count", build(["COUNT", "JOIN 1000000000", "COUNT"])
    # คนเข้าแถวรวมครบแสนพอดี อาเรย์ต้องมีแสนช่อง
    yield "big-full-day", build([f"JOIN {i}" for i in range(1, 100000)] + ["RIDE 100000"])
    yield "rand1", build(random_commands(30, 0.6, 4))
    yield "rand2", build(random_commands(3000, 0.7, 10))
    yield "big-rand", build(random_commands(100000, 0.75, 6))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
