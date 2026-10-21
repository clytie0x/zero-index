"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/14-linked-structures/03-card-deck   (รันที่รากของโปรเจกต์)
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1403)


def build(commands):
    return "\n".join([str(len(commands))] + commands)


def random_commands(q, add_rate):
    cards = random.sample(range(1, 10**9 + 1), q)
    commands = []
    for i in range(q):
        if random.random() < add_rate:
            commands.append(f"{random.choice(['TOP', 'BOTTOM'])} {cards[i]}")
        else:
            commands.append(random.choice(["DRAWTOP", "DRAWBOTTOM"]))
    return commands


def cases():
    yield "sample1", build(["TOP 5", "TOP 8", "BOTTOM 3", "DRAWBOTTOM", "TOP 1", "BOTTOM 9", "DRAWTOP"])
    yield "sample2", build(["DRAWTOP", "BOTTOM 4", "DRAWTOP", "DRAWBOTTOM"])
    # วางบนอย่างเดียวคือ stack ครั้งแรก head ต้องวนไปท้ายอาเรย์
    yield "top-only", build([f"TOP {i}" for i in range(1, 9)] + ["DRAWTOP", "DRAWTOP"])
    # วางล่างหยิบบนคือ queue
    yield "bottom-only", build([f"BOTTOM {i}" for i in range(1, 9)] + ["DRAWTOP", "DRAWTOP", "DRAWBOTTOM"])
    yield "single", build(["BOTTOM 1000000000"])
    yield "draw-empty", build(["DRAWBOTTOM", "DRAWTOP", "TOP 2", "DRAWBOTTOM", "DRAWBOTTOM"])
    # หยิบออกจนหมดแล้วเพิ่มใหม่ ซ้ำหลายรอบ head กับ tail วนผ่านขอบอาเรย์
    cmds = []
    for r in range(1, 30001):
        cmds += [f"TOP {r}", f"BOTTOM {r + 500000}", "DRAWTOP"]
    yield "big-wrap-around", build(cmds[:100000])
    # ไพ่ครบแสนใบพร้อมกัน วางสลับบนล่าง
    yield "big-full-deck", build([f"{'TOP' if i % 2 else 'BOTTOM'} {i}" for i in range(1, 100001)])
    yield "rand1", build(random_commands(25, 0.6))
    yield "rand2", build(random_commands(5000, 0.55))
    yield "big-rand", build(random_commands(100000, 0.6))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
