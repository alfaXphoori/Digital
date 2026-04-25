# Chapter 8: หน่วยความจำและอุปกรณ์ลอจิกโปรแกรมได้

## Memory Devices & Programmable Logic

---

## 8.1 บทนำ

หน่วยความจำ (Memory) เป็นส่วนสำคัญของระบบดิจิทัล ใช้เก็บข้อมูลและโปรแกรม ส่วน PLD (Programmable Logic Device) ช่วยให้สร้างวงจรที่ซับซ้อนโดยไม่ต้องต่อเกตจำนวนมาก

---

## 8.2 โครงสร้างหน่วยความจำ (Memory Architecture)

```
              Address Bus (n bits)
                    │
                    ↓
            ┌───────────────┐
            │   Address     │
            │   Decoder     │
            │  (n → 2ⁿ)     │
            ├───────────────┤
  CS ──────→│               │
  R/W̄ ─────→│  Memory Array │   2ⁿ × m bits
  OE ──────→│  (Storage)    │
            │               │
            ├───────────────┤
            │  I/O Buffers  │
            └───────┬───────┘
                    │
              Data Bus (m bits)
```

### สัญญาณควบคุม

| สัญญาณ | ความหมาย |
|:---:|:---|
| **Address Bus** | ระบุตำแหน่งที่ต้องการอ่าน/เขียน |
| **Data Bus** | ข้อมูลที่อ่าน/เขียน |
| **CS** (Chip Select) | เลือกชิปหน่วยความจำ |
| **R/W̄** (Read/Write) | 1 = อ่าน, 0 = เขียน |
| **OE** (Output Enable) | เปิดเอาต์พุต |

### การคำนวณความจุ

$$\text{ความจุ} = 2^n \times m \text{ bits}$$

- $n$ = จำนวน address lines
- $m$ = จำนวน data lines (ความกว้างข้อมูล)

**ตัวอย่าง:**
| Address Bus | Data Bus | ความจุ |
|:---:|:---:|:---|
| 10 bits | 8 bits | $2^{10} \times 8$ = 1K × 8 = 8 Kbit = **1 KB** |
| 12 bits | 16 bits | $2^{12} \times 16$ = 4K × 16 = 64 Kbit = **8 KB** |
| 16 bits | 8 bits | $2^{16} \times 8$ = 64K × 8 = 512 Kbit = **64 KB** |
| 20 bits | 8 bits | $2^{20} \times 8$ = 1M × 8 = **1 MB** |

---

## 8.3 ประเภทหน่วยความจำ

```
                   Memory
                     │
           ┌─────────┴─────────┐
         RAM                  ROM
      (Volatile)          (Non-Volatile)
           │                   │
     ┌─────┴─────┐      ┌─────┼─────┬─────┬──────┐
   SRAM        DRAM    ROM   PROM  EPROM EEPROM Flash
  (Static)  (Dynamic) (Mask)       (UV)
```

### RAM (Random Access Memory) — ความจำชั่วคราว

| คุณสมบัติ | SRAM (Static) | DRAM (Dynamic) |
|:---|:---:|:---:|
| โครงสร้างเซลล์ | Flip-Flop (6 transistors) | Capacitor (1T1C) |
| ความเร็ว | **เร็วมาก** ✅ | ช้ากว่า |
| ความหนาแน่น | ต่ำ | **สูง** ✅ |
| ต้อง Refresh? | ❌ ไม่ | ✅ ต้อง (ทุก ms) |
| ราคา | แพง | ถูก ✅ |
| การใช้งาน | Cache Memory | Main Memory (RAM ในคอม) |

> ⚠️ ทั้ง SRAM และ DRAM เป็น **Volatile** — ข้อมูลหายเมื่อปิดไฟ

### ROM (Read-Only Memory) — ความจำถาวร

| ประเภท | เขียนได้? | ลบได้? | วิธีลบ | การใช้งาน |
|:---|:---:|:---:|:---:|:---|
| **Mask ROM** | ❌ (โรงงาน) | ❌ | — | Mass production |
| **PROM** | 1 ครั้ง | ❌ | — | Prototype |
| **EPROM** | ✅ หลายครั้ง | ✅ | UV light (20 นาที) | Development |
| **EEPROM** | ✅ หลายครั้ง | ✅ | ไฟฟ้า (byte-level) | Firmware, Settings |
| **Flash** | ✅ หลายครั้ง | ✅ | ไฟฟ้า (block-level) | USB, SSD, SD Card |

> 💡 **Flash Memory** คือ EEPROM ที่ปรับปรุงให้ลบเป็น block ได้ → เร็วกว่า

---

## 8.4 Memory Address Decoding

### Full Decoding

ใช้ address line ทุกเส้น → แต่ละ chip มี address **ไม่ซ้ำ**

### Partial Decoding

ใช้ address line **บางส่วน** → อาจมี address ซ้ำ (mirroring) แต่ประหยัดวงจร

### ตัวอย่าง: Memory Map (16-bit Address Space = 64 KB)

```
0000h ┌──────────────────┐
      │   ROM (8 KB)     │  CS₁: A₁₅A₁₄A₁₃ = 000
1FFFh └──────────────────┘
2000h ┌──────────────────┐
      │   RAM 1 (8 KB)   │  CS₂: A₁₅A₁₄A₁₃ = 001
3FFFh └──────────────────┘
4000h ┌──────────────────┐
      │   RAM 2 (8 KB)   │  CS₃: A₁₅A₁₄A₁₃ = 010
5FFFh └──────────────────┘
6000h ┌──────────────────┐
      │   (Unused)       │
FFFFh └──────────────────┘
```

ใช้ **74138 (3-to-8 Decoder)** ถอดรหัสบิต A₁₅, A₁₄, A₁₃ → เลือก Chip Select

---

## 8.5 ROM ในฐานะ Combinational Logic

ROM สามารถสร้าง **ฟังก์ชันบูลีนใดก็ได้** — เพราะมันเก็บ Truth Table ทั้งหมดไว้

- Address = ตัวแปรอินพุต
- Data = ฟังก์ชันเอาต์พุต

**ตัวอย่าง:** ใช้ ROM 8×2 สร้าง 2 ฟังก์ชันของ 3 ตัวแปร

| Address (CBA) | Data (F₁ F₀) |
|:---:|:---:|
| 000 | 0 1 |
| 001 | 1 0 |
| 010 | 1 1 |
| 011 | 0 0 |
| 100 | 1 1 |
| 101 | 0 1 |
| 110 | 1 0 |
| 111 | 1 1 |

> 💡 **ข้อดี:** ไม่ต้องลดรูป ไม่ต้องออกแบบวงจร
> **ข้อเสีย:** ใช้ memory มาก (ทุก minterm ถูกเก็บ)

---

## 8.6 Programmable Logic Devices (PLD)

### โครงสร้างพื้นฐาน

```
Inputs → [AND Array] → Product Terms → [OR Array] → Outputs
```

### PLA (Programmable Logic Array)

- **AND Array: Programmable** — เลือก product terms ที่ต้องการ
- **OR Array: Programmable** — เลือกว่า product terms ไหนไปเอาต์พุตไหน

```
Inputs → [Programmable AND] → [Programmable OR] → Outputs
```

**ข้อดี:** ยืดหยุ่นมาก, ใช้ทรัพยากรน้อย
**ข้อเสีย:** ช้า (ทั้ง 2 array ต้อง program)

### PAL (Programmable Array Logic)

- **AND Array: Programmable**
- **OR Array: Fixed** (กำหนดไว้แล้ว)

```
Inputs → [Programmable AND] → [Fixed OR] → Outputs
```

**ข้อดี:** เร็วกว่า PLA ✅
**ข้อเสีย:** ยืดหยุ่นน้อยกว่า (OR connections คงที่)

### GAL (Generic Array Logic)

- เหมือน PAL แต่ **ลบและเขียนใหม่ได้** (Reprogrammable)
- มี output logic macrocell ที่ปรับแต่งได้

---

## 8.7 ตัวอย่าง: การออกแบบวงจรควบคุมไมโครเวฟด้วย PAL (Smart Microwave Controller)

เพื่อให้เห็นภาพการใช้งาน **PAL** ในชีวิตจริง เราจะออกแบบวงจรควบคุมไมโครเวฟที่มี 5 อินพุต และ 4 เอาต์พุต

### 1. กำหนดตัวแปร (I/O Mapping)

| ประเภท | สัญลักษณ์ | ความหมาย (1 = Active) |
|:---:|:---:|:---|
| **Input** | **D** (Door) | ประตูปิดสนิท |
| | **T** (Timer) | ยังมีเวลาเหลือ |
| | **W** (Weight) | มีอาหารวางบนจานหมุน |
| | **S** (Start) | กดปุ่มเริ่มทำงาน |
| | **H** (Overheat)| เครื่องร้อนเกินไป |
| **Output**| **M** (Magnetron)| หัวคลื่นทำงาน (เวฟอาหาร) |
| | **F** (Fan) | พัดลมระบายอากาศ |
| | **L** (Light) | ไฟส่องสว่างภายใน |
| | **B** (Buzzer) | เสียงเตือน |

### 2. สมการลอจิก (Boolean Equations)

ในโครงสร้าง PAL เรามักเขียนในรูป **Sum of Products (SOP)**:
- $M = D \cdot T \cdot W \cdot S \cdot \bar{H}$
- $F = M + H$ (ทำงานเมื่อเครื่องเวฟอยู่ หรือเครื่องร้อน)
- $L = \bar{D} + M$ (สว่างเมื่อเปิดประตู หรือเครื่องทำงาน)
- $B = (\bar{T} \cdot D) + H$ (ดังเมื่อหมดเวลาขณะประตูปิด หรือเครื่องร้อน)

### 3. โครงสร้างการเชื่อมต่อใน PAL

ใน PAL เราจะโปรแกรมส่วน **AND Array** เพื่อสร้าง Product Terms และต่อเข้ากับ **Fixed OR** ที่กำหนดไว้แล้ว:

| Output | Product Terms (AND Array) |
|:---:|:---|
| **M** | $D \cdot T \cdot W \cdot S \cdot \bar{H}$ |
| **F** | $(D \cdot T \cdot W \cdot S \cdot \bar{H}) + (H)$ |
| **L** | $(\bar{D}) + (D \cdot T \cdot W \cdot S \cdot \bar{H})$ |
| **B** | $(\bar{T} \cdot D) + (H)$ |

> 💡 **ข้อสังเกต:** PAL ช่วยให้เราสร้างวงจรที่มีเงื่อนไขความปลอดภัย (Interlock) ได้ง่าย เช่น Magnetron จะไม่ทำงานถ้าประตูปิดไม่สนิท ($D=0$) หรือเครื่องร้อนเกิน ($H=1$) แม้จะกดปุ่ม Start ก็ตาม

---

## 8.8 เปรียบเทียบ ROM, PLA, PAL

| เกณฑ์ | ROM | PLA | PAL |
|:---|:---:|:---:|:---:|
| AND Array | Fixed (Decoder) | **Programmable** | **Programmable** |
| OR Array | **Programmable** | **Programmable** | Fixed |
| จำนวน Product Terms | $2^n$ (ทั้งหมด) | จำกัด | จำกัด |
| ความยืดหยุ่น | สูงสุด ✅ | สูง | ปานกลาง |
| ความเร็ว | ปานกลาง | ช้า | **เร็ว** ✅ |
| ขนาด/ทรัพยากร | มาก | **น้อย** ✅ | ปานกลาง |

---

## 8.9 CPLD & FPGA (แนะนำเบื้องต้น)

### CPLD (Complex Programmable Logic Device)

- โครงสร้างแบบ PAL-like blocks หลายตัวเชื่อมด้วย interconnect
- ออกแบบด้วย **HDL** (Hardware Description Language)
- เหมาะกับงาน combinational logic ที่ซับซ้อนปานกลาง

### FPGA (Field-Programmable Gate Array)

```
┌──────────────────────────────┐
│  IOB   IOB   IOB   IOB  IOB │  IOB = I/O Block
│ ┌────┐ ┌────┐ ┌────┐        │
│ │CLB │─│CLB │─│CLB │  IOB   │  CLB = Configurable
│ └────┘ └────┘ └────┘        │        Logic Block
│ ┌────┐ ┌────┐ ┌────┐        │
│ │CLB │─│CLB │─│CLB │  IOB   │
│ └────┘ └────┘ └────┘        │
│  IOB   IOB   IOB   IOB  IOB │
└──────────────────────────────┘
     (Programmable Interconnect)
```

| ส่วนประกอบ | หน้าที่ |
|:---|:---|
| **CLB** | Logic Block ที่มี LUT (Look-Up Table) + FF |
| **IOB** | เชื่อมต่อกับภายนอก |
| **Interconnect** | สายเชื่อมระหว่าง CLB |
| **Block RAM** | หน่วยความจำภายใน |

**ข้อดี FPGA:**
- สร้างวงจรซับซ้อนมากได้ (CPU, GPU, AI accelerator)
- โปรแกรมใหม่ได้ไม่จำกัด
- ออกแบบด้วย **VHDL** หรือ **Verilog**

### CPLD vs FPGA

| เกณฑ์ | CPLD | FPGA |
|:---|:---:|:---:|
| โครงสร้าง | PAL-based | LUT-based |
| ความซับซ้อน | น้อย–ปานกลาง | **สูงมาก** ✅ |
| ความเร็ว (Predictable) | ✅ | ขึ้นกับ routing |
| มี Block RAM? | ❌ | ✅ |
| ราคา | ถูก ✅ | แพงกว่า |

---

## แบบฝึกหัดท้ายบท

1. คำนวณความจุหน่วยความจำที่มี Address Bus 12 bits, Data Bus 16 bits
2. ออกแบบ Memory Map สำหรับ ROM 4KB + RAM 8KB + RAM 4KB ในระบบ 16-bit address
3. ใช้ ROM 16×4 สร้าง Full Adder 2 ชุด (เขียน content ของ ROM)
4. เปรียบเทียบข้อดีข้อเสียของ PLA กับ PAL พร้อมยกตัวอย่างสถานการณ์ที่เหมาะสม
5. อธิบายความแตกต่างระหว่าง SRAM, DRAM, ROM, และ Flash Memory พร้อมยกตัวอย่างการใช้งานจริง
