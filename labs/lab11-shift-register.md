# 🔬 Lab 11: Shift Register — 4-bit SIPO ด้วย 7474

## วัตถุประสงค์

- ต่อวงจร 4-bit SIPO Shift Register ด้วย D Flip-Flop (7474)
- เข้าใจการเลื่อนข้อมูลแบบ Serial-In Parallel-Out
- ป้อนข้อมูล serial แล้วสังเกตผล parallel

---

## อุปกรณ์ที่ใช้ (Tinkercad)

| อุปกรณ์ | จำนวน |
|:---|:---:|
| IC 7474 (Dual D FF) | 2 |
| LED | 4 |
| Resistor 220Ω | 4 |
| DIP Switch | 1 |
| Push Button | 1 |
| Breadboard | 1 |
| Power Supply 5V | 1 |

---

## ส่วนที่ 1: ทบทวน SIPO (5 นาที)

### Serial-In Parallel-Out Shift Register

```
Data ──→ [D FF₀] ──→ [D FF₁] ──→ [D FF₂] ──→ [D FF₃]
  (Serial    Q₀         Q₁         Q₂         Q₃
   Input)   LED₀       LED₁       LED₂       LED₃
                                          (Parallel Output)
            ↑CLK       ↑CLK       ↑CLK       ↑CLK
            └───────────┴───────────┴───────────┘
                        Common Clock
```

- **ทุก FF ใช้ Clock เดียวกัน** (Synchronous)
- ข้อมูลเลื่อนจาก FF₀ → FF₁ → FF₂ → FF₃ ทีละ 1 บิตต่อ Clock

---

## ส่วนที่ 2: IC 7474 — Dual D Flip-Flop (5 นาที)

### Pin Diagram

```
        ┌───U───┐
 1CLR ──┤1    14├── VCC
   1D ──┤2    13├── 2CLR
 1CLK ──┤3    12├── 2D
 1PRE ──┤4    11├── 2CLK
   1Q ──┤5    10├── 2PRE
  1Q̄ ──┤6     9├── 2Q
 GND ──┤7     8├── 2Q̄
        └───────┘
```

> 7474 ทำงานที่ **ขอบขาขึ้น (Positive Edge Triggered)**

---

## ส่วนที่ 3: ต่อวงจร (25 นาที)

### ใช้ IC 7474 จำนวน 2 ตัว (2 FF/ตัว = 4 FF)

**IC₁ — FF₀ และ FF₁:**

| สัญญาณ | FF₀ | FF₁ |
|:---|:---:|:---:|
| D | Switch Data (pin 2) | Q₀ ของ FF₀ (pin 5 → pin 12) |
| CLK | Push Button (pin 3) | Push Button (pin 11) |
| PRE | VCC (pin 4) | VCC (pin 10) |
| CLR | VCC (pin 1) | VCC (pin 13) |
| Q | LED₀ (pin 5) | LED₁ (pin 9) |

**IC₂ — FF₂ และ FF₃:**

| สัญญาณ | FF₂ | FF₃ |
|:---|:---:|:---:|
| D | Q₁ ของ FF₁ (IC₁ pin 9 → pin 2) | Q₂ ของ FF₂ (pin 5 → pin 12) |
| CLK | Push Button (pin 3) | Push Button (pin 11) |
| PRE | VCC (pin 4) | VCC (pin 10) |
| CLR | VCC (pin 1) | VCC (pin 13) |
| Q | LED₂ (pin 5) | LED₃ (pin 9) |

> ⚠️ **Clock ต้องต่อร่วมกันทั้ง 4 FF!**

---

## ส่วนที่ 4: ทดสอบ — ป้อนข้อมูล 1011 (20 นาที)

### เริ่มต้น: LED ทั้ง 4 ดับ (0000)

ป้อนข้อมูล **1011** (บิตซ้ายสุดเข้าก่อน):

| Clock | Data Input | Q₀ (LED₀) | Q₁ (LED₁) | Q₂ (LED₂) | Q₃ (LED₃) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| เริ่ม | — | 0 | 0 | 0 | 0 |
| 1 | **1** | | | | |
| 2 | **0** | | | | |
| 3 | **1** | | | | |
| 4 | **1** | | | | |

**หลัง 4 Clock:** Q₃Q₂Q₁Q₀ = __________ (ควรเป็น 1011)

📸 **Screenshot หลังป้อนครบ 4 บิต (LED แสดง 1011)**

### ทดสอบเพิ่ม — ป้อน 1100

ป้อนต่ออีก 4 บิต (1100):

| Clock | Data Input | Q₀ | Q₁ | Q₂ | Q₃ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | **1** | | | | |
| 6 | **1** | | | | |
| 7 | **0** | | | | |
| 8 | **0** | | | | |

**หลัง 8 Clock:** Q₃Q₂Q₁Q₀ = __________ (ควรเป็น 1100)

---

## ส่วนที่ 5: คำถาม (5 นาที)

1. SIPO ต้องใช้กี่ Clock pulses จึงจะได้ข้อมูลครบ n บิต?
2. ถ้าต้องการ SIPO 8-bit ต้องใช้ 7474 กี่ตัว?
3. SIPO กับ PIPO ต่างกันอย่างไร?
4. Shift Register ใช้ทำอะไรได้บ้างในระบบจริง?

---

## การส่งงาน

> 📋 **ส่งงานผ่าน Google Form**

### ขั้นตอน

1. ถ่าย Screenshot วงจรตามรายการด้านล่าง
2. เปิดวงจรใน Tinkercad → กด **Share** (มุมบนขวา) → **Copy Link**
3. เปิด Google Form → วาง Tinkercad Link → แนบ Screenshot → กรอกคำตอบ → กด **Submit**

### Checklist ก่อนกด Submit

- [ ] Screenshot วงจร 4-bit SIPO ที่ต่อเสร็จ
- [ ] Screenshot แสดงผล 1011 (ที่ LED ติดถูกตำแหน่ง)
- [ ] ตารางทดสอบครบทั้ง 2 ชุดข้อมูล
- [ ] ตอบคำถาม 4 ข้อ
- [ ] Tinkercad Share Link พร้อมแล้ว
- [ ] กรอก Google Form และกด Submit เรียบร้อย
