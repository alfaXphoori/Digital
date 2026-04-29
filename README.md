# Digital Logic Design — การออกแบบลอจิกดิจิทัล

วิชานี้ครอบคลุมตั้งแต่พื้นฐานระบบเลขฐานสอง ไปจนถึงการออกแบบวงจรดิจิทัลที่ซับซ้อน เช่น เครื่องจักรสถานะจำกัด (FSM) และการเชื่อมต่อกับอุปกรณ์จริง โดยแบ่งการเรียนการสอนออกเป็น 4 เฟสหลัก เพื่อให้นักศึกษาเห็นภาพรวมและเข้าใจการต่อยอดความรู้ได้อย่างเป็นระบบ

---

## 🟢 เฟสที่ 1: ปูพื้นฐานระบบดิจิทัล (Foundation of Digital Systems)
*เป้าหมาย: เข้าใจภาษาของคอมพิวเตอร์และชิ้นส่วนฮาร์ดแวร์พื้นฐานที่สุด*

| สัปดาห์ที่ | หัวข้อการเรียน | รายละเอียดเนื้อหา | ไฟล์อ้างอิง | Lab (ปฏิบัติ ~1 ชม.) |
|:---:|:---|:---|:---|:---|
| **1** | **Introduction & Number Systems** | แนะนำรายวิชา, ระบบเลขฐาน (2, 8, 10, 16), การแปลงเลขฐาน, การบวก/ลบเลขฐานสอง | [Chapter 1](chapters/ch01-number-systems/) | 🔬 [**Lab 1:** แปลงเลขฐาน 2↔8↔10↔16, บวก/ลบเลขฐานสอง + สมัคร Tinkercad](labs/lab01-number-systems.md) |
| **2** | **Digital Codes & Error Detection** | รหัส BCD, ASCII, Gray Code, Excess-3, บิตพาริตี (Parity Bit) และหลักการตรวจจับข้อผิดพลาด | [Chapter 1](chapters/ch01-number-systems/) | 🔬 [**Lab 2:** เข้ารหัส BCD / Gray Code / Parity จากข้อความจริง + ตรวจจับ error](labs/lab02-digital-codes.md) |
| **3** | **Logic Gates & Digital ICs** | พื้นฐานเกต (AND, OR, NOT, NAND, NOR, XOR), ตารางความจริง, แนะนำ Data Sheet และตระกูล IC | [Chapter 2](chapters/ch02-logic-gates/) | 🔬 [**Lab 3:** ต่อวงจรเกตพื้นฐานบน Tinkercad — ตรวจสอบ Truth Table ด้วย LED](labs/lab03-logic-gates.md) |

---

## 🟡 เฟสที่ 2: การออกแบบวงจรเชิงผสม (Combinational Logic Design)
*เป้าหมาย: สร้างวงจรที่ไม่มีความจำ เอาต์พุตตอบสนองตามอินพุตทันที (Math & Data Routing)*

| สัปดาห์ที่ | หัวข้อการเรียน | รายละเอียดเนื้อหา | ไฟล์อ้างอิง | Lab (ปฏิบัติ ~1 ชม.) |
|:---:|:---|:---|:---|:---|
| **4** | **Boolean Algebra & Theorems** | พีชคณิตบูลีน, ทฤษฎีเดอมอร์แกน (DeMorgan's Theorem), การลดรูปสมการลอจิกเบื้องต้น | [Chapter 3](chapters/ch03-boolean-algebra/) | 🔬 [**Lab 4:** พิสูจน์ DeMorgan's Theorem บน Tinkercad — เทียบผลลัพธ์ผ่าน LED](labs/lab04-demorgan.md) |
| **5** | **Karnaugh Maps (K-Maps)** | การลดรูปสมการด้วย K-Map (2, 3 และ 4 ตัวแปร), สภาวะแคร์/ไม่แคร์ (Don't Care Conditions) | [Chapter 4](chapters/ch04-karnaugh-maps/) | 🔬 [**Lab 5:** ลดรูปฟังก์ชัน 4 ตัวแปรด้วย K-Map แล้วต่อวงจรเปรียบเทียบก่อน/หลังลดรูป](labs/lab05-kmap.md) |
| **6** | **Combinational Logic I** | วงจรคำนวณทางคณิตศาสตร์: วงจรบวก (Half/Full Adder), วงจรลบ (Subtractor), วงจรเปรียบเทียบ | [Chapter 5](chapters/ch05-combinational-circuits/) | 🔬 [**Lab 6:** ต่อ Half Adder + Full Adder บน Tinkercad ด้วย IC พื้นฐาน](labs/lab06-adder.md) |
| **7** | **Combinational Logic II** | วงจรจัดการข้อมูล: ตัวเข้ารหัส (Encoder), ตัวถอดรหัส (Decoder), มัลติเพล็กเซอร์ (MUX, DEMUX) | [Chapter 5](chapters/ch05-combinational-circuits/) | 🔬 [**Lab 7:** ต่อวงจร BCD → 7-Segment Display ด้วย IC 4511 บน Tinkercad](labs/lab07-7segment.md) |
| **8** | **📝 สอบกลางภาค (Midterm Exam)** | **ทดสอบความรู้สัปดาห์ที่ 1 - 7 (เฟส 1 และ 2)** | - | — |

---

## 🟠 เฟสที่ 3: การออกแบบวงจรเชิงลำดับ (Sequential Logic Design)
*เป้าหมาย: สร้างวงจรที่มี "ความจำ (Memory)" และการทำงานเป็นจังหวะตามสัญญาณนาฬิกา (Clock)*

| สัปดาห์ที่ | หัวข้อการเรียน | รายละเอียดเนื้อหา | ไฟล์อ้างอิง | Lab (ปฏิบัติ ~1 ชม.) |
|:---:|:---|:---|:---|:---|
| **9** | **Intro to Sequential Logic & Latches**| แนวคิดวงจรเชิงลำดับ, วงจร Latch (SR, D), ความแตกต่างระหว่าง Latch กับ Flip-Flop | [Chapter 6](chapters/ch06-flip-flops/) | 🔬 [**Lab 8:** ต่อ SR Latch จาก NAND gate (7400) บน Tinkercad — ทดสอบสถานะ](labs/lab08-sr-latch.md) |
| **10** | **Flip-Flops & Timing Diagrams** | ฟลิปฟลอป (SR, D, JK, T), การทำงานด้วยสัญญาณนาฬิกา (Edge-triggered), Timing Diagram | [Chapter 6](chapters/ch06-flip-flops/) | 🔬 [**Lab 9:** ต่อ JK FF (7473) บน Tinkercad — ทดสอบ Toggle, วาด Timing Diagram](labs/lab09-jk-flipflop.md) |
| **11** | **Counters** | ตัวนับแบบ Async (Ripple) และ Sync, ตัวนับขึ้น/ลง (Up/Down), การออกแบบ MOD-N Counter | [Chapter 7](chapters/ch07-counters-registers/) | 🔬 [**Lab 10:** ต่อ 2-bit Ripple Counter ด้วย 7473 (JK FF) แสดงผลการนับด้วย LED](labs/lab10-ripple-counter.md) |
| **12** | **Shift Registers** | รีจิสเตอร์เลื่อนข้อมูล (SISO, SIPO, PISO, PIPO), Ring Counter, Johnson Counter | [Chapter 7](chapters/ch07-counters-registers/) | 🔬 [**Lab 11:** ต่อ 4-bit SIPO Shift Register ด้วย 7474 (D FF) — ป้อนข้อมูล serial](labs/lab11-shift-register.md) |
| **13** | **FSM I — State Diagram & Table** | แนวคิด Finite State Machine, Moore vs Mealy Machine, การวาด State Diagram และสร้างตาราง | [Chapter 9](chapters/ch09-fsm/) | 🔬 [**Lab 12:** ออกแบบ FSM ไฟจราจร 3 สถานะ (R→G→Y) — (worksheet)](labs/lab12-fsm-design.md) |
| **14** | **FSM II — Implementation** | การเลือก Flip-Flop, Excitation Table, ลดรูปด้วย K-Map, วาดวงจร, Sequence Detector | [Chapter 9](chapters/ch09-fsm/) | 🔬 [**Lab 13:** ต่อวงจร FSM ไฟจราจรจาก Lab 12 บน Tinkercad เพื่อขับ LED 3 สี](labs/lab13-fsm-implementation.md) |

---

## 🔴 เฟสที่ 4: สถาปัตยกรรมระบบและการเชื่อมต่อโลกจริง (System Architecture & Real-world)
*เป้าหมาย: ต่อยอดสู่ระบบสถาปัตยกรรมชิป การแปลงสัญญาณ และการประยุกต์ใช้งานเพื่อเตรียมพร้อมสู่วิชาไมโครคอนโทรลเลอร์*

| สัปดาห์ที่ | หัวข้อการเรียน | รายละเอียดเนื้อหา | ไฟล์อ้างอิง | Lab (ปฏิบัติ ~1 ชม.) |
|:---:|:---|:---|:---|:---|
| **15** | **Memory Devices & PLD** | ชนิดของหน่วยความจำ (RAM, ROM), สถาปัตยกรรม PLD (PLA, PAL), CPLD และพื้นฐาน FPGA | [Chapter 8](chapters/ch08-memory-pld/) | 🔬 [**Lab 14:** ใช้ ROM สร้างวงจร Full Adder บน Tinkercad — ป้อน Truth table ลง ROM](labs/lab14-rom-logic.md) |
| **16** | **Digital Interfacing & Mini-Project**| การเชื่อมต่อไฟฟ้าต่างระดับ, หลักการแปลงสัญญาณ ADC/DAC, บูรณาการสร้าง Mini-Project | [Chapter 10](chapters/ch10-digital-interfacing/) | 🔬 [**Lab 15:** Mini-Project — ต่อวงจร Counter + 7-Segment Display แบบครบวงจร](labs/lab15-mini-project.md) |
| **17** | **🚀 นำเสนอโปรเจกต์ & สอบปลายภาค** | **ทดสอบความรู้สัปดาห์ที่ 9 - 16 และการปฏิบัติการต่อวงจร** | [Summary](chapters/summary.md) | 🎤 **นำเสนอ Mini-Project + สอบปฏิบัติต่อวงจร** |

---

## 🛠️ เครื่องมือและ Simulator ที่ใช้ในวิชา

เพื่อให้เห็นภาพการทำงานของกระแสไฟฟ้าและลอจิกเกตอย่างชัดเจน วิชานี้จะใช้เครื่องมือจำลอง (Simulator) แทน/ควบคู่ กับการต่อวงจรบน Breadboard จริง:

| Simulator | ลิงก์ | เหมาะสำหรับ |
|:---|:---|:---|
| **Tinkercad Circuits** | [tinkercad.com/circuits](https://www.tinkercad.com/circuits) | (เครื่องมือหลัก) จำลองการต่อสายไฟบน Breadboard จริงด้วย IC เบอร์ 74xx |
| **CircuitVerse** | [circuitverse.org](https://circuitverse.org/) | วาดวงจรลอจิกแบบ Block (ลาก-วาง) เหมาะกับบทที่ 1–7 ที่เน้นสมการ |
| **Logisim Evolution** | [github.com/logisim-evolution](https://github.com/logisim-evolution/logisim-evolution/releases) | ออกแบบระบบใหญ่ เช่น FSM, Counter, Memory (โปรแกรม Desktop) |
| **Falstad Circuit Sim** | [falstad.com/circuit](https://www.falstad.com/circuit/) | จำลองวงจรระดับทรานซิสเตอร์ ดูการไหลของกระแสไฟและแรงดัน |