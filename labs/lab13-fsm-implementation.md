# 🔬 Lab 13: FSM Implementation — ต่อวงจรไฟจราจรจาก Lab 12

## วัตถุประสงค์

- ต่อวงจร FSM ไฟจราจรที่ออกแบบใน Lab 12 บน Tinkercad
- ทดสอบว่าวงจรทำงานตรงกับ State Diagram
- เข้าใจกระบวนการ Design → Implementation ครบวงจร

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน |
|:---|:---:|
| IC 7474 (Dual D FF) | 1 |
| IC 7408 (AND) | 1 |
| IC 7404 (NOT) | 1 |
| LED สีเขียว | 1 |
| LED สีเหลือง | 1 |
| LED สีแดง | 1 |
| Resistor 220Ω | 3 |
| Push Button | 1 |
| Breadboard | 1 |
| Power Supply 5V | 1 |

> ⚠️ จำนวน IC อาจเปลี่ยนตามสมการที่ลดรูปได้จาก Lab 12

---

## ส่วนที่ 1: ทบทวนสมการจาก Lab 12 (5 นาที)

เขียนสมการที่ได้จาก Lab 12 ลงที่นี่:

$$D_1 = $$

$$D_0 = $$

$$G = $$

$$Y = $$

$$R = $$

---

## ส่วนที่ 2: ต่อวงจร (30 นาที)

### ขั้นตอน

#### 1. วาง IC และต่อไฟเลี้ยง

- 7474: VCC (pin 14), GND (pin 7)
- 7408: VCC (pin 14), GND (pin 7)
- 7404: VCC (pin 14), GND (pin 7)

#### 2. ต่อ D Flip-Flop (7474)

**FF₀ (D₀):**
- D₀ input (pin 2) ← ต่อตามสมการ D₀
- CLK (pin 3) ← Push Button (Clock)
- PRE (pin 4) ← VCC
- CLR (pin 1) ← VCC
- Q₀ output (pin 5)

**FF₁ (D₁):**
- D₁ input (pin 12) ← ต่อตามสมการ D₁
- CLK (pin 11) ← Push Button (Clock เดียวกัน!)
- PRE (pin 10) ← VCC
- CLR (pin 13) ← VCC
- Q₁ output (pin 9)

#### 3. ต่อ Next State Logic

ต่อเกต AND, NOT ตามสมการ D₁ และ D₀ ที่ได้จาก Lab 12

#### 4. ต่อ Output Logic → LED

ต่อเกตตามสมการ G, Y, R แล้วต่อ LED:
- สมการ G → Resistor 220Ω → **LED สีเขียว** → GND
- สมการ Y → Resistor 220Ω → **LED สีเหลือง** → GND
- สมการ R → Resistor 220Ω → **LED สีแดง** → GND

---

## ส่วนที่ 3: ทดสอบ (20 นาที)

### กด Clock ทีละครั้ง บันทึกสถานะ

| Clock | Q₁ | Q₀ | State | LED G | LED Y | LED R | ถูกต้อง? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 (เริ่ม) | 0 | 0 | S0 | | | | |
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |
| 7 | | | | | | | |
| 8 | | | | | | | |

**ลำดับที่คาดหวัง:** 🟢→🟡→🔴→🟢→🟡→🔴→...

📸 **Screenshot แต่ละสถานะ (3 ภาพ: GREEN, YELLOW, RED)**

---

## ส่วนที่ 4: Debugging (ถ้าวงจรไม่ทำงาน)

### Checklist

- [ ] VCC และ GND ต่อครบทุก IC?
- [ ] PRE และ CLR ของ 7474 ต่อ VCC?
- [ ] Clock ต่อร่วมกันทั้ง 2 FF?
- [ ] สมการ D₁, D₀ ต่อถูกต้องตาม K-Map?
- [ ] Output Logic (G, Y, R) ต่อถูกต้อง?
- [ ] LED ต่อถูกขั้ว? (Anode → Resistor → IC output, Cathode → GND)

### ปัญหาที่พบบ่อย

| ปัญหา | สาเหตุ | วิธีแก้ |
|:---|:---|:---|
| LED ไม่ติดเลย | ไม่ได้ต่อ VCC/GND ให้ IC | ตรวจสอบไฟเลี้ยง |
| ค้างที่ state เดิม | สมการ D ผิด | ตรวจสอบ K-Map ใหม่ |
| LED ติดมากกว่า 1 ดวง | Output Logic ผิด | ตรวจสอบสมการ G, Y, R |
| ไม่วนกลับ | State 11 ไม่ได้จัดการ | เพิ่ม don't care ใน K-Map |

---

## ส่วนที่ 5: คำถาม (5 นาที)

1. ถ้าเปิดเครื่องแล้ว Q₁Q₀ = 11 (state ที่ไม่ได้กำหนด) วงจรจะกลับมาทำงานปกติหรือไม่?
2. ถ้าต้องการเพิ่ม state ที่ 4 (เช่น กะพริบเหลือง) ต้องเปลี่ยนอะไรบ้าง?
3. เปรียบเทียบขั้นตอนที่ทำใน Lab 12 (กระดาษ) กับ Lab 13 (วงจรจริง) — ขั้นตอนไหนยากกว่า?

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจรตามรายการด้านล่าง
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กรอกคำตอบ → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot วงจรที่ต่อเสร็จสมบูรณ์
- [ ] Screenshot สถานะ GREEN, YELLOW, RED (3 ภาพ)
- [ ] ตารางทดสอบครบ 9 Clock pulses
- [ ] ตอบคำถาม 3 ข้อ
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
