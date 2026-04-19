# 🔬 Lab 14: ROM as Combinational Logic — สร้าง Full Adder จาก ROM

## วัตถุประสงค์

- เข้าใจว่า ROM เก็บ Truth Table ทั้งหมดไว้
- ออกแบบ content ของ ROM สำหรับ Full Adder
- จำลองการทำงานของ ROM บน Tinkercad

---

## ส่วนที่ 1: ทบทวนแนวคิด (10 นาที)

### ROM = ตาราง Truth Table ที่เก็บไว้

```
Address (Input) ──→ [ROM] ──→ Data (Output)
   A, B, Cin              Sum, Cout
```

- **Address Bus** = ตัวแปร Input
- **Data** = ค่า Output ที่ต้องการ
- ROM ขนาด $2^n \times m$: n = จำนวน input, m = จำนวน output

### Full Adder ต้องการ ROM ขนาดเท่าไร?

- Input: A, B, Cin = **3 bits** → Address = 3 bits
- Output: Sum, Cout = **2 bits** → Data = 2 bits
- ROM ขนาด: $2^3 \times 2 = $ **8 × 2 bits**

---

## ส่วนที่ 2: เขียน Content ของ ROM (15 นาที)

### จงเติม Truth Table ของ Full Adder ลงใน ROM

| Address (A₂A₁A₀) | A | B | Cin | Sum | Cout | Data (D₁D₀) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 000 | 0 | 0 | 0 | | | |
| 001 | 0 | 0 | 1 | | | |
| 010 | 0 | 1 | 0 | | | |
| 011 | 0 | 1 | 1 | | | |
| 100 | 1 | 0 | 0 | | | |
| 101 | 1 | 0 | 1 | | | |
| 110 | 1 | 1 | 0 | | | |
| 111 | 1 | 1 | 1 | | | |

> D₁ = Cout, D₀ = Sum

---

## ส่วนที่ 3: จำลอง ROM ด้วย MUX บน Tinkercad (30 นาที)

> Tinkercad ไม่มี ROM IC โดยตรง แต่เราสามารถจำลองได้ด้วย **8:1 MUX** หรือต่อแบบ Decoder + OR

### วิธี A: ใช้ Logic Gate ต่อตาม Truth Table

เนื่องจาก ROM = Truth Table → เราสามารถต่อวงจรจาก **SOP (Sum of Products)** ของ Sum และ Cout

จาก Truth Table ข้างบน:

$$Sum = $$ (เขียนสมการ SOP)

$$Cout = $$ (เขียนสมการ SOP)

### ต่อวงจร

1. ต่อวงจร **Sum** จากสมการ SOP (ใช้ AND + OR + NOT)
2. ต่อวงจร **Cout** จากสมการ SOP
3. ทดสอบทุก Input (000 ถึง 111)

### วิธี B: ใช้ Arduino + Array (ตัวเลือก)

ถ้าต้องการจำลอง ROM จริงๆ ใช้ Arduino:

```cpp
// ROM content สำหรับ Full Adder
int rom[8][2] = {
  // {Cout, Sum}
  {0, 0},  // Address 000: 0+0+0
  {0, 1},  // Address 001: 0+0+1
  {0, 1},  // Address 010: 0+1+0
  {1, 0},  // Address 011: 0+1+1
  {0, 1},  // Address 100: 1+0+0
  {1, 0},  // Address 101: 1+0+1
  {1, 0},  // Address 110: 1+1+0
  {1, 1},  // Address 111: 1+1+1
};
```

---

## ส่วนที่ 4: ทดสอบ (10 นาที)

### เปรียบเทียบผลของวงจร ROM กับ Full Adder (Lab 6)

| A | B | Cin | Sum (ROM) | Cout (ROM) | ตรงกับ Full Adder? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | | | |
| 0 | 0 | 1 | | | |
| 0 | 1 | 0 | | | |
| 0 | 1 | 1 | | | |
| 1 | 0 | 0 | | | |
| 1 | 0 | 1 | | | |
| 1 | 1 | 0 | | | |
| 1 | 1 | 1 | | | |

📸 **Screenshot วงจร ROM-based Full Adder**

---

## ส่วนที่ 5: เปรียบเทียบ (5 นาที)

| เกณฑ์ | Full Adder แบบ Gate (Lab 6) | Full Adder แบบ ROM |
|:---|:---:|:---:|
| จำนวนเกตที่ใช้ | | |
| ต้องลดรูปสมการ? | ✅ ต้อง | |
| เพิ่มฟังก์ชันใหม่ง่าย? | | |
| ขนาดวงจร | | |

### คำถาม

1. ข้อดีของการใช้ ROM แทน Logic Gate คืออะไร?
2. ข้อเสียของ ROM คืออะไร? (คิดในกรณี Input หลายตัวแปร)
3. ถ้าต้องการสร้างฟังก์ชัน 8 ตัวแปร ต้องใช้ ROM ขนาดเท่าไร?

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่ายรูป Worksheet (ROM Content + สมการ SOP)
2. ถ่าย Screenshot วงจร ROM-based Full Adder จาก Tinkercad
3. เปิดวงจรใน Tinkercad → กด **Share** → **Copy Link**
4. เปิด Google Form → วาง Link → แนบรูป → กรอกคำตอบ → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] ถ่ายรูปตาราง ROM Content ที่เติมครบ
- [ ] สมการ SOP ของ Sum และ Cout
- [ ] Screenshot วงจรที่ต่อบน Tinkercad
- [ ] ตารางเปรียบเทียบผล
- [ ] ตอบคำถาม 3 ข้อ
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
