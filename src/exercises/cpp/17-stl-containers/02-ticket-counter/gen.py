"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/02-ticket-counter   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี Q เป็นแสน ใหญ่เกินกว่าจะเก็บใน git
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1702)

NAMES = ["Ploy", "Krit", "Mint", "Tan", "Fah", "Beam", "Nam", "Pim", "Ton", "Jane", "Bank", "Gun", "Fern", "Ice"]


def case(tickets, commands):
    return f"{tickets} {len(commands)}\n" + "\n".join(commands)


def random_commands(q, want_max):
    commands = []
    for _ in range(q):
        r = random.random()
        if r < 0.5:
            commands.append(f"JOIN {random.choice(NAMES)} {random.randint(1, want_max)}")
        elif r < 0.8:
            commands.append("SELL")
        elif r < 0.9:
            commands.append("LAST")
        else:
            commands.append("COUNT")
    return commands


def cases():
    yield "sample1", case(10, ["JOIN Ploy 4", "JOIN Krit 3", "JOIN Mint 5", "LAST", "SELL", "SELL", "COUNT",
                               "SELL", "SELL"])
    # ไม่มีตั๋วเลยตั้งแต่ต้น ทุกคนได้ 0
    yield "zero-tickets", case(0, ["JOIN Fah 2", "JOIN Beam 1", "COUNT", "SELL", "SELL", "SELL", "COUNT"])
    # ตั๋ว 10^15 เกิน int และขอทีละพันล้าน
    yield "huge-tickets", case(10**15, ["JOIN Nam 1000000000", "JOIN Pim 999999999", "COUNT", "SELL", "SELL",
                                        "COUNT", "LAST"])
    # ขอมากกว่าตั๋วที่เหลือมาก
    yield "big-request", case(5, ["JOIN Ton 1000000000", "JOIN Jane 3", "SELL", "SELL", "COUNT"])
    # ตั๋วหมดพอดีกับคนสุดท้าย
    yield "exact", case(9, ["JOIN Bank 2", "JOIN Gun 3", "JOIN Fern 4", "SELL", "SELL", "SELL", "COUNT"])
    # แถวว่างแล้วมีคนมาใหม่ LAST ต้องเป็นคนใหม่
    yield "refill", case(100, ["LAST", "SELL", "COUNT", "JOIN Ice 1", "LAST", "SELL", "LAST", "JOIN Ploy 7",
                               "JOIN Ploy 8", "LAST", "COUNT"])
    yield "rand1", case(500, random_commands(300, 20))
    yield "rand2", case(random.randint(10**12, 10**15), random_commands(3000, 10**9))
    yield "big1", case(random.randint(10**14, 10**15), random_commands(100000, 10**9))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
