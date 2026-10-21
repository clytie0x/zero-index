"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/06-days-in-month/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/06-days-in-month
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(306)


def cases():
    yield "sample1", "4 2025"
    yield "sample2", "2 2024"
    # ทุกเดือนในปีปกติ จับคนที่สลับ 30 กับ 31 เช่น คิดว่ากรกฎาคมกับสิงหาคมต่างกัน
    for month in range(1, 13):
        yield f"month{month}", f"{month} 2023"
    # กุมภาพันธ์กับทุกกฎของปีอธิกสุรทิน
    yield "feb-1900", "2 1900"
    yield "feb-2000", "2 2000"
    yield "feb-2100", "2 2100"
    yield "feb-2400", "2 2400"
    yield "feb-year1", "2 1"
    yield "feb-year4", "2 4"
    yield "feb-year100", "2 100"
    yield "feb-year9996", "2 9996"
    yield "dec-max", "12 9999"
    for i in range(1, 3):
        yield f"rand{i}", f"{random.randint(1, 12)} {random.randint(1, 9999)}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
