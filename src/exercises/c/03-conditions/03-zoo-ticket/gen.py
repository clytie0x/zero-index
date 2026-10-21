"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/03-zoo-ticket/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/03-zoo-ticket
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent


def cases():
    yield "sample1", "8"
    yield "sample2", "35"
    # อายุสองฝั่งของทุกขอบ รวมค่าน้อยสุดและมากสุด
    for age in (0, 2, 3, 12, 13, 59, 60, 120):
        yield f"age{age}", str(age)


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
