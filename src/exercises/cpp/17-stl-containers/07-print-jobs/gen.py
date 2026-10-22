"""สร้างไฟล์ข้อมูลเข้า tests/*.in ของข้อนี้

    python gen.py
    python tools/make_outputs.py src/exercises/cpp/17-stl-containers/07-print-jobs   (รันที่รากของโปรเจกต์)

ไฟล์ .out สร้างจากเฉลยด้วย tools/make_outputs.py ห้ามเขียนเอง
ชุดที่ชื่อขึ้นต้นด้วย big มี N เป็นแสน ใหญ่เกินกว่าจะเก็บใน git
ทุกชุดต้องมีจำนวนรอบรวมไม่เกินสองล้านตามที่โจทย์รับประกัน gen.py ตรวจไว้ด้วย assert
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1707)


def case(k, jobs):
    rounds = sum((p + k - 1) // k for _, p in jobs)
    assert rounds <= 2000000, rounds
    assert all(jobs[i][0] <= jobs[i + 1][0] for i in range(len(jobs) - 1))
    return f"{len(jobs)} {k}\n" + "\n".join(f"{a} {p}" for a, p in jobs)


def random_jobs(n, arrive_max, page_max):
    arrivals = sorted(random.randint(0, arrive_max) for _ in range(n))
    return [(a, random.randint(1, page_max)) for a in arrivals]


def cases():
    # งานที่ 4 มาถึงวินาทีที่ 8 พอดีตอนงานที่ 3 พิมพ์จบรอบ งานที่ 4 จึงต่อคิวก่อน
    yield "sample1", case(3, [(0, 5), (1, 2), (2, 4), (8, 1)])
    # เครื่องว่างรอระหว่างงาน
    yield "sample2", case(5, [(0, 3), (10, 4)])
    yield "single", case(300000000, [(1000000000, 1000000000)])
    # K ใหญ่มาก กลายเป็นใครมาก่อนได้ก่อน เวลารวมเกิน int ไปมาก
    yield "k-huge", case(1000000000, [(0, 1000000000)] * 5 + [(5, 999999999), (6, 1)])
    # หลายงานมาพร้อมกัน ต้องเรียงตามลำดับในข้อมูลเข้า
    yield "same-arrival", case(2, [(3, 5), (3, 1), (3, 4), (3, 2), (3, 3)])
    # K = 1 สลับทุกหน้า
    yield "k-one", case(1, [(0, 4), (0, 1), (2, 3), (2, 2), (9, 1)])
    # งานมาถึงตอนเครื่องกำลังพิมพ์ และตรงเวลาจบรอบพอดีหลายครั้ง
    yield "ties", case(4, [(0, 8), (4, 4), (4, 1), (8, 5), (12, 4), (13, 2)])
    yield "rand1", case(3, random_jobs(200, 300, 20))
    yield "rand2", case(10, random_jobs(3000, 50000, 100))
    yield "rand3", case(1000, random_jobs(2000, 10**9, 10**6))
    yield "big1", case(1, random_jobs(100000, 1000000, 20))
    yield "big2", case(10**9, [(0, random.randint(10**8, 10**9)) for _ in range(100000)])
    yield "big3", case(3, random_jobs(100000, 10**7, 60))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
