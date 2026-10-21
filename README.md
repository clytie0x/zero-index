# zero-index

เอกสารสอนเขียนโปรแกรมภาษา C แล้วต่อด้วย C++ ตั้งแต่ศูนย์ ไปจนถึงระดับ TOI Zero สำหรับน้องที่เตรียมตัวเข้าค่าย สอวน. คอมพิวเตอร์

อ่านเป็นเว็บได้ที่ https://clytie0x.github.io/zero-index/

## โครงสร้าง

เขียน HTML CSS และ JS เอง ไม่ใช้ framework มีสคริปต์ Python เล็กๆ ประกอบหน้าให้ จึงไม่ต้องเขียนเมนูซ้ำในทุกหน้า

| ที่อยู่ | คืออะไร |
|---|---|
| `src/site.toml` | ลำดับบทและหน้าทั้งหมด เมนูซ้าย ปุ่มก่อนหน้าถัดไป และชื่อแท็บสร้างจากไฟล์นี้ |
| `src/pages/` | เนื้อหาของแต่ละหน้า เก็บเฉพาะ `<article>` |
| `src/layout.html` | โครงหน้าที่ทุกหน้าใช้ร่วมกัน (แถบหัว เมนู ท้ายเว็บ) |
| `src/assets/` | `site.css` `site.js` และ favicon |
| `tools/build.py` | ประกอบหน้าทั้งหมดไปไว้ที่ `dist/` แล้วตรวจลิงก์ |
| `.github/workflows/pages.yml` | build แล้วขึ้น GitHub Pages ทุกครั้งที่ push เข้า `main` |

`dist/` สร้างใหม่ทุกครั้ง ห้ามแก้ไฟล์ในนั้นโดยตรง และไม่ได้เก็บไว้ใน git

## เปิดดูในเครื่อง

ต้องมี Python 3.11 ขึ้นไป ไม่ต้องลงอะไรเพิ่ม

```bash
python tools/build.py --serve
```

แล้วเปิด http://127.0.0.1:8000

## เพิ่มหน้าใหม่

1. สร้างไฟล์ใน `src/pages/` เช่น `src/pages/c/01-variables/index.html` ใส่เนื้อหาไว้ใน `<article class="doc">` และต้องมี `<h1>` เป็นชื่อเดียวกับใน `site.toml`
2. เพิ่มหน้านั้นใน `src/site.toml` ตามลำดับที่ต้องการ
3. รัน `python tools/build.py`

build จะหยุดพร้อมบอกสาเหตุถ้าเจอปัญหาเหล่านี้
- มีหน้าใน `site.toml` แต่ไม่มีไฟล์ หรือมีไฟล์แต่ไม่ได้ใส่ใน `site.toml`
- ลิงก์ชี้ไปไฟล์ที่ไม่มี หรือชี้ไป `#id` ที่ไม่มีในหน้านั้น
- `<h1>` ไม่ตรงกับชื่อใน `site.toml`
- มี `id` ซ้ำในหน้าเดียวกัน

## ส่วนประกอบที่ใช้ในเนื้อหา

| ต้องการ | เขียนแบบนี้ |
|---|---|
| โค้ด C มีสีและเลขบรรทัด | `<div class="code" data-lang="c" data-linenums><pre><code>...</code></pre></div>` |
| ผลลัพธ์ที่โปรแกรมพิมพ์ออกจอ | `<div class="code" data-lang="output" data-title="C:\code\hello.exe"><pre><code>...</code></pre></div>` ขึ้นเป็นหน้าต่างสีดำ |
| ข้อความ error จาก compiler | `<div class="code" data-lang="gcc"><pre><code>...</code></pre></div>` ระบายสีคำว่า error note และ `^` ให้เอง |
| หัวข้อขั้นตอน | `<h2 id="step-1" class="step"><span class="step-label"><span class="step-word">ขั้นที่ </span>1</span> ชื่อขั้น</h2>` |
| แผนที่คอร์สในหน้าแรก | `<!-- course-map -->` build สร้างจากบททั้งหมดใน `site.toml` |
| คำอธิบายโค้ดแบบกดวงกลม | ใส่ `// (1)!` ท้ายบรรทัด เพิ่ม `data-annotate` แล้วตามด้วย `<ol class="anno-list">` |
| กล่องเตือน | `<div class="adm adm-warning" role="note"><p class="adm-title">หัวข้อ</p><p>...</p></div>` ใช้ `adm-note` `adm-tip` `adm-info` `adm-success` ได้ด้วย |
| ปุ่มคีย์บอร์ด | `<span class="keys"><kbd>Ctrl</kbd><span class="plus">+</span><kbd>S</kbd></span>` |
| ที่ว่างรอภาพหน้าจอ | `<div class="shot">คำอธิบายภาพ</div>` |

ดูตัวอย่างการใช้ครบทุกแบบได้ที่ `src/pages/c/00-start/hello.html`

## สถานะ

`active` กำลังเขียนทีละบท ตอนนี้มีบทที่ 0
