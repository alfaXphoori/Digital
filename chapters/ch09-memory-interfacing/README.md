# Chapter 9: หน่วยความจำ PLD และการแปลงสัญญาณ ADC/DAC

## Memory Devices & Programmable Logic (PLD)

---

<div class="chapter-tab-content" data-tab-name="Concept" data-tab-icon="💡" id="concept" markdown="1">

## 9.1 บทนำ (Introduction)

ในระบบดิจิทัลและคอมพิวเตอร์ **หน่วยความจำ (Memory)** ทำหน้าที่จัดเก็บข้อมูล (Data) และชุดคำสั่ง (Instruction) เพื่อให้หน่วยประมวลผลนำไปใช้งาน ส่วน **อุปกรณ์ลอจิกโปรแกรมได้ (PLD)** เป็นอุปกรณ์ที่ช่วยให้เราสามารถสร้างวงจรลอจิกที่ซับซ้อนลงในชิปเพียงตัวเดียวได้ โดยการกำหนดฟังก์ชันการทำงานผ่านซอฟต์แวร์ แทนการต่อเกตจำนวนมากบนแผงวงจร

> 💡 มองภาพรวมก่อนเริ่ม: ครึ่งแรกของบทนี้ (9.1–9.11) พูดถึง "หน่วยความจำ" และ "ลอจิกโปรแกรมได้" ส่วนครึ่งหลัง (9.12 เป็นต้นไป) พูดถึงการเชื่อมต่อโลกแอนะล็อกกับโลกดิจิทัลผ่าน ADC/DAC ทั้งสองหัวข้อเชื่อมกันด้วยแนวคิดเดียวกันคือ "การเก็บและถอดรหัสข้อมูลเป็นบิต"

---

## 9.2 สถาปัตยกรรมหน่วยความจำ (Memory Architecture)

โครงสร้างภายในของหน่วยความจำประกอบด้วยเซลล์จัดเก็บข้อมูลที่เรียงตัวกันเป็นแถว (Rows) และคอลัมน์ (Columns) โดยมีส่วนประกอบหลักดังนี้

<svg viewBox="0 0 640 460" role="img" aria-label="สถาปัตยกรรมหน่วยความจำ: Address Bus เข้า Address Decoder, สัญญาณควบคุม CS, R/W, OE เข้า Memory Array, ส่งต่อไป I/O Buffers และ Data Bus แบบสองทาง" style="width:100%; max-width:620px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-mem" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Address Bus label + arrow down into decoder -->
  <text x="320" y="28" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Address Bus (n bits)</text>
  <text x="320" y="46" text-anchor="middle" font-size="11.5" fill="#475569">[ระบุตำแหน่ง]</text>
  <path d="M320,54 L320,90" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-mem)"/>

  <!-- Address Decoder -->
  <rect x="180" y="90" width="280" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="320" y="118" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">Address Decoder</text>
  <text x="320" y="136" text-anchor="middle" font-size="12" fill="#1e293b">(n → 2ⁿ) [เลือกแถวที่ตรงกับที่อยู่]</text>

  <!-- Decoder -> Memory Array -->
  <path d="M320,160 L320,196" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-mem)"/>

  <!-- Memory Array -->
  <rect x="180" y="196" width="280" height="100" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="320" y="234" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">Memory Array</text>
  <text x="320" y="252" text-anchor="middle" font-size="12" fill="#1e293b">(Storage)</text>
  <text x="320" y="270" text-anchor="middle" font-size="11.5" fill="#1e293b">(n แถว, m คอลัมน์)</text>

  <!-- Control signals into Memory Array -->
  <text x="30" y="216" font-size="12.5" fill="#0f172a">CS</text>
  <path d="M60,222 L180,222" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-mem)"/>

  <text x="30" y="246" font-size="12.5" fill="#0f172a">R/W̄</text>
  <path d="M60,252 L180,252" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-mem)"/>

  <text x="30" y="276" font-size="12.5" fill="#0f172a">OE</text>
  <path d="M60,282 L180,282" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-mem)"/>

  <!-- Annotation: capacity -->
  <text x="560" y="234" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">ความจุรวม</text>
  <text x="560" y="252" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">= 2ⁿ × m bits</text>

  <!-- Memory Array -> I/O Buffers -->
  <path d="M320,296 L320,332" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-mem)"/>

  <!-- I/O Buffers -->
  <rect x="180" y="332" width="280" height="60" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="320" y="358" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">I/O Buffers</text>
  <text x="320" y="376" text-anchor="middle" font-size="11.5" fill="#1e293b">[พักข้อมูลชั่วคราว]</text>

  <!-- I/O Buffers <-> Data Bus (bi-directional) -->
  <path d="M320,392 L320,426" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-mem)" marker-start="url(#arrow-mem)"/>
  <text x="320" y="446" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Data Bus (m bits)</text>
</svg>

### สัญญาณควบคุมที่สำคัญ (Control Signals)

1. **Address Bus:** เส้นสัญญาณระบุตำแหน่งข้อมูล (Input)
2. **Data Bus:** เส้นสัญญาณรับ-ส่งข้อมูล (Bi-directional)
3. **CS (Chip Select) / CE (Chip Enable):** เปิดการใช้งานชิปตัวนั้นๆ
4. **R/W̄ (Read/Write):** กำหนดทิศทางข้อมูล (1 = อ่าน, 0 = เขียน)
5. **OE (Output Enable):** เปิดเอาต์พุตของชิปให้ต่อกับ Data Bus (Tri-state control)

### การคำนวณความจุ (Memory Capacity)

ความจุวัดเป็น **จำนวนตำแหน่ง (Address) × ความกว้างข้อมูล (Bit per Address)**

- $2^{10} = 1024 = 1K$
- $2^{20} = 1,048,576 = 1M$

**ตัวอย่าง:** หน่วยความจำที่มี Address 12 เส้น และ Data 8 เส้น

- จำนวนตำแหน่ง = $2^{12} = 4096 = 4K$
- ความกว้างข้อมูล = 8 บิต (1 ไบต์)
- ความจุรวม = 4K × 8 bits = **4 KB**

> 💡 **เทคนิคจำเร็ว:** จำนวนเส้น Address บอก "จำนวนตำแหน่งที่เก็บได้" (ยกกำลัง 2) ส่วนจำนวนเส้น Data บอก "ความกว้างของข้อมูลต่อตำแหน่ง" คูณสองค่านี้เข้าด้วยกันจะได้ความจุรวมเสมอ

---

## 9.3 ประเภทของหน่วยความจำ (Memory Types)

แบ่งตามลักษณะการเก็บข้อมูลเมื่อไม่มีกระแสไฟฟ้า

### 9.3.1 RAM (Random Access Memory) — หน่วยความจำแบบลบเลือนได้ (Volatile)

ข้อมูลจะหายไปเมื่อปิดเครื่อง อ่านและเขียนข้อมูลได้รวดเร็วเท่ากันทุกตำแหน่ง

| คุณสมบัติ | SRAM (Static RAM) | DRAM (Dynamic RAM) |
|:---|:---:|:---:|
| **องค์ประกอบหลัก** | Flip-Flop (6 Transistors) | Capacitor (1T-1C) |
| **ความเร็ว** | **สูงมาก** ✅ | ช้ากว่า |
| **ความหนาแน่น** | ต่ำ (ชิปใหญ่) | **สูงมาก** ✅ |
| **การ Refresh** | ไม่ต้อง | **ต้องทำตลอดเวลา** (เพราะประจุรั่ว) |
| **ราคา** | แพง | ถูกกว่า |
| **การใช้งาน** | Cache Memory, Register | Main Memory (DDR4, DDR5) |

### 9.3.2 ROM (Read-Only Memory) — หน่วยความจำแบบไม่ลบเลือน (Non-Volatile)

ข้อมูลไม่หายเมื่อปิดเครื่อง เดิมทีออกแบบมาเพื่ออ่านอย่างเดียว แต่ปัจจุบันพัฒนาให้เขียนใหม่ได้หลายวิธี

1. **Mask ROM:** บันทึกข้อมูลจากโรงงาน (แก้ไขไม่ได้)
2. **PROM (Programmable ROM):** เขียนได้ครั้งเดียวโดยผู้ใช้
3. **EPROM (Erasable PROM):** ลบข้อมูลได้ด้วยแสง UV (สังเกตได้จากช่องกระจกใสบนชิป)
4. **EEPROM (Electrically Erasable PROM):** ลบและเขียนใหม่ได้ด้วยไฟฟ้า (ทีละไบต์)
5. **Flash Memory:** พัฒนาจาก EEPROM ให้ลบข้อมูลเป็นบล็อก (Block-level) ได้รวดเร็วและทนทาน

> 💡 จำลำดับวิวัฒนาการ ROM ได้ง่ายๆ ว่า "เขียนยากขึ้นเรื่อยๆ แต่ใช้ซ้ำได้มากขึ้นเรื่อยๆ": Mask ROM (เขียนครั้งเดียวจากโรงงาน) → PROM (เขียนเองได้ครั้งเดียว) → EPROM (ลบด้วยแสง UV) → EEPROM/Flash (ลบด้วยไฟฟ้า ใช้ซ้ำได้นับแสนครั้ง)

---

## 9.4 NAND Flash vs NOR Flash (ความรู้ขั้นสูง)

ปัจจุบัน Flash Memory แบ่งออกเป็น 2 สถาปัตยกรรมหลักตามลักษณะการต่อเซลล์

| คุณสมบัติ | NAND Flash | NOR Flash |
|:---|:---:|:---:|
| **ความจุ / ราคา** | สูง / ถูก ✅ | ต่ำ / แพง |
| **ความเร็วการอ่าน** | ช้ากว่า (อ่านเป็นบล็อก) | **เร็วมาก** (สุ่มตำแหน่งได้) ✅ |
| **ความเร็วการเขียน** | **เร็ว** ✅ | ช้า |
| **ความทนทาน** | สูง (หลักแสนครั้ง) | ต่ำกว่า |
| **การนำไปใช้** | SSD, USB Drive, SD Card | เก็บ BIOS, Firmware |

---

## 9.5 ไทม์มิ่งของหน่วยความจำ (Memory Timing)

ในการออกแบบระบบจริง เราต้องพิจารณาเวลาที่สัญญาณใช้ในการตอบสนอง

- **Access Time ($t_{AA}$):** เวลาที่นับตั้งแต่ป้อนที่อยู่ (Address) จนกระทั่งข้อมูลปรากฏบน Data Bus อย่างเสถียร
- **Write Cycle Time ($t_{WC}$):** เวลาขั้นต่ำที่ต้องรอเพื่อให้กระบวนการเขียนข้อมูลเสร็จสมบูรณ์ก่อนจะเริ่มคำสั่งถัดไป

---

## 9.6 การถอดรหัสที่อยู่ (Address Decoding)

ในระบบคอมพิวเตอร์มักมีชิปหน่วยความจำหลายตัวต่อรวมกันบนบัสเดียว เราจึงต้องมีวงจร **Address Decoder** เพื่อเลือกชิปที่ต้องการ (Chip Select)

### 1. Full Decoding

ใช้เส้น Address ที่เหลือทั้งหมดมาถอดรหัส ทำให้ชิปแต่ละตัวมีตำแหน่งที่ไม่ซ้ำซ้อนกันเลย

### 2. Partial Decoding (การถอดรหัสบางส่วน)

ใช้เส้น Address เพียงบางส่วนเพื่อประหยัดวงจร แต่จะเกิดปรากฏการณ์ **Mirroring** (ข้อมูลชุดเดียวโผล่มาในหลายๆ ที่อยู่)

**ตัวอย่าง:** ระบบ 16-bit Address (64KB Space) ใช้ชิป 8KB สองตัว

- ชิป 1 (ROM): อยู่ที่ตำแหน่ง 0000h - 1FFFh
- ชิป 2 (RAM): อยู่ที่ตำแหน่ง 2000h - 3FFFh

#### ตารางการถอดรหัสที่อยู่ (Address Decoding Truth Table)

| A15 | A14 | A13 | ช่วงที่อยู่ (Hex) | ชิปที่ถูกเลือก | สัญญาณเปิดใช้งาน |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0000h - 1FFFh | **ROM** | CS1 (Active LOW) |
| 0 | 0 | 1 | 2000h - 3FFFh | **RAM** | CS2 (Active LOW) |
| 0 | 1 | 0 | 4000h - 5FFFh | Unused | - |
| ... | ... | ... | ... | ... | ... |

> 💡 **ใช้อุปกรณ์ 74138 (Decoder) ในการถอดรหัสบิต A15, A14, A13** เพื่อสร้างสัญญาณ Chip Select (CS) ให้กับหน่วยความจำแต่ละตัว

---

## 9.7 อุปกรณ์ลอจิกโปรแกรมได้ (Programmable Logic Devices - PLD)

PLD คือชิปที่เราสามารถ "โปรแกรม" ความเชื่อมต่อภายในได้ โครงสร้างหลักประกอบด้วย **AND Array** และ **OR Array**

### 1. PLA (Programmable Logic Array)

- **AND Array:** โปรแกรมได้
- **OR Array:** โปรแกรมได้
- **ข้อดี:** ยืดหยุ่นสูงสุด ใช้ทรัพยากรน้อย
- **ข้อเสีย:** ความเร็วต่ำ (เพราะสัญญาณผ่านส่วนที่โปรแกรมได้ 2 ระดับ)

#### 9.7.1 โครงสร้างลอจิกเกตภายในของ PLA (Internal Logic Gate Structure)

เพื่อให้เข้าใจว่าจุดตัด (X) ใน Matrix กลายเป็นวงจรไฟฟ้าได้อย่างไร ให้พิจารณาโครงสร้างที่ประกอบด้วย **AND-OR Gates** ดังนี้

**1. ส่วนอินพุต (Input Inverters):**
ทุกอินพุตจะถูกแยกออกเป็น 2 เส้น คือสัญญาณปกติ และสัญญาณกลับค่า เพื่อให้พร้อมสำหรับการสร้าง Product Term ทุกรูปแบบ

**2. ส่วนสร้างเทอมคูณ (AND Array):**
ใช้ AND Gate ที่มีจุดเชื่อมต่อที่โปรแกรมได้ (Fuses) เพื่อสร้าง Product Terms

**3. ส่วนสร้างเทอมบวก (OR Array):**
รับผลลัพธ์จาก AND Gate มาผ่าน OR Gate ที่สามารถเลือกเชื่อมต่อได้ตามสมการ Sum of Products (SOP)

<svg viewBox="0 0 720 380" role="img" aria-label="โครงสร้าง PLA: อินพุต A, B และค่ากลับ A', B' เข้า AND Array สร้าง Product Term P1=A.B, P2=A'.B', P3=A.B' แล้วส่งต่อเข้า OR Array รวมเป็นเอาต์พุต O0, O1, O2" style="width:100%; max-width:700px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-pla" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Column headers -->
  <text x="90" y="24" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">อินพุต (Inputs)</text>
  <text x="330" y="24" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">AND Array (เทอมคูณ)</text>
  <text x="600" y="24" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">OR Array (เทอมบวก)</text>

  <!-- Input lines: A, A', B, B' -->
  <text x="40" y="60" font-size="13" font-weight="600" fill="#0f172a">A</text>
  <path d="M55,64 L260,64" fill="none" stroke="#475569" stroke-width="1.5"/>

  <text x="40" y="100" font-size="13" font-weight="600" fill="#0f172a">A'</text>
  <path d="M55,104 L260,104" fill="none" stroke="#475569" stroke-width="1.5"/>

  <text x="40" y="140" font-size="13" font-weight="600" fill="#0f172a">B</text>
  <path d="M55,144 L260,144" fill="none" stroke="#475569" stroke-width="1.5"/>

  <text x="40" y="180" font-size="13" font-weight="600" fill="#0f172a">B'</text>
  <path d="M55,184 L260,184" fill="none" stroke="#475569" stroke-width="1.5"/>

  <!-- Connection dots showing programmed fuses for each AND gate -->
  <!-- P1 = A.B : connects to A (y=64) and B (y=144) -->
  <circle cx="120" cy="64" r="4.5" fill="#4f46e5"/>
  <circle cx="120" cy="144" r="4.5" fill="#4f46e5"/>
  <path d="M120,64 L120,144" fill="none" stroke="#4f46e5" stroke-width="1.5"/>
  <path d="M120,104 L260,104" fill="none" stroke="#475569" stroke-width="0" opacity="0"/>

  <!-- P2 = A'.B' : connects to A' (y=104) and B' (y=184) -->
  <circle cx="165" cy="104" r="4.5" fill="#4f46e5"/>
  <circle cx="165" cy="184" r="4.5" fill="#4f46e5"/>
  <path d="M165,104 L165,184" fill="none" stroke="#4f46e5" stroke-width="1.5"/>

  <!-- P3 = A.B' : connects to A (y=64) and B' (y=184) -->
  <circle cx="210" cy="64" r="4.5" fill="#4f46e5"/>
  <circle cx="210" cy="184" r="4.5" fill="#4f46e5"/>
  <path d="M210,64 L210,184" fill="none" stroke="#4f46e5" stroke-width="1.5"/>

  <!-- vertical tap lines down to AND gates -->
  <path d="M120,144 L120,200" fill="none" stroke="#4f46e5" stroke-width="1.5" marker-end="url(#arrow-pla)"/>
  <path d="M165,184 L165,210 L300,210" fill="none" stroke="#4f46e5" stroke-width="1.5" marker-end="url(#arrow-pla)"/>
  <path d="M210,184 L210,300" fill="none" stroke="#4f46e5" stroke-width="1.5" marker-end="url(#arrow-pla)"/>

  <!-- AND gate P1 -->
  <rect x="300" y="64" width="100" height="44" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="350" y="82" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">AND (P1)</text>
  <text x="350" y="98" text-anchor="middle" font-size="11" fill="#1e293b">(A·B)</text>
  <path d="M120,64 L120,86 L300,86" fill="none" stroke="#4f46e5" stroke-width="1.5" marker-end="url(#arrow-pla)"/>

  <!-- AND gate P2 -->
  <rect x="300" y="188" width="100" height="44" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="350" y="206" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">AND (P2)</text>
  <text x="350" y="222" text-anchor="middle" font-size="11" fill="#1e293b">(A'·B')</text>

  <!-- AND gate P3 -->
  <rect x="300" y="296" width="100" height="44" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="350" y="314" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">AND (P3)</text>
  <text x="350" y="330" text-anchor="middle" font-size="11" fill="#1e293b">(A·B')</text>
  <path d="M210,184 L210,318 L300,318" fill="none" stroke="#4f46e5" stroke-width="1.5" marker-end="url(#arrow-pla)"/>

  <!-- P1 -> O0 directly -->
  <path d="M400,86 L600,86" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pla)"/>
  <text x="660" y="91" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">O0</text>

  <!-- P1, P2 -> OR Gate -> O1 -->
  <rect x="500" y="150" width="100" height="44" rx="8" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
  <text x="550" y="168" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">OR Gate</text>
  <text x="550" y="184" text-anchor="middle" font-size="11" fill="#1e293b">(P1+P2)</text>
  <path d="M400,86 L460,86 L460,164 L500,164" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pla)"/>
  <path d="M400,210 L460,210 L460,180 L500,180" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pla)"/>
  <path d="M600,172 L660,172" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pla)"/>
  <text x="690" y="177" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">O1</text>

  <!-- P1, P3 -> OR Gate -> O2 -->
  <rect x="500" y="280" width="100" height="44" rx="8" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
  <text x="550" y="298" text-anchor="middle" font-size="12" font-weight="600" fill="#0f172a">OR Gate</text>
  <text x="550" y="314" text-anchor="middle" font-size="11" fill="#1e293b">(P1+P3)</text>
  <path d="M400,86 L440,86 L440,292 L500,292" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pla)"/>
  <path d="M400,318 L470,318 L470,308 L500,308" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pla)"/>
  <path d="M600,302 L660,302" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pla)"/>
  <text x="690" y="307" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">O2</text>
</svg>

---

### 2. PAL (Programmable Array Logic)

- **AND Array:** โปรแกรมได้
- **OR Array:** **Fixed (กำหนดมาตายตัว)**
- **ข้อดี:** **เร็วมาก** ✅ เพราะลดส่วนที่โปรแกรมได้ลง ออกแบบวงจรง่าย
- **ข้อเสีย:** ยืดหยุ่นน้อยกว่า PLA

### 3. GAL (Generic Array Logic)

พัฒนาจาก PAL โดยใช้เทคโนโลยี EEPROM ทำให้ลบและเขียนใหม่ได้หลายครั้ง และมี Output Logic Macrocell (OLMC) ที่ปรับเปลี่ยนรูปแบบเอาต์พุตได้

> ⚠️ อย่าสับสน PLA กับ PAL: ทั้งคู่มี **AND Array โปรแกรมได้เหมือนกัน** แต่ต่างกันที่ **OR Array** — PLA โปรแกรมได้ทั้งสองฝั่ง (ยืดหยุ่นแต่ช้า) ส่วน PAL ตรึง OR Array ไว้ตายตัว (เร็วแต่ต้องสร้าง Product Term ซ้ำบ่อยกว่า)

---

## 9.8 ตัวอย่างการออกแบบ: วงจรควบคุมไมโครเวฟด้วย PAL (Smart Microwave Controller)

เพื่อให้เห็นภาพการใช้งาน **PAL (Programmable Array Logic)** อย่างละเอียด เราจะออกแบบวงจรควบคุมไมโครเวฟ จุดเด่นของ PAL คือ **AND Array โปรแกรมได้ แต่ OR Array ถูกกำหนดมาตายตัว** ทำให้วงจรเร็วกว่า PLA แต่มักจะต้อง "สร้าง Product Term ซ้ำ" หากเอาต์พุตหลายตัวใช้เงื่อนไขเดียวกัน

### 1. การกำหนดอินพุตและเอาต์พุต (Consistent Descriptive Mapping)

| ประเภท | สัญลักษณ์ | ความหมาย (1 = Active) |
|:---:|:---:|:---|
| **Input** | **Door** | ประตูปิดสนิท ($I_0$) |
| | **Timer** | ยังมีเวลาเหลือ ($I_1$) |
| | **Weight** | มีอาหารวางบนจานหมุน ($I_2$) |
| | **Start** | กดปุ่มเริ่มทำงาน ($I_3$) |
| | **Hot** | เครื่องร้อนเกินไป ($I_4$) |
| **Output**| **Mag** | หัวคลื่นทำงาน (เวฟอาหาร) ($O_0$) |
| | **Fan** | พัดลมระบายอากาศ ($O_1$) |
| | **Light** | ไฟส่องสว่างภายใน ($O_2$) |
| | **Buzzer** | เสียงเตือน ($O_3$) |

### 2. สมการลอจิก (Consistent Boolean Logic)

ในโครงสร้าง PAL เรามักเขียนในรูป **Sum of Products (SOP)**

- **Mag ($O_0$):** $\text{Door} \cdot \text{Timer} \cdot \text{Weight} \cdot \text{Start} \cdot \overline{\text{Hot}}$
- **Fan ($O_1$):** $(\text{Door} \cdot \text{Timer} \cdot \text{Weight} \cdot \text{Start} \cdot \overline{\text{Hot}}) + \text{Hot}$
- **Light ($O_2$):** $\overline{\text{Door}} + (\text{Door} \cdot \text{Timer} \cdot \text{Weight} \cdot \text{Start} \cdot \overline{\text{Hot}}$
- **Buzzer ($O_3$):** $(\overline{\text{Timer}} \cdot \text{Door}) + \text{Hot}$

### 3. โครงสร้างภายใน Matrix ของ PAL (Logic Implementation)

ใน PAL เราต้องโปรแกรมส่วน **AND Array** เพื่อสร้าง Product Terms และต่อเข้ากับ **Fixed OR** ที่กำหนดไว้แล้ว

```text
[ AND Array - โปรแกรมได้ ]
อินพุต (Inputs)  │ P1 │ P2 │ P3 │ P4 │ P5 │ P6 │ P7 │
─────────────────┼────┼────┼────┼────┼────┼────┼────┤
Door             │ X  │ X  │ ·  │ ·  │ X  │ X  │ ·  │
Door'            │ ·  │ ·  │ ·  │ X  │ ·  │ ·  │ ·  │
Timer            │ X  │ X  │ ·  │ ·  │ X  │ ·  │ ·  │
Timer'           │ ·  │ ·  │ ·  │ ·  │ ·  │ X  │ ·  │
Weight           │ X  │ X  │ ·  │ ·  │ X  │ ·  │ ·  │
Start            │ X  │ X  │ ·  │ ·  │ X  │ ·  │ ·  │
Hot              │ ·  │ ·  │ X  │ ·  │ ·  │ ·  │ X  │
Hot'             │ X  │ X  │ ·  │ ·  │ X  │ ·  │ ·  │
─────────────────┴────┴────┴────┴────┴────┴────┴────┘
(X = Connected, · = Disconnected)

[ OR Array - ตายตัว (Fixed) ]
Product Term 1 ──────────────────────────────► Mag (หัวคลื่น)
Product Term 2 ──┐
Product Term 3 ──┴───────────────────────────► Fan (พัดลม)
Product Term 4 ──┐
Product Term 5 ──┴───────────────────────────► Light (ไฟ)
Product Term 6 ──┐
Product Term 7 ──┴───────────────────────────► Buzzer (ออด)
```

> 💡 **ข้อสังเกตสำคัญของ PAL:** สังเกตว่า Product Term สำหรับเงื่อนไขเครื่องทำงาน ต้องถูกสร้างซ้ำหลายครั้ง เพราะโครงสร้าง OR Array ของ PAL ถูกตีกรอบตายตัว ไม่สามารถแชร์ Product Term ข้ามเอาต์พุตได้เหมือน PLA

---

## 9.9 เทคโนโลยีระดับสูง: CPLD และ FPGA

สำหรับงานที่ซับซ้อนมาก เช่น การสร้าง CPU หรือวงจรประมวลผล AI

### CPLD (Complex PLD)

ประกอบด้วย PAL-like blocks หลายๆ ตัวเชื่อมต่อกัน เหมาะกับงานลอจิกเชิงผสมที่ซับซ้อน

### FPGA (Field Programmable Gate Array)

ประกอบด้วย **Logic Blocks (CLBs)** จำนวนมหาศาล และ **Interconnect** ที่ซับซ้อน

- ใช้โครงสร้าง **Look-Up Table (LUT)** แทนเกตจริง
- มีหน่วยความจำ RAM และวงจรคำนวณคณิตศาสตร์ภายใน
- โปรแกรมใหม่ได้ไม่จำกัดด้วยภาษา **VHDL** หรือ **Verilog**

> 💡 ลำดับความซับซ้อนจากน้อยไปมาก: **PLD พื้นฐาน (PLA/PAL/GAL)** → **CPLD** (รวม PAL-like block หลายตัว) → **FPGA** (ลอจิกระดับ LUT นับพันถึงนับล้านบล็อก) — ยิ่งซับซ้อนขึ้น ยิ่งต้องใช้ภาษาโปรแกรมฮาร์ดแวร์ (HDL) ในการออกแบบ

---

## 9.10 การใช้งาน PLA ในระบบจริง: ระบบควบคุมลิฟต์ความเร็วสูง 4 ชั้น (Advanced 4-Floor Elevator)

ในส่วนนี้เราจะออกแบบ "มันสมอง" ของลิฟต์สำหรับอาคาร 4 ชั้น ซึ่งมีความซับซ้อนสูงกว่าปกติ โดยเพิ่มระบบควบคุมความเร็ว (High/Low Speed) เพื่อการจอดที่นุ่มนวล และระบบความปลอดภัยแบบหลายชั้น

### 1. การกำหนดอินพุตและเอาต์พุต (Full Descriptive Mapping)

- **Floor Sensors:** `Sensor_Floor_1` ถึง `Sensor_Floor_4` ($I_0 - I_3$)
- **Call Buttons:** `Button_Call_1` ถึง `Button_Call_4` ($I_4 - I_7$)
- **Safety & Status:**
  - $I_8$: `Status_Door_Closed` (ประตูปิดสนิท)
  - $I_9$: `Safety_Overweight` (น้ำหนักเกิน)
  - $I_{10}$: `Safety_Emergency` (ปุ่มหยุดฉุกเฉิน)
  - $I_{11}$: `Sensor_Obstruction` (สิ่งกีดขวางประตู)
  - $I_{12}$: `Safety_Fire_Alarm` (ตรวจจับไฟไหม้)
  - $I_{13}$: `Safety_Motor_Hot` (มอเตอร์ร้อนจัด)

**กลุ่มเอาต์พุต (6 Outputs):**

- $O_0$: `Motor_Move_Up` (ดึงขึ้น)
- $O_1$: `Motor_Move_Down` (หย่อนลง)
- $O_2$: `Motor_Speed_High` (วิ่งเร็วข้ามชั้น)
- $O_3$: `Brake_Engage_Command` (สั่งล็อคเบรก)
- $O_4$: `Door_Open_Command` (สั่งเปิดประตู)
- $O_5$: `System_Alarm_Siren` (ไซเรนเตือนภัย)

### 2. โครงสร้าง Matrix ของ PLA (Full High-Complexity Implementation)

นี่คือแผนผังการโปรแกรมภายในชิป PLA สำหรับระบบลิฟต์ 4 ชั้น ที่มีความซับซ้อนสูง โดยแยกตรรกะออกเป็น Product Terms (P1-P15) เพื่อความถูกต้องทางตรรกะ (Logical Correctness)

```text
[ AND Array - Programmable ]
อินพุต (Inputs)                │P1│P2│P3│P4│P5│P6│P7│P8│P9│P10│P11│P12│P13│P14│P15
─────────────────────────────┼──┼──┼──┼──┼──┼──┼──┼──┼──┼───┼───┼───┼───┼───┼───
Sensor_Floor_1 (I0)          │X │X │· │· │· │· │· │X │· │·  │·  │·  │·  │·  │·  
Sensor_Floor_2 (I1)          │· │· │X │· │· │· │· │· │X │·  │·  │·  │·  │·  │·  
Sensor_Floor_3 (I2)          │· │· │· │X │· │· │· │· │· │X  │·  │·  │·  │·  │·  
Sensor_Floor_4 (I3)          │· │· │· │· │X │X │· │· │· │·  │X  │·  │·  │·  │·  
Button_Call_1 (I4)           │· │· │· │X │· │X │· │X │· │·  │·  │·  │·  │·  │·  
Button_Call_2 (I5)           │· │· │· │X │X │· │· │· │X │·  │·  │·  │·  │·  
Button_Call_3 (I6)           │X │· │X │· │· │· │· │· │· │X  │·  │·  │·  │·  │·  
Button_Call_4 (I7)           │X │X │· │· │· │· │· │· │· │·  │X  │·  │·  │·  │·  
Status_Door_Closed (I8)      │X │X │X │X │X │X │· │· │· │·  │·  │·  │·  │·  │·  
Safety_Overweight (I9)       │·'│·'│·'│·'│·'│·'│· │· │· │·  │·  │X  │·  │·  │·  
Safety_Emergency (I10)       │·'│·'│·'│·'│·'│·'│· │· │· │·  │·  │·  │X  │·  │·  
Sensor_Obstruction (I11)     │·'│·'│·'│·'│·'│·'│· │· │· │·  │·  │·  │·  │X  │·  
Safety_Fire_Alarm (I12)      │·'│·'│·'│·'│·'│·'│· │· │· │·  │·  │·  │·  │·  │X  
Safety_Motor_Hot (I13)       │·'│·'│·'│·'│·'│·'│· │· │· │·  │·  │·  │·  │·  │X  
─────────────────────────────┼──┼──┼──┼──┼──┼──┼──┼──┼──┼───┼───┼───┼───┼───┼───
จำนวน Input เข้าเกต AND       │9 │8 │8 │9 │8 │8 │0 │2 │2 │2  │2  │1  │1  │1  │2  
─────────────────────────────┴──┴──┴──┴──┴──┴──┴──┴──┴──┴───┴───┴───┴───┴───┴───
(หมายเหตุ: P1-P6 ใช้เงื่อนไขความปลอดภัย NOT (·') เพื่อให้ลิฟต์วิ่ง)

[ OR Array - Programmable ]
เอาต์พุต (Outputs)             │Motor_Up│Motor_Dn│Speed_Hi│Brake│Open│Alm
─────────────────────────────┼────────┼────────┼────────┼─────┼────┼───
P1 (Up Long: F1 to F3/4)     │   X    │   ·    │   X    │  ·  │ ·  │ · 
P2 (Up Short: F1 to F2)      │   X    │   ·    │   ·    │  ·  │ ·  │ · 
P3 (Up Normal: F2 to F4)     │   X    │   ·    │   ·    │  ·  │ ·  │ · 
P4 (Down Short: F3 to F2)    │   ·    │   X    │   ·    │  ·  │ ·  │ · 
P5 (Down Long: F4 to F1/2)   │   ·    │   X    │   X    │  ·  │ ·  │ · 
P6 (Down Short: F4 to F3)    │   ·    │   X    │   ·    │  ·  │ ·  │ · 
P7 (Wait / Idle / Static)    │   ·    │   ·    │   ·    │  X  │ ·  │ · 
P8 (Arrival @ Floor 1)       │   ·    │   ·    │   ·    │  X  │ X  │ · 
P9 (Arrival @ Floor 2)       │   ·    │   ·    │   ·    │  X  │ X  │ · 
P10(Arrival @ Floor 3)       │   ·    │   ·    │   ·    │  X  │ X  │ · 
P11(Arrival @ Floor 4)       │   ·    │   ·    │   ·    │  X  │ X  │ · 
P12(Safety: Overweight)      │   ·    │   ·    │   ·    │  X  │ X  │ X 
P13(Safety: Emergency)       │   ·    │   ·    │   ·    │  X  │ ·  │ X 
P14(Safety: Obstruction)     │   ·    │   ·    │   ·    │  X  │ X  │ X 
P15(Safety: Fire / Hot)      │   ·    │   ·    │   ·    │  X  │ ·  │ X 
─────────────────────────────┼────────┼────────┼────────┼─────┼────┼───
จำนวน Input เข้าเกต OR        │   3    │   3    │   2    │  9  │ 6  │ 4 
─────────────────────────────┴────────┴────────┴────────┴─────┴────┴───

(X คือจุดที่เชื่อมต่อกัน, · คือจุดที่ไม่ได้เชื่อม, ·' คือการเชื่อมต่อกับสัญญาณ Inverted)
```

> ⚠️ สังเกตหมายเหตุใต้ AND Array: `P1`–`P6` ทุกตัวต้องใช้สัญญาณความปลอดภัยแบบ **Inverted (·')** ครบทั้ง 6 เงื่อนไข ก่อนจะอนุญาตให้ลิฟต์เคลื่อนที่ — นี่คือหลักการ **Fail-safe** ที่ถ้าเซนเซอร์ความปลอดภัยใดๆ Active (เช่นไฟไหม้ หรือน้ำหนักเกิน) มอเตอร์จะถูกตัดการทำงานทันทีในระดับฮาร์ดแวร์ ไม่ต้องพึ่งซอฟต์แวร์เลย

### 3. แผนผังการเชื่อมต่อทั้งระบบ (System Interconnection Diagram)

ในการใช้งานจริง PLA จะทำหน้าที่เป็น "ลอจิกควบคุมหลัก" โดยเชื่อมต่อกับอุปกรณ์ภายนอกผ่านวงจร Isolation

<svg viewBox="0 0 760 280" role="img" aria-label="แผนผังการเชื่อมต่อระบบลิฟต์: แถวบน Sensors 14 Inputs ไป Opto-Isolators ไป PLA System จากนั้นวกลงแถวล่างไหลกลับ Output Bus 6 Signals ไป Power Drivers ไป Actuators 6 Outputs" style="width:100%; max-width:740px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-elev" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Top row: left to right -->
  <rect x="20" y="40" width="180" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="110" y="68" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Sensors</text>
  <text x="110" y="86" text-anchor="middle" font-size="11.5" fill="#1e293b">(14 Inputs)</text>

  <path d="M200,75 L280,75" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-elev)"/>

  <rect x="280" y="40" width="200" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="380" y="68" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Opto-Isolators</text>
  <text x="380" y="86" text-anchor="middle" font-size="11.5" fill="#1e293b">(Signal Protection)</text>

  <path d="M480,75 L560,75" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-elev)"/>

  <rect x="560" y="40" width="180" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="650" y="68" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">PLA System</text>
  <text x="650" y="86" text-anchor="middle" font-size="11.5" fill="#1e293b">(Decision Logic)</text>

  <!-- Vertical connector from PLA System down to Output Bus -->
  <path d="M650,110 L650,150 L650,170" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-elev)"/>

  <!-- Bottom row: right to left -->
  <rect x="560" y="170" width="180" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="650" y="198" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Output Bus</text>
  <text x="650" y="216" text-anchor="middle" font-size="11.5" fill="#1e293b">(6 Signals)</text>

  <path d="M560,205 L480,205" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-elev)"/>

  <rect x="280" y="170" width="200" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="380" y="198" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Power Drivers</text>
  <text x="380" y="216" text-anchor="middle" font-size="11.5" fill="#1e293b">(Relays/VFD)</text>

  <path d="M280,205 L200,205" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-elev)"/>

  <rect x="20" y="170" width="180" height="70" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="110" y="198" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Actuators</text>
  <text x="110" y="216" text-anchor="middle" font-size="11.5" fill="#1e293b">(6 Outputs)</text>
</svg>

### 4. รายละเอียดการเชื่อมต่อฮาร์ดแวร์ (Hardware Wiring Details)

1. **การเชื่อมต่อมอเตอร์หลัก (VFD Interface):**
   - เอาต์พุต **Motor_Move_Up ($O_0$)**, **Motor_Move_Down ($O_1$)**, และ **Motor_Speed_High ($O_2$)** จะต่อเข้ากับอินพุตดิจิทัลของ **Variable Frequency Drive (VFD)**
   - VFD จะทำหน้าที่เปลี่ยนความถี่ไฟฟ้าเพื่อควบคุมมอเตอร์ 3 เฟส ให้หมุนด้วยความเร็วและทิศทางที่ PLA กำหนด
2. **ระบบเบรกความปลอดภัย (Brake Interlock):**
   - เอาต์พุต **Brake_Engage_Command ($O_3$)** จะควบคุม Magnetic Contactor ที่จ่ายไฟให้คอยล์เบรกแม่เหล็กไฟฟ้า (ปกติเบรกจะจับค้างไว้ด้วยสปริง และจะคลายเมื่อมีไฟจ่ายเข้า $O_3$ เท่านั้น — Fail-safe)
3. **การป้องกันสัญญาณรบกวน (Isolation):**
   - อินพุตทั้ง 14 ตัว จะต้องผ่าน **Opto-Isolators** ก่อนเข้า PLA เพื่อป้องกันแรงดันกระชาก (Surge) จากมอเตอร์ทำลายชิป
4. **การจดจำสถานะ (Flip-Flop Storage):**
   - ใช้ **D-Flip Flops** เก็บสถานะปัจจุบัน (Present State) และส่งกลับเข้าเป็นอินพุตของ PLA เพื่อใช้ตัดสินใจในสถานะถัดไป (Next State)

### 5. จุดเด่นของการออกแบบระดับสูงนี้

1. **Redundancy Safety:** หากมอเตอร์ร้อนจัด (`Safety_Motor_Hot`) หรือเกิดไฟไหม้ (`Safety_Fire_Alarm`) ตรรกะใน AND Array จะตัดการทำงานของมอเตอร์ทันทีโดยไม่ต้องผ่านซอฟต์แวร์
2. **Smooth Deceleration:** การแยกเอาต์พุต **Motor_Speed_High** ออกมา ช่วยให้ระบบขับเคลื่อนรู้ว่าควรชะลอความเร็วเมื่อเข้าใกล้ชั้นเป้าหมาย
3. **Logic Optimization:** การใช้ PLA ช่วยให้เราสามารถรวมเงื่อนไขความปลอดภัย 6 อย่างเข้าเป็น Product Term เดียว ($S$) แล้วนำไป "แชร์" ให้กับมอเตอร์ทุกตัวได้ ช่วยลดจำนวนเกตลงได้มหาศาล

> 💡 ตัวอย่างลิฟต์นี้คือเหตุผลที่ใช้ **PLA** แทน **PAL** — เพราะ OR Array ของ PLA โปรแกรมได้ จึงสามารถนำ Product Term เดียวกัน (เช่นเงื่อนไขความปลอดภัย) ไป "แชร์" ให้กับเอาต์พุตหลายตัว (Brake, Open, Alarm) ได้พร้อมกัน ลดความซับซ้อนของวงจรลงมาก เทียบกับ PAL ที่ต้องสร้าง Product Term ซ้ำทุกครั้งตามที่เห็นในหัวข้อ 9.8

---

## 9.11 ตารางความจริงสรุปสถานะ (Advanced Truth Table)

| สถานการณ์จำลอง | Motor_Move_Up | Motor_Move_Down | Motor_Speed_High | Brake_Engage | Door_Open | System_Alarm |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| อยู่ Floor 1 เรียก Floor 4 | 1 | 0 | 1 | 0 | 0 | 0 |
| อยู่ Floor 3 เรียก Floor 4 | 1 | 0 | 0 | 0 | 0 | 0 |
| จอดนิ่งสนิทตรงชั้นเป้าหมาย | 0 | 0 | 0 | 1 | 1 | 0 |
| น้ำหนักเกิน (ขณะจอด/วิ่ง) | 0 | 0 | 0 | 1 | 1 | 1 |
| เหตุฉุกเฉิน/ไฟไหม้/ร้อนจัด | 0 | 0 | 0 | 1 | 0 | 1 |

---

## ส่วนที่ 2: การแปลงสัญญาณ ADC/DAC และการเชื่อมต่อ (Interfacing)

## 9.12 บทนำ

ในโลกจริง สัญญาณส่วนใหญ่เป็น **แอนะล็อก** (Analog) เช่น อุณหภูมิ แสง เสียง — แต่คอมพิวเตอร์ทำงานกับ **ดิจิทัล** (Digital, 0 กับ 1) ดังนั้นต้องมีวงจร **แปลงสัญญาณ** เชื่อมสองโลกนี้เข้าด้วยกัน

```text
Analog World              Digital World
   │                          │
   │ Sensor → [ADC] ──────→  │  Processing
   │                          │  (CPU, FPGA)
   │ Actuator ← [DAC] ←───── │
   │                          │
```

> 💡 จำง่ายๆ ว่า **ADC แปลงเข้า** (Analog-to-Digital, เซนเซอร์ → ตัวประมวลผล) ส่วน **DAC แปลงออก** (Digital-to-Analog, ตัวประมวลผล → อุปกรณ์ขับเคลื่อน) ทั้งสองตัวทำงานสวนทางกันเสมอ

---

## 9.13 โปรโตคอลการสื่อสารดิจิทัลพื้นฐาน (Serial Protocols)

เมื่อต้องการนำชิปหลายๆ ตัวมาคุยกัน (เช่น ไมโครคอนโทรลเลอร์อ่านค่าจากเซนเซอร์) จะนิยมใช้บัสสื่อสารข้อมูลแบบอนุกรม (Serial Communication)

1. **UART (Universal Asynchronous Receiver-Transmitter):**
   - สื่อสาร 2 เส้น (TX, RX)
   - ไม่ต้องใช้ Clock (Asynchronous) แต่ต้องตกลงความเร็ว (Baud Rate) ให้ตรงกัน
2. **I2C (Inter-Integrated Circuit):**
   - สื่อสาร 2 เส้น (SDA, SCL) + Pull-up
   - สื่อสารแบบ Master-Slave มีระบุ Address ของอุปกรณ์
3. **SPI (Serial Peripheral Interface):**
   - สื่อสาร 4 เส้น (MOSI, MISO, SCK, CS)
   - มี Clock เป็นตัวให้จังหวะ (Synchronous) สื่อสารได้รวดเร็วมาก

> 💡 เลือกโปรโตคอลตามงาน: **UART** เหมาะกับการสื่อสารแบบจุดต่อจุดง่ายๆ (เช่น Debug Console), **I2C** เหมาะกับการต่อเซนเซอร์หลายตัวบนสาย 2 เส้นเดียวกัน, **SPI** เหมาะกับงานที่ต้องการความเร็วสูง เช่น จอแสดงผลหรือ SD Card

---

## 9.14 PWM (Pulse Width Modulation)

ในอุปกรณ์ที่ไม่มี DAC แต่อยากสร้างแรงดันแอนะล็อกเทียม จะใช้วิธี **PWM**

คือการสลับปล่อยสัญญาณดิจิทัล HIGH และ LOW ด้วยความถี่สูงมากๆ โดยปรับสัดส่วนความกว้างของขั้ว HIGH (Duty Cycle) ให้เปลี่ยนไป

- **แรงดันเฉลี่ย ($V_{avg}$)** = $V_{max} \times$ Duty Cycle
- นิยมใช้หรี่ความสว่าง LED และควบคุมความเร็วมอเตอร์

---

## 9.15 แอนะล็อก vs ดิจิทัล

| เกณฑ์ | Analog | Digital |
|:---|:---:|:---:|
| สัญญาณ | ต่อเนื่อง (Continuous) | ไม่ต่อเนื่อง (Discrete) |
| ค่าที่เป็นไปได้ | ∞ | จำกัด ($2^n$ ค่า) |
| สัญญาณรบกวน | ไวต่อ noise | **ทนทาน** ✅ |
| การประมวลผล | ยาก | ง่าย ✅ |
| ตัวอย่าง | เสียง, อุณหภูมิ, แรงดัน | ข้อมูลในคอมพิวเตอร์ |

---

## 9.16 DAC (Digital-to-Analog Converter)

### หลักการ

แปลง **รหัสดิจิทัล (binary)** เป็น **แรงดันไฟฟ้าแอนะล็อก**

$$V_{out} = V_{ref} \times \frac{D}{2^n}$$

- $V_{ref}$ = แรงดันอ้างอิง (Reference Voltage)
- $D$ = ค่าดิจิทัล (0 ถึง $2^n - 1$)
- $n$ = จำนวนบิต (Resolution)

### ตัวอย่าง: DAC 3-bit, V_ref = 8V

| Input (D₂D₁D₀) | Decimal | V_out |
|:---:|:---:|:---:|
| 000 | 0 | 0.0 V |
| 001 | 1 | 1.0 V |
| 010 | 2 | 2.0 V |
| 011 | 3 | 3.0 V |
| 100 | 4 | 4.0 V |
| 101 | 5 | 5.0 V |
| 110 | 6 | 6.0 V |
| 111 | 7 | 7.0 V |

### วงจร DAC แบบ R-2R Ladder

```text
Vref
  │
  ├──[2R]──┬──[2R]──┬──[2R]──┬──→ GND
  │        │        │        │
 [R]      [R]      [R]      [R]
  │        │        │        │
 D₃       D₂       D₁       D₀
(MSB)                      (LSB)
```

**R-2R Ladder** ใช้ตัวต้านทานเพียง 2 ค่า (R และ 2R) → ผลิตง่าย, ความแม่นยำดี

### พารามิเตอร์สำคัญ

| พารามิเตอร์ | ความหมาย |
|:---|:---|
| **Resolution** | จำนวนบิต (n) → ค่า output ที่เป็นไปได้ = $2^n$ |
| **Step Size** | ขนาดการเปลี่ยนแปลงต่อ 1 LSB = $V_{ref} / 2^n$ |
| **Full-Scale** | Output สูงสุด = $V_{ref} \times (2^n - 1) / 2^n$ |
| **Settling Time** | เวลาที่ output นิ่งหลังเปลี่ยน input |

> 💡 **Step Size** คือค่าที่ตอบคำถาม "DAC/ADC นี้ละเอียดแค่ไหน" ยิ่ง $n$ มาก Step Size ยิ่งเล็ก ยิ่งใกล้เคียงสัญญาณแอนะล็อกจริงมากขึ้น

---

## 9.17 ADC (Analog-to-Digital Converter)

### หลักการ

แปลง **แรงดันไฟฟ้าแอนะล็อก** เป็น **รหัสดิจิทัล**

### กระบวนการแปลง ADC

```text
Analog → [Sampling] → [Quantization] → [Encoding] → Digital
สัญญาณ     สุ่มตัวอย่าง    แบ่งระดับ      แปลงเป็นเลขฐาน 2
```

#### 1) Sampling (การสุ่มตัวอย่าง)

วัดค่าสัญญาณ ณ ช่วงเวลาที่แน่นอน

> **Nyquist Theorem:** อัตราสุ่มตัวอย่างต้อง ≥ 2 เท่าของความถี่สูงสุดของสัญญาณ
>
> $$f_s \geq 2 \times f_{max}$$

#### 2) Quantization (การแบ่งระดับ)

ปัดค่าที่วัดได้ให้ตรงกับระดับที่ใกล้ที่สุด

```text
V
7 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │111│
6 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │110│  ← ค่าที่ ADC ให้ได้
5 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │101│    (3-bit = 8 ระดับ)
4 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │100│
3 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │011│
2 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │010│
1 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │001│
0 ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ │000│
```

> **Quantization Error** สูงสุด = ±½ LSB

#### 3) Encoding (การเข้ารหัส)

แปลงระดับที่ได้เป็นเลข binary

### ชนิดของ ADC

| ชนิด | วิธีการ | ความเร็ว | ความแม่นยำ |
|:---|:---|:---:|:---:|
| **Flash ADC** | Comparator ขนาน ($2^n - 1$ ตัว) | **เร็วมาก** ✅ | ดี |
| **SAR ADC** | Binary search (ทีละบิต) | ปานกลาง | **ดี** ✅ |
| **Dual-Slope** | Integrate → count | ช้า | **แม่นมาก** ✅ |
| **Sigma-Delta** | Oversampling + noise shaping | ช้า | **แม่นมาก** ✅ |

### Flash ADC (3-bit ตัวอย่าง)

```text
Vin ──┬──[Comp 7]── (>7/8 Vref?)
      ├──[Comp 6]── (>6/8 Vref?)
      ├──[Comp 5]── (>5/8 Vref?)
      ├──[Comp 4]── (>4/8 Vref?)    → Priority  → Binary
      ├──[Comp 3]── (>3/8 Vref?)      Encoder      Output
      ├──[Comp 2]── (>2/8 Vref?)                   (3 bits)
      └──[Comp 1]── (>1/8 Vref?)
```

- ใช้ Comparator $2^n - 1 = 7$ ตัว สำหรับ 3-bit
- ผล Thermometer Code → Priority Encoder → Binary

> ⚠️ Flash ADC เร็วที่สุดเพราะ Comparator ทำงานพร้อมกันทั้งหมด แต่ต้องใช้ Comparator จำนวนมาก ($2^n - 1$ ตัว) — ถ้าต้องการความละเอียดสูง (n มาก) จำนวนวงจรจะเพิ่มแบบเอ็กซ์โพเนนเชียล ทำให้ไม่คุ้มสำหรับ ADC ความละเอียดสูง จึงนิยมใช้ SAR หรือ Sigma-Delta แทน

---

## 9.18 ตัวอย่างการเลือก ADC/DAC

**โจทย์:** ต้องการวัดอุณหภูมิ 0–100°C ด้วยความละเอียด 0.5°C

- ต้องแยกได้ = $100 / 0.5 = 200$ ระดับ
- จำนวนบิต: $2^n \geq 200$ → $n \geq 8$ (ใช้ **8-bit ADC**, $2^8 = 256$ ระดับ)
- ถ้า Sensor ให้ output 0–5V → Step Size = $5/256 \approx 19.5$ mV

---

## 9.19 Tinkercad: สร้างวงจรดิจิทัลจำลอง

### Tinkercad คืออะไร?

**Tinkercad Circuits** (circuits.tinkercad.com) เป็นเครื่องมือจำลองวงจรออนไลน์ ฟรี โดย Autodesk

### ขั้นตอนการใช้งาน

1. **สร้างบัญชี** ที่ [tinkercad.com](https://www.tinkercad.com)
2. เลือก **Circuits** → **Create new Circuit**
3. ลากชิ้นส่วนจากแถบด้านขวา
4. **ต่อสาย** โดยคลิกที่ขาแล้วลากไปอีกขา
5. กด **Start Simulation** เพื่อทดสอบ

### ชิ้นส่วนที่ใช้บ่อย

| ชิ้นส่วน | หน้าที่ | ตัวอย่าง IC |
|:---|:---|:---:|
| Logic Gate IC | เกตลอจิก | 7408 (AND), 7432 (OR), 7404 (NOT) |
| LED + Resistor | แสดงผล output | — |
| Switch / Push Button | ใส่ input | — |
| 7-Segment Display | แสดงตัวเลข | ใช้กับ 4511 (BCD decoder) |
| Flip-Flop IC | หน่วยความจำ 1 บิต | 7473 (JK), 7474 (D) |
| Arduino | Microcontroller | — |
| Breadboard | ต่อวงจร prototype | — |

### ตัวอย่างโปรเจกต์ที่ทำได้

1. **ต่อวงจรเกตพื้นฐาน** — AND, OR, NOT ด้วย IC 7408, 7432, 7404
2. **วงจร Half/Full Adder** — ใช้ XOR (7486) + AND (7408)
3. **วงจร 7-Segment Decoder** — BCD input → 4511 → 7-Segment Display
4. **วงจร Counter** — JK FF (7473) ต่อเป็น Ripple Counter
5. **วงจร FSM อย่างง่าย** — D FF + Logic Gates

### เคล็ดลับ Tinkercad

| ปัญหา | วิธีแก้ |
|:---|:---|
| LED ไม่ติด | ตรวจสอบ: ต่อ Resistor (220Ω–1kΩ) แล้วหรือยัง? |
| Output ไม่ถูกต้อง | ตรวจสอบ: ต่อ VCC (+5V) และ GND ให้ IC แล้วหรือยัง? |
| สัญญาณลอย | ต่อ Pull-up/Pull-down resistor ที่ input ที่ไม่ได้ใช้ |
| จำลองช้า | ลดจำนวนชิ้นส่วน หรือปิด animation |

---

## 9.20 การอ่าน Data Sheet (ทบทวน)

### ข้อมูลสำคัญใน Data Sheet

| หัวข้อ | สิ่งที่ต้องดู |
|:---|:---|
| **Pin Diagram** | ขาไหนเป็นอะไร (Input, Output, VCC, GND) |
| **Function Table** | Truth Table / ตารางการทำงาน |
| **Absolute Maximum Ratings** | ค่าสูงสุดที่รับได้ (ห้ามเกิน!) |
| **Recommended Operating Conditions** | VCC, Input Voltage, Temperature ที่ควรใช้ |
| **Propagation Delay** | เวลาหน่วง (tpLH, tpHL) |
| **Fan-out** | จำนวนเกตที่ต่อ output ได้ |

### ตัวอย่าง IC ที่ใช้ในวิชานี้

| IC | ฟังก์ชัน | จำนวนเกต |
|:---:|:---|:---:|
| **7408** | Quad 2-input AND | 4 |
| **7432** | Quad 2-input OR | 4 |
| **7404** | Hex Inverter (NOT) | 6 |
| **7486** | Quad 2-input XOR | 4 |
| **7400** | Quad 2-input NAND | 4 |
| **7402** | Quad 2-input NOR | 4 |
| **7473** | Dual JK Flip-Flop | 2 |
| **7474** | Dual D Flip-Flop | 2 |
| **74138** | 3-to-8 Decoder | 1 |
| **74151** | 8-to-1 MUX | 1 |
| **4511** | BCD to 7-Segment | 1 |

> ⚠️ ก่อนต่อวงจรจริงทุกครั้ง ต้องเช็ก **Absolute Maximum Ratings** ก่อนเสมอ — การจ่ายแรงดันหรือกระแสเกินค่านี้แม้เพียงชั่วขณะอาจทำให้ชิปเสียหายถาวร

---

---

## 9.21 ตัวอย่างการนำไปใช้งานจริง (Real-world Interfacing Applications)

### 9.21.1 ระบบวัดอุณหภูมิดิจิทัล (Digital Temperature Monitor)

**โครงสร้างระบบ (System Structure):**

<svg viewBox="0 0 760 200" role="img" aria-label="ระบบวัดอุณหภูมิดิจิทัล: LM35 Sensor ส่งแรงดันแอนะล็อกไป 8-bit ADC แปลงเป็นไบนารีส่งให้ Processor แปลงเป็น BCD ส่งให้ 4511 Decoder ส่งสาย a ถึง g ไป 7-Segment" style="width:100%; max-width:740px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-temp" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- LM35 Sensor -->
  <rect x="20" y="30" width="150" height="60" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="95" y="65" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">LM35 Sensor</text>

  <path d="M170,60 L290,60" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-temp)"/>
  <text x="230" y="48" text-anchor="middle" font-size="11.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">(Analog V)</text>

  <!-- 8-bit ADC -->
  <rect x="290" y="30" width="150" height="60" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="365" y="65" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">8-bit ADC</text>

  <path d="M440,60 L560,60" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-temp)"/>
  <text x="500" y="48" text-anchor="middle" font-size="11.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">(Binary)</text>

  <!-- Processor -->
  <rect x="560" y="30" width="170" height="60" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="645" y="65" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Processor</text>

  <!-- vertical connector down to 4511 Decoder -->
  <path d="M645,90 L645,120 L645,140" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-temp)"/>
  <text x="700" y="118" text-anchor="middle" font-size="11.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">(BCD)</text>

  <!-- 4511 Decoder -->
  <rect x="560" y="140" width="170" height="60" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="645" y="175" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">4511 Decoder</text>

  <path d="M560,170 L150,170" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-temp)"/>
  <text x="355" y="188" text-anchor="middle" font-size="11.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">(a-g lines)</text>

  <!-- 7-Segment -->
  <rect x="20" y="140" width="130" height="60" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="85" y="175" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">7-Segment</text>
</svg>

**ตารางความสัมพันธ์ของข้อมูล (Data Mapping):**

| อุณหภูมิ (°C) | แรงดัน Sensor (V) | ค่าดิจิทัล (8-bit) | การแสดงผล (7-Seg) |
|:---:|:---:|:---:|:---:|
| 0 | 0.00 | 0000 0000 | 0 |
| 25 | 0.25 | 0100 0000 | 25 |
| 100 | 1.00 | 1111 1111 | 99* |

*\*หมายเหตุ: หากใช้ 8-bit ADC เต็มสเกล 5V ค่า 1V จะได้ประมาณ 51 ในฐานสิบ ระบบต้องมีการ Scaling*

> ⚠️ จากหมายเหตุข้างต้น สังเกตว่าค่าดิจิทัลสูงสุด (`1111 1111` = 255) ไม่ได้แปลตรงๆ เป็น 100°C — นี่คือเหตุผลที่ระบบเซนเซอร์จริงต้องมีวงจรหรือซอฟต์แวร์ **Scaling** เพื่อแปลงค่า ADC ดิบให้ตรงกับสเกลอุณหภูมิที่ต้องการแสดงผล

### 9.21.2 ระบบควบคุมความเร็วมอเตอร์ (PWM Speed Control)

**โครงสร้างระบบ (System Structure):**

<svg viewBox="0 0 760 200" role="img" aria-label="ระบบควบคุมความเร็วมอเตอร์ด้วย PWM: Digital Logic ส่งพัลส์ PWM ไป Opto-Isolator ไป MOSFET Driver ไปขับ DC Motor" style="width:100%; max-width:740px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-pwm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Digital Logic -->
  <rect x="20" y="30" width="170" height="60" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="105" y="65" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Digital Logic</text>

  <path d="M190,60 L310,60" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pwm)"/>
  <text x="250" y="48" text-anchor="middle" font-size="11.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">(PWM Pulse)</text>

  <!-- Opto-Isolator -->
  <rect x="310" y="30" width="170" height="60" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="395" y="65" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Opto-Isolator</text>

  <path d="M480,60 L600,60" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pwm)"/>

  <!-- MOSFET Driver -->
  <rect x="600" y="30" width="150" height="60" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="675" y="65" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">MOSFET Driver</text>

  <!-- connector down to DC Motor -->
  <path d="M675,90 L675,130 L675,150" fill="none" stroke="#475569" stroke-width="2"/>
  <path d="M675,150 L105,150" fill="none" stroke="#475569" stroke-width="2"/>
  <path d="M105,150 L105,140" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-pwm)"/>

  <!-- DC Motor -->
  <rect x="20" y="140" width="170" height="60" rx="8" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
  <text x="105" y="175" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">DC Motor</text>
</svg>

**ตารางควบคุมความเร็ว (Duty Cycle Table):**

| Duty Cycle (%) | แรงดันเฉลี่ย ($V_{avg}$) | สถานะมอเตอร์ |
|:---:|:---:|:---|
| 0 | 0 V | หยุดนิ่ง |
| 25 | 1.25 V | หมุนช้า |
| 50 | 2.50 V | ความเร็วปานกลาง |
| 100 | 5.00 V | ความเร็วสูงสุด |

> 💡 ทั้งสองระบบในหัวข้อนี้ใช้สถาปัตยกรรมแบบเดียวกันคือ **เซนเซอร์/ตรรกะ → วงจรแยกสัญญาณ (Isolation) → วงจรขับกำลัง (Driver) → อุปกรณ์จริง (Actuator)** ลองสังเกตว่าหลักการ "แยกสัญญาณก่อนขับกำลังสูง" นี้ซ้ำกับระบบลิฟต์ในหัวข้อ 9.10 ด้วย — เป็นรูปแบบมาตรฐานของการอินเตอร์เฟซวงจรดิจิทัลกับโลกจริง

</div>

<div class="chapter-tab-content" data-tab-name="Interactive Sim" data-tab-icon="🎮" id="sim" markdown="1">

## Interactive Simulators (ห้องทดลองหน่วยความจำและการแปลงสัญญาณ)

เครื่องมือจำลองเหล่านี้ออกแบบมาเพื่อช่วยสร้างความเข้าใจผ่านการโต้ตอบและลงมือเล่น (Simulate-First)

### 1. เครื่องมือจำลองหน่วยความจำแรม (RAM Array Simulator)
ทดลองคลิกสลับบิตข้อมูล 0/1 และระบุตำแหน่งแอดเดรส (000 - 111) เพื่อเขียน (Write) และอ่าน (Read) ข้อมูลเข้า/ออกจากตัวเก็บข้อมูลหน่วยความจำ RAM 8x8 บิตจริง:

{% include ram-sim.html %}

---

### 2. ลิงก์สู่เครื่องมือแปลงสัญญาณภายนอก (Circuit Playgrounds)
- [Tinkercad Circuits - DAC R-2R Resistor Ladder Simulation](https://www.tinkercad.com/) (ทดลองสร้างวงจรแปลงดิจิทัลเป็นแอนะล็อกด้วยตัวต้านทาน R-2R บน Tinkercad เพื่อควบคุมแรงดันเอาต์พุต)

</div>

<div class="chapter-tab-content" data-tab-name="Waveform / Truth Table" data-tab-icon="📊" id="waveform" markdown="1">

## Reference Tables (ตารางสรุปโปรโตคอลและการจัดการที่อยู่)

ตารางสรุปและแผ่นอ้างอิงคุณสมบัติสำหรับหน่วยความจำและการสื่อสาร:

### 1. เปรียบเทียบ SRAM vs DRAM

| คุณสมบัติ | Static RAM (SRAM) | Dynamic RAM (DRAM) |
|---|---|---|
| **โครงสร้างเซลล์** | ใช้ฟลิปฟลอป (6 Transistors) | ใช้ตัวเก็บประจุ (1 Transistor + 1 Cap) |
| **ความเร็ว** | เร็วมาก (มักใช้เป็น Cache) | ช้ากว่า (มักใช้เป็น RAM หลัก) |
| **การ Refresh** | ไม่ต้องการการรีเฟรชตราบใดที่มีไฟเลี้ยง | ต้องทำการรีเฟรชข้อมูลตลอดเวลา (เพราะประจุรั่วไหล) |
| **ความหนาแน่น/ราคา** | ความหนาแน่นต่ำ / ราคาสูงกว่า | ความหนาแน่นสูงมาก / ราคาถูกกว่า |

---

### 2. ตารางการทำงานของโปรโตคอล Serial (UART, SPI, I2C)

| คุณสมบัติ | UART | SPI | I2C |
|---|---|---|---|
| **ประเภทสายสัญญาณ** | Asynchronous | Synchronous | Synchronous |
| **จำนวนสาย (Wires)** | 2 เส้น (TX, RX) | 4 เส้น (SCLK, MOSI, MISO, SS) | 2 เส้น (SDA, SCL) |
| **ความเร็ว** | ช้าสุด | เร็วที่สุด | ปานกลาง |
| **โหมดการเชื่อมต่อ** | Point-to-Point (1 ต่อ 1) | Multi-device (มีสาย SS แยก) | Multi-master/Multi-slave (ใช้แอดเดรส) |

</div>

<div class="chapter-tab-content" data-tab-name="Challenge" data-tab-icon="🏆" id="challenge" markdown="1">

## แบบฝึกหัดท้ายบท

### 📅 ส่วนที่ 1 — หน่วยความจำและอุปกรณ์ลอจิกโปรแกรมได้ (Memory & PLD)

1. หน่วยความจำขนาด 16K x 16 บิต จะมี Address Bus และ Data Bus กี่เส้น?
2. จงคำนวณหาที่อยู่สุดท้าย (Ending Address) ของชิป 4KB หากที่อยู่เริ่มต้นคือ 2000h
3. จงอธิบายความแตกต่างระหว่าง Static RAM และ Dynamic RAM ในแง่ของความเร็วและราคา
4. อุปกรณ์ PAL แตกต่างจาก PLA อย่างไร?
5. เพราะเหตุใด NOR Flash ถึงเหมาะสำหรับการเก็บชุดคำสั่งโปรแกรม (Firmware) มากกว่า NAND Flash?
6. ออกแบบวงจร Address Decoder อย่างง่ายเพื่อเลือกชิป 2 ตัวในระบบ 16-bit address โดยใช้เกตลอจิกพื้นฐาน

### 📅 ส่วนที่ 2 — การแปลงสัญญาณและการเชื่อมต่อ (ADC/DAC & Interfacing)

7. DAC 4-bit มี V_ref = 10V — จงคำนวณ Step Size และ V_out เมื่อ Input = 1010₂
8. ต้องการวัดแรงดัน 0–3.3V ด้วยความละเอียด 10 mV → ต้องใช้ ADC กี่บิต?
9. อธิบายข้อดีข้อเสียของ Flash ADC เทียบกับ SAR ADC
10. สร้างวงจร Full Adder บน Tinkercad โดยใช้ IC 7486 (XOR) และ 7408 (AND) และ 7432 (OR) — Capture ภาพผลลัพธ์
11. สร้างวงจร 2-bit Counter บน Tinkercad โดยใช้ IC 7473 (JK FF) — ต่อเป็น Ripple Counter แสดงผลด้วย LED

</div>
</content>
