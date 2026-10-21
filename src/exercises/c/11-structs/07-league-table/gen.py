"""สร้างไฟล์ .in ของข้อนี้ แล้วสร้าง .out จากเฉลยด้วย make_outputs.py

    python src/exercises/c/11-structs/07-league-table/gen.py
    python tools/make_outputs.py src/exercises/c/11-structs/07-league-table
"""

import random
import string
from pathlib import Path

HERE = Path(__file__).resolve().parent
random.seed(1107)


def team_names(n):
    result = []
    while len(result) < n:
        name = random.choice(string.ascii_uppercase) + "".join(
            random.choice(string.ascii_lowercase) for _ in range(random.randint(2, 14)))
        if name not in result:
            result.append(name)
    return result


def league(names, matches):
    lines = [f"{len(names)} {len(matches)}", " ".join(names)]
    lines += [f"{a} {b} {x} {y}" for a, b, x, y in matches]
    return "\n".join(lines)


def random_matches(names, m, max_goals):
    out = []
    for _ in range(m):
        a, b = random.sample(names, 2)
        out.append((a, b, random.randint(0, max_goals), random.randint(0, max_goals)))
    return out


def cases():
    yield "sample1", league(["Lions", "Tigers", "Eagles", "Sharks"], [
        ("Lions", "Tigers", 2, 1), ("Eagles", "Sharks", 0, 0), ("Lions", "Eagles", 1, 3),
        ("Tigers", "Sharks", 4, 0), ("Lions", "Sharks", 2, 2), ("Tigers", "Eagles", 1, 1)])
    # แต้มเท่ากัน ทีมที่ยิงได้มากกว่ากลับอยู่ต่ำกว่า เพราะผลต่างประตูน้อยกว่า
    yield "sample2", league(["Alpha", "Beta", "Gamma", "Delta"], [
        ("Alpha", "Gamma", 10, 9), ("Beta", "Delta", 3, 0), ("Gamma", "Delta", 0, 0)])
    # แต้มเท่ากันหมด ผลต่างประตูกับประตูได้เรียงลำดับเดียวกัน
    yield "gd-and-gf", league(["Red", "Blue", "Green"], [
        ("Red", "Blue", 3, 0), ("Blue", "Green", 2, 0), ("Green", "Red", 1, 0)])
    # สามทีมแต้มเท่ากัน ลำดับตามผลต่างประตูกลับกันกับลำดับตามประตูได้
    yield "gd-vs-gf", league(["Pa", "Qa", "Ra", "Sa", "Ta"], [
        ("Pa", "Sa", 8, 7), ("Ta", "Qa", 0, 2), ("Ra", "Sa", 5, 1)])
    # แต้มและผลต่างเท่ากัน ต่างกันที่ประตูได้
    yield "goals-tie", league(["Ant", "Bee", "Cat", "Dog"], [
        ("Ant", "Bee", 1, 1), ("Cat", "Dog", 4, 4), ("Ant", "Dog", 2, 1), ("Cat", "Bee", 3, 2)])
    # ทุกนัดเสมอ 0 0 ทุกเกณฑ์เท่ากัน ต้องเรียงด้วยชื่อ
    names = ["Zulu", "Mike", "Alpha", "Kilo", "Bravo"]
    yield "name-tie", league(names, [(a, b, 0, 0) for a in names for b in names if a != b])
    yield "no-matches", league(["Pear", "Apple", "Mango", "Fig"], [])
    yield "three-teams", league(["X", "Y", "Z"], [("Z", "X", 20, 0), ("Y", "Z", 20, 19)])
    # ทีมเดียวชนะทุกนัด อันดับ 2 และ 3 มีผลต่างประตูติดลบ
    yield "negative-diff", league(["Giant", "Small", "Tiny", "Mini"], [
        ("Giant", "Small", 5, 0), ("Tiny", "Giant", 0, 7), ("Giant", "Mini", 3, 1),
        ("Small", "Tiny", 1, 0), ("Mini", "Small", 2, 2)])
    # ชื่อที่เป็นส่วนต้นของกันและกัน
    yield "prefix-names", league(["Ab", "A", "Abc", "B"], [
        ("A", "Ab", 1, 1), ("Abc", "B", 0, 0), ("Ab", "Abc", 2, 2), ("B", "A", 1, 1)])
    names = team_names(8)
    yield "rand1", league(names, random_matches(names, 40, 4))
    names = team_names(20)
    yield "rand2", league(names, random_matches(names, 500, 20))
    names = team_names(20)
    yield "rand3", league(names, random_matches(names, 500, 1))


def main():
    tests = HERE / "tests"
    tests.mkdir(exist_ok=True)
    for case_name, text in cases():
        (tests / f"{case_name}.in").write_text(text + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
