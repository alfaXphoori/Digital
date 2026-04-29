# 🔬 Lab 7: BCD to 7-Segment Display — IC 4511

## วัตถุประสงค์

- ต่อวงจร BCD → 7-Segment Display ด้วย IC 4511
- อ่าน Data Sheet ของ IC 4511 ได้
- เข้าใจการทำงานของ Decoder

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน |
|:---|:---:|
| IC 4511 (BCD to 7-Segment) | 1 |
| 7-Segment Display (Common Cathode) | 1 |
| Resistor 220Ω | 7 |
| DIP Switch | 4 |
| Breadboard | 1 |
| Power Supply 5V | 1 |

---

## ส่วนที่ 1: ทำความเข้าใจ IC 4511 (10 นาที)

### Pin Diagram

```
        ┌───U───┐
   B ──┤1    16├── VCC (+5V)
   C ──┤2    15├── f
  LT ──┤3    14├── g
  BL ──┤4    13├── a
  LE ──┤5    12├── b
   D ──┤6    11├── c
   A ──┤7    10├── d
 GND ──┤8     9├── e
        └───────┘
```

### สัญญาณสำคัญ

| Pin | ชื่อ | หน้าที่ | ต่อกับ |
|:---|:---:|:---|:---|
| A, B, C, D | Input | BCD Input (A=LSB, D=MSB) | DIP Switch |
| a–g | Output | ขับ 7-Segment | 7-Segment Display |
| LT | Lamp Test | ต่อ HIGH = ปกติ, LOW = ติดหมด | VCC |
| BL | Blanking | ต่อ HIGH = ปกติ, LOW = ดับหมด | VCC |
| LE | Latch Enable | ต่อ LOW = แสดงผลปกติ | GND |

> ⚠️ ต้องต่อ **LT = HIGH, BL = HIGH, LE = LOW** ให้ IC ทำงานปกติ

---

## ส่วนที่ 2: ต่อวงจร (25 นาที)

### ขั้นตอน

1. วาง IC 4511 + 7-Segment Display บน breadboard
2. ต่อ **VCC (pin 16)** และ **GND (pin 8)**
3. ต่อ **LT (pin 3) → VCC**, **BL (pin 4) → VCC**, **LE (pin 5) → GND**
4. ต่อ DIP Switch:
   - Switch A → pin 7 (A, LSB)
   - Switch B → pin 1 (B)
   - Switch C → pin 2 (C)
   - Switch D → pin 6 (D, MSB)
5. ต่อ Output a–g ไปยัง 7-Segment Display ผ่าน Resistor 220Ω:
   - pin 13 (a) → Resistor → Segment a
   - pin 12 (b) → Resistor → Segment b
   - pin 11 (c) → Resistor → Segment c
   - pin 10 (d) → Resistor → Segment d
   - pin 9 (e) → Resistor → Segment e
   - pin 15 (f) → Resistor → Segment f
   - pin 14 (g) → Resistor → Segment g

### 7-Segment Layout

```
     ─a─
    │   │
    f   b
    │   │
     ─g─
    │   │
    e   c
    │   │
     ─d─
```

---

## ส่วนที่ 3: ทดสอบแสดงเลข 0–9 (15 นาที)

สลับ DIP Switch (D, C, B, A) แล้วบันทึกผล

| D | C | B | A | BCD (Decimal) | แสดงผล 7-Seg | Segments ที่ติด | ถูกต้อง? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| 0 | 0 | 0 | 0 | 0 | | a,b,c,d,e,f | |
| 0 | 0 | 0 | 1 | 1 | | | |
| 0 | 0 | 1 | 0 | 2 | | | |
| 0 | 0 | 1 | 1 | 3 | | | |
| 0 | 1 | 0 | 0 | 4 | | | |
| 0 | 1 | 0 | 1 | 5 | | | |
| 0 | 1 | 1 | 0 | 6 | | | |
| 0 | 1 | 1 | 1 | 7 | | | |
| 1 | 0 | 0 | 0 | 8 | | | |
| 1 | 0 | 0 | 1 | 9 | | | |

📸 **Screenshot แสดงเลข 0, 5, 9 (3 ภาพ)**

---

## ส่วนที่ 4: ความรู้เพิ่มเติม — การจัดการข้อมูล (Data Routing) (10 นาที) ⭐

1. **Multiplexer (MUX):** ทำหน้าที่เหมือนอะไร?
   - [ ] ตัวแยกสัญญาณ
   - [ ] ตัวเลือกสัญญาณ (Data Selector)
2. **Barrel Shifter:** เป็นวงจรที่สามารถทำอะไรได้ใน 1 Clock?
   - [ ] เลื่อนบิต (Shift) หลายตำแหน่งพร้อมกัน
   - [ ] นับเลขฐานสิบ

---

## ส่วนที่ 5: ทดสอบ Invalid BCD (5 นาที)

ลองใส่ค่าที่ > 9 (Invalid BCD) แล้วสังเกตผล

| D | C | B | A | Decimal | แสดงผล | หมายเหตุ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 1 | 0 | 10 | | |
| 1 | 1 | 1 | 1 | 15 | | |

**คำถาม:** เกิดอะไรขึ้นเมื่อใส่ค่า > 9? ________________________

---

## ส่วนที่ 5: ท้าทาย — Lamp Test & Blanking (5 นาที)

1. ลอง **ถอดสาย LT (pin 3)** แล้วต่อ GND → เกิดอะไร? ________________
2. ลอง **ถอดสาย BL (pin 4)** แล้วต่อ GND → เกิดอะไร? ________________

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจรที่แสดงเลขตามรายการด้านล่าง
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กรอกคำตอบ → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot แสดงเลข 0, 5, 9 (3 ภาพ)
- [ ] ตารางทดสอบเลข 0–9 ครบ
- [ ] ตอบคำถาม Invalid BCD
- [ ] ตอบคำถาม Lamp Test / Blanking
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
