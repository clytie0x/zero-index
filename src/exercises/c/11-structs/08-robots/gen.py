"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/11-structs/08-robots/gen.py
    python tools/make_outputs.py src/exercises/c/11-structs/08-robots

ชุด big ไม่เก็บใน git สร้างใหม่ได้ด้วยสคริปต์นี้
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1108)
LIMIT = 10**9


def depot(robots, commands):
    lines = [f"{len(robots)} {len(commands)}"]
    lines += [f"{x} {y} {d}" for x, y, d in robots]
    lines += commands
    return "\n".join(lines)


def random_robots(n, spread):
    return [(random.randint(-spread, spread), random.randint(-spread, spread), random.choice("NESW"))
            for _ in range(n)]


def random_commands(n, q, max_steps):
    out = []
    for _ in range(q):
        i = random.randint(1, n)
        kind = random.choice("FFLR")
        out.append(f"{i} F {random.randint(1, max_steps)}" if kind == "F" else f"{i} {kind}")
    return out


def cases():
    yield "sample1", depot([(0, 0, "N"), (3, 2, "W"), (-1, 5, "E")],
                           ["1 F 2", "1 R", "1 F 3", "2 L", "3 F 4", "3 R", "3 F 3"])
    yield "sample2", depot([(0, 0, "E"), (5, 5, "S"), (2, -3, "N"), (9, 9, "W")],
                           ["1 F 5", "2 F 5", "3 F 3", "3 R", "3 F 3", "4 L", "4 L", "4 L"])
    yield "single", depot([(7, -7, "S")], ["1 L", "1 F 10", "1 L", "1 F 3"])
    yield "no-commands", depot([(1, 1, "N"), (1, 1, "E"), (2, 1, "N")], [])
    # หมุนครบรอบต้องกลับทิศเดิม ทั้งซ้ายและขวา
    yield "spin", depot([(0, 0, "N"), (0, 0, "W")], ["1 L"] * 4 + ["2 R"] * 7 + ["1 R", "1 R", "1 L"])
    # ทุกตัวเริ่มที่ช่องเดียวกัน คู่มากที่สุด 1000 x 999 / 2
    yield "all-same", depot([(LIMIT, -LIMIT, random.choice("NESW")) for _ in range(1000)], ["5 L", "17 R"])
    # เดินไกลสุดจากขอบ ไปถึงหลัก 10^12 ต้องใช้ long long
    yield "far", depot([(LIMIT, LIMIT, "E"), (-LIMIT, -LIMIT, "S")], ["1 F 1000000000"] * 500 + ["2 F 1000000000"] * 500)
    # สองตัวเดินไปเจอกันจากคนละทาง
    yield "meet", depot([(0, 0, "N"), (10, 10, "W"), (10, 0, "N"), (-5, 10, "E")],
                        ["1 F 10", "2 F 10", "3 F 5", "3 L", "3 F 10", "3 R", "3 F 5", "4 F 5"])
    yield "rand1", depot(random_robots(20, 5), random_commands(20, 200, 3))
    yield "rand2", depot(random_robots(300, 3), random_commands(300, 2000, 2))
    yield "big1", depot(random_robots(1000, LIMIT), random_commands(1000, 100000, LIMIT))
    yield "big2", depot([(-LIMIT, LIMIT, "N")], ["1 F 1000000000"] * 100000)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for case_name, text in cases():
        (tests / f"{case_name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
