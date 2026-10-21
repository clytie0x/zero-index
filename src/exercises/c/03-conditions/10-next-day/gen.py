"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/10-next-day/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/10-next-day
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(310)


def cases():
    yield "sample1", "14 2 2025"
    yield "sample2", "31 12 2024"
    yield "middle", "15 7 2023"
    yield "first-ever", "1 1 1"
    # วันสุดท้ายของเดือนที่มี 30 วัน และ 31 วัน
    yield "end-of-30", "30 4 2024"
    yield "end-of-nov", "30 11 2023"
    yield "end-of-31", "31 1 2023"
    yield "end-of-jul", "31 7 2023"
    yield "end-of-aug", "31 8 2023"
    # วันที่ 30 ของเดือนที่มี 31 วัน ยังไม่ใช่วันสุดท้าย
    yield "thirty-in-31", "30 1 2023"
    yield "thirty-in-dec", "30 12 2023"
    # กุมภาพันธ์กับทุกกฎของปีอธิกสุรทิน
    yield "feb28-common", "28 2 2023"
    yield "feb28-leap", "28 2 2024"
    yield "feb29-leap", "29 2 2024"
    yield "feb28-1900", "28 2 1900"
    yield "feb28-2000", "28 2 2000"
    yield "feb29-2000", "29 2 2000"
    yield "last-allowed", "30 12 9999"
    yield "year-end-max", "31 12 9998"
    for i in range(1, 3):
        yield f"rand{i}", f"{random.randint(1, 28)} {random.randint(1, 12)} {random.randint(1, 9999)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
