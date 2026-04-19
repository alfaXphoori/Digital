# Chapter 5: วงจรลอจิกเชิงผสม

## Combinational Logic Circuits

---

## 5.1 บทนำ

**วงจรเชิงผสม (Combinational Circuit)** — เอาต์พุตขึ้นอยู่กับ **อินพุตปัจจุบัน** เท่านั้น (ไม่มีหน่วยความจำ)

$$\text{Output} = f(\text{Current Inputs})$$

แบ่งเนื้อหาเป็น 2 ส่วน:
- **ส่วนที่ 1:** วงจรคำนวณทางคณิตศาสตร์ (Arithmetic Circuits)
- **ส่วนที่ 2:** วงจรจัดการข้อมูล (Data Routing Circuits)

---

# ส่วนที่ 1: วงจรคำนวณ (Arithmetic Circuits)

---

## 5.2 Half Adder (วงจรบวกครึ่ง)

บวกเลขฐานสอง **2 บิต** — ไม่มี carry input

| A | B | Sum (S) | Carry (C) |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

$$S = A \oplus B$$
$$C = A \cdot B$$

```
 A ──┬──[XOR]── S (Sum)
     │
 B ──┼──[AND]── C (Carry)
```

---

## 5.3 Full Adder (วงจรบวกเต็ม) ⭐

บวกเลขฐานสอง **3 บิต** (A, B, และ Carry-in จากหลักก่อนหน้า)

| A | B | Cᵢₙ | Sum (S) | Cₒᵤₜ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

$$S = A \oplus B \oplus C_{in}$$
$$C_{out} = AB + C_{in}(A \oplus B)$$

### สร้าง Full Adder จาก Half Adder 2 ตัว:

```
        ┌─────────┐           ┌─────────┐
A ─────→│  Half   │──S1──────→│  Half   │──── S (Sum)
B ─────→│ Adder 1 │──C1──┐   │ Adder 2 │
        └─────────┘      │   └────┬────┘
                         │        │ C2
Cin ─────────────────────┼───────→│
                         │        ↓
                         └──[OR]──── Cout
```

### Parallel Adder (4-bit Ripple Carry Adder)

นำ Full Adder 4 ตัวมาต่อกันเป็นลูกโซ่:

```
  A3 B3      A2 B2      A1 B1      A0 B0
   ↓  ↓       ↓  ↓       ↓  ↓       ↓  ↓
 ┌──FA──┐   ┌──FA──┐   ┌──FA──┐   ┌──FA──┐
 │ Cout │←──│ Cout │←──│ Cout │←──│ Cout │←── Cin=0
 └──┬───┘   └──┬───┘   └──┬───┘   └──┬───┘
    S3          S2          S1          S0
```

**IC: 7483** (4-bit Binary Full Adder)

> ⚠️ **ข้อเสีย Ripple Carry:** Carry ต้อง "ลูกโซ่" จากหลักต่ำไปหลักสูง → ช้า

---

## 5.4 Half Subtractor / Full Subtractor

### Half Subtractor

| A | B | Diff (D) | Borrow (Bₒᵤₜ) |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

$$D = A \oplus B$$
$$B_{out} = \overline{A} \cdot B$$

### Full Subtractor

$$D = A \oplus B \oplus B_{in}$$
$$B_{out} = \overline{A}B + B_{in}(\overline{A \oplus B})$$

---

## 5.5 Comparator (วงจรเปรียบเทียบ)

เปรียบเทียบเลขฐานสอง 2 จำนวน → 3 เอาต์พุต: A>B, A<B, A=B

### 1-bit Comparator

$$A = B \quad \Rightarrow \quad \text{EQ} = \overline{A \oplus B}$$
$$A > B \quad \Rightarrow \quad \text{GT} = A\overline{B}$$
$$A < B \quad \Rightarrow \quad \text{LT} = \overline{A}B$$

**IC: 7485** (4-bit Magnitude Comparator)

- มีอินพุต cascade สำหรับต่อขยาย (A>B in, A<B in, A=B in)

---

# ส่วนที่ 2: วงจรจัดการข้อมูล (Data Routing Circuits)

---

## 5.6 Encoder (ตัวเข้ารหัส)

แปลง $2^n$ input lines → $n$-bit output (รหัส Binary)

### 8-to-3 Encoder

| อินพุตที่ Active | D₂ | D₁ | D₀ |
|:---:|:---:|:---:|:---:|
| I₀ | 0 | 0 | 0 |
| I₁ | 0 | 0 | 1 |
| I₂ | 0 | 1 | 0 |
| I₃ | 0 | 1 | 1 |
| I₄ | 1 | 0 | 0 |
| I₅ | 1 | 0 | 1 |
| I₆ | 1 | 1 | 0 |
| I₇ | 1 | 1 | 1 |

### Priority Encoder

เมื่อมีหลายอินพุต active พร้อมกัน → เลือกตัวที่มี **ลำดับความสำคัญสูงสุด**

**IC: 74148** (8-to-3 Priority Encoder)

---

## 5.7 Decoder (ตัวถอดรหัส) ⭐

แปลง $n$-bit input → $2^n$ output lines (active เพียง 1 เส้นในแต่ละเวลา)

### 2-to-4 Decoder

| A₁ | A₀ | D₀ | D₁ | D₂ | D₃ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | **1** | 0 | 0 | 0 |
| 0 | 1 | 0 | **1** | 0 | 0 |
| 1 | 0 | 0 | 0 | **1** | 0 |
| 1 | 1 | 0 | 0 | 0 | **1** |

$$D_0 = \overline{A_1}\,\overline{A_0}, \quad D_1 = \overline{A_1}\,A_0, \quad D_2 = A_1\,\overline{A_0}, \quad D_3 = A_1\,A_0$$

**IC: 74138** (3-to-8 Decoder), **74139** (Dual 2-to-4 Decoder)

> 💡 **ประยุกต์:** ใช้ Decoder + OR gates สร้างฟังก์ชันบูลีนใดก็ได้ (แต่ละเอาต์พุตของ Decoder = 1 minterm)

### BCD to 7-Segment Decoder ⭐

แปลง BCD (0–9) เป็นสัญญาณขับ 7-Segment Display

```
                ─── a ───
               │         │
               f         b
               │         │
                ─── g ───
               │         │
               e         c
               │         │
                ─── d ───
```

| BCD Input (DCBA) | Display | a | b | c | d | e | f | g |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0000 | **0** | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| 0001 | **1** | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| 0010 | **2** | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 0011 | **3** | 1 | 1 | 1 | 1 | 0 | 0 | 1 |
| 0100 | **4** | 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| 0101 | **5** | 1 | 0 | 1 | 1 | 0 | 1 | 1 |
| 0110 | **6** | 1 | 0 | 1 | 1 | 1 | 1 | 1 |
| 0111 | **7** | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| 1000 | **8** | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 1001 | **9** | 1 | 1 | 1 | 1 | 0 | 1 | 1 |

**IC: 7447** (active LOW), **4511** (active HIGH, CMOS)

---

## 5.8 Multiplexer — MUX (ตัวเลือกสัญญาณ) ⭐

เลือก **1 อินพุตจากหลายตัว** ส่งไปเอาต์พุต ตาม select lines

### MUX 2:1

$$Y = \overline{S} \cdot I_0 + S \cdot I_1$$

| S | Y |
|:---:|:---:|
| 0 | I₀ |
| 1 | I₁ |

### MUX 4:1

$$Y = \overline{S_1}\,\overline{S_0}\,I_0 + \overline{S_1}\,S_0\,I_1 + S_1\,\overline{S_0}\,I_2 + S_1\,S_0\,I_3$$

| S₁ | S₀ | Y |
|:---:|:---:|:---:|
| 0 | 0 | I₀ |
| 0 | 1 | I₁ |
| 1 | 0 | I₂ |
| 1 | 1 | I₃ |

**IC: 74153** (Dual 4:1 MUX), **74151** (8:1 MUX)

> 💡 **MUX เป็น Universal Function Generator:** ใช้ MUX n:1 สร้างฟังก์ชันบูลีน n ตัวแปรได้ โดยต่อ 0, 1, หรือตัวแปรเข้าที่อินพุตข้อมูล

### ตัวอย่าง: ใช้ MUX 4:1 สร้าง $F(A,B) = \sum m(1,2,3)$

```
S₁ = A, S₀ = B

I₀ = 0  (m0 = 0)
I₁ = 1  (m1 = 1)
I₂ = 1  (m2 = 1)
I₃ = 1  (m3 = 1)

ผลลัพธ์: F = A + B
```

---

## 5.9 Demultiplexer — DEMUX (ตัวกระจายสัญญาณ)

รับ **1 อินพุต** กระจายไปยัง **1 ใน n เอาต์พุต** ตาม select lines

### DEMUX 1-to-4

```
               ┌──── Y₀
 D ──[DEMUX]───┤──── Y₁
               ├──── Y₂
               └──── Y₃
        ↑↑
       S₁ S₀
```

| S₁ | S₀ | Y₀ | Y₁ | Y₂ | Y₃ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | D | 0 | 0 | 0 |
| 0 | 1 | 0 | D | 0 | 0 |
| 1 | 0 | 0 | 0 | D | 0 |
| 1 | 1 | 0 | 0 | 0 | D |

> 💡 Decoder + Enable = DEMUX (ถ้าต่ออินพุตข้อมูลเข้าที่ Enable)

---

## 5.10 สรุป IC วงจรเชิงผสมที่ใช้บ่อย

| IC | ฟังก์ชัน |
|:---:|:---|
| **7483** | 4-bit Full Adder |
| **7485** | 4-bit Magnitude Comparator |
| **74138** | 3-to-8 Decoder |
| **74139** | Dual 2-to-4 Decoder |
| **74148** | 8-to-3 Priority Encoder |
| **74151** | 8:1 MUX |
| **74153** | Dual 4:1 MUX |
| **7447** | BCD to 7-Segment (Active Low) |
| **4511** | BCD to 7-Segment (Active High, CMOS) |

---

## แบบฝึกหัดท้ายบท

1. ออกแบบ 4-bit Ripple Carry Adder จาก Full Adder (วาดแผนผัง)
2. ใช้ MUX 8:1 สร้างฟังก์ชัน $F(A,B,C) = \sum m(1, 2, 6, 7)$
3. ใช้ Decoder 3-to-8 + OR gate สร้าง $F(A,B,C) = \sum m(0, 3, 5, 6)$
4. ออกแบบ BCD to 7-Segment สำหรับ segment `a` โดยใช้ K-Map
5. เปรียบเทียบข้อดีข้อเสียของ Encoder กับ Priority Encoder
6. ต่อวงจร 4-bit Adder + 7-Segment Display บน **Tinkercad** โดยใช้ IC 7483 + 4511
