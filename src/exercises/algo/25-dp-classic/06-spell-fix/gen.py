"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/25-dp-classic/06-spell-fix   (รันที่รากของโปรเจกต์)

ข้อนี้ไม่มี naive เพราะวิธีตรงไปตรงมาคือ recursion ที่ใช้ได้แค่คำสั้นมาก
long1 กับ long2 ยาว 2000 ตัว ใช้ตรวจว่าตารางเต็มหรือสองแถวก็ทันเวลา
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2506)

LETTERS = "abcdefghijklmnopqrstuvwxyz"


def word(length, letters=LETTERS):
    return "".join(random.choice(letters) for _ in range(length))


def mutate(text, edits):
    chars = list(text)
    for _ in range(edits):
        kind = random.randint(0, 2)
        pos = random.randint(0, len(chars) - 1)
        if kind == 0:
            chars[pos] = random.choice(LETTERS)
        elif kind == 1 and len(chars) > 1:
            del chars[pos]
        else:
            chars.insert(pos, random.choice(LETTERS))
    return "".join(chars)


def cases():
    yield "sample1", "nakornpathom\nnakhonpathom"
    yield "sample2", "kanchanaburi\nkanjanaburi"
    yield "same", "phitsanulok\nphitsanulok"
    yield "one-char", "a\nb"
    yield "all-different", "aaaa\nbbbbbbb"
    # คำแรกเป็นส่วนหน้าของคำที่สอง ต้องแทรกท้ายอย่างเดียว
    yield "prefix", "nakhon\nnakhonratchasima"
    yield "delete-middle", "suphanburi\nsuburi"
    yield "reversed", "abcdefgh\nhgfedcba"
    yield "rand1", word(15, "abc") + "\n" + word(12, "abc")
    yield "long1", word(2000) + "\n" + word(2000)
    base = word(2000)
    yield "long2", base + "\n" + mutate(base, 25)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
