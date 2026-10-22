"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/28-shortest-paths/09-meeting-town   (รันที่รากของโปรเจกต์)

parallel ดักการตั้งตารางด้วยถนนเส้นที่อ่านทีหลังแทนเส้นที่สั้นที่สุด
order ดักการวางลูป k ไว้ในสุด (ทางที่ดีที่สุดต้องแวะหลายเมือง)
tie มีสองเมืองที่ผลรวมเท่ากัน split และ rand3 มีเพื่อนอยู่คนละก้อนจึงตอบ -1
over-int rand2 rand4 และ big1 มีผลรวมเกิน int big1 ใช้ขอบเขตสูงสุด ไม่มี naive เพราะ N เล็ก
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2809)


def build(n, edges, homes):
    rows = [f"{n} {len(edges)} {len(homes)}"] + [f"{u} {v} {w}" for u, v, w in edges]
    rows.append(" ".join(map(str, homes)))
    return "\n".join(rows)


def random_graph(n, m, top, nodes=None):
    nodes = nodes if nodes is not None else list(range(1, n + 1))
    order = nodes[:]
    random.shuffle(order)
    edges = [(order[random.randrange(i)], order[i], random.randint(1, top)) for i in range(1, len(order))]
    while len(edges) < m:
        u, v = random.sample(nodes, 2)
        edges.append((u, v, random.randint(1, top)))
    random.shuffle(edges)
    return edges


def cases():
    yield "sample1", "5 6 3\n1 2 4\n2 3 3\n3 4 2\n4 5 6\n1 5 20\n2 4 9\n1 3 5"
    yield "sample2", "4 2 2\n1 2 5\n3 4 5\n1 4"
    yield "single", "1 0 3\n1 1 1"
    yield "parallel", build(3, [(1, 2, 50), (1, 2, 5), (2, 3, 5), (2, 3, 70), (1, 3, 100)], [1, 3])
    # ทางที่ดีที่สุดจาก 1 ไป 2 ต้องแวะ 3 แล้ว 4 ทุกเมืองได้ผลรวมเท่ากัน จึงตอบเมือง 1
    yield "order", build(4, [(1, 2, 10), (1, 3, 1), (3, 4, 2), (4, 2, 3)], [1, 2])
    yield "tie", build(4, [(1, 2, 7), (2, 3, 7), (3, 4, 7)], [1, 4])
    yield "over-int", build(4, [(1, 2, 10**9), (2, 3, 10**9), (3, 4, 10**9)], [1, 1, 4, 4, 1])
    yield "split", build(6, random_graph(3, 3, 50, [1, 2, 3]) + random_graph(3, 3, 50, [4, 5, 6]), [2, 3, 6])
    yield "rand1", build(20, random_graph(20, 40, 100), [random.randint(1, 20) for _ in range(6)])
    yield "rand2", build(300, random_graph(300, 8000, 10**9), [random.randint(1, 300) for _ in range(1000)])
    left = list(range(1, 301, 2))
    right = list(range(2, 301, 2))
    edges = random_graph(300, 2000, 10**6, left) + random_graph(300, 2000, 10**6, right)
    random.shuffle(edges)
    yield "rand3", build(300, edges, [random.choice(left) for _ in range(999)] + [random.choice(right)])
    # ถนนน้อย ทางยาว ผลรวมสูง
    yield "rand4", build(300, random_graph(300, 320, 10**9), [random.randint(1, 300) for _ in range(1000)])
    # ขอบเขตสูงสุด ถนนห้าหมื่นเส้น ไฟล์ใหญ่เกินจะเก็บใน git จึงขึ้นต้นด้วย big
    yield "big1", build(300, random_graph(300, 50000, 10**9), [random.randint(1, 300) for _ in range(1000)])


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, text in cases():
        (tests / f"{name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
