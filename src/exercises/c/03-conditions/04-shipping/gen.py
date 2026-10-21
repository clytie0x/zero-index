"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/03-conditions/04-shipping/gen.py
    python tools/make_outputs.py src/exercises/c/03-conditions/04-shipping
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent


def cases():
    yield "sample1", "1 750"
    yield "sample2", "2 3200"
    # ทุกพื้นที่ คูณกับน้ำหนักสองฝั่งของทุกขอบ รวมค่าน้อยสุดและมากสุด
    for zone in (1, 2):
        for weight in (1, 1000, 1001, 5000, 5001, 20000):
            yield f"zone{zone}-w{weight}", f"{zone} {weight}"


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
