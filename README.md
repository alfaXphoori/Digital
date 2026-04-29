# Digital Logic — วิศวกรรมคอมพิวเตอร์

## แผนการสอน (17 สัปดาห์)

| สัปดาห์ที่ | หัวข้อการเรียน | รายละเอียดเนื้อหา | ไฟล์อ้างอิง | Lab (ปฏิบัติ ~1 ชม.) |
|:---:|:---|:---|:---|:---|
| **1** | **Introduction & Number Systems** | แนะนำรายวิชา, ระบบเลขฐาน (2, 8, 10, 16), การแปลงเลขฐาน, การบวก/ลบเลขฐานสอง | [Number Systems](chapters/ch01-number-systems/) | 🔬 [**Lab 1:** แปลงเลขฐาน 2↔8↔10↔16, บวก/ลบเลขฐานสอง (worksheet) + สมัคร Tinkercad](labs/lab01-number-systems.md) |
| **2** | **Digital Codes & Error Detection** | รหัส BCD, ASCII, Gray Code, Excess-3, บิตพาริตี (Parity Bit) และหลักการตรวจจับข้อผิดพลาดเบื้องต้น | [Number Systems](chapters/ch01-number-systems/) | 🔬 [**Lab 2:** เข้ารหัส BCD / Gray Code / Parity จากข้อความจริง + ตรวจจับ error](labs/lab02-digital-codes.md) |
| **3** | **Logic Gates & Digital ICs** | พื้นฐานเกต (AND, OR, NOT, NAND, NOR, XOR), ตารางความจริง, แนะนำ Data Sheet และตระกูล IC | [Logic Gates](chapters/ch02-logic-gates/) | 🔬 [**Lab 3:** ต่อวงจร AND (7408), OR (7432), NOT (7404) บน Tinkercad — ตรวจสอบ Truth Table ด้วย LED](labs/lab03-logic-gates.md) |
| **4** | **Boolean Algebra & Theorems** | พีชคณิตบูลีน, ทฤษฎีเดอมอร์แกน (DeMorgan's Theorem), การลดรูปสมการลอจิกเบื้องต้น | [Boolean Algebra](chapters/ch03-boolean-algebra/) | 🔬 [**Lab 4:** พิสูจน์ DeMorgan's Theorem บน Tinkercad — ต่อ $\overline{AB}$ vs $\bar{A}+\bar{B}$ เทียบผล LED](labs/lab04-demorgan.md) |
| **5** | **Karnaugh Maps (K-Maps)** | การลดรูปสมการด้วย K-Map (2, 3 และ 4 ตัวแปร), สภาวะแคร์/ไม่แคร์ (Don't Care Conditions) | [Karnaugh Maps](chapters/ch04-karnaugh-maps/) | 🔬 [**Lab 5:** ลดรูปฟังก์ชัน 4 ตัวแปรด้วย K-Map แล้วต่อวงจรจริงบน Tinkercad เปรียบเทียบก่อน/หลังลดรูป](labs/lab05-kmap.md) |
| **6** | **Combinational Logic I** | การออกแบบวงจรเชิงผสม: วงจรบวก (Half/Full Adder), วงจรลบ (Subtractor), วงจรเปรียบเทียบ | [Combinational Circuits](chapters/ch05-combinational-circuits/) | 🔬 [**Lab 6:** ต่อ Half Adder + Full Adder บน Tinkercad ด้วย 7486 (XOR) + 7408 (AND) + 7432 (OR)](labs/lab06-adder.md) |
| **7** | **Combinational Logic II** | ตัวเข้ารหัส (Encoder), ตัวถอดรหัส (Decoder), มัลติเพล็กเซอร์ (MUX), ดีมัลติเพล็กเซอร์ (DEMUX) | [Combinational Circuits](chapters/ch05-combinational-circuits/) | 🔬 [**Lab 7:** ต่อวงจร BCD → 7-Segment Display ด้วย IC 4511 บน Tinkercad — แสดงเลข 0–9](labs/lab07-7segment.md) |
| **8** | **📝 สอบกลางภาค (Midterm Exam)** | **ทดสอบความรู้สัปดาห์ที่ 1 - 7 (วงจรเชิงผสม)** | - | — |
| **9** | **Intro to Sequential Logic & Latches**| แนวคิดของวงจรเชิงลำดับ, วงจร Latch (SR, D), ความแตกต่างระหว่าง Latch กับ Flip-Flop | [Flip-Flops](chapters/ch06-flip-flops/) | 🔬 [**Lab 8:** ต่อ SR Latch จาก NAND gate (7400) บน Tinkercad — ทดสอบ Set/Reset/Forbidden state](labs/lab08-sr-latch.md) |
| **10** | **Flip-Flops & Timing Diagrams** | ฟลิปฟลอป (SR, D, JK, T), การทำงานด้วยสัญญาณนาฬิกา, การอ่าน Timing Diagram | [Flip-Flops](chapters/ch06-flip-flops/) | 🔬 [**Lab 9:** ต่อ JK FF (7473) บน Tinkercad — ทดสอบ Toggle, วาด Timing Diagram จากผลจริง](labs/lab09-jk-flipflop.md) |
| **11** | **Counters** | ตัวนับแบบ Async (Ripple) และ Sync, ตัวนับขึ้น/ลง (Up/Down), MOD-N Counter | [Counters & Registers](chapters/ch07-counters-registers/) | 🔬 [**Lab 10:** ต่อ 2-bit Ripple Counter ด้วย 7473 (JK FF) แสดงผล LED — นับ 0→3 วนซ้ำ](labs/lab10-ripple-counter.md) |
| **12** | **Shift Registers** | รีจิสเตอร์เลื่อนข้อมูล (SISO, SIPO, PISO, PIPO), Ring/Johnson Counter, การประยุกต์ใช้งาน | [Counters & Registers](chapters/ch07-counters-registers/) | 🔬 [**Lab 11:** ต่อ 4-bit SIPO Shift Register ด้วย 7474 (D FF) — ป้อนข้อมูล serial แสดงผล LED 4 ดวง](labs/lab11-shift-register.md) |
| **13** | **FSM I — State Diagram & State Table** | แนวคิด Finite State Machine, Moore vs Mealy Machine, การวาด State Diagram และสร้าง State Table | [FSM](chapters/ch09-fsm/) | 🔬 [**Lab 12:** ออกแบบ FSM ไฟจราจร 3 สถานะ (R→G→Y) — วาด State Diagram + สร้าง State Table (worksheet)](labs/lab12-fsm-design.md) |
| **14** | **FSM II — Design & Implementation** | การเลือก Flip-Flop, Excitation Table, ลดรูปด้วย K-Map, วาดวงจร, ตัวอย่าง Sequence Detector | [FSM](chapters/ch09-fsm/) | 🔬 [**Lab 13:** ต่อวงจร FSM ไฟจราจรจาก Lab 12 บน Tinkercad — ใช้ D FF + Logic Gates ขับ LED 3 สี](labs/lab13-fsm-implementation.md) |
| **15** | **Memory Devices & PLD** | ชนิดของหน่วยความจำ (RAM, ROM, EEPROM), สถาปัตยกรรมของ PLD, CPLD และพื้นฐาน FPGA | [Memory & PLD](chapters/ch08-memory-pld/) | 🔬 [**Lab 14:** ใช้ ROM (Truth Table) สร้าง Full Adder บน Tinkercad — เขียน content ของ ROM แล้วทดสอบ](labs/lab14-rom-logic.md) |
| **16** | **Digital Interfacing & Mini-Project Prep**| การเชื่อมต่อโลกแอนะล็อก (ADC/DAC เบื้องต้น), ทบทวนการใช้โปรแกรม Tinkercad เพื่อต่อวงจร | [Digital Interfacing](chapters/ch10-digital-interfacing/) | 🔬 [**Lab 15:** Mini-Project — ต่อวงจร Counter + 7-Segment Display (7473 + 7408 + 7432 + 4511) ครบวงจร](labs/lab15-mini-project.md) |
| **17** | **🚀 นำเสนอโปรเจกต์ & สอบปลายภาค** | **ทดสอบความรู้สัปดาห์ที่ 9 - 15 และการปฏิบัติการต่อวงจร** | [summary.md](chapters/summary.md) | 🎤 **นำเสนอ Mini-Project + สอบปฏิบัติต่อวงจร** |

---

## 🎯 Learning Outcomes (เป้าหมายการเรียนรู้)

เมื่อจบวิชานี้ นักศึกษาจะสามารถ:
1. เข้าใจระบบเลขฐานและรหัสดิจิทัลที่ใช้ในคอมพิวเตอร์
2. ออกแบบและลดรูปวงจรลอจิกเชิงผสม (Combinational Logic) ได้อย่างมีประสิทธิภาพ
3. ออกแบบและวิเคราะห์วงจรลอจิกเชิงลำดับ (Sequential Logic) เช่น ตัวนับและรีจิสเตอร์
4. เข้าใจสถาปัตยกรรมของหน่วยความจำและอุปกรณ์ลอจิกโปรแกรมได้ (PLD/FPGA)
5. ต่อวงจรดิจิทัลจริงบน Breadboard และใช้ Simulator ในการทดสอบวงจรได้

---

## 📚 หนังสืออ้างอิง (Recommended Textbooks)

- **Digital Fundamentals** (11th Edition) — Thomas L. Floyd
- **Digital Design** (6th Edition) — M. Morris Mano & Michael D. Ciletti
- **Digital Systems: Principles and Applications** — Ronald J. Tocci

---

## 🛠️ Simulator ที่ใช้ในวิชา

| Simulator | ลิงก์ | ใช้สำหรับ |
|:---|:---|:---|
| **Tinkercad Circuits** | [tinkercad.com/circuits](https://www.tinkercad.com/circuits) | ต่อวงจร IC จริง (7408, 7432, 7473, 4511), Lab หลักของวิชา |
| **CircuitVerse** | [circuitverse.org](https://circuitverse.org/) | วาด Logic Gate ลาก-วาง, เหมาะ Lab สัปดาห์ 1–7 |
| **Logisim Evolution** | [github.com/logisim-evolution](https://github.com/logisim-evolution/logisim-evolution/releases) | ออกแบบ FSM, Counter, Memory (Desktop App) |
| **Falstad Circuit Sim** | [falstad.com/circuit](https://www.falstad.com/circuit/) | จำลองวงจรแบบเห็นกระแสไหล animation |

---

