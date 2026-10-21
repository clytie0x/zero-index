"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/c/13-sort-search/09-anagram-pairs   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นแสน ตั้งใจให้ bubble sort ใน naive.c ไม่ทัน 1 วินาที
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1309)


def case(words):
    return f"{len(words)}\n" + "\n".join(words)


def random_word(letters, min_length, max_length):
    return "".join(random.choice(letters) for _ in range(random.randint(min_length, max_length)))


def shuffled(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def cases():
    yield "sample1", case(["listen", "google", "silent", "stop", "enlist", "pots", "tops"])
    yield "sample2", case(["lose", "loose", "sole", "cat", "act", "tac", "dog"])
    yield "single", case(["zebra"])
    yield "same-word", case(["aa", "aa", "aa", "aa"])
    # ตัวอักษรชุดเดียวกันแต่จำนวนไม่เท่า หรือยาวไม่เท่า ต้องไม่นับ
    yield "counts-differ", case(["ab", "aab", "abb", "ba", "b", "a", "bab"])
    yield "max-length", case(["abcdefgh", "hgfedcba", "aaaaaaaa", "zzzzzzzz", "hgfedcbb"])
    yield "rand1", case([random_word("abc", 1, 3) for _ in range(1000)])
    yield "rand2", case([random_word("abcdefghij", 3, 8) for _ in range(5000)])
    yield "big1", case([random_word("abcde", 1, 8) for _ in range(100000)])
    # ทุกคำเป็นคู่สลับอักษรกันหมด จำนวนคู่ 4999950000 เกิน int
    yield "big2", case([shuffled("parallel") for _ in range(100000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
