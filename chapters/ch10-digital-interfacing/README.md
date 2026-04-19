# Chapter 10: การเชื่อมต่อระบบดิจิทัล

## Digital Interfacing: ADC, DAC & Tinkercad

---

## 10.1 บทนำ

ในโลกจริง สัญญาณส่วนใหญ่เป็น **แอนะล็อก** (Analog) เช่น อุณหภูมิ แสง เสียง — แต่คอมพิวเตอร์ทำงานกับ **ดิจิทัล** (Digital, 0 กับ 1) ดังนั้นต้องมีวงจร **แปลงสัญญาณ** เชื่อมสองโลกนี้เข้าด้วยกัน

```
Analog World              Digital World
   │                          │
   │ Sensor → [ADC] ──────→  │  Processing
   │                          │  (CPU, FPGA)
   │ Actuator ← [DAC] ←───── │
   │                          │
```

---

## 10.2 แอนะล็อก vs ดิจิทัล

| เกณฑ์ | Analog | Digital |
|:---|:---:|:---:|
| สัญญาณ | ต่อเนื่อง (Continuous) | ไม่ต่อเนื่อง (Discrete) |
| ค่าที่เป็นไปได้ | ∞ | จำกัด ($2^n$ ค่า) |
| สัญญาณรบกวน | ไวต่อ noise | **ทนทาน** ✅ |
| การประมวลผล | ยาก | ง่าย ✅ |
| ตัวอย่าง | เสียง, อุณหภูมิ, แรงดัน | ข้อมูลในคอมพิวเตอร์ |

---

## 10.3 DAC (Digital-to-Analog Converter)

### หลักการ

แปลง **รหัสดิจิทัล (binary)** เป็น **แรงดันไฟฟ้าแอนะล็อก**

$$V_{out} = V_{ref} \times \frac{D}{2^n}$$

- $V_{ref}$ = แรงดันอ้างอิง (Reference Voltage)
- $D$ = ค่าดิจิทัล (0 ถึง $2^n - 1$)
- $n$ = จำนวนบิต (Resolution)

### ตัวอย่าง: DAC 3-bit, V_ref = 8V

| Input (D₂D₁D₀) | Decimal | V_out |
|:---:|:---:|:---:|
| 000 | 0 | 0.0 V |
| 001 | 1 | 1.0 V |
| 010 | 2 | 2.0 V |
| 011 | 3 | 3.0 V |
| 100 | 4 | 4.0 V |
| 101 | 5 | 5.0 V |
| 110 | 6 | 6.0 V |
| 111 | 7 | 7.0 V |

### วงจร DAC แบบ R-2R Ladder

```
Vref
  │
  ├──[2R]──┬──[2R]──┬──[2R]──┬──→ GND
  │        │        │        │
 [R]      [R]      [R]      [R]
  │        │        │        │
 D₃       D₂       D₁       D₀
(MSB)                      (LSB)
```

**R-2R Ladder** ใช้ตัวต้านทานเพียง 2 ค่า (R และ 2R) → ผลิตง่าย, ความแม่นยำดี

### พารามิเตอร์สำคัญ

| พารามิเตอร์ | ความหมาย |
|:---|:---|
| **Resolution** | จำนวนบิต (n) → ค่า output ที่เป็นไปได้ = $2^n$ |
| **Step Size** | ขนาดการเปลี่ยนแปลงต่อ 1 LSB = $V_{ref} / 2^n$ |
| **Full-Scale** | Output สูงสุด = $V_{ref} \times (2^n - 1) / 2^n$ |
| **Settling Time** | เวลาที่ output นิ่งหลังเปลี่ยน input |

---

## 10.4 ADC (Analog-to-Digital Converter)

### หลักการ

แปลง **แรงดันไฟฟ้าแอนะล็อก** เป็น **รหัสดิจิทัล**

### กระบวนการแปลง ADC

```
Analog → [Sampling] → [Quantization] → [Encoding] → Digital
สัญญาณ     สุ่มตัวอย่าง    แบ่งระดับ      แปลงเป็นเลขฐาน 2
```

#### 1) Sampling (การสุ่มตัวอย่าง)

วัดค่าสัญญาณ ณ ช่วงเวลาที่แน่นอน

> **Nyquist Theorem:** อัตราสุ่มตัวอย่างต้อง ≥ 2 เท่าของความถี่สูงสุดของสัญญาณ
>
> $$f_s \geq 2 \times f_{max}$$

#### 2) Quantization (การแบ่งระดับ)

ปัดค่าที่วัดได้ให้ตรงกับระดับที่ใกล้ที่สุด

```
V
7 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │111│
6 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │110│  ← ค่าที่ ADC ให้ได้
5 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │101│    (3-bit = 8 ระดับ)
4 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │100│
3 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │011│
2 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │010│
1 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │001│
0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │000│
```

> **Quantization Error** สูงสุด = ±½ LSB

#### 3) Encoding (การเข้ารหัส)

แปลงระดับที่ได้เป็นเลข binary

### ชนิดของ ADC

| ชนิด | วิธีการ | ความเร็ว | ความแม่นยำ |
|:---|:---|:---:|:---:|
| **Flash ADC** | Comparator ขนาน ($2^n - 1$ ตัว) | **เร็วมาก** ✅ | ดี |
| **SAR ADC** | Binary search (ทีละบิต) | ปานกลาง | **ดี** ✅ |
| **Dual-Slope** | Integrate → count | ช้า | **แม่นมาก** ✅ |
| **Sigma-Delta** | Oversampling + noise shaping | ช้า | **แม่นมาก** ✅ |

### Flash ADC (3-bit ตัวอย่าง)

```
Vin ──┬──[Comp 7]── (>7/8 Vref?)
      ├──[Comp 6]── (>6/8 Vref?)
      ├──[Comp 5]── (>5/8 Vref?)
      ├──[Comp 4]── (>4/8 Vref?)    → Priority  → Binary
      ├──[Comp 3]── (>3/8 Vref?)      Encoder      Output
      ├──[Comp 2]── (>2/8 Vref?)                   (3 bits)
      └──[Comp 1]── (>1/8 Vref?)
```

- ใช้ Comparator $2^n - 1 = 7$ ตัว สำหรับ 3-bit
- ผล Thermometer Code → Priority Encoder → Binary

---

## 10.5 ตัวอย่างการเลือก ADC/DAC

**โจทย์:** ต้องการวัดอุณหภูมิ 0–100°C ด้วยความละเอียด 0.5°C

- ต้องแยกได้ = $100 / 0.5 = 200$ ระดับ
- จำนวนบิต: $2^n \geq 200$ → $n \geq 8$ (ใช้ **8-bit ADC**, $2^8 = 256$ ระดับ)
- ถ้า Sensor ให้ output 0–5V → Step Size = $5/256 \approx 19.5$ mV

---

## 10.6 Tinkercad: สร้างวงจรดิจิทัลจำลอง

### Tinkercad คืออะไร?

**Tinkercad Circuits** (circuits.tinkercad.com) เป็นเครื่องมือจำลองวงจรออนไลน์ ฟรี โดย Autodesk

### ขั้นตอนการใช้งาน

1. **สร้างบัญชี** ที่ [tinkercad.com](https://www.tinkercad.com)
2. เลือก **Circuits** → **Create new Circuit**
3. ลากชิ้นส่วนจากแถบด้านขวา
4. **ต่อสาย** โดยคลิกที่ขาแล้วลากไปอีกขา
5. กด **Start Simulation** เพื่อทดสอบ

### ชิ้นส่วนที่ใช้บ่อย

| ชิ้นส่วน | หน้าที่ | ตัวอย่าง IC |
|:---|:---|:---:|
| Logic Gate IC | เกตลอจิก | 7408 (AND), 7432 (OR), 7404 (NOT) |
| LED + Resistor | แสดงผล output | — |
| Switch / Push Button | ใส่ input | — |
| 7-Segment Display | แสดงตัวเลข | ใช้กับ 4511 (BCD decoder) |
| Flip-Flop IC | หน่วยความจำ 1 บิต | 7473 (JK), 7474 (D) |
| Arduino | Microcontroller | — |
| Breadboard | ต่อวงจร prototype | — |

### ตัวอย่างโปรเจกต์ที่ทำได้

1. **ต่อวงจรเกตพื้นฐาน** — AND, OR, NOT ด้วย IC 7408, 7432, 7404
2. **วงจร Half/Full Adder** — ใช้ XOR (7486) + AND (7408)
3. **วงจร 7-Segment Decoder** — BCD input → 4511 → 7-Segment Display
4. **วงจร Counter** — JK FF (7473) ต่อเป็น Ripple Counter
5. **วงจร FSM อย่างง่าย** — D FF + Logic Gates

### เคล็ดลับ Tinkercad

| ปัญหา | วิธีแก้ |
|:---|:---|
| LED ไม่ติด | ตรวจสอบ: ต่อ Resistor (220Ω–1kΩ) แล้วหรือยัง? |
| Output ไม่ถูกต้อง | ตรวจสอบ: ต่อ VCC (+5V) และ GND ให้ IC แล้วหรือยัง? |
| สัญญาณลอย | ต่อ Pull-up/Pull-down resistor ที่ input ที่ไม่ได้ใช้ |
| จำลองช้า | ลดจำนวนชิ้นส่วน หรือปิด animation |

---

## 10.7 การอ่าน Data Sheet (ทบทวน)

### ข้อมูลสำคัญใน Data Sheet

| หัวข้อ | สิ่งที่ต้องดู |
|:---|:---|
| **Pin Diagram** | ขาไหนเป็นอะไร (Input, Output, VCC, GND) |
| **Function Table** | Truth Table / ตารางการทำงาน |
| **Absolute Maximum Ratings** | ค่าสูงสุดที่รับได้ (ห้ามเกิน!) |
| **Recommended Operating Conditions** | VCC, Input Voltage, Temperature ที่ควรใช้ |
| **Propagation Delay** | เวลาหน่วง (tpLH, tpHL) |
| **Fan-out** | จำนวนเกตที่ต่อ output ได้ |

### ตัวอย่าง IC ที่ใช้ในวิชานี้

| IC | ฟังก์ชัน | จำนวนเกต |
|:---:|:---|:---:|
| **7408** | Quad 2-input AND | 4 |
| **7432** | Quad 2-input OR | 4 |
| **7404** | Hex Inverter (NOT) | 6 |
| **7486** | Quad 2-input XOR | 4 |
| **7400** | Quad 2-input NAND | 4 |
| **7402** | Quad 2-input NOR | 4 |
| **7473** | Dual JK Flip-Flop | 2 |
| **7474** | Dual D Flip-Flop | 2 |
| **74138** | 3-to-8 Decoder | 1 |
| **74151** | 8-to-1 MUX | 1 |
| **4511** | BCD to 7-Segment | 1 |

---

## แบบฝึกหัดท้ายบท

1. DAC 4-bit มี V_ref = 10V — จงคำนวณ Step Size และ V_out เมื่อ Input = 1010₂
2. ต้องการวัดแรงดัน 0–3.3V ด้วยความละเอียด 10 mV → ต้องใช้ ADC กี่บิต?
3. อธิบายข้อดีข้อเสียของ Flash ADC เทียบกับ SAR ADC
4. สร้างวงจร Full Adder บน Tinkercad โดยใช้ IC 7486 (XOR) และ 7408 (AND) และ 7432 (OR) — Capture ภาพผลลัพธ์
5. สร้างวงจร 2-bit Counter บน Tinkercad โดยใช้ IC 7473 (JK FF) — ต่อเป็น Ripple Counter แสดงผลด้วย LED
