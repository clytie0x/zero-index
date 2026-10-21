# zero-index

เอกสารสอนเขียนโปรแกรมภาษา C แล้วต่อด้วย C++ ตั้งแต่ศูนย์ ไปจนถึงระดับ TOI Zero สำหรับน้องที่เตรียมตัวเข้าค่าย สอวน. คอมพิวเตอร์

อ่านเป็นเว็บได้ที่ https://clytie0x.github.io/zero-index/

## โครงสร้าง

| ที่อยู่ | คืออะไร |
|---|---|
| `docs/` | เนื้อหาทุกบท เขียนเป็น Markdown |
| `docs/c/` | ช่วงภาษา C |
| `mkdocs.yml` | ตั้งค่าเว็บและสารบัญ |
| `.github/workflows/pages.yml` | build และขึ้น GitHub Pages ทุกครั้งที่ push เข้า `main` |

## เปิดดูในเครื่อง

```bash
python -m venv .venv
.venv/Scripts/pip install -r requirements.txt
.venv/Scripts/mkdocs serve
```

แล้วเปิด http://127.0.0.1:8000

## สถานะ

`active` กำลังเขียนทีละบท ตอนนี้มีบทที่ 0
