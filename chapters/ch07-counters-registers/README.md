# Chapter 7: ตัวนับและรีจิสเตอร์

## Counters & Registers

---

## 7.1 บทนำ

- **Counter** = วงจร Sequential ที่เปลี่ยนสถานะตามลำดับที่กำหนดทุก Clock cycle
- **Register** = กลุ่ม Flip-Flop ที่เก็บข้อมูลหลายบิตพร้อมกัน

---

# ส่วนที่ 1: ตัวนับ (Counters)

---

## 7.2 Asynchronous (Ripple) Counter

### หลักการ

- Clock ป้อนเข้าเฉพาะ **FF ตัวแรก** เท่านั้น
- เอาต์พุตของ FF ตัวหนึ่ง → เป็น Clock ของตัวถัดไป
- ใช้ **T Flip-Flop** (หรือ JK FF ที่ J=K=1) ในโหมด Toggle

### 3-bit Binary Up Counter

```
CLK ──→ [T FF₀] ──Q₀──→ [T FF₁] ──Q₁──→ [T FF₂] ──Q₂
          (LSB)                              (MSB)
```

### Timing Diagram

```
CLK: ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
Q₀:  0 1 0 1 0 1 0 1 0   (หาร 2)
Q₁:  0 0 1 1 0 0 1 1 0   (หาร 4)
Q₂:  0 0 0 0 1 1 1 1 0   (หาร 8)

Count: 0 1 2 3 4 5 6 7 0 (วนกลับ MOD-8)
```

### Down Counter

ต่อ $\overline{Q}$ ของ FF ตัวก่อนหน้าเป็น Clock ของตัวถัดไป (แทนที่จะใช้ Q)

```
Count: 7 6 5 4 3 2 1 0 7 (นับลง)
```

> ⚠️ **ข้อเสีย Ripple Counter:**
> - มี **Propagation Delay** สะสม → ช้า
> - อาจเกิด **Glitch** ชั่วขณะระหว่างเปลี่ยนสถานะ

---

## 7.3 MOD-N Counter (ตัวนับแบบไม่ครบ $2^n$)

### หลักการ

นับไม่ครบ $2^n$ → ใช้วงจร **Reset** เมื่อถึงค่าที่กำหนด

### ตัวอย่าง: MOD-6 Counter (นับ 0–5)

```
ลำดับ: 0 → 1 → 2 → 3 → 4 → 5 → (reset) → 0

เมื่อถึง 6 (110₂): Q₂=1, Q₁=1
→ ใช้ NAND gate detect: RESET = NAND(Q₂, Q₁)
→ ป้อน RESET เข้าขา CLR ของทุก FF
```

### ตัวอย่าง: MOD-10 Counter / Decade Counter (นับ 0–9)

```
ลำดับ: 0 → 1 → 2 → ... → 9 → (reset) → 0

เมื่อถึง 10 (1010₂): Q₃=1, Q₁=1
→ RESET = NAND(Q₃, Q₁)
```

**IC: 7490** (Decade Counter, MOD-10)
**IC: 7493** (4-bit Binary Counter, MOD-16)

---

## 7.4 Synchronous Counter ⭐

### หลักการ

- **Clock เดียวกัน** ป้อนให้ FF ทุกตัวพร้อมกัน
- ใช้ combinational logic ควบคุมอินพุตของแต่ละ FF
- **เร็วกว่า** ripple counter (ไม่มี delay สะสม)
- ไม่มี glitch

### ขั้นตอนการออกแบบ Synchronous Counter

```
1. กำหนด State Diagram (ลำดับการนับ)
         ↓
2. สร้าง State Table (Present State → Next State)
         ↓
3. เลือกชนิด Flip-Flop (D หรือ JK)
         ↓
4. ใช้ Excitation Table หาค่าอินพุต FF
         ↓
5. ใช้ K-Map ลดรูปสมการอินพุตของแต่ละ FF
         ↓
6. วาดวงจรลอจิก
```

### ตัวอย่าง: 3-bit Synchronous Up Counter (JK FF)

**State Table:**

| Q₂ | Q₁ | Q₀ | Q₂⁺ | Q₁⁺ | Q₀⁺ | J₂ | K₂ | J₁ | K₁ | J₀ | K₀ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | 1 | 0 | X | 0 | X | 1 | X |
| 0 | 0 | 1 | 0 | 1 | 0 | 0 | X | 1 | X | X | 1 |
| 0 | 1 | 0 | 0 | 1 | 1 | 0 | X | X | 0 | 1 | X |
| 0 | 1 | 1 | 1 | 0 | 0 | 1 | X | X | 1 | X | 1 |
| 1 | 0 | 0 | 1 | 0 | 1 | X | 0 | 0 | X | 1 | X |
| 1 | 0 | 1 | 1 | 1 | 0 | X | 0 | 1 | X | X | 1 |
| 1 | 1 | 0 | 1 | 1 | 1 | X | 0 | X | 0 | 1 | X |
| 1 | 1 | 1 | 0 | 0 | 0 | X | 1 | X | 1 | X | 1 |

**ผลลัพธ์จาก K-Map:**

$$J_0 = K_0 = 1 \quad \text{(Toggle ทุก clock)}$$
$$J_1 = K_1 = Q_0$$
$$J_2 = K_2 = Q_0 \cdot Q_1$$

```
วงจร:
CLK ──→ [JK FF₀] ──Q₀──┬──→ [JK FF₁] ──Q₁──┬──→ [JK FF₂] ──Q₂
         J=K=1          │    J=K=Q₀          │    J=K=Q₀·Q₁
                        └────────────────────┤
                                             └──[AND]──→ J₂,K₂
```

---

## 7.5 เปรียบเทียบ Async vs Sync Counter

| เกณฑ์ | Asynchronous (Ripple) | Synchronous |
|:---|:---:|:---:|
| Clock | ป้อนแค่ FF ตัวแรก | ป้อนทุก FF ✅ |
| ความเร็ว | ช้า (delay สะสม) | เร็ว ✅ |
| Glitch | อาจเกิด | ไม่มี ✅ |
| ความซับซ้อน | ง่าย ✅ | ซับซ้อนกว่า |
| ออกแบบ | ไม่ต้องใช้ K-Map | ต้องใช้ K-Map |

---

## 7.6 Up/Down Counter

เพิ่มสัญญาณ **UP/DOWN** เพื่อเลือกทิศทาง

| UP/DOWN | การทำงาน |
|:---:|:---|
| 1 | นับขึ้น |
| 0 | นับลง |

**IC: 74190** (Sync BCD Up/Down), **74191** (Sync Binary Up/Down)

---

## 7.7 Ring Counter & Johnson Counter

### Ring Counter

```
วงจร: Q₃ → Serial In ของ FF₃ (วนกลับ)

Initial:  1 0 0 0
CLK 1:    0 1 0 0
CLK 2:    0 0 1 0
CLK 3:    0 0 0 1
CLK 4:    1 0 0 0  ← วนกลับ

n Flip-Flops → MOD-n Counter
ข้อดี: ไม่ต้อง decode, ไม่มี glitch
ข้อเสีย: ใช้ FF มาก (n FF สำหรับ n สถานะ)
```

### Johnson Counter (Twisted Ring)

```
วงจร: Q̄₃ → Serial In ของ FF₃ (complement feedback)

Initial:  0 0 0 0
CLK 1:    1 0 0 0
CLK 2:    1 1 0 0
CLK 3:    1 1 1 0
CLK 4:    1 1 1 1
CLK 5:    0 1 1 1
CLK 6:    0 0 1 1
CLK 7:    0 0 0 1
CLK 8:    0 0 0 0  ← วนกลับ

n Flip-Flops → MOD-2n Counter
ข้อดี: decode ง่าย (ใช้ 2-input AND gate), สถานะมากกว่า Ring
```

---

# ส่วนที่ 2: รีจิสเตอร์ (Registers)

---

## 7.8 Parallel Register

โหลดข้อมูลทุกบิตพร้อมกันเมื่อ Clock edge

```
D₃ D₂ D₁ D₀    (Parallel Input)
 ↓  ↓  ↓  ↓
┌──┬──┬──┬──┐
│D │D │D │D │   (D Flip-Flops)
│FF│FF│FF│FF│
└──┴──┴──┴──┘
 ↓  ↓  ↓  ↓
Q₃ Q₂ Q₁ Q₀    (Parallel Output)
       ↑
      CLK
```

---

## 7.9 Shift Register (รีจิสเตอร์เลื่อน) ⭐

ข้อมูลเลื่อนจาก FF ตัวหนึ่งไปอีกตัวทุก Clock cycle

### ประเภท Shift Register

| ประเภท | Input | Output | IC ตัวอย่าง |
|:---|:---:|:---:|:---:|
| **SISO** (Serial In, Serial Out) | อนุกรม | อนุกรม | — |
| **SIPO** (Serial In, Parallel Out) | อนุกรม | ขนาน | 74164 |
| **PISO** (Parallel In, Serial Out) | ขนาน | อนุกรม | 74165 |
| **PIPO** (Parallel In, Parallel Out) | ขนาน | ขนาน | 74194 |

### ตัวอย่าง: 4-bit SIPO Shift Register

```
Serial In → [D FF₃] → [D FF₂] → [D FF₁] → [D FF₀]
               ↓         ↓         ↓         ↓
              Q₃        Q₂        Q₁        Q₀  (Parallel Out)

โหลดข้อมูล 1011 (MSB first):
CLK 1: Serial In=1 → 1 _ _ _
CLK 2: Serial In=0 → 0 1 _ _
CLK 3: Serial In=1 → 1 0 1 _
CLK 4: Serial In=1 → 1 1 0 1  ← ข้อมูลครบ!
```

### Universal Shift Register (74194)

ทำได้ทุกโหมดในชิปเดียว:

| S₁ | S₀ | โหมด |
|:---:|:---:|:---|
| 0 | 0 | **Hold** (ค้างค่าเดิม) |
| 0 | 1 | **Shift Right** |
| 1 | 0 | **Shift Left** |
| 1 | 1 | **Parallel Load** |

---

## 7.10 การประยุกต์ใช้ Shift Register

| การประยุกต์ | วิธีการ |
|:---|:---|
| **Serial ↔ Parallel Converter** | SIPO: serial → parallel, PISO: parallel → serial |
| **Time Delay** | ข้อมูลผ่าน n FF = หน่วง n clock cycles |
| **Ring Counter** | ต่อ output วนกลับ input |
| **Sequence Generator** | สร้างลำดับบิตตามต้องการ |

---

## 7.11 สรุป IC ที่ใช้บ่อย

| IC | ฟังก์ชัน | ประเภท |
|:---:|:---|:---:|
| **7490** | Decade Counter (MOD-10) | Async |
| **7493** | 4-bit Binary Counter (MOD-16) | Async |
| **74160** | Sync Decade Counter (with sync clear) | Sync |
| **74163** | Sync 4-bit Binary Counter | Sync |
| **74190** | Sync BCD Up/Down Counter | Sync |
| **74191** | Sync Binary Up/Down Counter | Sync |
| **74164** | 8-bit SIPO Shift Register | — |
| **74165** | 8-bit PISO Shift Register | — |
| **74194** | 4-bit Universal Shift Register | — |

---

## แบบฝึกหัดท้ายบท

1. ออกแบบ MOD-5 Ripple Counter โดยใช้ JK Flip-Flop (วาด State Diagram + วงจร)
2. ออกแบบ 3-bit Synchronous Down Counter โดยใช้ JK FF (ทำครบทุกขั้นตอน)
3. วาด Timing Diagram ของ 4-bit Johnson Counter เป็นเวลา 8 clock cycles
4. ออกแบบวงจร SIPO 4-bit Shift Register โดยใช้ D Flip-Flop
5. ต่อวงจร MOD-10 Counter + 7-Segment Display บน **Tinkercad** โดยใช้ IC 7490 + 4511
