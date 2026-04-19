# 🔬 Lab 15: Mini-Project — Counter + 7-Segment Display

## วัตถุประสงค์

- ต่อวงจร Counter + Decoder + 7-Segment Display ครบวงจร
- ผสมผสานความรู้ทั้งหมดตั้งแต่ Flip-Flop, Counter, Decoder
- เตรียมพร้อมสำหรับสอบปฏิบัติ

---

## โจทย์

สร้าง **วงจรนับเลข 0–9** แสดงผลบน 7-Segment Display โดยกดปุ่ม Clock ทีละครั้ง

```
[Push Button] → [2-bit Counter] → [BCD Counter Logic] → [4511 Decoder] → [7-Segment]
    (Clock)        (7473 JK FF)                              (BCD→7Seg)     (แสดงเลข)
```

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน | หน้าที่ |
|:---|:---:|:---|
| IC 7473 (Dual JK FF) | 2 | Counter 4-bit (ใช้ 4 FF) |
| IC 7408 (AND) | 1 | Reset Logic (MOD-10) |
| IC 7432 (OR) | 1 | Reset Logic |
| IC 4511 (BCD→7-Seg) | 1 | Decoder |
| 7-Segment Display (CC) | 1 | แสดงเลข |
| Resistor 220Ω | 7 | ต่อกับ 7-Segment |
| LED | 4 | แสดง BCD (optional) |
| Push Button | 1 | Clock |
| Breadboard | 1–2 | |
| Power Supply 5V | 1 | |

---

## ส่วนที่ 1: ต่อ 4-bit Ripple Counter (20 นาที)

### ต่อ JK FF 4 ตัว เป็น Ripple Counter

```
CLK → [FF₀] Q₀→ [FF₁] Q₁→ [FF₂] Q₂→ [FF₃] Q₃
       J=K=1      J=K=1      J=K=1      J=K=1
```

**IC 7473 ตัวที่ 1:** FF₀ (Q₀, LSB) และ FF₁ (Q₁)
**IC 7473 ตัวที่ 2:** FF₂ (Q₂) และ FF₃ (Q₃, MSB)

> ทบทวนจาก Lab 10: Q ของ FF ก่อนหน้า → CLK ของ FF ถัดไป

### ทดสอบ: กด Clock 16 ครั้ง ดูว่านับ 0–15 ถูกต้อง

| Clock | Q₃ | Q₂ | Q₁ | Q₀ | Decimal |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | | | | | |
| 2 | | | | | |
| ... | | | | | |
| 9 | | | | | |
| 10 | | | | | |

📸 **Screenshot 4-bit Counter ที่นับถูก**

---

## ส่วนที่ 2: เพิ่ม MOD-10 Reset (15 นาที)

4-bit Counter นับ 0–15 แต่เราต้องการ **0–9** (MOD-10)

### วิธี: ตรวจจับ State 10 (1010) แล้ว Reset

เมื่อนับถึง 10 (Q₃=1, Q₂=0, Q₁=1, Q₀=0):
- ใช้ AND gate ตรวจ Q₃ · Q₁ = 1 (เพราะ state 10 เป็นค่าแรกที่ Q₃=1 และ Q₁=1)
- นำผลไป Clear ทุก FF กลับเป็น 0

```
Q₃ ──┐
     ├──[AND 7408]──→ CLR̄ ของทุก FF (Active LOW → ใช้ NOT ถ้าจำเป็น)
Q₁ ──┘
```

> ⚠️ 7473 CLR เป็น **Active LOW** — ปกติต่อ HIGH, เมื่อจะ Clear ให้เป็น LOW

### ทดสอบ MOD-10

| Clock | Q₃Q₂Q₁Q₀ | Decimal | Reset? |
|:---:|:---:|:---:|:---:|
| 8 | 1000 | 8 | ❌ |
| 9 | 1001 | 9 | ❌ |
| 10 | 1010 → 0000 | 10 → **0** | ✅ |
| 11 | 0001 | 1 | ❌ |

📸 **Screenshot ที่แสดงว่า Counter วนกลับ 0 หลังนับถึง 9**

---

## ส่วนที่ 3: ต่อ 4511 + 7-Segment Display (15 นาที)

ต่อ Output ของ Counter (Q₃Q₂Q₁Q₀) เข้ากับ IC 4511 แล้วต่อ 7-Segment

### การต่อ

| Counter Output | 4511 Input |
|:---:|:---:|
| Q₀ (LSB) | A (pin 7) |
| Q₁ | B (pin 1) |
| Q₂ | C (pin 2) |
| Q₃ (MSB) | D (pin 6) |

- 4511: LT (pin 3) → VCC, BL (pin 4) → VCC, LE (pin 5) → GND
- 4511 output a–g → Resistor 220Ω → 7-Segment Display

> ทบทวนจาก Lab 7!

---

## ส่วนที่ 4: ทดสอบวงจรรวม (10 นาที)

กด Clock ทีละครั้ง บันทึกเลขที่แสดงบน 7-Segment

| Clock | BCD (Q₃Q₂Q₁Q₀) | 7-Segment แสดง | ถูกต้อง? |
|:---:|:---:|:---:|:---:|
| 0 | 0000 | 0 | |
| 1 | 0001 | | |
| 2 | 0010 | | |
| 3 | 0011 | | |
| 4 | 0100 | | |
| 5 | 0101 | | |
| 6 | 0110 | | |
| 7 | 0111 | | |
| 8 | 1000 | | |
| 9 | 1001 | | |
| 10 | 0000 (reset) | 0 (วนใหม่) | |

📸 **Screenshot แสดงเลข 0, 5, 9 บน 7-Segment**

---

## ส่วนที่ 5: Debugging Guide

| ปัญหา | ตรวจสอบ |
|:---|:---|
| 7-Segment ไม่ติด | VCC/GND ของ 4511 ครบ? LT=HIGH, BL=HIGH, LE=LOW? |
| นับข้ามเลข | Ripple connection ถูก? Q → CLK ของ FF ถัดไป |
| ไม่ Reset ที่ 10 | AND gate ตรวจ Q₃·Q₁ ถูก? CLR ต่อถูกขั้ว? |
| แสดงเลขผิด | Q₀→A, Q₁→B, Q₂→C, Q₃→D ถูกลำดับ? |

---

## สรุป IC ที่ใช้ทั้งหมด

| IC | จำนวน | หน้าที่ |
|:---|:---:|:---|
| 7473 | 2 | 4-bit Ripple Counter |
| 7408 | 1 | MOD-10 Reset Detection |
| 4511 | 1 | BCD → 7-Segment Decoder |
| **รวม** | **4 IC** | |

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจรตามรายการด้านล่าง
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot วงจรรวมทั้งหมด
- [ ] Screenshot แสดงเลข 0, 5, 9 (3 ภาพ)
- [ ] ตารางทดสอบเลข 0–9 + Reset
- [ ] วิดีโอสั้น (optional) กด Clock แล้วเลขเปลี่ยน 0→9→0
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
