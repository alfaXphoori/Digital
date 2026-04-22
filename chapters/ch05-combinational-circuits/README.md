# Chapter 5: วงจรลอจิกเชิงผสม

## Combinational Logic Circuits

---

## 5.1 บทนำ

**วงจรเชิงผสม (Combinational Circuit)** — เอาต์พุตขึ้นอยู่กับ **อินพุตปัจจุบัน** เท่านั้น (ไม่มีหน่วยความจำ)

$$\text{Output} = f(\text{Current Inputs})$$

```
                ┌──────────────────┐
 Inputs ───────→│  Combinational   │───────→ Outputs
                │     Logic        │
                │                  │
                └──────────────────┘     
```

### ลักษณะสำคัญ:
- ไม่มี feedback path จากเอาต์พุตกลับเข้าอินพุต
- ไม่มีองค์ประกอบเก็บค่า (ไม่มี Flip-flop, Latch)
- เอาต์พุตตอบสนองทันที (มีเฉพาะ propagation delay)

### กระบวนการออกแบบวงจรเชิงผสม:

```
1. กำหนดปัญหา (สร้าง Truth Table)
          ↓
2. เขียนสมการบูลีน (SOP / POS)
          ↓
3. ลดรูปสมการ (K-Map / Algebra)
          ↓
4. วาดวงจรด้วยเกต
          ↓
5. ตรวจสอบความถูกต้อง
```

แบ่งเนื้อหาเป็น 2 ส่วน:
- **ส่วนที่ 1:** วงจรคำนวณทางคณิตศาสตร์ (Arithmetic Circuits)
- **ส่วนที่ 2:** วงจรจัดการข้อมูล (Data Routing Circuits)

---

# ส่วนที่ 1: วงจรคำนวณ (Arithmetic Circuits)

---

## 5.2 Half Adder (วงจรบวกครึ่ง)

บวกเลขฐานสอง **2 บิต** — ไม่มี Carry input (ใช้กับหลักหน่วยเท่านั้น)

### Truth Table

| A | B | Sum (S) | Carry (C) |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

### สมการ:

$$S = A \oplus B \quad \text{(XOR)}$$
$$C = A \cdot B \quad \text{(AND)}$$

### วงจร Half Adder:

<img src="./images/half-adder.png" width="650" alt="Half Adder Circuit">

*ที่มา: Wikimedia Commons (Public Domain)*

### ตัวอย่างการบวก:

```
  A = 1
+ B = 1
──────
  S = 0  (ผลบวก)
  C = 1  (ทดไปหลักถัดไป)
```

---

## 5.3 Full Adder (วงจรบวกเต็ม) ⭐

บวกเลขฐานสอง **3 บิต** (A, B, และ Carry-in $C_{in}$ จากหลักก่อนหน้า)

### Truth Table

| A | B | $C_{in}$ | Sum (S) | $C_{out}$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

### K-Map ลดรูป Sum และ Carry-out

**K-Map สำหรับ S** $= \sum m(1, 2, 4, 7)$:

```
  ┌──────────┬──────┬──────┬──────┬──────┐
  │ A \ BC   │  00  │  01  │  11  │  10  │
  ├──────────┼──────┼──────┼──────┼──────┤
  │    0     │  0   │  1   │  0   │  1   │
  ├──────────┼──────┼──────┼──────┼──────┤
  │    1     │  1   │  0   │  1   │  0   │
  └──────────┴──────┴──────┴──────┴──────┘
  (ไม่มีกลุ่มที่จัดได้ → ต้องใช้ XOR)
```

$$S = A \oplus B \oplus C_{in}$$

**K-Map สำหรับ $C_{out}$** $= \sum m(3, 5, 6, 7)$:

```
  ┌──────────┬──────┬──────┬──────┬──────┐
  │ A \ BC   │  00  │  01  │  11  │  10  │
  ├──────────┼──────┼──────┼──────┼──────┤
  │    0     │  0   │  0   │  1   │  0   │
  ├──────────┼──────┼──────┼──────┼──────┤
  │    1     │  0   │  1   │  1   │  1   │
  └──────────┴──────┴──────┴──────┴──────┘
```

$$C_{out} = AB + AC_{in} + BC_{in} = AB + C_{in}(A \oplus B)$$

### วงจร Full Adder (gate level):

<img src="./images/full-adder.png" width="650" alt="Full Adder Circuit">

*ที่มา: Wikimedia Commons (Public Domain)*

### 4-bit Ripple Carry Adder (วงจรบวก 4 บิต)

นำ Full Adder 4 ตัวมาต่อกันเป็นลูกโซ่ — $C_{out}$ ของแต่ละหลักต่อเป็น $C_{in}$ ของหลักถัดไป:

<img src="./images/ripple-carry-adder.png" width="650" alt="4-bit Ripple Carry Adder">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

**ตัวอย่าง:** 0101 + 0011 = ?

```
    0 1 0 1    (= 5)
  + 0 0 1 1    (= 3)
  ─────────
  0 1 0 0 0    (= 8)
         ↑
    Carry = 1 ทดไปเรื่อยๆ
```

**IC: 7483** (4-bit Binary Full Adder with Fast Carry)

> ⚠️ **ข้อเสีย Ripple Carry:** Carry ต้อง "ripple" จากหลักต่ำไปหลักสูง → delay สะสม เช่น 8-bit = delay × 8
> 💡 **ทางแก้:** Carry Look-Ahead Adder (CLA) — คำนวณ carry ล่วงหน้าพร้อมกัน

---

## 5.4 Half Subtractor / Full Subtractor

### Half Subtractor (ลบ 2 บิต ไม่มี Borrow-in)

| A | B | Diff (D) | $B_{out}$ |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 |

$$D = A \oplus B$$
$$B_{out} = \overline{A} \cdot B$$

> $B_{out} = 1$ หมายถึง "ยืม" จากหลักถัดไป (เหมือน borrow ในการลบทศนิยม)

### วงจร Half Subtractor:

<img src="./images/half-subtractor.png" width="650" alt="Half Subtractor Circuit">

*ที่มา: Wikimedia Commons (CC0 Public Domain)*

### Full Subtractor (ลบ 3 บิต รวม Borrow-in)

| A | B | $B_{in}$ | Diff (D) | $B_{out}$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 0 | 0 |
| 1 | 1 | 1 | 1 | 1 |

$$D = A \oplus B \oplus B_{in}$$
$$B_{out} = \overline{A}B + B_{in}(\overline{A \oplus B})$$

### วงจร Full Subtractor:

<img src="./images/full-subtractor.png" width="650" alt="Full Subtractor Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 4.0)*

### วงจรลบด้วย Adder + 2's Complement

$$A - B = A + \overline{B} + 1$$

```
 A [4-bit] ──────────────────────────[7483 Adder]─── Result (A−B)
 B [4-bit] ──[NOT each bit]─────────↗
                         Cin = 1 ───↗              Cout = Borrow̄
```

---

## 5.5 Comparator (วงจรเปรียบเทียบ)

เปรียบเทียบเลขฐานสอง 2 จำนวน → 3 เอาต์พุต: $A>B$, $A<B$, $A=B$

### 1-bit Comparator

| A | B | $A>B$ | $A=B$ | $A<B$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | 0 |
| 0 | 1 | 0 | 0 | 1 |
| 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 | 0 |

$$GT = A\overline{B}, \quad EQ = \overline{A \oplus B}, \quad LT = \overline{A}B$$

### วงจร 1-bit Comparator:

<img src="./images/comparator-1bit.png" width="650" alt="1-bit Binary Comparator">

*ที่มา: Wikimedia Commons (CC BY 4.0)*

### 4-bit Comparator (IC 7485)

เปรียบเทียบ A (A3-A0) กับ B (B3-B0) โดยเริ่มจาก **MSB ก่อน**:

```
  ถ้า A3 ≠ B3 → ผลลัพธ์จาก bit นี้เลย
  ถ้า A3 = B3 → ดู A2 ≠ B2
  ถ้า A2 = B2 → ดู A1 ≠ B1
  ถ้า A1 = B1 → ดู A0 ≠ B0
  ถ้าทุก bit เท่ากัน → ดูจาก Cascade Input

       ┌──────────────┐
  A ──→│   7485       ├──→ A > B
  B ──→│ Comparator   ├──→ A = B
       │              ├──→ A < B
  IA>B →│  Cascade     │
  IA=B →│  Input       │
  IA<B →│              │
       └──────────────┘
```

> IC **7485** มีขา Cascade Input: $I_{A>B}$, $I_{A<B}$, $I_{A=B}$ สำหรับต่อขยายเป็น n-bit comparator

---

# ส่วนที่ 2: วงจรจัดการข้อมูล (Data Routing Circuits)

---

## 5.6 Encoder (ตัวเข้ารหัส)

แปลง $2^n$ input lines → $n$-bit binary output

> มีเพียง **1 input ที่ active** ในแต่ละเวลา → บอกว่า "input ตัวไหน active"

### 8-to-3 Encoder (Octal-to-Binary)

```
  I₀ ──┐
  I₁ ──┤
  I₂ ──┤
  I₃ ──┤──[8-to-3 Encoder]──→ D₂ D₁ D₀ (3-bit code)
  I₄ ──┤    (OR gates only)
  I₅ ──┤
  I₆ ──┤
  I₇ ──┘
```

| Input Active | $D_2$ | $D_1$ | $D_0$ |
|:---:|:---:|:---:|:---:|
| $I_0$ | 0 | 0 | 0 |
| $I_1$ | 0 | 0 | 1 |
| $I_2$ | 0 | 1 | 0 |
| $I_3$ | 0 | 1 | 1 |
| $I_4$ | 1 | 0 | 0 |
| $I_5$ | 1 | 0 | 1 |
| $I_6$ | 1 | 1 | 0 |
| $I_7$ | 1 | 1 | 1 |

### สมการของ 8-to-3 Encoder:

$$D_0 = I_1 + I_3 + I_5 + I_7$$
$$D_1 = I_2 + I_3 + I_6 + I_7$$
$$D_2 = I_4 + I_5 + I_6 + I_7$$

วงจรใช้เพียง **OR gates เท่านั้น**

### วงจร 8-to-3 Encoder:

<img src="./images/encoder-8to3.png" width="650" alt="8-to-3 Encoder Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 4.0)*

### 16-to-4 Encoder

ขยายจาก 8-to-3 → รับ **16 input lines** แปลงเป็น **4-bit** output

```
  I₀  ──┐
  I₁  ──┤
  I₂  ──┤
  I₃  ──┤
  I₄  ──┤──[16-to-4 Encoder]──→ D₃ D₂ D₁ D₀ (4-bit code)
  I₅  ──┤    (OR gates only)
  I₆  ──┤
  I₇  ──┤
  I₈  ──┤
  I₉  ──┤
  I₁₀ ──┤
  I₁₁ ──┤
  I₁₂ ──┤
  I₁₃ ──┤
  I₁₄ ──┤
  I₁₅ ──┘
```

### สมการของ 16-to-4 Encoder:

$$D_0 = I_1 + I_3 + I_5 + I_7 + I_9 + I_{11} + I_{13} + I_{15}$$
$$D_1 = I_2 + I_3 + I_6 + I_7 + I_{10} + I_{11} + I_{14} + I_{15}$$
$$D_2 = I_4 + I_5 + I_6 + I_7 + I_{12} + I_{13} + I_{14} + I_{15}$$
$$D_3 = I_8 + I_9 + I_{10} + I_{11} + I_{12} + I_{13} + I_{14} + I_{15}$$

### วงจร 16-to-4 Encoder:

<img src="./images/encoder-16to4.png" width="650" alt="16-to-4 Encoder Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 4.0)*

> 💡 ต่อ Encoder 2 ตัว ขนาด 8-to-3 + วงจรเลือก MSB เพื่อสร้าง 16-to-4 ได้

### วงจร Simple Encoder (4-to-2 ตัวอย่าง):

<img src="./images/encoder-4to2.png" width="650" alt="4-to-2 Simple Encoder">

*ที่มา: Wikimedia Commons (CC BY-SA 4.0)*

### Priority Encoder ⭐

เมื่อมีหลายอินพุต active พร้อมกัน → เลือกตัวที่มี **ลำดับความสำคัญสูงสุด** (index สูงสุด)

เพิ่ม output พิเศษ **V (Valid)** = 1 เมื่อมี input active อย่างน้อย 1 ตัว

**IC 74148** — 8-to-3 Priority Encoder (Active LOW):

| $I_7$ | $I_6$ | $I_5$ | $I_4$ | $I_3$ | $I_2$ | $I_1$ | $I_0$ | $A_2$ | $A_1$ | $A_0$ | V |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | **0** | 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 | 1 | **0** | X | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 1 | **0** | X | X | 0 | 1 | 0 | 1 |
| 1 | 1 | 1 | 1 | **0** | X | X | X | 0 | 1 | 1 | 1 |
| 1 | 1 | 1 | **0** | X | X | X | X | 1 | 0 | 0 | 1 |
| 1 | 1 | **0** | X | X | X | X | X | 1 | 0 | 1 | 1 |
| 1 | **0** | X | X | X | X | X | X | 1 | 1 | 0 | 1 |
| **0** | X | X | X | X | X | X | X | 1 | 1 | 1 | 1 |

> 74148 ใช้ logic Active LOW: อินพุต 0 = active

---

## 5.7 Decoder (ตัวถอดรหัส) ⭐

แปลง $n$-bit input → $2^n$ output lines (active เพียง 1 เส้นในแต่ละเวลา)

> ตรงข้ามกับ Encoder — บอกว่า "input นี้ตรงกับ output ตัวไหน"

### 2-to-4 Decoder

<img src="./images/decoder-2to4.png" width="650" alt="2-to-4 Decoder Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

| $A_1$ | $A_0$ | $D_0$ | $D_1$ | $D_2$ | $D_3$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | **1** | 0 | 0 | 0 |
| 0 | 1 | 0 | **1** | 0 | 0 |
| 1 | 0 | 0 | 0 | **1** | 0 |
| 1 | 1 | 0 | 0 | 0 | **1** |

$$D_0 = \overline{A_1}\,\overline{A_0}, \quad D_1 = \overline{A_1}\,A_0, \quad D_2 = A_1\,\overline{A_0}, \quad D_3 = A_1\,A_0$$

แต่ละเอาต์พุต = **minterm 1 ตัว** ของอินพุต

### 3-to-8 Decoder (IC 74138)

มี **Enable inputs** 3 ตัว ($E_1$ active HIGH, $E_2$ และ $E_3$ active LOW):

```
  ┌──────────────────┐
  │  74138           │
  ──┤ A (LSB)        ├── Y0 = Ā B̄ C̄ · EN  (Active LOW)
  ──┤ B              ├── Y1 = Ā B̄ C  · EN
  ──┤ C (MSB)        ├── Y2 = Ā B  C̄ · EN
  ──┤ E1 (HIGH)      ├── Y3 = Ā B  C  · EN
  ──┤ /E2 (LOW)      ├── Y4 = A  B̄ C̄ · EN
  ──┤ /E3 (LOW)      ├── Y5 = A  B̄ C  · EN
  └──────────────────┘── Y6 = A  B  C̄ · EN
                      ── Y7 = A  B  C  · EN
```

เมื่อ $EN = E_1 \cdot \overline{E_2} \cdot \overline{E_3} = 1$ → เอาต์พุต Active LOW

### วงจร 3-to-8 Decoder:

<img src="./images/decoder-3to8.png" width="650" alt="3-to-8 Decoder Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

### ประยุกต์: ใช้ Decoder สร้างฟังก์ชันบูลีน ⭐

เนื่องจากแต่ละเอาต์พุต Decoder = minterm 1 ตัว → ต่อ NAND gate เข้ากับเอาต์พุตที่ต้องการ

**ตัวอย่าง:** $F(A,B,C) = \sum m(1, 3, 5, 6)$ จาก 74138:

```
  Y1 (m1) ──┐
  Y3 (m3) ──┤──[NAND]──── F
  Y5 (m5) ──┤
  Y6 (m6) ──┘
```

> ⚠️ 74138 เอาต์พุต Active LOW → ใช้ NAND แทน OR

### ต่อ Decoder ขนาดเล็กเป็นขนาดใหญ่ (4-to-16):

```
  A3 ──→ [Enable Control]
                   ├──→ EN of [74138 #1] → Y0–Y7  (เมื่อ A3=0)
  A2 A1 A0 ─┬────→ └──→ EN of [74138 #2] → Y8–Y15 (เมื่อ A3=1)
             ├──────────→ [74138 #1] A,B,C
             └──────────→ [74138 #2] A,B,C
```

<img src="./images/decoder-4to16.png" width="650" alt="4-to-16 Decoder Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

### BCD to 7-Segment Decoder ⭐

<img src="./images/7segment-display.png" width="650" alt="7-Segment Display Labeled">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

| BCD (DCBA) | หลัก | a | b | c | d | e | f | g |
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

#### ตัวอย่าง: K-Map ลดรูป segment `g`

$$g = \sum m(2, 3, 4, 5, 6, 9) + \sum d(10, 11, 12, 13, 14, 15)$$

```
  ┌─────────┬──────┬──────┬──────┬──────┐
  │ AB \ CD │  00  │  01  │  11  │  10  │
  ├─────────┼──────┼──────┼──────┼──────┤
  │   00    │  0   │  0   │  1   │  1   │
  ├─────────┼──────┼──────┼──────┼──────┤
  │   01    │  1   │  1   │  0   │  1   │
  ├─────────┼──────┼──────┼──────┼──────┤
  │   11    │  X   │  X   │  X   │  X   │
  ├─────────┼──────┼──────┼──────┼──────┤
  │   10    │  1   │  X   │  X   │  X   │
  └─────────┴──────┴──────┴──────┴──────┘
```

→ $g = A + BC + B\overline{D} + \overline{B}C\overline{D}$

**IC: 7447** (active LOW, common-anode) | **IC: 4511** (active HIGH, CMOS)

---

## 5.8 Multiplexer — MUX (ตัวเลือกสัญญาณ) ⭐

เลือก **1 อินพุตจากหลายตัว** ส่งไปเอาต์พุต ตาม Select lines

> คิดว่าเป็น "สวิตช์หมุนดิจิทัล" — n select bits → เลือกจาก $2^n$ inputs

### MUX 2:1 (พื้นฐาน)

รับ **2 อินพุต** เลือกด้วย **1 Select bit**:

<img src="./images/mux-2to1.png" width="650" alt="Multiplexer 2:1 Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

$$Y = \overline{S}\,I_0 + S\,I_1$$

| $S$ | Y |
|:---:|:---:|
| 0 | $I_0$ |
| 1 | $I_1$ |

**IC: 74157** (Quad 2:1 MUX)

### วงจร MUX (4:1):

<img src="./images/mux-4to1.png" width="650" alt="Multiplexer 4:1 Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

$$Y = \overline{S_1}\,\overline{S_0}\,I_0 + \overline{S_1}\,S_0\,I_1 + S_1\,\overline{S_0}\,I_2 + S_1\,S_0\,I_3$$

| $S_1$ | $S_0$ | Y |
|:---:|:---:|:---:|
| 0 | 0 | $I_0$ |
| 0 | 1 | $I_1$ |
| 1 | 0 | $I_2$ |
| 1 | 1 | $I_3$ |

### MUX 8:1 (IC 74151)

| $S_2$ | $S_1$ | $S_0$ | Y |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | $I_0$ |
| 0 | 0 | 1 | $I_1$ |
| 0 | 1 | 0 | $I_2$ |
| 0 | 1 | 1 | $I_3$ |
| 1 | 0 | 0 | $I_4$ |
| 1 | 0 | 1 | $I_5$ |
| 1 | 1 | 0 | $I_6$ |
| 1 | 1 | 1 | $I_7$ |

<img src="./images/mux-8to1.png" width="650" alt="Multiplexer 8:1 Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

**IC: 74153** (Dual 4:1 MUX), **74151** (8:1 MUX)

### MUX 16:1

รับ **16 อินพุต** เลือกด้วย **4 Select bits** ($S_3 S_2 S_1 S_0$):

<img src="./images/mux-16to1.png" width="650" alt="Multiplexer 16:1 Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

$$Y = \sum_{i=0}^{15} m_i \cdot I_i \quad \text{(เลือก } I_i \text{ ที่ตรงกับ } S_3S_2S_1S_0 = i\text{)}$$

> 💡 สร้างจาก MUX 8:1 × 2 + MUX 2:1 ต่อขยาย หรือใช้ IC **74150** (16:1 MUX)

### MUX เป็น Universal Function Generator ⭐

**เทคนิค 1:** ต่อ Select = ตัวแปรทั้งหมด, Data input = ค่าฟังก์ชัน

**ตัวอย่าง:** ใช้ MUX 4:1 สร้าง $F(A,B) = \sum m(1, 2, 3)$

```
  S₁=A, S₀=B  →  I₀=0  I₁=1  I₂=1  I₃=1
  → F = A + B
```

**เทคนิค 2:** MUX $2^{n-1}$:1 สร้างฟังก์ชัน n ตัวแปร — ตัวแปรสุดท้ายต่อที่ data input โดยตรง

**ตัวอย่าง:** ใช้ MUX 4:1 สร้าง $F(A,B,C) = \sum m(1, 2, 4, 7)$

| A | B | $C=0$ | $C=1$ | Data Input |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 1 | $C$ |
| 0 | 1 | 1 | 0 | $\overline{C}$ |
| 1 | 0 | 1 | 0 | $\overline{C}$ |
| 1 | 1 | 0 | 1 | $C$ |

### ต่อ MUX ขยายขนาด (สร้าง 8:1 จาก 4:1 × 2):

```
  I₀–I₃ ──[MUX 4:1 #1]──┐
                          ├──[MUX 2:1]──── Y
  I₄–I₇ ──[MUX 4:1 #2]──┘
  S₁S₀ ──→ ทั้ง 2 ตัว   S₂ ──→ MUX 2:1
```

---

## 5.9 Demultiplexer — DEMUX (ตัวกระจายสัญญาณ)

รับ **1 อินพุต** กระจายไปยัง **1 ใน $2^n$ เอาต์พุต** ตาม Select lines

### DEMUX 1-to-2 (พื้นฐาน)

กระจาย D ไป 1 ใน 2 เอาต์พุต ด้วย **1 Select bit**:

<img src="./images/demux-1to2.png" width="650" alt="DEMUX 1-to-2 Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

| $S$ | $Y_0$ | $Y_1$ |
|:---:|:---:|:---:|
| 0 | D | 0 |
| 1 | 0 | D |

$$Y_0 = D \cdot \overline{S}, \quad Y_1 = D \cdot S$$

### วงจร DEMUX 1-to-4:

<img src="./images/demux-1to4.png" width="650" alt="DEMUX 1-to-4 Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

| $S_1$ | $S_0$ | $Y_0$ | $Y_1$ | $Y_2$ | $Y_3$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | D | 0 | 0 | 0 |
| 0 | 1 | 0 | D | 0 | 0 |
| 1 | 0 | 0 | 0 | D | 0 |
| 1 | 1 | 0 | 0 | 0 | D |

$$Y_0 = D \cdot \overline{S_1}\,\overline{S_0}, \quad Y_1 = D \cdot \overline{S_1}\,S_0, \quad Y_2 = D \cdot S_1\,\overline{S_0}, \quad Y_3 = D \cdot S_1\,S_0$$

### DEMUX 1-to-8

กระจาย D ไป 1 ใน 8 เอาต์พุต ด้วย **3 Select bits** ($S_2 S_1 S_0$):

<img src="./images/demux-1to8.png" width="650" alt="DEMUX 1-to-8 Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

| $S_2$ | $S_1$ | $S_0$ | Output Active |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | $Y_0 = D$ |
| 0 | 0 | 1 | $Y_1 = D$ |
| 0 | 1 | 0 | $Y_2 = D$ |
| 0 | 1 | 1 | $Y_3 = D$ |
| 1 | 0 | 0 | $Y_4 = D$ |
| 1 | 0 | 1 | $Y_5 = D$ |
| 1 | 1 | 0 | $Y_6 = D$ |
| 1 | 1 | 1 | $Y_7 = D$ |

**IC: 74138** (ใช้เป็น DEMUX 1-to-8 โดยต่อ Data เข้าขา Enable)

### DEMUX 1-to-16

กระจาย D ไป 1 ใน 16 เอาต์พุต ด้วย **4 Select bits** ($S_3 S_2 S_1 S_0$):

<img src="./images/demux-1to16.png" width="650" alt="DEMUX 1-to-16 Circuit">

*ที่มา: Wikimedia Commons (CC BY-SA 3.0)*

```
  S3 S2 S1 S0 → เลือก Y0–Y15 ที่ D จะถูกส่งไป

  สร้างจาก 74138 × 2 ตัว:
  S3 = 0 → [74138 #1] ใช้งาน → Y0–Y7
  S3 = 1 → [74138 #2] ใช้งาน → Y8–Y15
  S2 S1 S0 → ต่อร่วม A, B, C ทั้ง 2 ตัว
```

**IC: 74154** (4-to-16 Decoder / DEMUX 1-to-16)

### Decoder ← → DEMUX

**Decoder + Enable = DEMUX** — ต่อ Data เข้าที่ขา Enable ของ 74138

### ประยุกต์: Data Multiplexing ผ่านสายเดียว

```
  Ch0 ──┐                             ┌── Ch0
  Ch1 ──┤──[MUX]──[single wire]──[DEMUX]──┤── Ch1
  Ch2 ──┤                             ├── Ch2
  Ch3 ──┘                             └── Ch3
          S₁S₀ (sync clock)          S₁S₀
```

---

## 5.10 สรุปเปรียบเทียบวงจรเชิงผสม

| วงจร | ทิศทาง | Input | Output | IC |
|:---|:---:|:---:|:---:|:---:|
| Encoder | $2^n \to n$ | $2^n$ | $n$ | 74148 |
| Priority Encoder | $2^n \to n$ (priority) | $2^n$ | $n+1$ (V) | 74148 |
| Decoder | $n \to 2^n$ | $n$ | $2^n$ | 74138, 74139 |
| MUX | หลาย → 1 | $2^n + n$ | 1 | 74151, 74153 |
| DEMUX | 1 → หลาย | $1 + n$ | $2^n$ | 74138 |

### IC สรุปที่ต้องรู้:

| IC | ฟังก์ชัน | หมายเหตุ |
|:---:|:---|:---|
| **7483** | 4-bit Full Adder | พร้อม Fast Carry |
| **7485** | 4-bit Magnitude Comparator | Cascade ได้ |
| **74138** | 3-to-8 Decoder / DEMUX 1-to-8 | Active LOW output |
| **74139** | Dual 2-to-4 Decoder | Active LOW output |
| **74148** | 8-to-3 Priority Encoder | Active LOW I/O |
| **74151** | 8:1 MUX | มี complement output |
| **74153** | Dual 4:1 MUX | 2 ตัวใน IC เดียว |
| **7447** | BCD→7-Seg Decoder | Active LOW, common-anode |
| **4511** | BCD→7-Seg Decoder | Active HIGH, CMOS |

---

## แบบฝึกหัดท้ายบท

1. ออกแบบ 4-bit Ripple Carry Adder จาก Full Adder — วาดแผนผังและทดสอบ 6+9
2. ใช้ MUX 4:1 สร้างฟังก์ชัน $F(A,B,C) = \sum m(0, 2, 5, 7)$ ด้วยเทคนิคตัวแปรสุดท้าย
3. ใช้ MUX 8:1 สร้างฟังก์ชัน $F(A,B,C) = \sum m(1, 2, 6, 7)$
4. ใช้ Decoder 3-to-8 + NAND gate สร้าง $F(A,B,C) = \sum m(0, 3, 5, 6)$
5. ออกแบบ BCD to 7-Segment สำหรับ segment `e` โดยใช้ K-Map
6. เปรียบเทียบข้อดีข้อเสียของ Normal Encoder กับ Priority Encoder
7. ต่อวงจร 4-bit Adder + 7-Segment Display บน **Tinkercad** โดยใช้ IC 7483 + 4511
8. ออกแบบวงจร 2's complement subtractor โดยใช้ IC 7483 + NOT gates
