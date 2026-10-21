"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/04-word-hunt   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1304)


def mixed_case(s):
    return "".join(c.upper() if random.random() < 0.5 else c for c in s)


def random_text(length, alphabet):
    return "".join(random.choice(alphabet) for _ in range(length))


def cases():
    yield "sample1", "The cat sat on THE mat with the other cat\nthe"
    yield "sample2", "BaNaNa bandana\nANA"
    yield "none", "hello world\ncat"
    yield "longer-word", "short\nshortcake"
    yield "exact", "Songkhla\nsONGKHLA"
    yield "at-end", "where is the cat\nCAT"
    yield "single-letter", "a A b B a\na"
    # ตำแหน่งซ้อนกันมากที่สุด จับวิธีที่นับแบบไม่ซ้อน
    yield "all-a", "a" * 1000 + "\n" + "aaa"
    # คำยาว 100 ตัวที่ตรงเกือบทั้งคำทุกตำแหน่ง
    yield "almost", "A" * 1000 + "\n" + "a" * 99 + "b"
    text = random_text(1000, "abAB ")
    yield "rand1", text + "\n" + "abA"
    words = ["cat", "concat", "category", "scatter", "dog", "Cat", "CATCH", "bobcat"]
    sentence = " ".join(mixed_case(random.choice(words)) for _ in range(150))[:1000].rstrip()
    yield "rand2", sentence + "\n" + "cAt"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
