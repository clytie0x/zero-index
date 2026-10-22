"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/04-undo-editor   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี Q เป็นสองแสน ใหญ่เกินกว่าจะเก็บใน git
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1704)


def word():
    return "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10)))


def case(commands):
    return f"{len(commands)}\n" + "\n".join(commands)


def random_commands(q, weights):
    commands = []
    kinds = ["TYPE", "DELETE", "UNDO", "LAST"]
    for _ in range(q):
        kind = random.choices(kinds, weights)[0]
        commands.append(f"TYPE {word()}" if kind == "TYPE" else kind)
    return commands


def cases():
    yield "sample1", case(["TYPE i", "TYPE like", "TYPE cats", "DELETE", "TYPE dogs", "LAST", "UNDO", "UNDO",
                           "LAST"])
    # DELETE ตอนว่างไม่นับเป็นการแก้ไข UNDO ต้องข้ามไปย้อน DELETE ที่มีผลจริง
    yield "noop-delete", case(["UNDO", "DELETE", "LAST", "TYPE a", "DELETE", "DELETE", "UNDO", "LAST", "UNDO",
                               "LAST", "UNDO", "LAST"])
    # ย้อนจนหมดแล้วกดเกิน
    yield "undo-all", case(["TYPE red", "TYPE green", "DELETE", "TYPE blue", "UNDO", "UNDO", "UNDO", "UNDO",
                            "UNDO", "LAST"])
    # ลบแล้วย้อนสลับกันหลายชั้น คำซ้ำกันได้
    yield "nested", case(["TYPE go", "TYPE go", "TYPE stop", "DELETE", "DELETE", "TYPE wait", "UNDO", "UNDO",
                          "LAST", "DELETE", "DELETE", "DELETE", "UNDO", "LAST", "UNDO", "LAST"])
    yield "single", case(["LAST"])
    yield "rand1", case(random_commands(300, [4, 2, 2, 1]))
    yield "rand2", case(random_commands(5000, [3, 2, 3, 1]))
    # ข้อความยาวเป็นพันคำ
    yield "long-text", case(random_commands(3000, [10, 1, 1, 1]))
    yield "big1", case(random_commands(200000, [4, 2, 2, 1]))
    # พิมพ์แสนคำแล้วย้อนทั้งหมด วิธีเก็บสำเนาข้อความทุกครั้งจะใช้หน่วยความจำมหาศาล
    yield "big2", case([f"TYPE {word()}" for _ in range(100000)] + ["UNDO"] * 99999 + ["LAST"])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
