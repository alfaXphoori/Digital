# 🔬 Lab 9: JK Flip-Flop — IC 7473 & Timing Diagram

## วัตถุประสงค์

- ต่อวงจร JK Flip-Flop (7473) บน Tinkercad ได้
- ทดสอบโหมด Set, Reset, Toggle, Hold
- วาด Timing Diagram จากผลทดสอบจริง

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน |
|:---|:---:|
| IC 7473 (Dual JK FF) | 1 |
| LED | 2 |
| Resistor 220Ω | 2 |
| DIP Switch | 2 |
| Push Button | 1 |
| Breadboard | 1 |
| Power Supply 5V | 1 |

---

## ส่วนที่ 1: ทำความเข้าใจ IC 7473 (10 นาที)

### Pin Diagram

```
        ┌───U───┐
  1CLK──┤1    14├── VCC
 1CLR ──┤2    13├── 1Q
   1K ──┤3    12├── 1Q̄
        ┤4    11├── GND
   2K ──┤5    10├── 2CLR
  2CLK──┤6     9├── 2Q̄
   2J ──┤7     8├── 2Q
        └───────┘
```

> ⚠️ **7473 ทำงานที่ขอบขาลง (Negative Edge Triggered)**

### JK FF Truth Table

| J | K | Q⁺ (Next State) | โหมด |
|:---:|:---:|:---:|:---|
| 0 | 0 | Q (ค่าเดิม) | **Hold** |
| 0 | 1 | 0 | **Reset** |
| 1 | 0 | 1 | **Set** |
| 1 | 1 | Q̄ (สลับ) | **Toggle** |

---

## ส่วนที่ 2: ต่อวงจร (15 นาที)

### ขั้นตอน (ใช้ FF ตัวที่ 1)

1. ต่อ **VCC (pin 14)** และ **GND (pin 11)**
2. ต่อ **1CLR (pin 2) → VCC** (ไม่ Clear)
3. ต่อ DIP Switch J → **pin 14** ... ⚠️ ใช้ FF ตัวที่ 2:
   - **2J (pin 7)** ← Switch J
   - **2K (pin 5)** ← Switch K
   - **2CLK (pin 6)** ← Push Button (สร้าง Clock)
   - **2CLR (pin 10)** ← VCC
4. ต่อ **2Q (pin 8)** → Resistor → LED (Q)
5. ต่อ **2Q̄ (pin 9)** → Resistor → LED (Q̄)

---

## ส่วนที่ 3: ทดสอบแต่ละโหมด (20 นาที)

### ทดสอบ 1 — SET (J=1, K=0)

ตั้ง Switch: J=1, K=0 แล้วกด Clock หลายครั้ง

| Clock Pulse | J | K | Q (ก่อน) | Q (หลัง) | โหมด |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 1 | 0 | 0 | | |
| 2 | 1 | 0 | | | |

### ทดสอบ 2 — RESET (J=0, K=1)

| Clock Pulse | J | K | Q (ก่อน) | Q (หลัง) | โหมด |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 1 | 1 | | |
| 2 | 0 | 1 | | | |

### ทดสอบ 3 — TOGGLE (J=1, K=1) ⭐

ตั้ง J=1, K=1 แล้วกด Clock หลายครั้ง สังเกตว่า Q สลับค่าทุกครั้ง

| Clock Pulse | J | K | Q (ก่อน) | Q (หลัง) | สลับ? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | 1 | 0 | | |
| 2 | 1 | 1 | | | |
| 3 | 1 | 1 | | | |
| 4 | 1 | 1 | | | |
| 5 | 1 | 1 | | | |
| 6 | 1 | 1 | | | |

### ทดสอบ 4 — HOLD (J=0, K=0)

| Clock Pulse | J | K | Q (ก่อน) | Q (หลัง) | เปลี่ยน? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 0 | | | |
| 2 | 0 | 0 | | | |

---

## ส่วนที่ 4: วาด Timing Diagram (15 นาที)

จากทดสอบ Toggle (J=1, K=1) วาด Timing Diagram สำหรับ 6 Clock pulses:

```
CLK  ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐
     │ │ │ │ │ │ │ │ │ │ │ │
   ──┘ └─┘ └─┘ └─┘ └─┘ └─┘ └──

Q    
   ──                           
     (วาดจากผลทดสอบ)

Q̄   
   ──
     (วาดจากผลทดสอบ)
```

**คำถาม:** ความถี่ของ Q เทียบกับ CLK เป็นเท่าไร? → $f_Q =$ _________ $\times f_{CLK}$

📸 **Screenshot วงจรในโหมด Toggle**

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจร + ถ่ายรูป Timing Diagram ที่วาดลงกระดาษ
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กรอกคำตอบ → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot วงจร JK FF ที่ต่อเสร็จ
- [ ] ตารางทดสอบครบ 4 โหมด
- [ ] ถ่ายรูป Timing Diagram ที่วาดจากผลจริง
- [ ] ตอบคำถามความถี่
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
