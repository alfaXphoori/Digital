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

---

## 3.3 กฎพื้นฐาน (Basic Laws)

| กฎ | AND Form | OR Form |
|:---|:---:|:---:|
| **Identity** | $A \cdot 1 = A$ | $A + 0 = A$ |
| **Null** | $A \cdot 0 = 0$ | $A + 1 = 1$ |
| **Idempotent** | $A \cdot A = A$ | $A + A = A$ |
| **Complement** | $A \cdot \overline{A} = 0$ | $A + \overline{A} = 1$ |
| **Involution** | $\overline{\overline{A}} = A$ | |

---

## 3.4 กฎสำคัญ (Important Laws)

### Commutative Law (สลับที่)

$$A \cdot B = B \cdot A$$
$$A + B = B + A$$

### Associative Law (จัดหมู่)

$$(A \cdot B) \cdot C = A \cdot (B \cdot C)$$
$$(A + B) + C = A + (B + C)$$

### Distributive Law (แจกแจง)

$$A \cdot (B + C) = AB + AC$$
$$A + BC = (A + B)(A + C) \quad \text{⭐ สำคัญ!}$$

> ⚠️ กฎข้อที่ 2 ไม่มีใน Algebra ปกติ — เป็นเอกลักษณ์ของ Boolean Algebra

### Absorption Law (ดูดซับ)

$$A + AB = A$$
$$A(A + B) = A$$

### Consensus Theorem

$$AB + \overline{A}C + BC = AB + \overline{A}C$$
$$(A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$$

> 💡 เทอม $BC$ เป็น **consensus term** ที่ตัดออกได้เสมอ

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
$$= \overline{A}(B + \overline{B}C + BC)$$
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

### การใช้ Universal Gates ในการออกแบบ

ในทางปฏิบัติ นิยมแปลงวงจรให้ใช้ **NAND เท่านั้น** หรือ **NOR เท่านั้น** เพื่อ:
- ใช้ IC ชนิดเดียว → ลดต้นทุน
- ลดจำนวน IC บนบอร์ด

**ขั้นตอนแปลง SOP → NAND-NAND:**

1. เขียนสมการในรูป SOP: $F = AB + CD$
2. ใช้ Double Inversion: $F = \overline{\overline{AB + CD}}$
3. ใช้ De Morgan: $F = \overline{\overline{AB} \cdot \overline{CD}}$
4. แต่ละเทอมเป็น NAND → วงจร NAND 2 ระดับ

**ขั้นตอนแปลง POS → NOR-NOR:**

1. เขียนสมการในรูป POS: $F = (A+B)(C+D)$
2. ใช้ Double Inversion
3. ใช้ De Morgan → วงจร NOR 2 ระดับ

---

## 3.9 การพิสูจน์สมการบูลีน

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

คอลัมน์ $A$ กับ $A + AB$ เหมือนกันทุกแถว ✅

---

## 3.10 Duality Principle

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
