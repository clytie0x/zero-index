"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/09-recursion/05-spaced-seats   (รันที่รากของโปรเจกต์)

ทุก n มีคำตอบเดียว จึงเลือก n ให้ครอบคลุมค่าน้อยสุด ค่ากลาง และค่ามากสุด
ชุด n = 20 มีคำตอบราว 370 KB จึงตั้งชื่อขึ้นต้นด้วย big เพื่อไม่เก็บใน git
ข้อนี้ไม่มี naive.c เพราะทุกวิธีต้องพิมพ์ทุกแบบเหมือนกัน
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent


def cases():
    yield "sample1", "3"
    yield "min", "1"
    yield "two", "2"
    yield "four", "4"
    yield "seven", "7"
    yield "ten", "10"
    yield "fifteen", "15"
    yield "big-max", "20"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
