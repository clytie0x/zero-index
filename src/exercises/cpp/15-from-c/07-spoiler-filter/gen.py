"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/15-from-c/07-spoiler-filter   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1507)

MAX = 100000


def case(banned, text):
    assert text.strip() and not text.endswith(" ") and len(text) <= MAX
    return f"{len(banned)}\n{' '.join(banned)}\n{text}"


def word(low, high):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(random.randint(low, high)))


def sentence(words, total, max_gap, lead):
    """ต่อคำที่สุ่มจาก words ให้ยาวประมาณ total ตัว คั่นด้วยช่องว่าง 1 ถึง max_gap ช่อง"""
    parts = [" " * lead]
    length = lead
    while True:
        w = random.choice(words)
        if length + len(w) > total:
            break
        parts.append(w)
        length += len(w)
        gap = " " * random.randint(1, max_gap)
        parts.append(gap)
        length += len(gap)
    return "".join(parts).rstrip(" ")


def cases():
    yield "sample1", case(["vader", "father"], "darth vader is luke father")
    yield "sample2", case(["cat"], "the cat  can catch a cat")
    yield "single", case(["a"], "a")
    # คำต้องห้ามอยู่หน้าคำ กลางคำ ท้ายคำ และซ้อนกันสองชั้น จับคนที่ใช้ find กับทั้งข้อความ
    yield "inside-words", case(["ring", "lord"], "the lord of the rings brings a ring to lordly ring ringring")
    # ข้อความขึ้นต้นด้วยช่องว่าง และมีช่องว่างติดกันหลายช่อง จับคนที่อ่านทีละคำด้วย cin แล้วพิมพ์ใหม่
    yield "spaces", case(["end"], "   the   end    is   not  the end")
    # คำต้องห้ามซ้ำกัน และคำต้องห้ามยาวกว่าทุกคำในข้อความ
    yield "duplicates", case(["dog", "dog", "elephantelephantelep", "dog"], "dog dogs hotdog dog")
    yield "nothing-hidden", case(["zzz"], "nothing here is a spoiler")
    yield "all-hidden", case(["x", "yy"], "x yy x yy  yy x")
    vocab = [word(1, 8) for _ in range(300)]
    banned = random.sample(vocab, 20)
    yield "rand1", case(banned, sentence(vocab, 3000, 3, 2))
    vocab = [word(1, 20) for _ in range(2000)]
    banned = random.sample(vocab, 100)
    yield "max", case(banned, sentence(vocab, MAX, 2, 0))
    # คำสั้นหนึ่งถึงสองตัวจำนวนมาก คำต้องห้ามครบ 100 คำ
    vocab = sorted({word(1, 2) for _ in range(400)})
    banned = random.sample(vocab, 100)
    yield "short-words", case(banned, sentence(vocab, 30000, 1, 3))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
