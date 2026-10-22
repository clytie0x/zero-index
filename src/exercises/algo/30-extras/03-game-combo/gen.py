"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/30-extras/03-game-combo   (รันที่รากของโปรเจกต์)

ชุดที่ชื่อขึ้นต้นด้วย big มีบันทึกยาวล้านตัวอักษร ตั้งใจให้วิธีเทียบทีละตำแหน่งใน naive.cpp ไม่ทัน
big1 เป็น a ล้านตัวกับท่า a ห้าหมื่นตัว ตรงทุกตำแหน่ง
big2 เป็น a ล้านตัวกับท่า a แสนตัวตามด้วย b ไม่ตรงเลยแต่ต้องเทียบเกือบสุดทุกครั้ง
big3 สุ่มจากสองตัวอักษร
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(3003)


def build(presses, combo):
    return f"{presses}\n{combo}\n"


def random_text(n, letters):
    return "".join(random.choice(letters) for _ in range(n))


def cases():
    yield "sample1", build("kddpkddpddpp", "ddp")
    yield "sample2", build("aaaa", "aa")
    yield "none", build("abcabcabd", "abdx")
    yield "combo-longer", build("ab", "abc")
    yield "same", build("kick", "kick")
    yield "one-letter", build("q", "q")
    # ท่าที่มีส่วนหน้าซ้ำกับส่วนท้าย ต้องย้อนกลับถูกจุด
    yield "self-overlap", build("abababcabababab", "ababab")
    yield "near-miss", build("aabaabaaab", "aaab")
    yield "rand1", build(random_text(60, "ab"), "aba")
    combo = random_text(4, "abc")
    yield "rand2", build(random_text(5000, "abc"), combo)
    n = 1000000
    yield "big1", build("a" * n, "a" * 50000)
    yield "big2", build("a" * n, "a" * 100000 + "b")
    yield "big3", build(random_text(n, "ab"), random_text(12, "ab"))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
