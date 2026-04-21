# Chapter 3: พีชคณิตบูลีน

## Boolean Algebra

---

## 3.1 บทนำ

**พีชคณิตบูลีน (Boolean Algebra)** คือระบบคณิตศาสตร์ที่ใช้ในการวิเคราะห์และ **ลดรูป** วงจรตรรกะ โดยตัวแปรมีค่าได้เพียง `0` หรือ `1` เท่านั้น

> 💡 **ทำไมต้องลดรูป?** สมการที่สั้นลง = เกตน้อยลง = ต้นทุนต่ำลง + วงจรเร็วขึ้น

---

## 3.2 ตัวดำเนินการพื้นฐาน (Basic Operations)

| ตัวดำเนินการ | สัญลักษณ์ | ความหมาย | เกตที่สอดคล้อง |
|:---:|:---:|:---:|:---:|
| AND | $A \cdot B$ หรือ $AB$ | คอนจังก์ชัน | AND gate |
| OR | $A + B$ | ดิสจังก์ชัน | OR gate |
| NOT | $\overline{A}$ หรือ $A'$ | คอมพลีเมนต์ | NOT gate |

**ลำดับความสำคัญ (Precedence):** NOT > AND > OR

$$\text{ตัวอย่าง: } A + B \cdot \overline{C} = A + (B \cdot (\overline{C}))$$

### ตาราง Truth Table ของตัวดำเนินการพื้นฐาน

| A | B | $A \cdot B$ | $A + B$ | $\overline{A}$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

### ตัวอย่างการคำนวณ

**กำหนด:** $A = 1, B = 0, C = 1$

| นิพจน์ | การคำนวณ | ผลลัพธ์ |
|:---|:---|:---:|
| $AB$ | $1 \cdot 0$ | **0** |
| $A + B$ | $1 + 0$ | **1** |
| $\overline{A}$ | $\overline{1}$ | **0** |
| $AB + C$ | $0 + 1$ | **1** |
| $A(B + C)$ | $1 \cdot (0 + 1)$ | **1** |
| $\overline{A + B}$ | $\overline{1 + 0} = \overline{1}$ | **0** |
| $\overline{A} \cdot \overline{B}$ | $0 \cdot 1$ | **0** |

### ตาราง Truth Table ของตัวดำเนินการพื้นฐาน

| A | B | $A \cdot B$ | $A + B$ | $\overline{A}$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

### ตัวอย่างการคำนวณ


### พิสูจน์กฎพื้นฐานด้วย Truth Table

**พิสูจน์ $A + \overline{A} = 1$ และ $A \cdot \overline{A} = 0$**

| A | $\overline{A}$ | $A + \overline{A}$ | $A \cdot \overline{A}$ |
|:---:|:---:|:---:|:---:|
| 0 | 1 | **1** | **0** |
| 1 | 0 | **1** | **0** |

**พิสูจน์ Idempotent $A + A = A$**

| A | $A + A$ |
|:---:|:---:|
| 0 | 0 |
| 1 | 1 |

**พิสูจน์ Involution $\overline{\overline{A}} = A$**

| A | $\overline{A}$ | $\overline{\overline{A}}$ |
|:---:|:---:|:---:|
| 0 | 1 | **0** |
| 1 | 0 | **1** |
**กำหนด:** $A = 1, B = 0, C = 1$

| นิพจน์ | การคำนวณ | ผลลัพธ์ |
|:---|:---|:---:|
| $AB$ | $1 \cdot 0$ | **0** |
| $A + B$ | $1 + 0$ | **1** |
| $\overline{A}$ | $\overline{1}$ | **0** |
| $AB + C$ | $0 + 1$ | **1** |
| $A(B + C)$ | $1 \cdot (0 + 1)$ | **1** |
| $\overline{A + B}$ | $\overline{1 + 0} = \overline{1}$ | **0** |
> **ตัวอย่าง:** $1 \cdot 0 = 0 \cdot 1 = 0$ &nbsp;&nbsp; $1 + 0 = 0 + 1 = 1$

### Associative Law (จัดหมู่)

$$(A \cdot B) \cdot C = A \cdot (B \cdot C)$$
$$(A + B) + C = A + (B + C)$$

> **ตัวอย่าง:** $(1 \cdot 1) \cdot 0 = 1 \cdot (1 \cdot 0) = 0$ — จัดหมู่อย่างไรก็ได้ผลเหมือนกัน

### Distributive Law (แจกแจง)

$$A \cdot (B + C) = AB + AC$$
$$A + BC = (A + B)(A + C) \quad \text{⭐ สำคัญ!}$$

> ⚠️ กฎข้อที่ 2 ไม่มีใน Algebra ปกติ — เป็นเอกลักษณ์ของ Boolean Algebra

**พิสูจน์ $A + BC = (A+B)(A+C)$ ด้วย Truth Table:**

| A | B | C | BC | A+BC | A+B | A+C | (A+B)(A+C) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | **0** |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | **0** |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 | **1** |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | **1** |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | **1** |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |

### Absorption Law (ดูดซับ)

$$A + AB = A$$
$$A(A + B) = A$$

**พิสูจน์ $A + AB = A$ ด้วยพีชคณิต:**

$$A + AB = A \cdot 1 + AB \quad [\text{Identity}]$$
$$= A(1 + B) \quad [\text{Distributive}]$$
$$= A \cdot 1 \quad [\text{Null: } 1 + B = 1]$$
$$= A \quad [\text{Identity}]$$

**Absorption ขยาย:**

$$A + \overline{A}B = A + B$$
$$A(\overline{A} + B) = AB$$

### Consensus Theorem

$$AB + \overline{A}C + BC = AB + \overline{A}C$$
$$(A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$$

> 💡 เทอม $BC$ เป็น **consensus term** ที่ตัดออกได้เสมอ

**พิสูจน์ด้วยพีชคณิต:**

$$AB + \overline{A}C + BC$$
$$= AB + \overline{A}C + BC(A + \overline{A}) \quad [\text{Complement}]$$
$$= AB + \overline{A}C + ABC + \overline{A}BC \quad [\text{Distributive}]$$
$$= AB(1 + C) + \overline{A}C(1 + B) \quad [\text{จัดกลุ่ม}]$$
$$= AB + \overline{A}C \quad [\text{Null: } 1+x=1]$$
**พิสูจน์ Idempotent $A + A = A$**

| A | $A + A$ |
|:---:|:---:|
| 0 | 0 |
| 1 | 1 |

**พิสูจน์ Involution $\overline{\overline{A}} = A$**

| A | $\overline{A}$ | $\overline{\overline{A}}$ |
|:---:|:---:|:---:|
| 0 | 1 | **0** |
| 1 | 0 | **1** |

---

## 3.4 กฎสำคัญ (Important Laws)

### Commutative Law (สลับที่)

$$A \cdot B = B \cdot A$$
$$A + B = B + A$$

> **ตัวอย่าง:** $1 \cdot 0 = 0 \cdot 1 = 0$ &nbsp;&nbsp; $1 + 0 = 0 + 1 = 1$

### Associative Law (จัดหมู่)

$$(A \cdot B) \cdot C = A \cdot (

### ตัวอย่าง De Morgan แบบ Step-by-Step

**ตัวอย่างที่ 1:** แปลง $\overline{AB + C}$

$$\overline{AB + C}$$
$$= \overline{AB} \cdot \overline{C} \quad [\text{De Morgan Theorem 2}]$$
$$= (\overline{A} + \overline{B}) \cdot \overline{C} \quad [\text{De Morgan Theorem 1}]$$

**ตัวอย่างที่ 2:** แปลง $\overline{(A + B)(C + D)}$

$$\overline{(A + B)(C + D)}$$
$$= \overline{(A + B)} + \overline{(C + D)} \quad [\text{De Morgan Theorem 1}]$$
$$= (\overline{A} \cdot \overline{B}) + (\overline{C} \cdot \overline{D}) \quad [\text{De Morgan Theorem 2}]$$

**ตัวอย่างที่ 3:** หา complement ของ $F = A\overline{B} + \overline{A}B$

$$\overline{F} = \overline{A\overline{B} + \overline{A}B}$$
$$= \overline{A\overline{B}} \cdot \overline{\overline{A}B} \quad [\text{De Morgan}]$$
$$= (\overline{A} + B)(A + \overline{B}) \quad [\text{De Morgan}]$$
$$= \overline{A}A + \overline{A}\,\overline{B} + BA + B\overline{B} \quad [\text{Distributive}]$$
$$= 0 + \overline{A}\,\overline{B} + AB + 0 \quad [\text{Complement}]$$
$$= \overline{A}\,\overline{B} + AB$$

> 💡 $F = A \oplus B$ และ $\overline{F} = A \odot B$ (XNOR) — De Morgan ยืนยันความสัมพันธ์ XOR กับ XNOR

### พิสูจน์ De Morgan ด้วย Truth Table

**พิสูจน์ $\overline{A \cdot B} = \overline{A} + \overline{B}$**

| A | B | $A \cdot B$ | $\overline{A \cdot B}$ | $\overline{A}$ | $\overline{B}$ | $\overline{A} + \overline{B}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | **1** | 1 | 1 | **1** |
| 0 | 1 | 0 | **1** | 1 | 0 | **1** |
| 1 | 0 | 0 | **1** | 0 | 1 | **1** |
| 1 | 1 | 1 | **0** | 0 | 0 | **0** |B \cdot C)$$
$$(A + B) + C = A + (B + C)$$

> **ตัวอย่าง:** $(1 \cdot 1) \cdot 0 = 1 \cdot (1 \cdot 0) = 0$ — จัดหมู่อย่างไรก็ได้ผลเหมือนกัน

### Distributive Law (แจกแจง)

$$A \cdot (B + C) = AB + AC$$
$$A + BC = (A + B)(A + C) \quad \text{⭐ สำคัญ!}$$

> ⚠️ กฎข้อที่ 2 ไม่มีใน Algebra ปกติ — เป็นเอกลักษณ์ของ Boolean Algebra

**พิสูจน์ $A + BC = (A+B)(A+C)$ ด้วย Truth Table:**

| A | B | C | BC | A+BC | A+B | A+C | (A+B)(A+C) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | **0** |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | **0** |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | **0** |
| 0 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |
| 1 | 0 | 0 | 0 | 1 | 1 | 1 | **1** |
| 1 | 0 | 1 | 0 | 1 | 1 | 1 | **1** |
| 1 | 1 | 0 | 0 | 1 | 1 | 1 | **1** |
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | **1** |

### Absorption Law (ดูดซับ)

$$A + AB = A$$
$$A(A + B) = A$$

**พิสูจน์ $A + AB = A$ ด้วยพีชคณิต:**

$$A + AB = A \cdot 1 + AB \quad [\text{Identity}]$$
$$= A(1 + B) \quad [\text{Distributive}]$$
$$= A \cdot 1 \quad [\text{Null: } 1 + B = 1]$$
$$= A \quad [\text{Identity}]$$

### ตัวอย่างที่ 6: ลดรูปซับซ้อน 3 ขั้นตอน

$$F = (A + B)(A + \overline{B})$$
$$= A + B\overline{B} \quad [\text{Distributive Boolean}]$$
$$= A + 0 \quad [\text{Complement}]$$
$$= A \quad [\text{Identity}]$$

### ตัวอย่างที่ 7: มี 4 ตัวแปร

$$F = ABCD + AB\overline{C}D + AB\overline{C}\,\overline{D} + ABC\overline{D}$$
$$= ABD(C + \overline{C}) + AB\overline{C}(D + \overline{D}) \quad [\text{จัดกลุ่ม}]$$
Wait, let me redo:
$$= ABD(C + \overline{C}) + AB\overline{C}\,\overline{D} \quad [\text{step 1}]$$
Let me use a cleaner example:

$$F = AB + A\overline{B}C + \overline{A}BC + \overline{A}\,\overline{B}C$$
$$= AB + C(A\overline{B} + \overline{A}B + \overline{A}\,\overline{B}) \quad [\text{Distributive}]$$
$$= AB + C(A\overline{B} + \overline{A}(B + \overline{B})) \quad [\text{Distributive}]$$
$$= AB + C(A\overline{B} + \overline{A}) \quad [\text{Complement}]$$
$$= AB + C(\overline{A} + A\overline{B}) \quad [\text{Commutative}]$$
$$= AB + C(\overline{A} + \overline{B}) \quad [\text{Absorption}]$$
$$= AB + C\,\overline{AB} \quad [\text{De Morgan}]$$
$$= AB + C \quad [\text{Absorption ขยาย: } X + \overline{X}Y = X + Y]$$

**Absorption ขยาย:**

$$A + \overline{A}B = A + B$$
$$A(\overline{A} + B) = AB$$

### Consensus Theorem

$$AB + \overline{A}C + BC = AB + \overline{A}C$$
$$(A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$$

> 💡 เทอม $BC$ เป็น **consensus term** ที่ตัดออกได้เสมอ

**พิสูจน์ด้วยพีชคณิต:**

$$AB + \overline{A}C + BC$$
$$= AB + \overline{A}C + BC(A + \overline{A}) \quad [\text{Complement}]$$
$$= AB + \overline{A}C + ABC + \overline{A}BC \quad [\text{Distributive}]$$
$$= AB(1 + C) + \overline{A}C(1 + B) \quad [\text{จัดกลุ่ม}]$$
$$= AB + \overline{A}C \quad [\text{Null: } 1+x=1]$$

---

## 3.5 ทฤษฎีบทเดอมอร์แกน (De Morgan's Theorem) ⭐

### Theorem 1:

$$\overline{A \cdot B} = \overline{A} + \overline{B}$$

> "NOT ของ AND = OR ของ NOT"

### Theorem 2:

$$\overline{A + B} = \overline{A} \cdot \overline{B}$$

> "NOT ของ OR = AND ของ NOT"

### ขยายไปหลายตัวแปร:

$$\overline{A \cdot B \cdot C \cdots} = \overline{A} + \overline{B} + \overline{C} + \cdots$$

$$\overline{A + B + C + \cdots} = \overline{A} \cdot \overline{B} \cdot \overline{C} \cdots$$

### วิธีจำง่าย:

1. **แยกเส้น** (break the bar)
2. **เปลี่ยนเครื่องหมาย** (AND↔OR)
3. **กลับบิตตัวแปร** ที่อยู่ภายใน

### ตัวอย่าง De Morgan แบบ Step-by-Step

**ตัวอย่างที่ 1:** แปลง $\overline{AB + C}$

$$\overline{AB + C}$$
$$= \overline{AB} \cdot \overline{C} \quad [\text{De Morgan Theorem 2}]$$
$$= (\overline{A} + \overline{B}) \cdot \overline{C} \quad [\text{De Morgan Theorem 1}]$$

**ตัวอย่างที่ 2:** แปลง $\overline{(A + B)(C + D)}$

$$\overline{(A + B)(C + D)}$$
$$= วงจร → สมการ (ตัวอย่าง)

```
A ──┐
    AND ──┐
B ──┘     OR ── Y
C ────────┘
```

อ่านจากซ้ายไปขวา: AND gate รับ A, B → ได้ $AB$, จากนั้น OR กับ C:

$$Y = AB + C$$

```
A ──────────┐
             AND ── NOT ── Y
B ── NOT ──┘
```

$$Y = \overline{A \cdot \overline{B}} = \overline{A} + B \quad [\text{De Morgan}]$$

### สมการ → วงจร (ตัวอย่าง)

**$F = A\overline{B} + \overline{A}B$ (XOR)**

```
A ── NOT ──┐
           AND ──┐
B ─────────┘     OR ── F
A ─────────┐     |
B ── NOT ──┘AND ──┘
```

### การใช้ Universal Gates ในการออกแบบ

ในทางปฏิบัติ นิยมแปลงวงจรให้ใช้ **NAND เท่านั้น** หรือ **NOR เท่านั้น** เพื่อ:
- ใช้ IC ชนิดเดียว → ลดต้นทุน
- ลดจำนวน IC บนบอร์ด

**ขั้นตอนแปลง SOP → NAND-NAND:**

1. เขียนสมการในรูป SOP: $F = AB + CD$
2. ใช้ Double Inversion: $F = \overline{\overline{AB + CD}}$
3. ใช้ De Morgan: $F = \overline{\overline{AB} \cdot \overline{CD}}$
4. แต่ละเทอมเป็น NAND → วงจร NAND 2 ระดับ

```
A ──┐
    NAND ──┐
B ──┘      NAND ── F
C ──┐      |
    NAND ──┘
D ──┘
```

**ขั้นตอนแปลง POS → NOR-NOR:**

1. เขียนสมการในรูป POS: $F = (A+B)(C+D)$
2. ใช้ Double Inversion
3. ใช้ De Morgan → วงจร NOR 2 ระดับ

```
A ──┐
    NOR ──┐
B ──┘     NOR ── F
C ──┐     |
    NOR ──┘
D ──┘
```
| A | B | $A \cdot B$ | $\overline{A \cdot B}$ | $\overline{A}$ | $\overline{B}$ | $\overline{A} + \overline{B}$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | **1** | 1 | 1 | **1** |
| 0 | 1คุณสมบัติของ XOR และ XNOR

ฟังก์ชัน XOR มีคุณสมบัติพิเศษที่ใช้บ่อยในการลดรูปวงจร

### นิยาม

$$A \oplus B = A\overline{B} + \overline{A}B$$

$$A \odot B = \overline{A \oplus B} = AB + \overline{A}\,\overline{B}$$

### คุณสมบัติของ XOR

| คุณสมบัติ | สมการ |
|:---|:---:|
| Commutative | $A \oplus B = B \oplus A$ |
| Associative | $(A \oplus B) \oplus C = A \oplus (B \oplus C)$ |
| Identity | $A \oplus 0 = A$ |
| Null | $A \oplus 1 = \overline{A}$ |
| Self-inverse | $A \oplus A = 0$ |
| Complement | $A \oplus \overline{A} = 1$ |
| XOR-XNOR | $A \oplus B = \overline{A \odot B}$ |

> 💡 **$A \oplus 1 = \overline{A}$** → สามารถใช้ XOR gate ทำหน้าที่เป็น Controlled Inverter

### ตัวอย่างการใช้ XOR ในการลดรูป

$$F = AB + A\overline{B} + \overline{A}B$$
$$= A(B + \overline{B}) + \overline{A}B \quad [\text{Distributive}]$$
$$= A + \overline{A}B \quad [\text{Complement}]$$
$$= A + B \quad [\text{Absorption ขยาย}]$$

หรืออีกทางหนึ่ง สังเกตว่า:
$$AB + A\overline{B} + \overline{A}B = A + (A \oplus B)$$

### Parity ด้วย XOR

XOR หลายตัวใช้ตรวจสอบ **parity** (จำนวนบิต 1 คี่หรือคู่)

$$P = A \oplus B \oplus C \oplus D$$

- $P = 1$ → จำนวนบิต 1 ใน A,B,C,D เป็นจำนวน **คี่**
- $P = 0$ → จำนวนบิต 1 เป็นจำนวน **คู่**

---

## 3.10  | 0 | **1** | 1 | 0 | **1** |
| 1 | 0 | 0 | **1** | 0 | 1 | **1** |
| 1 | 1 | 1 | **0** | 0 | 0 | **0** |

---

## 3.6 ตัวอย่างการลดรูป

### ตัวอย่างที่ 1: ใช้กฎพื้นฐาน

$$F = AB + A\overline{B}$$
$$= A(B + \overline{B}) \quad \text{[Distributive]}$$
$$= A \cdot 1 \quad \text{[Complement]}$$
$$= A \quad \text{[Identity]}$$

### ตัวอย่างที่ 2: ใช้ Absorption

$$F = A + AB$$
$$= A \quad \text{[Absorption]}$$

### ตัวอย่างที่ 3: ซับซ้อนขึ้น

$$F = \overline{A}B + \overline{A}\,\overline{B}C + \overline{A}BC$$
$$= \o1erline{A}(B + \overline{B}C + BC)$$
$$= \overline{A}(B + C(\overline{B} + B))$$
$$= \overline{A}(B + C \cdot 1)$$
$$= \overline{A}(B + C)$$

### ตัวอย่างที่ 4: ใช้ De Morgan

$$F = \overline{\overline{A}B + C\overline{D}}$$
$$= \overline{\overline{A}B} \cdot \overline{C\overline{D}} \quad \text{[De Morgan]}$$
$$= (A + \overline{B})(\overline{C} + D) \quad \text{[De Morgan]}$$

### ตัวอย่างที่ 5: Consensus Theorem

$$F = AB + \overline{A}C + BC$$
$$= AB + \overline{A}C \quad \text{[Consensus: BC ตัดออกได้]}$$

### ตัวอย่างที่ 6: ลดรูปซับซ้อน 3 ขั้นตอน

$$F = (A + B)(A + \overline{B})$$
$$= A + B\overline{B} \quad [\text{Distributive Boolean}]$$
$$= A + 0 \quad [\text{Complement}]$$
$$= A \quad [\text{Identity}]$$
7. พิสูจน์ $A \oplus B = (A + B)(\overline{A} + \overline{B})$ ด้วย Truth Table
8. ลดรูป $F = \overline{A}\,\overline{B}\,\overline{C} + \overline{A}\,\overline{B}C + \overline{A}BC + ABC$
9. แสดงว่า $\overline{AB + \overline{A}\,\overline{B}} = A \oplus B$
10. สร้างวงจร NAND-only สำหรับ $F = (A \oplus B) \cdot C$

### ตัวอย่างที่ 7: มี 4 ตัวแปร

$$F = AB + A\overline{B}C + \overline{A}BC + \overline{A}\,\overline{B}C$$
$$= AB + C(A\overline{B} + \overline{A}B + \overline{A}\,\overline{B}) \quad [\text{Distributive}]$$
$$= AB + C(A\overline{B} + \overline{A}(B + \overline{B})) \quad [\text{Distributive}]$$
$$= AB + C(A\overline{B} + \overline{A}) \quad [\text{Complement}]$$
$$= AB + C(\overline{A} + A\overline{B}) \quad [\text{Commutative}]$$
$$= AB + C(\overline{A} + \overline{B}) \quad [\text{Absorption}]$$
$$= AB + C\,\overline{AB} \quad [\text{De Morgan}]$$
$$= AB + C \quad [\text{Absorption ขยาย: } X + \overline{X}Y = X + Y]$$

---

## 3.7 รูปแบบมาตรฐาน (Canonical Forms)

### Sum of Products (SOP) — ผลรวมของผลคูณ

$$F = \sum m(\ldots)$$

แต่ละ **minterm** คือ AND ของตัวแปรทั้งหมด (ตรงหรือ complement)

**ตัวอย่าง (3 ตัวแปร):**

| Minterm | A | B | C | สัญลักษณ์ |
|:---:|:---:|:---:|:---:|:---:|
| $m_0$ | 0 | 0 | 0 | $\overline{A}\,\overline{B}\,\overline{C}$ |
| $m_1$ | 0 | 0 | 1 | $\overline{A}\,\overline{B}\,C$ |
| $m_2$ | 0 | 1 | 0 | $\overline{A}\,B\,\overline{C}$ |
| $m_3$ | 0 | 1 | 1 | $\overline{A}\,B\,C$ |
| $m_4$ | 1 | 0 | 0 | $A\,\overline{B}\,\overline{C}$ |
| $m_5$ | 1 | 0 | 1 | $A\,\overline{B}\,C$ |
| $m_6$ | 1 | 1 | 0 | $A\,B\,\overline{C}$ |
| $m_7$ | 1 | 1 | 1 | $A\,B\,C$ |

$$F = \sum m(1, 5, 6, 7) = \overline{A}\,\overline{B}\,C + A\,\overline{B}\,C + AB\overline{C} + ABC$$

### Product of Sums (POS) — ผลคูณของผลรวม

$$F = \prod M(\ldots)$$

แต่ละ **maxterm** คือ OR ของตัวแปรทั้งหมด

| Maxterm | A | B | C | สัญลักษณ์ |
|:---:|:---:|:---:|:---:|:---:|
| $M_0$ | 0 | 0 | 0 | $A + B + C$ |
| $M_1$ | 0 | 0 | 1 | $A + B + \overline{C}$ |
| $M_7$ | 1 | 1 | 1 | $\overline{A} + \overline{B} + \overline{C}$ |

### ความสัมพันธ์ SOP ↔ POS

$$\text{Minterm ที่ไม่อยู่ใน SOP} = \text{Maxterm ใน POS}$$

**ตัวอย่าง:**

$$F = \sum m(1, 5, 6, 7) = \prod M(0, 2, 3, 4)$$

---

## 3.8 การแปลงวงจรลอจิกเป็นสมการบูลีน

### วงจร → สมการ

1. เริ่มจากเอาต์พุต
2. เขียนสมการของแต่ละเกตย้อนกลับไปหาอินพุต

### สมการ → วงจร

1. หาลำดับ precedence (NOT > AND > OR)
2. วาดเกตตามลำดับจากอินพุตไปเอาต์พุต

### วงจร → สมการ (ตัวอย่าง)

```
A ──┐
    AND ──┐
B ──┘     OR ── Y
C ────────┘
```

อ่านจากซ้ายไปขวา: AND gate รับ A, B → ได้ $AB$, จากนั้น OR กับ C:

$$Y = AB + C$$

```
A ──────────┐
             AND ── NOT ── Y
B ── NOT ──┘
```

$$Y = \overline{A \cdot \overline{B}} = \overline{A} + B \quad [\text{De Morgan}]$$

### สมการ → วงจร (ตัวอย่าง)

**$F = A\overline{B} + \overline{A}B$ (XOR)**

```
A ── NOT ──┐
           AND ──┐
B ─────────┘     OR ── F
A ─────────┐     |
B ── NOT ──┘AND ──┘
```

### การใช้ Universal Gates ในการออกแบบ

ในทางปฏิบัติ นิยมแปลงวงจรให้ใช้ **NAND เท่านั้น** หรือ **NOR เท่านั้น** เพื่อ:
- ใช้ IC ชนิดเดียว → ลดต้นทุน
- ลดจำนวน IC บนบอร์ด

**ขั้นตอนแปลง SOP → NAND-NAND:**

1. เขียนสมการในรูป SOP: $F = AB + CD$
2. ใช้ Double Inversion: $F = \overline{\overline{AB + CD}}$
3. ใช้ De Morgan: $F = \overline{\overline{AB} \cdot \overline{CD}}$
4. แต่ละเทอมเป็น NAND → วงจร NAND 2 ระดับ

```
A ──┐
    NAND ──┐
B ──┘      NAND ── F
C ──┐      |
    NAND ──┘
D ──┘
```

**ขั้นตอนแปลง POS → NOR-NOR:**

1. เขียนสมการในรูป POS: $F = (A+B)(C+D)$
2. ใช้ Double Inversion
3. ใช้ De Morgan → วงจร NOR 2 ระดับ

```
A ──┐
    NOR ──┐
B ──┘     NOR ── F
C ──┐     |
    NOR ──┘
D ──┘
```

---

## 3.9 คุณสมบัติของ XOR และ XNOR

ฟังก์ชัน XOR มีคุณสมบัติพิเศษที่ใช้บ่อยในการลดรูปวงจร

### นิยาม

$$A \oplus B = A\overline{B} + \overline{A}B$$

$$A \odot B = \overline{A \oplus B} = AB + \overline{A}\,\overline{B}$$

### คุณสมบัติของ XOR

| คุณสมบัติ | สมการ |
|:---|:---:|
| Commutative | $A \oplus B = B \oplus A$ |
| Associative | $(A \oplus B) \oplus C = A \oplus (B \oplus C)$ |
| Identity | $A \oplus 0 = A$ |
| Null | $A \oplus 1 = \overline{A}$ |
| Self-inverse | $A \oplus A = 0$ |
| Complement | $A \oplus \overline{A} = 1$ |
| XOR-XNOR | $A \oplus B = \overline{A \odot B}$ |

> 💡 **$A \oplus 1 = \overline{A}$** → สามารถใช้ XOR gate ทำหน้าที่เป็น Controlled Inverter

### ตัวอย่างการใช้ XOR ในการลดรูป

$$F = AB + A\overline{B} + \overline{A}B$$
$$= A(B + \overline{B}) + \overline{A}B \quad [\text{Distributive}]$$
$$= A + \overline{A}B \quad [\text{Complement}]$$
$$= A + B \quad [\text{Absorption ขยาย}]$$

หรืออีกทางหนึ่ง สังเกตว่า:
$$AB + A\overline{B} + \overline{A}B = A + (A \oplus B)$$

### Parity ด้วย XOR

XOR หลายตัวใช้ตรวจสอบ **parity** (จำนวนบิต 1 คี่หรือคู่)

$$P = A \oplus B \oplus C \oplus D$$

- $P = 1$ → จำนวนบิต 1 ใน A,B,C,D เป็นจำนวน **คี่**
- $P = 0$ → จำนวนบิต 1 เป็นจำนวน **คู่**

---

## 3.10 การพิสูจน์สมการบูลีน

### วิธีที่ 1: ใช้กฎพีชคณิต

จัดรูปทั้งสองข้างให้เท่ากัน โดยใช้กฎต่าง ๆ

### วิธีที่ 2: ใช้ Truth Table

ตรวจสอบทุก combination ว่าให้ผลเหมือนกัน

**ตัวอย่าง:** พิสูจน์ $A + AB = A$

| A | B | AB | A + AB |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | **0** |
| 0 | 1 | 0 | **0** |
| 1 | 0 | 0 | **1** |
| 1 | 1 | 1 | **1** |

คอลัมน์ $A$ กับ $A + AB$ เหมือนกันทุกแถว

---

## 3.11 Duality Principle

ถ้าสมการบูลีนเป็นจริง จะได้สมการ **dual** ที่เป็นจริงเช่นกัน โดย:
- สลับ AND ↔ OR
- สลับ 0 ↔ 1

| ต้นฉบับ | Dual |
|:---|:---|
| $A + 0 = A$ | $A \cdot 1 = A$ |
| $A + \overline{A} = 1$ | $A \cdot \overline{A} = 0$ |
| $A + AB = A$ | $A(A + B) = A$ |

---

## แบบฝึกหัดท้ายบท

1. ลดรูป $F = ABC + AB\overline{C} + \overline{A}BC$
2. ใช้ De Morgan ลดรูป $\overline{(A+B)(\overline{C}+D)}$
3. แปลง $F(A,B,C) = \sum m(0, 2, 5, 7)$ เป็นรูป POS
4. พิสูจน์ $AB + \overline{A}C + BC = AB + \overline{A}C$ (Consensus Theorem) ด้วย Truth Table
5. แปลง $F = AB + CD$ เป็นวงจร NAND-NAND (วาดแผนผังวงจร)
6. เขียน $F = (A+B)(C+D)$ ในรูป SOP
7. พิสูจน์ $A \oplus B = (A + B)(\overline{A} + \overline{B})$ ด้วย Truth Table
8. ลดรูป $F = \overline{A}\,\overline{B}\,\overline{C} + \overline{A}\,\overline{B}C + \overline{A}BC + ABC$
9. แสดงว่า $\overline{AB + \overline{A}\,\overline{B}} = A \oplus B$
10. สร้างวงจร NAND-only สำหรับ $F = (A \oplus B) \cdot C$
7. พิสูจน์ $A \oplus B = (A + B)(\overline{A} + \overline{B})$ ด้วย Truth Table
8. ลดรูป $F = \overline{A}\,\overline{B}\,\overline{C} + \overline{A}\,\overline{B}C + \overline{A}BC + ABC$
9. แสดงว่า $\overline{AB + \overline{A}\,\overline{B}} = A \oplus B$
10. สร้างวงจร NAND-only สำหรับ $F = (A \oplus B) \cdot C$
