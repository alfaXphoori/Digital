# 🔬 Lab 10: 2-bit Ripple Counter — นับ 0→3

## วัตถุประสงค์

- ต่อวงจร 2-bit Asynchronous (Ripple) Counter ด้วย 7473
- เข้าใจการทำงานของ Ripple Counter
- สังเกต Ripple Delay

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน |
|:---|:---:|
| IC 7473 (Dual JK FF) | 1 |
| LED | 2 |
| Resistor 220Ω | 2 |
| Push Button | 1 |
| Breadboard | 1 |
| Power Supply 5V | 1 |

---

## ส่วนที่ 1: ทบทวนหลักการ (5 นาที)

### 2-bit Ripple Counter

```
                    ┌──────┐      ┌──────┐
  CLK ────────────→│ JK   │ Q₀──→│ JK   │ Q₁──→ LED (MSB)
                   │ FF₀  │      │ FF₁  │
  J₀=1, K₀=1      │      │      │      │
  (Toggle)         └──────┘      └──────┘
                    LED (LSB)     J₁=1, K₁=1
```

- **FF₀:** Clock = สัญญาณภายนอก (Push Button)
- **FF₁:** Clock = Q₀ ของ FF₀ (ต่อต่อกัน → Ripple)
- ทั้งสอง FF ตั้ง **J=1, K=1 (Toggle mode)**

### ลำดับการนับ

| Clock Pulse | Q₁ (MSB) | Q₀ (LSB) | Decimal |
|:---:|:---:|:---:|:---:|
| 0 (เริ่ม) | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 2 | 1 | 0 | 2 |
| 3 | 1 | 1 | 3 |
| 4 | 0 | 0 | 0 (วนใหม่) |

---

## ส่วนที่ 2: ต่อวงจร (25 นาที)

### ขั้นตอน (ใช้ IC 7473 ที่มี 2 JK FF)

**FF₀ (ตัวที่ 1 ของ 7473):**
1. ต่อ **1J (ใช้ internal)** = VCC (J=1)
2. ต่อ **1K (pin 3)** = VCC (K=1) → Toggle mode
3. ต่อ **1CLK (pin 1)** = Push Button (Clock ภายนอก)
4. ต่อ **1CLR (pin 2)** = VCC (ไม่ Clear)
5. ต่อ **1Q (pin 13)** → Resistor → LED₀ (LSB)

**FF₁ (ตัวที่ 2 ของ 7473):**
1. ต่อ **2J (pin 7)** = VCC (J=1)
2. ต่อ **2K (pin 5)** = VCC (K=1) → Toggle mode
3. ต่อ **2CLK (pin 6)** = **1Q (pin 13)** ← ⭐ Q₀ เป็น Clock ของ FF₁
4. ต่อ **2CLR (pin 10)** = VCC
5. ต่อ **2Q (pin 8)** → Resistor → LED₁ (MSB)

> ⚠️ **จุดสำคัญ:** 7473 trigger ที่ **ขอบขาลง** — FF₁ จะเปลี่ยนสถานะเมื่อ Q₀ เปลี่ยนจาก 1→0

---

## ส่วนที่ 3: ทดสอบ (20 นาที)

### กด Clock ทีละครั้ง บันทึก LED

| Clock Pulse | LED₁ (Q₁) | LED₀ (Q₀) | Decimal | ตรง? |
|:---:|:---:|:---:|:---:|:---:|
| เริ่มต้น | | | | |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |

**คำถาม:** Counter วนซ้ำทุกกี่ pulse? → MOD-___

### วาด Timing Diagram

```
CLK  ┌┐ ┌┐ ┌┐ ┌┐ ┌┐ ┌┐ ┌┐ ┌┐
     ││ ││ ││ ││ ││ ││ ││ ││
   ──┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└──

Q₀   
   ── (วาดจากผลทดสอบ)

Q₁   
   ── (วาดจากผลทดสอบ)
```

📸 **Screenshot วงจรเมื่อแสดง 10₂ (Decimal 2)**

---

## ส่วนที่ 4: ความรู้เพิ่มเติม — Clock Divider และ LFSR (5 นาที) ⭐

1. **Clock Divider:** ในวงจรนี้ Q₀ มีความถี่เป็นกี่เท่าของความถี่ CLK (Push button)?
   - [ ] 2 เท่า
   - [ ] 1/2 เท่า
   - [ ] 1/4 เท่า

2. **LFSR (Linear Feedback Shift Register):** มักนำไปใช้ทำอะไรในระบบดิจิทัล?
   - [ ] ตัวนับเลขฐานสิบ
   - [ ] เครื่องกำเนิดเลขสุ่ม (Pseudo-random number generator)

---

## ส่วนที่ 5: คำถาม (10 นาที)

1. 2-bit Ripple Counter นับได้ตั้งแต่ _______ ถึง _______ (MOD-___)
2. ถ้าต้องการ 3-bit Counter (นับ 0–7) ต้องใช้ JK FF กี่ตัว?
3. ทำไมถึงเรียกว่า "Ripple" Counter?
4. ข้อเสียของ Ripple Counter คืออะไร? (เทียบกับ Synchronous Counter)

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจร + ถ่ายรูป Timing Diagram ที่วาดลงกระดาษ
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กรอกคำตอบ → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot วงจร 2-bit Counter ที่ต่อเสร็จ
- [ ] Screenshot แสดง Decimal 2 (Q₁=1, Q₀=0)
- [ ] ตารางทดสอบครบ 8 pulses
- [ ] ถ่ายรูป Timing Diagram
- [ ] ตอบคำถาม 4 ข้อ
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
