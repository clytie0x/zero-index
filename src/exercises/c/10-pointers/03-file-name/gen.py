"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/c/10-pointers/03-file-name   (รันที่รากของโปรเจกต์)
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1003)
CHARS = string.ascii_letters + string.digits + "_-"


def make(paths):
    return "\n".join([str(len(paths))] + paths)


def word(low, high):
    return "".join(random.choice(CHARS) for _ in range(random.randint(low, high)))


def rand_path():
    folders = [word(1, 6) + random.choice(["", "", "." + word(1, 3)]) for _ in range(random.randint(0, 5))]
    parts = [word(1, 8) for _ in range(random.randint(1, 3))]
    return "/".join(folders + [".".join(parts)])


def cases():
    yield "sample1", make(["photos/2026/trip.jpg", "readme", "backup.old/notes", "code/week10/swap.c"])
    yield "sample2", make(["music/song.final.mp3", "a.b"])
    # ไม่มีโฟลเดอร์เลย find_last หา / ไม่เจอ ต้องได้ NULL
    yield "no-folder", make(["hello.c", "data", "x.y.z", "Makefile"])
    # จุดอยู่ในชื่อโฟลเดอร์อย่างเดียว ถ้าหาจุดในทั้ง path จะได้คำตอบผิด
    yield "dot-in-folder", make(["v1.2/report", "my.docs/old.files/plan", "a.b/c.d/e", "site.github.io/index"])
    # มีหลายจุด นามสกุลคือส่วนหลังจุดตัวสุดท้าย
    yield "many-dots", make(["archive.tar.gz", "backup/db.2026.10.21.sql", "x/y/a.b.c.d.e"])
    yield "single-char", make(["a", "b/c", "d.e", "f/g.h"])
    long_name = "a" * 49 + "." + "b" * 50
    yield "longest", make(["/".join(["d"] * 50), long_name, "z" * 100])
    yield "rand1", make([rand_path() for _ in range(30)])
    yield "rand2", make([rand_path() for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        assert all(len(p) <= 100 for p in text.split("\n")[1:])
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
