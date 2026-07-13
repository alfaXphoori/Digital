# Chapter 3: พีชคณิตบูลีน

## Boolean Algebra

---

<div class="chapter-tab-content" data-tab-name="Concept" data-tab-icon="💡" id="concept" markdown="1">

## 3.1 บทนำ

**พีชคณิตบูลีน (Boolean Algebra)** คือระบบคณิตศาสตร์ที่ใช้ในการวิเคราะห์และ **ลดรูป** วงจรตรรกะ โดยตัวแปรมีค่าได้เพียง `0` หรือ `1` เท่านั้น

แนวคิดนี้เป็นภาษากลางระหว่าง 3 สิ่ง:

| มุมมอง | ค่า `0` | ค่า `1` |
|:---|:---:|:---:|
| ตรรกศาสตร์ | False | True |
| วงจรดิจิทัล | LOW | HIGH |
| สวิตช์ | เปิดวงจร | ปิดวงจร |

> 💡 **ทำไมต้องลดรูป?** สมการที่สั้นลง = เกตน้อยลง = ต้นทุนต่ำลง + วงจรเร็วขึ้น

ตัวอย่างเช่น ถ้าได้สมการ

$$F = AB + A\overline{B}$$

สามารถลดรูปได้เป็น

$$F = A(B+\overline{B}) = A \cdot 1 = A$$

วงจรเดิมต้องใช้ NOT, AND 2 ตัว และ OR 1 ตัว แต่ผลลัพธ์จริงใช้เพียงสายสัญญาณ `A` ต่อออกไปได้เลย

---

## 3.2 ตัวดำเนินการพื้นฐาน (Basic Operations)

| ตัวดำเนินการ | สัญลักษณ์ | ความหมาย | เกตที่สอดคล้อง |
|:---:|:---:|:---:|:---:|
| AND | $A \cdot B$ หรือ $AB$ | คอนจังก์ชัน | AND gate |
| OR | $A + B$ | ดิสจังก์ชัน | OR gate |
| NOT | $\overline{A}$ หรือ $A'$ | คอมพลีเมนต์ | NOT gate |

**ลำดับความสำคัญ (Precedence):** NOT > AND > OR

$$\text{ตัวอย่าง: } A + B \cdot \overline{C} = A + (B \cdot (\overline{C}))$$

ถ้าไม่แน่ใจ ให้ใส่วงเล็บก่อนเสมอ เพราะสมการดิจิทัลมักถูกนำไปวาดเป็นวงจรจริง

### ตาราง Truth Table ของตัวดำเนินการพื้นฐาน

| A | B | $A \cdot B$ | $A + B$ | $\overline{A}$ |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 |

---

## 3.3 กฎพื้นฐานและสัจพจน์ (Postulates & Basic Laws)

กฎพื้นฐานเป็นเครื่องมือสำหรับแปลงสมการให้สั้นลงโดยไม่เปลี่ยนพฤติกรรมของฟังก์ชัน

### ตารางกฎหลักของพีชคณิตบูลีน

| กฎ | รูป AND | รูป OR | ตัวอย่างสั้นๆ |
|:---|:---|:---|:---|
| **Commutative** | $AB = BA$ | $A+B = B+A$ | $XY + Z = Z + XY$ |
| **Associative** | $(AB)C = A(BC)$ | $(A+B)+C = A+(B+C)$ | $(A+B)+D = A+B+D$ |
| **Distributive** | $A(B+C)=AB+AC$ | $A+BC=(A+B)(A+C)$ | $X(Y+Z)=XY+XZ$ |
| **Identity** | $A \cdot 1 = A$ | $A+0=A$ | $BC+0=BC$ |
| **Null** | $A \cdot 0 = 0$ | $A+1=1$ | $A\overline{B}\cdot0=0$ |
| **Idempotent** | $AA=A$ | $A+A=A$ | $AB+AB=AB$ |
| **Complement** | $A\overline{A}=0$ | $A+\overline{A}=1$ | $X+\overline{X}=1$ |
| **Involution** | - | $\overline{\overline{A}}=A$ | $\overline{\overline{BC}}=BC$ |
| **Absorption** | $A(A+B)=A$ | $A+AB=A$ | $X+XY=X$ |
| **Consensus** | - | $AB+\overline{A}C+BC=AB+\overline{A}C$ | $XY+\overline{X}Z+YZ=XY+\overline{X}Z$ |

### กฎของ 0 และ 1 (Null & Identity)

| AND | OR | ชื่อกฎ |
|:---|:---|:---|
| $A \cdot 0 = 0$ | $A + 1 = 1$ | **Null Law** |
| $A \cdot 1 = A$ | $A + 0 = A$ | **Identity Law** |
| $A \cdot A = A$ | $A + A = A$ | **Idempotent Law** |
| $A \cdot \overline{A} = 0$ | $A + \overline{A} = 1$ | **Complement Law** |

ตัวอย่างการใช้:

$$F = A(B+0) + C \cdot 0$$

$$F = AB + 0 \quad \text{(Identity และ Null)}$$

$$F = AB$$

### กฎการนิเสธสองชั้น (Double Negation / Involution)

$$\overline{\overline{A}} = A$$

ตัวอย่าง:

$$F = \overline{\overline{A+B}}$$

$$F = A+B$$

### Complement ของค่าคงที่

$$\overline{0}=1$$

$$\overline{1}=0$$

ใช้บ่อยเมื่อแทนค่าในตารางความจริงหรือกระจายตามทฤษฎีของแชนนอน

---

## 3.4 กฎการจัดรูปสมการ (Algebraic Laws)

หัวข้อนี้เน้นการใช้กฎเพื่อจัดรูปสมการ ไม่ใช่แค่ท่องสูตร เป้าหมายคือเปลี่ยนสมการให้สั้นลงหรือให้อยู่ในรูปที่เหมาะกับวงจร

### Commutative Law (สลับที่)

$$A \cdot B = B \cdot A$$

$$A + B = B + A$$

ตัวอย่าง:

$$F = BA + C$$

$$F = AB + C$$

ใช้เพื่อจัดเทอมให้เห็นรูปซ้ำหรือรูปที่ดูดซับกันได้ง่ายขึ้น

### Associative Law (จัดหมู่)

$$(A \cdot B) \cdot C = A \cdot (B \cdot C)$$

$$(A + B) + C = A + (B + C)$$

ตัวอย่าง:

$$F = (A+B)+(C+D)$$

$$F = A+B+C+D$$

ในพีชคณิตบูลีน ถ้าเป็นตัวดำเนินการชนิดเดียวกันทั้งหมด สามารถละวงเล็บได้

### Distributive Law (แจกแจง)

$$A \cdot (B + C) = AB + AC$$

$$A + BC = (A + B)(A + C) \quad \text{⭐ สำคัญ!}$$

> ⚠️ กฎ $A + BC = (A + B)(A + C)$ ไม่มีในพีชคณิตปกติ แต่เป็นจริงในพีชคณิตบูลีน

ตัวอย่างแบบ SOP:

$$F = A(B+\overline{C})$$

$$F = AB + A\overline{C}$$

ตัวอย่างแบบ POS:

$$F = A + BC$$

$$F = (A+B)(A+C)$$

### Identity, Null, Idempotent, Complement

ตัวอย่างรวม:

$$F = A + A + B\cdot1 + C\cdot0$$

$$F = A + B + 0 \quad \text{(Idempotent, Identity, Null)}$$

$$F = A + B$$

ตัวอย่าง Complement:

$$F = AB + A\overline{A}C$$

$$F = AB + 0\cdot C \quad \text{(Complement)}$$

$$F = AB$$

### Absorption Law (ดูดซับ)

$$A + AB = A$$

$$A(A + B) = A$$

$$A + \overline{A}B = A + B \quad \text{(ขยาย)}$$

$$A(\overline{A} + B) = AB \quad \text{(ขยาย)}$$

ตัวอย่างที่ 1:

$$F = X + XY$$

$$F = X \quad \text{(Absorption)}$$

ตัวอย่างที่ 2:

$$F = A + \overline{A}B$$

$$F = (A+\overline{A})(A+B) \quad \text{(Distributive)}$$

$$F = 1(A+B) \quad \text{(Complement)}$$

$$F = A+B \quad \text{(Identity)}$$

### Consensus Theorem

รูป SOP:

$$AB + \overline{A}C + BC = AB + \overline{A}C$$

รูป POS ซึ่งเป็น Dual:

$$(A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$$

เทอม $BC$ เรียกว่า **Consensus term** เพราะถูกครอบคลุมโดยสองเทอมแรกอยู่แล้ว

ตัวอย่าง:

$$F = XY + \overline{X}Z + YZ$$

$$F = XY + \overline{X}Z \quad \text{(Consensus)}$$

### Worked Examples: การลดรูปแบบ Step-by-Step

#### ตัวอย่างที่ 1: SOP แบบดึงตัวร่วม

ลดรูป:

$$F = AB + A\overline{B}$$

ขั้นตอน:

$$F = A(B+\overline{B}) \quad \text{(Distributive)}$$

$$F = A \cdot 1 \quad \text{(Complement)}$$

$$F = A \quad \text{(Identity)}$$

#### ตัวอย่างที่ 2: SOP แบบ Absorption

ลดรูป:

$$F = A + AB + \overline{A}C$$

ขั้นตอน:

$$F = A + \overline{A}C \quad \text{(Absorption: } A+AB=A\text{)}$$

$$F = A + C \quad \text{(Absorption แบบขยาย: } A+\overline{A}C=A+C\text{)}$$

#### ตัวอย่างที่ 3: SOP แบบ Consensus

ลดรูป:

$$F = AB + \overline{A}C + BC$$

ขั้นตอน:

$$F = AB + \overline{A}C + BC(A+\overline{A}) \quad \text{(Identity และ Complement)}$$

$$F = AB + \overline{A}C + ABC + \overline{A}BC \quad \text{(Distributive)}$$

$$F = AB(1+C) + \overline{A}C(1+B) \quad \text{(ดึงตัวร่วม)}$$

$$F = AB + \overline{A}C \quad \text{(Null/Identity)}$$

จึงตรงกับ Consensus Theorem

#### ตัวอย่างที่ 4: POS แบบดูดซับ

ลดรูป:

$$F = (A+B)(A+\overline{B})$$

ขั้นตอน:

$$F = A + B\overline{B} \quad \text{(รูปกลับของ Distributive: } (A+B)(A+C)=A+BC\text{)}$$

$$F = A + 0 \quad \text{(Complement)}$$

$$F = A \quad \text{(Identity)}$$

#### ตัวอย่างที่ 5: POS แบบ Consensus

ลดรูป:

$$F = (A+B)(\overline{A}+C)(B+C)$$

ขั้นตอน:

$$F = (A+B)(\overline{A}+C) \quad \text{(Consensus รูป POS)}$$

ถ้าต้องการตรวจเพิ่ม:

$$F = (A+B)(\overline{A}+C)$$

$$F = A\overline{A}+AC+\overline{A}B+BC \quad \text{(Distributive)}$$

$$F = AC+\overline{A}B+BC$$

$$F = AC+\overline{A}B \quad \text{(Consensus รูป SOP โดยให้ } A \leftrightarrow \overline{A}\text{)}$$

---

## 3.5 ทฤษฎีบทเดอมอร์แกน (De Morgan's Theorem) ⭐

เป็นทฤษฎีที่สำคัญที่สุดในการแปลงวงจรและกลับค่าฟังก์ชัน

### Theorem 1: NOT ของ AND = OR ของ NOT

$$\overline{A \cdot B} = \overline{A} + \overline{B}$$

### Theorem 2: NOT ของ OR = AND ของ NOT

$$\overline{A + B} = \overline{A} \cdot \overline{B}$$

### De Morgan สำหรับ 3 ตัวแปร

$$\overline{ABC} = \overline{A}+\overline{B}+\overline{C}$$

$$\overline{A+B+C} = \overline{A}\,\overline{B}\,\overline{C}$$

หลักทั่วไปคือ เมื่อเส้นบาร์ครอบทั้งกลุ่ม ให้เปลี่ยน AND เป็น OR หรือ OR เป็น AND แล้วกลับค่าทุกตัวแปรภายในกลุ่ม

### วิธีการแปลงอย่างรวดเร็ว (Break the Bar)

1. แยกเส้นบาร์ (Break the bar)
2. เปลี่ยนเครื่องหมาย (AND ↔ OR)
3. กลับบิตตัวแปรแต่ละตัว (Complement individual variables)

### Worked Example 1: กระจาย De Morgan 2 ตัวแปร

แปลง:

$$F = \overline{A+\overline{B}}$$

ขั้นตอน:

$$F = \overline{A}\cdot\overline{\overline{B}} \quad \text{(De Morgan)}$$

$$F = \overline{A}B \quad \text{(Involution)}$$

### Worked Example 2: กระจาย De Morgan 3 ตัวแปร

แปลง:

$$F = \overline{A\overline{B}C}$$

ขั้นตอน:

$$F = \overline{A} + \overline{\overline{B}} + \overline{C} \quad \text{(De Morgan)}$$

$$F = \overline{A} + B + \overline{C} \quad \text{(Involution)}$$

### Worked Example 3: กระจายหลายชั้น

แปลง:

$$F = \overline{(A+\overline{B})(C+D)}$$

ขั้นตอน:

$$F = \overline{(A+\overline{B})} + \overline{(C+D)} \quad \text{(De Morgan ชั้นนอก)}$$

$$F = (\overline{A}B) + (\overline{C}\,\overline{D}) \quad \text{(De Morgan ชั้นใน)}$$

$$F = \overline{A}B + \overline{C}\,\overline{D}$$

### ความสัมพันธ์กับ NAND/NOR

De Morgan อธิบายว่าทำไม NAND และ NOR จึงใช้สร้างวงจรได้ครบทุกชนิด:

$$\overline{AB} = \overline{A}+\overline{B} \quad \text{(NAND ทำหน้าที่เหมือน OR ของอินพุตกลับค่า)}$$

$$\overline{A+B} = \overline{A}\,\overline{B} \quad \text{(NOR ทำหน้าที่เหมือน AND ของอินพุตกลับค่า)}$$

---

## 3.6 รูปแบบมาตรฐาน (Canonical Forms)

ในการออกแบบวงจรดิจิทัล นิยมเขียนฟังก์ชันให้อยู่ในรูปแบบมาตรฐาน 2 แบบ:

### 1. Sum of Products (SOP) — ผลรวมของผลคูณ

คือการนำ **Minterms** (เทอมที่คูณกัน) มาบวกกัน ฟังก์ชันจะเป็น 1 เมื่อมี Minterm ใด Minterm หนึ่งเป็น 1

$$F = \sum m(1, 4, 7) = \overline{A}\,\overline{B}C + A\overline{B}\,\overline{C} + ABC$$

### 2. Product of Sums (POS) — ผลคูณของผลรวม

คือการนำ **Maxterms** (เทอมที่บวกกัน) มาคูณกัน ฟังก์ชันจะเป็น 0 เมื่อมี Maxterm ใด Maxterm หนึ่งเป็น 0

$$F = \prod M(0, 2, 3, 5, 6) = (A+B+C)(A+\overline{B}+C)(A+\overline{B}+\overline{C})\dots$$

### Minterm และ Maxterm จากตารางความจริง

สำหรับตัวแปร $A,B,C$ ให้เรียงแถวตามเลขฐานสอง $ABC$

| index | A | B | C | Minterm | Maxterm |
|:---:|:---:|:---:|:---:|:---|:---|
| 0 | 0 | 0 | 0 | $\overline{A}\,\overline{B}\,\overline{C}$ | $(A+B+C)$ |
| 1 | 0 | 0 | 1 | $\overline{A}\,\overline{B}C$ | $(A+B+\overline{C})$ |
| 2 | 0 | 1 | 0 | $\overline{A}B\overline{C}$ | $(A+\overline{B}+C)$ |
| 3 | 0 | 1 | 1 | $\overline{A}BC$ | $(A+\overline{B}+\overline{C})$ |
| 4 | 1 | 0 | 0 | $A\overline{B}\,\overline{C}$ | $(\overline{A}+B+C)$ |
| 5 | 1 | 0 | 1 | $A\overline{B}C$ | $(\overline{A}+B+\overline{C})$ |
| 6 | 1 | 1 | 0 | $AB\overline{C}$ | $(\overline{A}+\overline{B}+C)$ |
| 7 | 1 | 1 | 1 | $ABC$ | $(\overline{A}+\overline{B}+\overline{C})$ |

กฎจำง่าย:

- **Minterm:** แถวที่ต้องการให้ฟังก์ชันเป็น `1`
- **Maxterm:** แถวที่ต้องการให้ฟังก์ชันเป็น `0`
- ใน Minterm ค่า `0` เขียนเป็นตัวแปรกลับค่า เช่น $A=0 \Rightarrow \overline{A}$
- ใน Maxterm ค่า `0` เขียนเป็นตัวแปรไม่กลับค่า เช่น $A=0 \Rightarrow A$

### ตัวอย่างจาก Truth Table

กำหนดตารางความจริง:

| A | B | C | F |
|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 1 |
| 1 | 1 | 0 | 1 |
| 1 | 1 | 1 | 0 |

แถวที่ $F=1$ คือ index 1, 3, 5, 6

$$F = \sum m(1,3,5,6)$$

เขียนเป็น SOP:

$$F = \overline{A}\,\overline{B}C + \overline{A}BC + A\overline{B}C + AB\overline{C}$$

แถวที่ $F=0$ คือ index 0, 2, 4, 7

$$F = \prod M(0,2,4,7)$$

เขียนเป็น POS:

$$F = (A+B+C)(A+\overline{B}+C)(\overline{A}+B+C)(\overline{A}+\overline{B}+\overline{C})$$

### การแปลงระหว่าง SOP และ POS

ถ้ารู้เซตของ minterm ที่ทำให้ฟังก์ชันเป็น `1` แล้ว POS จะใช้ index ที่เหลือซึ่งทำให้ฟังก์ชันเป็น `0`

ตัวอย่าง:

$$F(A,B,C)=\sum m(1,3,5,6)$$

มี index ทั้งหมด $0$ ถึง $7$ ดังนั้น index ที่เหลือคือ $0,2,4,7$

$$F(A,B,C)=\prod M(0,2,4,7)$$

ในทางกลับกัน:

$$F(A,B,C)=\prod M(0,2,4,7)$$

จึงเท่ากับ:

$$F(A,B,C)=\sum m(1,3,5,6)$$

### ความสัมพันธ์กับ Complement

ถ้า

$$F = \sum m(1,3,5,6)$$

แล้วฟังก์ชันกลับค่าเป็น:

$$\overline{F} = \sum m(0,2,4,7)$$

และเขียนอีกแบบได้ว่า:

$$F = \prod M(0,2,4,7)$$

ดังนั้น SOP/POS เป็นคนละมุมมองของตารางความจริงเดียวกัน

```text
Truth Table
  F = 1 rows  -> SOP -> sum of minterms
  F = 0 rows  -> POS -> product of maxterms
```

---

## 3.7 การออกแบบและแปลงวงจร

### วงจร → สมการ

อ่านจากอินพุตไปหาเอาต์พุต เขียนกำกับแต่ละเกต

### สมการ → วงจร

วาดตามลำดับความสำคัญ (NOT → AND → OR)

### การใช้ Universal Gates (NAND/NOR)

ในทางปฏิบัติ นิยมใช้เกตชนิดเดียวเพื่อลดจำนวน IC:

- **SOP** เหมาะกับวงจร **NAND-NAND**
- **POS** เหมาะกับวงจร **NOR-NOR**

ตัวอย่าง SOP: $F=AB+CD=\overline{\overline{AB}\cdot\overline{CD}}$ จึงใช้ NAND ชั้นแรกสร้าง $\overline{AB}$, $\overline{CD}$ แล้วใช้ NAND ชั้นที่สองรวมผล

---

## 3.8 คุณสมบัติของ XOR และ XNOR

$$A \oplus B = A\overline{B} + \overline{A}B$$

$$A \odot B = AB + \overline{A}\,\overline{B}$$

| คุณสมบัติ | XOR ($\oplus$) | XNOR ($\odot$) |
|:---|:---|:---|
| กับ 0 | $A \oplus 0 = A$ | $A \odot 0 = \overline{A}$ |
| กับ 1 | $A \oplus 1 = \overline{A}$ | $A \odot 1 = A$ |
| กับ ตัวเอง | $A \oplus A = 0$ | $A \odot A = 1$ |
| กับ Complement | $A \oplus \overline{A} = 1$ | $A \odot \overline{A} = 0$ |

XOR ให้ `1` เมื่ออินพุต **ต่างกัน** ส่วน XNOR ให้ `1` เมื่ออินพุต **เหมือนกัน** ใช้บ่อยในวงจรบวกเลขและ parity

---

## 3.9 Duality Principle (หลักการคู่กัน)

ถ้าสมการบูลีนเป็นจริง สมการที่เป็น **Dual** ของมันก็จะเป็นจริงเช่นกัน โดยการ:

1. สลับ **AND ↔ OR**
2. สลับ **0 ↔ 1**

*ตัวอย่าง:* $A + 1 = 1$ มี Dual คือ $A \cdot 0 = 0$ และ $A+AB=A$ มี Dual คือ $A(A+B)=A$

---

## 3.10 ปรากฏการณ์ Glitch และ Hazards

แม้สมการบูลีนจะถูกต้องในทางคณิตศาสตร์ แต่ในวงจรจริง เกตแต่ละตัวมี **Propagation Delay** ที่ไม่เท่ากัน ทำให้สัญญาณเดินทางถึงปลายทางไม่พร้อมกัน เกิดสถานะชั่วขณะที่ไม่พึงประสงค์เรียกว่า **Glitch**

**ประเภทของ Hazard:**

1. **Static 1-Hazard:** เอาต์พุตควรจะเป็น 1 นิ่งๆ แต่ดันตกลงไปที่ 0 แวบหนึ่ง
2. **Static 0-Hazard:** เอาต์พุตควรจะเป็น 0 นิ่งๆ แต่ดันกระโดดขึ้นไปที่ 1 แวบหนึ่ง
3. **Dynamic Hazard:** เอาต์พุตเปลี่ยนไปมาหลายครั้งก่อนจะนิ่ง (เกิดในวงจรที่มีโครงสร้างหลายระดับ)

**การป้องกัน Hazard:**

สามารถทำได้โดยการเพิ่ม "เทอมส่วนเกิน (Redundant term)" เข้าไปในสมการบูลีน (เช่นการบวก Consensus term กลับเข้าไป) เพื่ออุดรอยรั่วของการสลับสถานะ (ใช้ K-Map ครอบทับกลุ่มที่ติดกัน)

ตัวอย่าง:

$$F = AB + \overline{A}C$$

ถ้า $B=1$ และ $C=1$ ฟังก์ชันควรเป็น `1` ไม่ว่า $A$ จะเปลี่ยนจาก `0` เป็น `1` หรือกลับกัน แต่ในวงจรจริงอาจเกิด static 1-hazard ได้ จึงเพิ่ม consensus term:

$$F_{\text{safe}} = AB + \overline{A}C + BC$$

ในเชิงพีชคณิต $BC$ เป็นเทอมส่วนเกิน เพราะลดออกได้ด้วย Consensus Theorem แต่ในวงจรจริงอาจช่วยให้สัญญาณไม่ตกชั่วคราว

**🔬 จำลอง Static-1 Hazard แบบ Timing Diagram (Interactive):**

กำหนด $B = C = 1$ คงที่ แล้วให้ $A$ สลับจาก `1 → 0` ตามทฤษฎี $F = AB + \overline{A}C$ ควรเป็น `1` ตลอด แต่เทอม $\overline{A}C$ ต้องผ่านเกต NOT จึงมาช้ากว่าเทอม $AB$ ที่กำลังดับ ทำให้มี **ช่วงสั้น ๆ ที่ทั้งสองเทอมเป็น `0` พร้อมกัน** → เอาต์พุตตก `0` แวบหนึ่ง (กด ▶ แล้วดู playhead วิ่งผ่านช่องที่ `F` ตก):

{% include timing-diagram.html preset="custom" signals="A:11110000,B:11111111,C:11111111,F:11110111" id="ch3-hazard-bad" %}

เมื่อเพิ่ม **consensus term `+ BC`** เข้าไป ($F_{\text{safe}} = AB + \overline{A}C + BC$) เทอม $BC$ จะ "ค้าง" เอาต์พุตไว้ที่ `1` ตลอดช่วงที่ $A$ กำลังสลับ (เพราะ $B=C=1$ ทำให้ $BC=1$ ไม่ขึ้นกับ $A$) — glitch จึงหายไป สัญญาณราบเรียบ:

{% include timing-diagram.html preset="custom" signals="A:11110000,B:11111111,C:11111111,F+BC:11111111" id="ch3-hazard-fixed" %}

> 💡 เทียบสองไดอะแกรม: ช่องที่ `F` ตกในอันแรกคือ glitch ที่ตำราพูดถึง ส่วนอันที่สองคือผลของการอุดด้วยเทอมส่วนเกิน — ในวงจรจริง glitch นี้สั้นระดับนาโนวินาที แต่อาจทำให้วงจรลำดับ (เช่น สัญญาณที่ป้อนเข้า clock/latch) ทำงานผิดพลาดได้

---


## Cheat Sheet: สรุปทฤษฎีบทที่ใช้บ่อย

| กลุ่ม | สูตร |
|:---|:---|
| Identity | $A+0=A$, $A\cdot1=A$ |
| Null | $A+1=1$, $A\cdot0=0$ |
| Idempotent | $A+A=A$, $AA=A$ |
| Complement | $A+\overline{A}=1$, $A\overline{A}=0$ |
| Involution | $\overline{\overline{A}}=A$ |
| Commutative | $A+B=B+A$, $AB=BA$ |
| Associative | $(A+B)+C=A+(B+C)$, $(AB)C=A(BC)$ |
| Distributive | $A(B+C)=AB+AC$, $A+BC=(A+B)(A+C)$ |
| Absorption | $A+AB=A$, $A(A+B)=A$ |
| Absorption ขยาย | $A+\overline{A}B=A+B$, $A(\overline{A}+B)=AB$ |
| De Morgan | $\overline{AB}=\overline{A}+\overline{B}$, $\overline{A+B}=\overline{A}\overline{B}$ |
| Consensus | $AB+\overline{A}C+BC=AB+\overline{A}C$ |
| Consensus Dual | $(A+B)(\overline{A}+C)(B+C)=(A+B)(\overline{A}+C)$ |

---

## ข้อผิดพลาดที่พบบ่อย (Common Mistakes)

1. **ลืมลำดับความสำคัญของตัวดำเนินการ**

   $$A+B C \neq (A+B)C$$

   ที่ถูกคือ $A+BC = A+(BC)$

2. **ใช้ De Morgan แต่ไม่เปลี่ยน AND/OR**

   ผิด:

   $$\overline{A+B} = \overline{A}+\overline{B}$$

   ถูก:

   $$\overline{A+B} = \overline{A}\,\overline{B}$$

3. **กลับค่าเฉพาะตัวแปร แต่ลืมเส้นบาร์ทั้งกลุ่ม**

   $$\overline{A\overline{B}+C}$$

   ต้องแยกเป็น:

   $$\overline{A\overline{B}}\cdot\overline{C}$$

4. **สับสน Minterm กับ Maxterm**

   Minterm ใช้กับแถวที่ $F=1$ ส่วน Maxterm ใช้กับแถวที่ $F=0$

5. **เขียน Maxterm กลับเครื่องหมายผิด**

   สำหรับแถว $A=0,B=1,C=0$:

   $$M_2 = (A+\overline{B}+C)$$

   ไม่ใช่ $(\overline{A}+B+\overline{C})$

6. **คิดว่าเทอมซ้ำทำให้ค่าเพิ่มขึ้น**

   ในบูลีน:

   $$A+A=A$$

   ไม่ใช่ $2A$

7. **ลดรูปจนถูกทางคณิตศาสตร์ แต่ลืมผลต่อ hazard**

   เทอม consensus อาจถูกลดออกได้ทางพีชคณิต แต่บางครั้งวงจรจริงต้องใส่กลับเพื่อป้องกัน glitch

---

## 📝 แบบทดสอบความรู้สั้นๆ (Quick Quiz)

ลองทดสอบความเข้าใจของตัวคุณเองด้วยคำถามสั้นๆ เหล่านี้ (คลิกเพื่อเลือกคำตอบและตรวจคะแนนได้ทันที):

<div class="quiz-container" style="margin-bottom: 25px; padding: 20px; border: 1px solid var(--line); border-radius: var(--radius); background: #ffffff; box-shadow: var(--shadow-sm);">
  
  <div class="quiz-item" style="margin-bottom: 20px;">
    <p style="margin-bottom: 10px; font-weight: 600;"><strong>ข้อที่ 1:</strong> สมการบูลีน $A + \overline{A}B$ สามารถลดรูปได้เป็นข้อใด?</p>
    <label style="display: flex; align-items: center; margin-bottom: 8px; cursor: pointer;"><input type="radio" name="q1" value="A" style="margin-right: 8px;"> A</label>
    <label style="display: flex; align-items: center; margin-bottom: 8px; cursor: pointer;"><input type="radio" name="q1" value="B" style="margin-right: 8px;"> B</label>
    <label style="display: flex; align-items: center; margin-bottom: 8px; cursor: pointer;"><input type="radio" name="q1" value="A+B" style="margin-right: 8px;"> $A + B$</label>
    <label style="display: flex; align-items: center; margin-bottom: 8px; cursor: pointer;"><input type="radio" name="q1" value="AB" style="margin-right: 8px;"> $AB$</label>
  </div>

  <hr style="border: 0; border-top: 1px solid var(--line); margin: 20px 0;">

  <div class="quiz-item" style="margin-bottom: 20px;">
    <p style="margin-bottom: 10px; font-weight: 600;"><strong>ข้อที่ 2:</strong> Complement ของฟังก์ชัน $Y = AB$ (ตามกฎของเดอมอร์แกน) คือข้อใด?</p>
    <label style="display: flex; align-items: center; margin-bottom: 8px; cursor: pointer;"><input type="radio" name="q2" value="A+B" style="margin-right: 8px;"> $\overline{A} + \overline{B}$</label>
    <label style="display: flex; align-items: center; margin-bottom: 8px; cursor: pointer;"><input type="radio" name="q2" value="AB" style="margin-right: 8px;"> $\overline{A}\cdot\overline{B}$</label>
    <label style="display: flex; align-items: center; margin-bottom: 8px; cursor: pointer;"><input type="radio" name="q2" value="A'+B'" style="margin-right: 8px;"> $\overline{A+B}$</label>
  </div>

  <button class="btn btn--light" onclick="checkAnswers()" style="margin-top: 10px; font-size: 0.95rem; background: var(--indigo); color: white;">ตรวจคำตอบ</button>
  <div id="quiz-result" style="margin-top: 15px; font-weight: 600; font-size: 1rem;"></div>
</div>

<script>
function checkAnswers() {
  var score = 0;
  var q1 = document.querySelector('input[name="q1"]:checked');
  var q2 = document.querySelector('input[name="q2"]:checked');
  
  if (!q1 || !q2) {
    document.getElementById('quiz-result').innerHTML = '<span style="color: #d97706;">⚠️ กรุณาตอบคำถามให้ครบทุกข้อ</span>';
    return;
  }
  
  if (q1.value === 'A+B') score++;
  if (q2.value === 'A+B') score++;
  
  var resultText = '';
  if (score === 2) {
    resultText = '<span style="color: #10b981;">🎉 ถูกต้องทั้งหมด! คุณได้คะแนน 2/2 ยอดเยี่ยมมากครับ</span>';
  } else {
    resultText = '<span style="color: #ef4444;">❌ คุณได้คะแนน ' + score + '/2 คะแนน ลองทบทวนข้อผิดพลาดและเลือกตรวจคำตอบอีกครั้งนะ</span>';
  }
  document.getElementById('quiz-result').innerHTML = resultText;
}
</script>
</div>

<div class="chapter-tab-content" data-tab-name="Interactive Sim" data-tab-icon="🎮" id="sim" markdown="1">

## Interactive Simulators (ตัวจำลองพีชคณิตบูลีน)

เครื่องมือจำลองเหล่านี้ออกแบบมาเพื่อช่วยสร้างความเข้าใจผ่านการโต้ตอบและลงมือเล่น (Simulate-First)

### 1. เครื่องมือลดรูปสมการบูลีน (Boolean Simplifier Explorer)
คลิกที่ปุ่มตัวอย่างฟังก์ชันตรรกะ เพื่อดูผลการลดรูปทีละขั้นตอนพร้อมคำอธิบายทฤษฎีและกฎทางคณิตศาสตร์ของบูลีนที่นำมาประยุกต์ใช้ในแต่ละสเต็ป:

{% include boolean-simplifier.html %}

</div>

<div class="chapter-tab-content" data-tab-name="Waveform / Truth Table" data-tab-icon="📊" id="waveform" markdown="1">

## Reference Tables (แผ่นสรุปทฤษฎีบูลีนและลอจิกคู่ขนาน)

สรุปกฎสำคัญของพีชคณิตบูลีน (Boolean Laws) ทั้งหมดที่ต้องจดจำไปใช้ในการออกแบบวงจรลอจิก:

### 1. กฎพื้นฐาน (Boolean Rules)
- **Identity:** $A \cdot 1 = A$ และ $A + 0 = A$
- **Null / Domination:** $A \cdot 0 = 0$ และ $A + 1 = 1$
- **Idempotent:** $A \cdot A = A$ และ $A + A = A$
- **Inverse / Complement:** $A \cdot \overline{A} = 0$ และ $A + \overline{A} = 1$
- **Double Negation:** $\overline{\overline{A}} = A$

### 2. กฎการจัดรูป (Algebraic Laws)
- **Commutative (สลับที่):** $A + B = B + A$ และ $A \cdot B = B \cdot A$
- **Associative (เปลี่ยนกลุ่ม):** $(A+B)+C = A+(B+C)$ และ $(A\cdot B)\cdot C = A\cdot (B\cdot C)$
- **Distributive (แจกแจง):** $A(B+C) = AB + AC$ และ $A + BC = (A+B)(A+C)$
- **De Morgan's Theorem:** $\overline{A \cdot B} = \overline{A} + \overline{B}$ และ $\overline{A + B} = \overline{A} \cdot \overline{B}$
- **Absorption (ดูดซึม):** $A + AB = A$ และ $A(A+B) = A$

</div>

<div class="chapter-tab-content" data-tab-name="Challenge" data-tab-icon="🏆" id="challenge" markdown="1">

## แบบฝึกหัดท้ายบท

1. ลดรูป $F = AB + A(B+C) + B(B+C)$
2. ใช้ De Morgan แปลง $\overline{(A + \overline{B}) \cdot (C + \overline{D})}$
3. พิสูจน์ $A + \overline{A}B = A + B$ ด้วย Truth Table
4. เขียน $F = \sum m(1, 3, 5)$ ให้อยู่ในรูปสมการ SOP สำหรับตัวแปร $A,B,C$
5. สร้างวงจร NAND-only สำหรับฟังก์ชัน $F = AB + C$
6. ลดรูป $F = \overline{\overline{A} + \overline{B}} + \overline{A}B$
7. จงหา Complement ของ $F = AB + \overline{C}D$ โดยใช้ De Morgan
8. พิสูจน์ $A \oplus B = \overline{A \odot B}$
9. เขียน Truth Table ของฟังก์ชัน $F = (A+B)\overline{C}$
10. ลดรูป $F = AB + \overline{A}C + BC$ (Consensus Theorem)

### เฉลยแนวคิด

1. กระจายก่อน: $A(B+C)=AB+AC$ และ $B(B+C)=B$ จากนั้นใช้ Absorption จะได้ $F=B+AC$
2. ใช้ De Morgan ชั้นนอกก่อน ได้ $\overline{A+\overline{B}}+\overline{C+\overline{D}}$ แล้วลดเป็น $\overline{A}B+\overline{C}D$
3. ทำตาราง 4 แถวของ $A,B$ แล้วเทียบคอลัมน์ $A+\overline{A}B$ กับ $A+B$
4. $m_1=\overline{A}\overline{B}C$, $m_3=\overline{A}BC$, $m_5=A\overline{B}C$
5. เขียน $F=\overline{\overline{AB}\cdot\overline{C}}$ โดยสร้าง $\overline{C}$ จาก NAND ที่ผูกอินพุตเข้าด้วยกัน
6. ใช้ De Morgan กับเทอมแรก ได้ $AB+\overline{A}B$ แล้วดึง $B$ เป็น $B(A+\overline{A})=B$
7. $\overline{F}=\overline{AB+\overline{C}D}=(\overline{A}+\overline{B})(C+\overline{D})$
8. เขียน $A\odot B=AB+\overline{A}\overline{B}$ แล้ว complement ทั้งสมการ จะได้ $A\overline{B}+\overline{A}B$
9. $F=1$ เฉพาะเมื่อ $C=0$ และอย่างน้อยหนึ่งตัวใน $A,B$ เป็น `1`
10. เทอม $BC$ เป็น consensus term จึงลดได้เป็น $F=AB+\overline{A}C$

</div>
