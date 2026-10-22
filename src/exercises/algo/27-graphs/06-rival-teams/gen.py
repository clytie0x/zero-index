"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python gen.py
    python tools/make_outputs.py src/exercises/algo/27-graphs/06-rival-teams   (รันที่รากของโปรเจกต์)

ทุกชุดยกเว้นตัวอย่างสลับหมายเลขนักเรียนแบบสุ่ม
ชุดที่ชื่อขึ้นต้นด้วย big มีราวสองแสนคน big1 เป็นเส้นตรงเส้นเดียวที่มีคนลงทะเบียนสีแดงไว้ฝั่งที่ใหญ่กว่า
big2 เป็นวงจำนวนคี่วงเดียว big3 เป็นกราฟสองฝั่งสุ่มหลายกลุ่มที่บางกลุ่มมีคนลงทะเบียน
big1 กับ big2 ทำให้ DFS แบบ recursion ลึกเกือบสองแสนชั้นและพัง
star big1 groups rand บังคับให้บางกลุ่มต้องให้ฝั่งที่ใหญ่กว่าเป็นสีแดง ดักวิธีที่เลือกฝั่งเล็กเสมอ
sample2 clash มีคนลงทะเบียนสองคนในกลุ่มเดียวกันที่สีขัดกัน ดักวิธีที่ดูแค่คนลงทะเบียนคนแรกของกลุ่ม
ข้อนี้ไม่มี naive.cpp เพราะการลองแบ่งทุกแบบใช้ได้แค่ N ไม่เกินราว 20
"""

import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(2706)


def relabel(n, edges, regs=()):
    label = [0] + random.sample(range(1, n + 1), n)
    edges = [(label[a], label[b]) if random.random() < 0.5 else (label[b], label[a]) for a, b in edges]
    random.shuffle(edges)
    regs = [(label[v], color) for v, color in regs]
    random.shuffle(regs)
    return n, edges, regs


def chain(n, first=1):
    return [(v, v + 1) for v in range(first, first + n - 1)]


def ring(n, first=1):
    return chain(n, first) + [(first, first + n - 1)]


def bipartite_part(first, left, right, m):
    """กลุ่มหนึ่งที่มีฝั่งซ้าย left คนและฝั่งขวา right คน เชื่อมเป็นต้นไม้ก่อนให้ถึงกันหมด แล้วเติมเส้นสุ่มให้ครบ m"""
    a = list(range(first, first + left))
    b = list(range(first + left, first + left + right))
    order = [a[0], b[0]] + random.sample(a[1:] + b[1:], left + right - 2)
    placed = ([], [])
    edges = {(a[0], b[0])}
    for v in order:
        side = 0 if v < first + left else 1
        if placed[1 - side] and v not in (a[0], b[0]):
            u = random.choice(placed[1 - side])
            edges.add((min(u, v), max(u, v)))
        placed[side].append(v)
    while len(edges) < m:
        u, v = random.choice(a), random.choice(b)
        edges.add((min(u, v), max(u, v)))
    return sorted(edges)


def groups(sizes, extra):
    edges, first = [], 1
    for left, right in sizes:
        edges += bipartite_part(first, left, right, min(left * right, left + right - 1 + extra))
        first += left + right
    return first - 1, edges


def sides(n, edges):
    """เลขกลุ่มและฝั่ง 0 หรือ 1 ของทุกคน ใช้กับกราฟสองฝั่งเท่านั้น"""
    adj = [[] for _ in range(n + 1)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    group, side = [0] * (n + 1), [0] * (n + 1)
    count = 0
    for s in range(1, n + 1):
        if group[s]:
            continue
        count += 1
        group[s] = count
        todo = [s]
        while todo:
            v = todo.pop()
            for u in adj[v]:
                if not group[u]:
                    group[u] = count
                    side[u] = 1 - side[v]
                    todo.append(u)
    return count, group, side


def register(n, edges, share, prefer_big):
    """สุ่มกลุ่มราว share ส่วนให้มีคนลงทะเบียน 1 ถึง 3 คนที่สีไม่ขัดกัน
    กลุ่มที่ถูกเลือกให้ฝั่งที่ใหญ่กว่าเป็นสีแดงด้วยความน่าจะเป็น prefer_big"""
    count, group, side = sides(n, edges)
    members = [[] for _ in range(count + 1)]
    for v in range(1, n + 1):
        members[group[v]].append(v)
    regs = []
    for g in range(1, count + 1):
        if random.random() >= share:
            continue
        size = [0, 0]
        for v in members[g]:
            size[side[v]] += 1
        big = 0 if size[0] >= size[1] else 1
        red_side = big if random.random() < prefer_big else 1 - big
        for v in random.sample(members[g], min(len(members[g]), random.randint(1, 3))):
            regs.append((v, "R" if side[v] == red_side else "B"))
    return regs


def text(n, edges, regs=()):
    lines = [f"{n} {len(edges)} {len(regs)}"] + [f"{a} {b}" for a, b in edges] + [f"{v} {c}" for v, c in regs]
    return "\n".join(lines)


def cases():
    yield "sample1", "\n".join(["9 9 2", "1 2", "1 4", "2 3", "2 5", "4 5", "5 6", "3 6", "7 8", "8 9", "9 R", "2 B"])
    yield "sample2", "\n".join(["3 2 2", "1 2", "2 3", "1 R", "3 B"])
    yield "single", "1 0 0"
    yield "single-red", "1 0 1\n1 R"
    yield "no-rivals", "\n".join(["6 0 3", "2 R", "5 B", "6 R"])
    yield "even-ring", text(*relabel(1000, ring(1000)))
    yield "odd-ring", text(*relabel(999, ring(999)))
    yield "star", text(*relabel(300, [(1, v) for v in range(2, 301)], [(1, "B")]))
    n, edges = groups([(random.randint(1, 8), random.randint(1, 8)) for _ in range(40)], 3)
    yield "groups", text(*relabel(n, edges, register(n, edges, 0.5, 0.7)))
    n, edges = groups([(random.randint(5, 30), random.randint(5, 30)) for _ in range(50)], 20)
    yield "rand", text(*relabel(n, edges, register(n, edges, 0.5, 0.7)))
    n, edges = groups([(random.randint(2, 10), random.randint(2, 10)) for _ in range(30)], 5)
    side = sides(n, edges)[2]
    yield "all-registered", text(*relabel(n, edges, [(v, "R" if side[v] == 0 else "B") for v in range(1, n + 1)]))
    sizes = [(random.randint(5, 30), random.randint(5, 30)) for _ in range(50)]
    n, edges = groups(sizes, 20)
    last_left = n - sum(sizes[-1]) + 1
    edges.append((last_left, last_left + 1))
    yield "late-conflict", text(n, edges)
    sizes = [(random.randint(5, 30), random.randint(5, 30)) for _ in range(50)]
    n, edges = groups(sizes, 20)
    first = sum(map(sum, sizes[:30])) + 1
    left, right = sizes[30]
    regs = [(v, c) for v, c in register(n, edges, 0.5, 0.5) if not first <= v < first + left + right]
    regs += [(first, "R"), (first + left, "R")]
    yield "clash", text(*relabel(n, edges, regs))
    yield "big1", text(*relabel(199999, chain(199999), [(1, "R"), (199999, "R")]))
    yield "big2", text(*relabel(199999, ring(199999)))
    sizes = []
    while sum(map(sum, sizes)) < 190000:
        sizes.append((random.randint(10, 1500), random.randint(10, 1500)))
    n, edges = groups(sizes[:-1], 50)
    yield "big3", text(*relabel(n, edges, register(n, edges, 0.5, 0.7)))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for name, data in cases():
        (tests / f"{name}.in").write_text(data + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
