"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/09-recursion/06-gift-draw   (รันที่รากของโปรเจกต์)

ทุก n มีคำตอบเดียว จึงใช้ n ทุกค่าตั้งแต่ 1 ถึง 8
n = 1 ไม่มีแบบที่เป็นไปได้ จับคนที่ลืมพิมพ์ none
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent


def cases():
    yield "sample1", "3"
    yield "none", "1"
    yield "two", "2"
    yield "four", "4"
    yield "five", "5"
    yield "six", "6"
    yield "seven", "7"
    yield "max", "8"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
