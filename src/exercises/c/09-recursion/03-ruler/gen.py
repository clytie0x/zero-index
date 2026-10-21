"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/09-recursion/03-ruler   (รันที่รากของโปรเจกต์)

ทุก K มีคำตอบเดียว จึงเลือก K ให้ครอบคลุมค่าน้อยสุด ค่ากลาง และค่ามากสุด
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent


def cases():
    yield "sample1", "3"
    yield "min", "1"
    yield "two", "2"
    yield "four", "4"
    yield "five", "5"
    yield "eight", "8"
    yield "twelve", "12"
    yield "max", "15"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
