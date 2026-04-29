# 🔬 Lab 3: Logic Gates — ต่อวงจรเกตลอจิกบน Tinkercad

## วัตถุประสงค์

- ต่อวงจร AND, OR, NOT Gate ด้วย IC จริงบน Tinkercad
- อ่าน Pin Diagram จาก Data Sheet ได้
- ตรวจสอบ Truth Table ด้วย LED

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน | หมายเหตุ |
|:---|:---:|:---|
| IC 7408 (Quad AND) | 1 | 4 เกต AND 2-input |
| IC 7432 (Quad OR) | 1 | 4 เกต OR 2-input |
| IC 7404 (Hex NOT) | 1 | 6 เกต NOT |
| LED | 3 | แสดงผล output |
| Resistor 220Ω | 3 | ต่ออนุกรมกับ LED |
| DIP Switch / Push Button | 2 | ใส่ input A, B |
| Breadboard | 1 | |
| Power Supply 5V | 1 | VCC = 5V, GND = 0V |

---

## ส่วนที่ 1: อ่าน Pin Diagram (10 นาที)

### IC 7408 — Quad 2-input AND Gate

```
        ┌───U───┐
  1A  ──┤1    14├── VCC (+5V)
  1B  ──┤2    13├── 4B
  1Y  ──┤3    12├── 4A
  2A  ──┤4    11├── 4Y
  2B  ──┤5    10├── 3B
  2Y  ──┤6     9├── 3A
 GND ──┤7     8├── 3Y
        └───────┘
```

> ⚠️ **ทุก IC ต้องต่อ VCC (pin 14) = +5V และ GND (pin 7) = 0V เสมอ!**

**คำถาม:** ถ้าต้องการใช้ AND gate ตัวที่ 1 ของ 7408 → Input อยู่ pin _____ กับ _____ , Output อยู่ pin _____

---

## ส่วนที่ 2: ต่อวงจร AND Gate (15 นาที)

### ขั้นตอน

1. วาง **Breadboard** และ **Power Supply 5V**
2. วาง **IC 7408** บน breadboard
3. ต่อ **pin 14 → VCC**, **pin 7 → GND**
4. ต่อ Switch A → **pin 1** (1A)
5. ต่อ Switch B → **pin 2** (1B)
6. ต่อ **pin 3** (1Y) → **Resistor 220Ω** → **LED** → **GND**
7. กด **Start Simulation**

### ทดสอบ Truth Table

สลับ Switch A, B ทุกรูปแบบ บันทึกผล LED (ติด = 1, ดับ = 0)

| A | B | Output (LED) | ตรงกับ AND? |
|:---:|:---:|:---:|:---:|
| 0 | 0 | | |
| 0 | 1 | | |
| 1 | 0 | | |
| 1 | 1 | | |

📸 **Screenshot วงจร AND Gate ที่ Output = 1**

---

## ส่วนที่ 3: ต่อวงจร OR Gate (10 นาที)

### ขั้นตอน

1. วาง **IC 7432** บน breadboard
2. ต่อ **VCC** และ **GND**
3. ต่อ Switch A → **pin 1**, Switch B → **pin 2**
4. ต่อ **pin 3** → Resistor → LED → GND

### ทดสอบ Truth Table

| A | B | Output (LED) | ตรงกับ OR? |
|:---:|:---:|:---:|:---:|
| 0 | 0 | | |
| 0 | 1 | | |
| 1 | 0 | | |
| 1 | 1 | | |

📸 **Screenshot วงจร OR Gate ที่ Output = 1 (A=0, B=1)**

---

## ส่วนที่ 4: ต่อวงจร NOT Gate (10 นาที)

### IC 7404 — Hex Inverter

```
        ┌───U───┐
  1A  ──┤1    14├── VCC
  1Y  ──┤2    13├── 6A
  2A  ──┤3    12├── 6Y
  2Y  ──┤4    11├── 5A
  3A  ──┤5    10├── 5Y
  3Y  ──┤6     9├── 4A
 GND ──┤7     8├── 4Y
        └───────┘
```

### ทดสอบ

| A (Input) | Y (Output LED) | ตรงกับ NOT? |
|:---:|:---:|:---:|
| 0 | | |
| 1 | | |

---

## ส่วนที่ 5: สัญญาณเอาต์พุตพิเศษ (10 นาที) ⭐

1. **Tri-State Logic:** ถ้าเกตตัวหนึ่งมีสถานะเป็น **Hi-Z** (High Impedance) หมายความว่าอะไร?
   - [ ] แรงดันเป็น 5V
   - [ ] แรงดันเป็น 0V
   - [ ] เสมือนการปลดสายสัญญาณ (เปิดสวิตช์) ออกจากวงจร

2. **Open-Collector:** ทำไมไอซีประเภท Open-collector (เช่น 7407) ถึงต้องต่อ **Pull-up Resistor** ที่เอาต์พุตเสมอ?
   _________________________________________________________

---

## ส่วนที่ 6: ท้าทาย — NAND จาก AND + NOT (15 นาที)

ต่อ **AND gate (7408)** ตามด้วย **NOT gate (7404)** เพื่อสร้าง **NAND function**

```
A ──┐
    ├──[7408 AND]──output──[7404 NOT]──LED
B ──┘
```

### ทดสอบ Truth Table

| A | B | AND output | NAND output (LED) | ตรงกับ NAND? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | | | |
| 0 | 1 | | | |
| 1 | 0 | | | |
| 1 | 1 | | | |

📸 **Screenshot วงจร NAND ที่ต่อเสร็จ**

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจรแต่ละส่วนตามรายการด้านล่าง
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot วงจร AND Gate (Output = 1)
- [ ] Screenshot วงจร OR Gate (Output = 1, A=0, B=1)
- [ ] Screenshot วงจร NAND (ต่อเสร็จ)
- [ ] Truth Table ครบทุกตาราง (ถ่ายรูปหรือพิมพ์ลงใน Form)
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
