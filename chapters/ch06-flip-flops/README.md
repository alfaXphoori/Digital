# Chapter 6: ฟลิปฟลอปและวงจรเชิงลำดับ

## Flip-Flops & Sequential Logic

---

## 6.1 บทนำ: Combinational vs Sequential

| เกณฑ์ | Combinational | Sequential |
|:---|:---:|:---:|
| หน่วยความจำ | ❌ ไม่มี | ✅ มี |
| เอาต์พุตขึ้นกับ | อินพุตปัจจุบัน | อินพุต + สถานะก่อนหน้า |
| ตัวอย่าง | Adder, MUX, Decoder | Counter, Register, FSM |

$$\text{Sequential Output} = f(\text{Inputs}, \text{Present State})$$

```
                ┌──────────────────┐
 Inputs ───────→│  Combinational   │───────→ Outputs
                │     Logic        │
         ┌─────→│                  │──────┐
         │      └──────────────────┘      │
         │      ┌──────────────────┐      │
         └──────│  Memory          │←─────┘
                │  (Flip-Flops)    │
                └───────┬──────────┘
                        ↑
                      Clock
```

---

## 6.2 วงจรแลตช์ (Latches) — หน่วยความจำพื้นฐาน

### SR Latch (NOR-based)

| S | R | Q | Q̄ | สถานะ |
|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | Q₀ | Q̄₀ | **Hold** (ค้างค่าเดิม) |
| 0 | 1 | 0 | 1 | **Reset** |
| 1 | 0 | 1 | 0 | **Set** |
| 1 | 1 | ? | ? | ❌ **Invalid** (ห้ามใช้!) |

```
 S ──[NOR]──┬── Q
      ↑     │
      └─────┼──────┐
            │      ↓
 R ──[NOR]──┴── Q̄
```

### SR Latch (NAND-based, Active Low)

| S̄ | R̄ | Q | Q̄ | สถานะ |
|:---:|:---:|:---:|:---:|:---|
| 1 | 1 | Q₀ | Q̄₀ | Hold |
| 1 | 0 | 0 | 1 | Reset |
| 0 | 1 | 1 | 0 | Set |
| 0 | 0 | ? | ? | ❌ Invalid |

### Gated SR Latch

เพิ่ม **Enable (E)** — Latch ทำงานเฉพาะเมื่อ E = 1

| E | S | R | Q(next) |
|:---:|:---:|:---:|:---|
| 0 | X | X | Q₀ (Hold) |
| 1 | 0 | 0 | Q₀ (Hold) |
| 1 | 0 | 1 | 0 (Reset) |
| 1 | 1 | 0 | 1 (Set) |
| 1 | 1 | 1 | ❌ Invalid |

### D Latch (Data/Transparent Latch)

แก้ปัญหา Invalid state — ใช้อินพุตเพียง **1 ตัว** (D)

$$Q_{next} = D \quad \text{(เมื่อ E = 1)}$$

| E | D | Q(next) |
|:---:|:---:|:---|
| 0 | X | Q₀ (Hold) |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

> ⚠️ **ข้อเสีย Latch:** เป็น **level-sensitive** — เอาต์พุตเปลี่ยนได้ตลอดเวลาที่ Enable = 1 (Transparent)

---

## 6.3 สัญญาณนาฬิกา (Clock Signal)

```
      ┌──┐  ┌──┐  ┌──┐  ┌──┐
CLK ──┘  └──┘  └──┘  └──┘  └──
      ↑        ↑        ↑
   Positive  Positive  Positive
    Edge      Edge      Edge

   T (Period) = เวลา 1 รอบ
   f (Frequency) = 1/T
```

| คำศัพท์ | ความหมาย |
|:---|:---|
| **Positive Edge (↑)** | ขอบขาขึ้น (0→1) |
| **Negative Edge (↓)** | ขอบขาลง (1→0) |
| **Period (T)** | เวลา 1 รอบ clock |
| **Frequency (f)** | จำนวนรอบต่อวินาที = 1/T |
| **Duty Cycle** | สัดส่วนเวลาที่เป็น HIGH |

---

## 6.4 Flip-Flop vs Latch

| เกณฑ์ | Latch | Flip-Flop |
|:---|:---:|:---:|
| Trigger | **Level**-sensitive | **Edge**-sensitive |
| เปลี่ยนสถานะ | ตลอดเวลาที่ Enable = 1 | เฉพาะ **ขอบ** Clock เท่านั้น |
| ความเสถียร | ต่ำกว่า | สูงกว่า ✅ |
| การใช้งาน | วงจร asynchronous | วงจร synchronous ✅ |

---

## 6.5 SR Flip-Flop

| Clock Edge | S | R | Q(next) |
|:---:|:---:|:---:|:---|
| ↑ | 0 | 0 | Q₀ (Hold) |
| ↑ | 0 | 1 | 0 (Reset) |
| ↑ | 1 | 0 | 1 (Set) |
| ↑ | 1 | 1 | ❌ Invalid |

**Characteristic Equation:**

$$Q_{next} = S + \overline{R} \cdot Q \quad \text{(เงื่อนไข: } SR = 0\text{)}$$

---

## 6.6 D Flip-Flop ⭐ (ใช้มากที่สุด)

ข้อมูลถูก "จับ" (Capture) ที่ขอบ Clock เท่านั้น

$$Q_{next} = D$$

| Clock Edge | D | Q(next) |
|:---:|:---:|:---|
| ↑ | 0 | 0 |
| ↑ | 1 | 1 |

> 💡 ง่ายที่สุด ไม่มี Invalid state เหมาะสำหรับเก็บข้อมูล

**IC: 7474** (Dual D Flip-Flop, positive-edge triggered)

---

## 6.7 JK Flip-Flop ⭐ (อเนกประสงค์)

แก้ปัญหา Invalid ของ SR — เมื่อ J=K=1 จะ **Toggle** (สลับสถานะ)

| Clock Edge | J | K | Q(next) | โหมด |
|:---:|:---:|:---:|:---:|:---|
| ↓ | 0 | 0 | Q₀ | Hold |
| ↓ | 0 | 1 | 0 | Reset |
| ↓ | 1 | 0 | 1 | Set |
| ↓ | 1 | 1 | Q̄₀ | **Toggle** |

**Characteristic Equation:**

$$Q_{next} = J\overline{Q} + \overline{K}Q$$

**IC: 7473** (Dual JK FF, negative-edge), **7476** (Dual JK FF with Preset/Clear)

---

## 6.8 T Flip-Flop (Toggle)

$$Q_{next} = T \oplus Q$$

| Clock Edge | T | Q(next) | โหมด |
|:---:|:---:|:---:|:---|
| ↑ | 0 | Q₀ | Hold |
| ↑ | 1 | Q̄₀ | Toggle |

> 💡 สร้างได้จาก JK FF โดยต่อ **J = K = T**
> ใช้เป็น **Frequency Divider** — ความถี่เอาต์พุต = ½ ความถี่ Clock

---

## 6.9 สรุปเปรียบเทียบ Flip-Flop ทุกชนิด

| ชนิด | Characteristic Equation | จุดเด่น | จุดด้อย |
|:---:|:---|:---|:---|
| SR | $Q^+ = S + \overline{R}Q$ | พื้นฐาน | มี Invalid (SR=1) |
| **D** | $Q^+ = D$ | ง่ายที่สุด | ไม่มี Toggle |
| **JK** | $Q^+ = J\overline{Q} + \overline{K}Q$ | มีครบทุกโหมด | ซับซ้อนกว่า |
| T | $Q^+ = T \oplus Q$ | Toggle mode | ไม่มี Set/Reset ตรง |

---

## 6.10 Excitation Table (ตารางกระตุ้น) ⭐

ใช้ในการ **ออกแบบวงจร Sequential** — หาค่าอินพุตที่ต้องใส่ให้ FF เปลี่ยนจากสถานะ Q ไปเป็น Q⁺

| Q → Q⁺ | SR | D | JK | T |
|:---:|:---:|:---:|:---:|:---:|
| 0 → 0 | 0X | 0 | 0X | 0 |
| 0 → 1 | 10 | 1 | 1X | 1 |
| 1 → 0 | 01 | 0 | X1 | 1 |
| 1 → 1 | X0 | 1 | X0 | 0 |

> 💡 **ท่องจำ JK:** "0→0: 0X, 0→1: 1X, 1→0: X1, 1→1: X0" (J ทำให้เป็น 1, K ทำให้เป็น 0)

---

## 6.11 Timing Diagram

### วิธีอ่าน Timing Diagram

1. ดูขอบ Clock (positive-edge ↑ หรือ negative-edge ↓)
2. ที่ขอบ Clock แต่ละจุด → ดูค่า Input → กำหนด Output

### ตัวอย่าง: D Flip-Flop (Positive Edge)

```
         ┌──┐  ┌──┐  ┌──┐  ┌──┐  ┌──┐
CLK: ────┘  └──┘  └──┘  └──┘  └──┘  └──
         ↑     ↑     ↑     ↑     ↑
     ┌──────┐     ┌──────────────┐
D:   ┘      └─────┘              └──────
         1     0     1     1     0

Q:   ────┐  ┌──────┐     ┌──────────┐
         └──┘      └─────┘          └──
         1     0     1     1     0
```

### ตัวอย่าง: JK Flip-Flop (Negative Edge, J=K=1 → Toggle)

```
         ┌──┐  ┌──┐  ┌──┐  ┌──┐
CLK: ────┘  └──┘  └──┘  └──┘  └──
            ↓     ↓     ↓     ↓

Q:   ───────┐  ┌──────┐  ┌──────
            └──┘      └──┘
    (Q=0)  (Q=1) (Q=0)(Q=1)(Q=0)
```

---

## 6.12 Preset และ Clear (Asynchronous Inputs)

FF ส่วนใหญ่มี Preset (PRE) และ Clear (CLR) สำหรับตั้งค่าเริ่มต้น **โดยไม่ต้องรอ Clock**

| PRE | CLR | Q | หมายเหตุ |
|:---:|:---:|:---:|:---|
| 0 | 1 | 1 | Force SET (Active Low) |
| 1 | 0 | 0 | Force RESET (Active Low) |
| 1 | 1 | ปกติ | ทำงานตาม Clock |
| 0 | 0 | ? | ❌ Invalid |

---

## แบบฝึกหัดท้ายบท

1. อธิบายความแตกต่างระหว่าง Latch กับ Flip-Flop พร้อมยกตัวอย่าง
2. สร้าง D Flip-Flop จาก NAND gates (วาดแผนผัง)
3. วาด Timing Diagram ของ JK Flip-Flop เมื่อ J=1, K=1 เป็นเวลา 8 clock cycles
4. หา Excitation inputs สำหรับ JK FF เมื่อต้องการลำดับสถานะ: 0→1→1→0→0→...
5. ต่อวงจร JK Flip-Flop บน **Tinkercad** โดยใช้ IC 7473 ในโหมด Toggle
