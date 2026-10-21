"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/01-dish-stack   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1401)


def build(commands):
    return "\n".join([str(len(commands))] + commands)


def random_commands(q, push_rate, max_dish):
    commands = []
    for _ in range(q):
        r = random.random()
        if r < push_rate:
            commands.append(f"PUSH {random.randint(1, max_dish)}")
        else:
            commands.append(random.choice(["POP", "POP", "TOP", "SIZE"]))
    commands[-1] = "SIZE"
    return commands


def cases():
    yield "sample1", build(["PUSH 12", "PUSH 7", "TOP", "PUSH 30", "SIZE", "POP", "POP", "TOP", "SIZE"])
    yield "sample2", build(["POP", "PUSH 5", "POP", "TOP", "SIZE"])
    yield "only-size", build(["SIZE"])
    # คำสั่งกับตั้งว่างซ้ำๆ ถ้าลืมเช็กว่าง size จะติดลบแล้วผิดต่อเนื่อง
    yield "empty-many", build(["POP", "TOP", "POP", "SIZE", "PUSH 9", "TOP", "POP", "POP", "TOP", "SIZE"])
    yield "max-dish", build(["PUSH 1000000000", "PUSH 999999999", "TOP", "POP", "TOP", "SIZE"])
    # วางครบแสนใบก่อนแล้วค่อยหยิบ stack ต้องสูงได้ถึงแสน
    q = 100000
    yield "big-tall", build([f"PUSH {i}" for i in range(1, q - 2)] + ["SIZE", "TOP", "POP"])
    yield "alternate", build([c for i in range(1, 501) for c in (f"PUSH {i * 7}", "POP")] + ["SIZE"])
    yield "rand1", build(random_commands(30, 0.5, 100))
    yield "rand2", build(random_commands(2000, 0.55, 10**9))
    yield "big-rand", build(random_commands(100000, 0.6, 10**9))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
