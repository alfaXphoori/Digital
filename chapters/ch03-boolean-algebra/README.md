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

---

## 3.3 กฎพื้นฐานและสัจพจน์ (Postulates & Basic Laws)

### กฎของ 0 และ 1 (Null & Identity)

| AND | OR | ชื่อกฎ |
|:---|:---|:---|
| $A \cdot 0 = 0$ | $A + 1 = 1$ | **Null Law** |
| $A \cdot 1 = A$ | $A + 0 = A$ | **Identity Law** |
| $A \cdot A = A$ | $A + A = A$ | **Idempotent Law** |
| $A \cdot \overline{A} = 0$ | $A + \overline{A} = 1$ | **Complement Law** |

### กฎการนิเสธสองชั้น (Double Negation)

$$\overline{\overline{A}} = A$$

---

## 3.4 กฎการจัดรูปสมการ (Algebraic Laws)

### Commutative Law (สลับที่)

$$A \cdot B = B \cdot A$$
$$A + B = B + A$$

### Associative Law (จัดหมู่)

$$(A \cdot B) \cdot C = A \cdot (B \cdot C)$$
$$(A + B) + C = A + (B + C)$$

### Distributive Law (แจกแจง)

$$A \cdot (B + C) = AB + AC$$
$$A + BC = (A + B)(A + C) \quad \text{⭐ สำคัญ!}$$

> ⚠️ กฎ $A + BC = (A + B)(A + C)$ ไม่มีในพีชคณิตปกติ แต่เป็นจริงในพีชคณิตบูลีน

### Absorption Law (ดูดซับ)

$$A + AB = A$$
$$A(A + B) = A$$
$$A + \overline{A}B = A + B \quad \text{(ขยาย)}$$
$$A(\overline{A} + B) = AB \quad \text{(ขยาย)}$$

### Consensus Theorem

$$AB + \overline{A}C + BC = AB + \overline{A}C$$
$$(A + B)(\overline{A} + C)(B + C) = (A + B)(\overline{A} + C)$$

---

## 3.5 ทฤษฎีบทเดอมอร์แกน (De Morgan's Theorem) ⭐

เป็นทฤษฎีที่สำคัญที่สุดในการแปลงวงจรและกลับค่าฟังก์ชัน

### Theorem 1: NOT ของ AND = OR ของ NOT

$$\overline{A \cdot B} = \overline{A} + \overline{B}$$

### Theorem 2: NOT ของ OR = AND ของ NOT

$$\overline{A + B} = \overline{A} \cdot \overline{B}$$

### วิธีการแปลงอย่างรวดเร็ว (Break the Bar):
1. แยกเส้นบาร์ (Break the bar)
2. เปลี่ยนเครื่องหมาย (AND ↔ OR)
3. กลับบิตตัวแปรแต่ละตัว (Complement individual variables)

---

## 3.6 รูปแบบมาตรฐาน (Canonical Forms)

ในการออกแบบวงจรดิจิทัล นิยมเขียนฟังก์ชันให้อยู่ในรูปแบบมาตรฐาน 2 แบบ:

### 1. Sum of Products (SOP) — ผลรวมของผลคูณ
คือการนำ **Minterms** (เทอมที่คูณกัน) มาบวกกัน ฟังก์ชันจะเป็น 1 เมื่อมี Minterm ใด Minterm หนึ่งเป็น 1
$$F = \sum m(1, 4, 7) = \overline{A}\,\overline{B}C + A\overline{B}\,\overline{C} + ABC$$

### 2. Product of Sums (POS) — ผลคูณของผลรวม
คือการนำ **Maxterms** (เทอมที่บวกกัน) มาคูณกัน ฟังก์ชันจะเป็น 0 เมื่อมี Maxterm ใด Maxterm หนึ่งเป็น 0
$$F = \prod M(0, 2, 3, 5, 6) = (A+B+C)(A+\overline{B}+C)(A+\overline{B}+\overline{C})\dots$$

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

---

## 3.9 Duality Principle (หลักการคู่กัน)

ถ้าสมการบูลีนเป็นจริง สมการที่เป็น **Dual** ของมันก็จะเป็นจริงเช่นกัน โดยการ:
1. สลับ **AND ↔ OR**
2. สลับ **0 ↔ 1**

*ตัวอย่าง:* $A + 1 = 1$ มี Dual คือ $A \cdot 0 = 0$

---

## 3.10 ปรากฏการณ์ Glitch และ Hazards

แม้สมการบูลีนจะถูกต้องในทางคณิตศาสตร์ แต่ในวงจรจริง เกตแต่ละตัวมี **Propagation Delay** ที่ไม่เท่ากัน ทำให้สัญญาณเดินทางถึงปลายทางไม่พร้อมกัน เกิดสถานะชั่วขณะที่ไม่พึงประสงค์เรียกว่า **Glitch**

**ประเภทของ Hazard:**
1. **Static 1-Hazard:** เอาต์พุตควรจะเป็น 1 นิ่งๆ แต่ดันตกลงไปที่ 0 แวบหนึ่ง
2. **Static 0-Hazard:** เอาต์พุตควรจะเป็น 0 นิ่งๆ แต่ดันกระโดดขึ้นไปที่ 1 แวบหนึ่ง
3. **Dynamic Hazard:** เอาต์พุตเปลี่ยนไปมาหลายครั้งก่อนจะนิ่ง (เกิดในวงจรที่มีโครงสร้างหลายระดับ)

**การป้องกัน Hazard:**
สามารถทำได้โดยการเพิ่ม "เทอมส่วนเกิน (Redundant term)" เข้าไปในสมการบูลีน (เช่นการบวก Consensus term กลับเข้าไป) เพื่ออุดรอยรั่วของการสลับสถานะ (ใช้ K-Map ครอบทับกลุ่มที่ติดกัน)

## 3.11 ทฤษฎีการกระจายของแชนนอน (Shannon's Expansion Theorem)

ฟังก์ชันบูลีนใดๆ สามารถกระจายรอบตัวแปรใดตัวแปรหนึ่ง (เช่น A) ได้ดังนี้:
$$ f(A, B, C, \dots) = A \cdot f(1, B, C, \dots) + \bar{A} \cdot f(0, B, C, \dots) $$
วิธีนี้มีประโยชน์มากในการออกแบบโครงสร้าง Multiplexer และระบบ FPGAs สมัยใหม่ที่ใช้ LUT (Look-Up Tables)

## แบบฝึกหัดท้ายบท

1. ลดรูป $F = AB + A(B+C) + B(B+C)$
2. ใช้ De Morgan แปลง $\overline{(A + \overline{B}) \cdot (C + \overline{D})}$
3. พิสูจน์ $A + \overline{A}B = A + B$ ด้วย Truth Table
4. เขียน $F = \sum m(1, 3, 5)$ ให้อยู่ในรูปสมการ (SOP)
5. สร้างวงจร NAND-only สำหรับฟังก์ชัน $F = AB + C$
6. ลดรูป $F = \overline{\overline{A} + \overline{B}} + \overline{A}B$
7. จงหา Complement ของ $F = AB + \overline{C}D$ โดยใช้ De Morgan
8. พิสูจน์ $A \oplus B = \overline{A \odot B}$
9. เขียน Truth Table ของฟังก์ชัน $F = (A+B)\overline{C}$
10. ลดรูป $F = AB + \overline{A}C + BC$ (Consensus Theorem)
