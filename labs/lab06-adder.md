# 🔬 Lab 6: Half Adder & Full Adder — วงจรบวกเลขฐานสอง

## วัตถุประสงค์

- ต่อวงจร Half Adder บน Tinkercad ได้
- ต่อวงจร Full Adder บน Tinkercad ได้
- เข้าใจความสัมพันธ์ระหว่าง Truth Table → สมการ → วงจร

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน |
|:---|:---:|
| IC 7486 (XOR) | 1 |
| IC 7408 (AND) | 1 |
| IC 7432 (OR) | 1 |
| LED | 2 |
| Resistor 220Ω | 2 |
| DIP Switch | 3 |
| Breadboard | 1 |
| Power Supply 5V | 1 |

---

## ส่วนที่ 1: Half Adder (20 นาที)

### ทบทวนทฤษฎี

| A | B | Sum (S) | Carry (C) |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

$$S = A \oplus B \quad \text{(XOR)}$$
$$C = A \cdot B \quad \text{(AND)}$$

### IC 7486 — Quad 2-input XOR

```
        ┌───U───┐
  1A  ──┤1    14├── VCC
  1B  ──┤2    13├── 4B
  1Y  ──┤3    12├── 4A
  2A  ──┤4    11├── 4Y
  2B  ──┤5    10├── 3B
  2Y  ──┤6     9├── 3A
 GND ──┤7     8├── 3Y
        └───────┘
```

### ขั้นตอนต่อวงจร

```
Switch A ──┬──[7486 XOR pin 1,2→3]── LED (Sum)
           │
Switch B ──┼──[7408 AND pin 1,2→3]── LED (Carry)
           │
           └──(ต่อ A,B เข้าทั้ง XOR และ AND)
```

1. ต่อ Switch A → pin 1 ของ 7486 **และ** pin 1 ของ 7408
2. ต่อ Switch B → pin 2 ของ 7486 **และ** pin 2 ของ 7408
3. pin 3 ของ 7486 (Sum) → Resistor → LED → GND
4. pin 3 ของ 7408 (Carry) → Resistor → LED → GND

### ทดสอบ

| A | B | LED Sum | LED Carry | ถูกต้อง? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | | | |
| 0 | 1 | | | |
| 1 | 0 | | | |
| 1 | 1 | | | |

📸 **Screenshot: Half Adder เมื่อ A=1, B=1 (Sum=0, Carry=1)**

---

## ส่วนที่ 2: Full Adder (30 นาที)

### ทบทวนทฤษฎี

| A | B | Cin | Sum | Cout |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

$$Sum = A \oplus B \oplus C_{in}$$
$$C_{out} = (A \cdot B) + (C_{in} \cdot (A \oplus B))$$

### ขั้นตอนต่อวงจร

```
A ──┬──[XOR₁ 7486 pin 1,2→3]──┬──[XOR₂ 7486 pin 4,5→6]── LED (Sum)
    │                          │         ↑
B ──┘                          │        Cin (Switch)
                               │
                    [AND₂ 7408 pin 4,5→6]──┐
                         ↑                 ├──[OR 7432 pin 1,2→3]── LED (Cout)
                        Cin                │
                                           │
A ──┬──[AND₁ 7408 pin 1,2→3]──────────────┘
B ──┘
```

**สรุปการต่อ:**
1. XOR₁: A (pin1) ⊕ B (pin2) → ผลที่ pin3
2. XOR₂: ผลจาก XOR₁ (pin4) ⊕ Cin (pin5) → **Sum** ที่ pin6
3. AND₁: A (pin1) · B (pin2) → ผลที่ pin3
4. AND₂: ผลจาก XOR₁ (pin4) · Cin (pin5) → ผลที่ pin6
5. OR: AND₁ output (pin1) + AND₂ output (pin2) → **Cout** ที่ pin3

### ทดสอบ

| A | B | Cin | LED Sum | LED Cout | ถูกต้อง? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | | | |
| 0 | 0 | 1 | | | |
| 0 | 1 | 0 | | | |
| 0 | 1 | 1 | | | |
| 1 | 0 | 0 | | | |
| 1 | 0 | 1 | | | |
| 1 | 1 | 0 | | | |
| 1 | 1 | 1 | | | |

📸 **Screenshot: Full Adder เมื่อ A=1, B=1, Cin=1 (Sum=1, Cout=1)**

---

## ส่วนที่ 3: ความรู้เพิ่มเติม — Carry Look-Ahead Adder (CLA) (5 นาที) ⭐

**คำถาม:** วงจรบวกแบบ **Ripple Carry Adder** มีข้อเสียอย่างไรเมื่อจำนวนบิตเพิ่มมากขึ้น (เช่น 32 บิต หรือ 64 บิต)?
_________________________________________________________

> 💡 **CLA (Carry Look-Ahead)** ถูกออกแบบมาเพื่อคำนวณตัวทดล่วงหน้าพร้อมกันทุกหลัก เพื่อลดปัญหาความล่าช้า (Propagation Delay)

---

## ส่วนที่ 4: คำถาม (10 นาที)

1. Half Adder กับ Full Adder ต่างกันอย่างไร?
2. ถ้าต้องการบวกเลข 4 บิต (เช่น 1010 + 0111) ต้องใช้ Full Adder กี่ตัว? Half Adder กี่ตัว?
3. นับจำนวน IC ที่ใช้ต่อ Full Adder 1 ตัว: 7486 = _____ , 7408 = _____ , 7432 = _____

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจรตามรายการด้านล่าง
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กรอกคำตอบ → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot วงจร Half Adder (แสดง Output)
- [ ] Screenshot วงจร Full Adder (แสดง Output)
- [ ] Truth Table ครบทั้ง 2 ส่วน
- [ ] ตอบคำถาม 3 ข้อ
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
