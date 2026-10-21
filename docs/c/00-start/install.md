# 0.2 ติดตั้ง Code::Blocks

**Code::Blocks** คือโปรแกรมสำหรับเขียนโค้ด (เรียกว่า IDE) รวมที่พิมพ์โค้ด ปุ่มแปล และปุ่มรันไว้ในที่เดียว ตัวติดตั้งที่เราจะใช้มี compiler GCC แถมมาด้วย ติดตั้งครั้งเดียวจบ

เอกสารนี้ใช้ **Code::Blocks 25.03** บน Windows 64-bit

## ขั้นที่ 1 ดาวน์โหลด

เข้าหน้าดาวน์โหลดทางการ

[codeblocks.org/downloads/binaries :material-open-in-new:](https://www.codeblocks.org/downloads/binaries/){ .md-button }

หน้านั้นมีไฟล์ให้เลือกหลายตัว ให้เลือกตัวนี้ **ตัวเดียว**

```text
codeblocks-25.03mingw-setup.exe
```

ในแถวของไฟล์นี้ กดลิงก์ **SourceForge** แล้วรอให้ดาวน์โหลดเริ่มเอง หรือกดลิงก์ตรงด้านล่าง

[ดาวน์โหลด codeblocks-25.03mingw-setup.exe :material-download:](https://sourceforge.net/projects/codeblocks/files/Binaries/25.03/Windows/codeblocks-25.03mingw-setup.exe/download){ .md-button .md-button--primary }

!!! warning "ต้องมีคำว่า mingw ในชื่อไฟล์"
    ไฟล์ `codeblocks-25.03-setup.exe` ที่ไม่มีคำว่า **mingw** จะไม่มี compiler มาด้วย ติดตั้งเสร็จแล้วจะกดรันโค้ดไม่ได้ ถ้าโหลดผิดตัว ให้ถอนการติดตั้งแล้วโหลดใหม่

<div class="shot">หน้าดาวน์โหลด วงกลมแถว codeblocks-25.03mingw-setup.exe และลิงก์ SourceForge</div>

## ขั้นที่ 2 ติดตั้ง

ดับเบิลคลิกไฟล์ที่โหลดมา แล้วกดตามนี้

1. หน้า Welcome กด **Next**
2. หน้า License Agreement กด **I Agree**
3. หน้า Choose Components เลือกแบบ **Full** แล้วกด **Next**
4. หน้า Choose Install Location ไม่ต้องแก้อะไร กด **Install**
5. รอจนเสร็จ ถ้าถามว่าจะเปิด Code::Blocks เลยไหม ตอบ **Yes**

<div class="shot">หน้า Choose Components ที่เลือก Full</div>

!!! info "ถ้า Windows ขึ้นกล่องสีน้ำเงินเตือน"
    บางเครื่องจะขึ้นว่า Windows protected your PC เพราะไฟล์มาจากอินเทอร์เน็ต ถ้าโหลดมาจากลิงก์ในหน้านี้ ให้กด **More info** แล้วกด **Run anyway**

## ขั้นที่ 3 เปิดครั้งแรก

ตอนเปิดครั้งแรกจะมีหน้าต่างเด้งขึ้นมาสองอัน

### หน้าต่าง Compilers auto-detection

Code::Blocks ค้นหา compiler ในเครื่อง จะเห็นบรรทัด **GNU GCC Compiler** ขึ้นสถานะว่า Detected

1. คลิกที่บรรทัด **GNU GCC Compiler**
2. กด **Set as default**
3. กด **OK**

<div class="shot">หน้าต่าง Compilers auto-detection ที่ GNU GCC Compiler ขึ้น Detected</div>

### หน้าต่าง File associations

ถามว่าจะให้ไฟล์โค้ดเปิดด้วย Code::Blocks ไหม เลือก **Yes, associate Code::Blocks with C/C++ file types** แล้วกด **OK**

ต่อไปดับเบิลคลิกไฟล์ `.c` ที่ไหนก็จะเปิดใน Code::Blocks

## ขั้นที่ 4 ตั้งค่า

ตั้งครั้งเดียว ใช้ได้ตลอด

### เปิดคำเตือนจาก compiler

ให้ compiler ช่วยบอกจุดที่น่าจะเขียนผิด ถึงโปรแกรมจะยังรันได้ก็ตาม

1. เมนู **Settings > Compiler...**
2. แท็บ **Compiler settings** แล้วแท็บย่อย **Compiler Flags**
3. ติ๊กช่อง **Enable all common compiler warnings (overrides many other settings) [-Wall]**
4. กด **OK**

<div class="shot">หน้า Compiler Flags ที่ติ๊ก -Wall แล้ว</div>

### ปรับตัวอักษรให้อ่านง่าย

1. เมนู **Settings > Editor...**
2. ตรง Font กด **Choose** แล้วเลือกขนาดที่อ่านสบาย แนะนำ 12 ขึ้นไป
3. ตรง TAB options ตั้ง **TAB size in spaces** เป็น **4**
4. กด **OK**

## ขั้นที่ 5 เตรียมโฟลเดอร์เก็บงาน

สร้างโฟลเดอร์ใหม่ที่

```text
C:\code
```

งานทุกชิ้นในเอกสารนี้ให้เก็บที่นี่ ที่เดียว หาไฟล์เจอง่าย ไม่ปนกับไฟล์อื่นบน Desktop

!!! success "ติดตั้งเสร็จแล้ว"
    ไปหน้าถัดไปเพื่อเขียนโปรแกรมแรก
