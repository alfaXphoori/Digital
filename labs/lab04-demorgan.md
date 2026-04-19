# 🔬 Lab 4: DeMorgan's Theorem — พิสูจน์ด้วยวงจรจริง

## วัตถุประสงค์

- พิสูจน์ DeMorgan's Theorem บน Tinkercad
- เข้าใจว่า NAND/NOR สามารถแทนที่ด้วยวงจรที่เทียบเท่าได้
- ฝึกต่อวงจรหลาย IC ร่วมกัน

---

## ทฤษฎี DeMorgan's Theorem

$$\overline{A \cdot B} = \bar{A} + \bar{B} \quad \text{(Theorem 1)}$$

$$\overline{A + B} = \bar{A} \cdot \bar{B} \quad \text{(Theorem 2)}$$

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน |
|:---|:---:|
| IC 7408 (AND) | 1 |
| IC 7432 (OR) | 1 |
| IC 7404 (NOT) | 1 |
| LED | 2 |
| Resistor 220Ω | 2 |
| DIP Switch | 2 |
| Breadboard | 1 |
| Power Supply 5V | 1 |

---

## ส่วนที่ 1: พิสูจน์ Theorem 1 (20 นาที)

### $\overline{A \cdot B} = \bar{A} + \bar{B}$

**ต่อ 2 วงจรพร้อมกัน แล้วเทียบผล:**

### วงจร A: $\overline{A \cdot B}$ (NAND)

```
Switch A ──┐
           ├──[7408 AND pin 1,2→3]──[7404 NOT pin 1→2]──LED 1
Switch B ──┘
```

### วงจร B: $\bar{A} + \bar{B}$ (NOT-NOT-OR)

```
Switch A ──[7404 NOT pin 3→4]──┐
                               ├──[7432 OR pin 1,2→3]──LED 2
Switch B ──[7404 NOT pin 5→6]──┘
```

### บันทึกผล

| A | B | LED 1 ($\overline{AB}$) | LED 2 ($\bar{A}+\bar{B}$) | เหมือนกัน? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | | | |
| 0 | 1 | | | |
| 1 | 0 | | | |
| 1 | 1 | | | |

📸 **Screenshot วงจรทั้งสอง LED ติดพร้อมกัน (A=0, B=1)**

**สรุป:** Theorem 1 ถูกต้องหรือไม่? _________________

---

## ส่วนที่ 2: พิสูจน์ Theorem 2 (20 นาที)

### $\overline{A + B} = \bar{A} \cdot \bar{B}$

### วงจร C: $\overline{A + B}$ (NOR)

```
Switch A ──┐
           ├──[7432 OR pin 4,5→6]──[7404 NOT pin 9→8]──LED 1
Switch B ──┘
```

### วงจร D: $\bar{A} \cdot \bar{B}$ (NOT-NOT-AND)

```
Switch A ──[7404 NOT pin 11→10]──┐
                                 ├──[7408 AND pin 4,5→6]──LED 2
Switch B ──[7404 NOT pin 13→12]──┘
```

### บันทึกผล

| A | B | LED 1 ($\overline{A+B}$) | LED 2 ($\bar{A} \cdot \bar{B}$) | เหมือนกัน? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | | | |
| 0 | 1 | | | |
| 1 | 0 | | | |
| 1 | 1 | | | |

📸 **Screenshot วงจรทั้งสอง LED ติดพร้อมกัน (A=0, B=0)**

**สรุป:** Theorem 2 ถูกต้องหรือไม่? _________________

---

## ส่วนที่ 3: ท้าทาย — ลดรูปสมการ (20 นาที)

### โจทย์

จงลดรูปสมการต่อไปนี้โดยใช้ DeMorgan's Theorem แล้วต่อวงจรทดสอบ

$$F = \overline{\overline{A} \cdot \overline{B}}$$

**ขั้นตอน:**

1. ลดรูปบนกระดาษ: $F = \overline{\bar{A} \cdot \bar{B}} = $ _________________
2. ต่อวงจร **ก่อนลดรูป** (ใช้ NOT 2 ตัว + AND + NOT)
3. ต่อวงจร **หลังลดรูป** (ใช้เกตที่ได้จากการลดรูป)
4. เปรียบเทียบผล

| A | B | ก่อนลดรูป | หลังลดรูป | เหมือนกัน? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | | | |
| 0 | 1 | | | |
| 1 | 0 | | | |
| 1 | 1 | | | |

---

## คำถามท้าย Lab

1. DeMorgan's Theorem มีประโยชน์อย่างไรในการออกแบบวงจร?
2. ถ้ามีแต่ NAND gate สามารถสร้างเกตอะไรได้บ้าง?

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจรแต่ละส่วนตามรายการด้านล่าง
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กรอกคำตอบ → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot วงจรพิสูจน์ Theorem 1 (แสดง LED ทั้งสองวงจรติดพร้อมกัน)
- [ ] Screenshot วงจรพิสูจน์ Theorem 2 (แสดง LED ทั้งสองวงจรติดพร้อมกัน)
- [ ] Truth Table ครบ 3 ส่วน
- [ ] ตอบคำถามท้าย Lab
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
