# 📟 Digital Logic & Computer Architecture — วิศวกรรมคอมพิวเตอร์

ยินดีต้อนรับสู่คลังบทเรียนวิชา **Digital Logic** เนื้อหาชุดนี้ถูกออกแบบมาสำหรับนักศึกษาวิศวกรรมคอมพิวเตอร์ โดยครอบคลุมตั้งแต่พื้นฐานระบบเลขฐานไปจนถึงสถาปัตยกรรมหน่วยความจำและการออกแบบระบบควบคุมอัตโนมัติ (FSM)

---

## 🎯 Learning Outcomes (เป้าหมายการเรียนรู้)

เมื่อจบวิชานี้ นักศึกษาจะสามารถ:
1. **วิเคราะห์และคำนวณ:** ระบบเลขฐาน, Signed Integers (2's Complement), และมาตรฐานทศนิยม IEEE 754
2. **ออกแบบและลดรูป:** วงจรลอจิกเชิงผสม (Combinational Logic) ด้วย K-Map 4-5 ตัวแปร และเทคนิคของ Shannon
3. **แก้ปัญหาฮาร์ดแวร์:** เข้าใจปรากฏการณ์ Glitch, Hazards, Race-around และ Metastability ในวงจรจริง
4. **ออกแบบระบบซับซ้อน:** สร้างระบบควบคุมด้วย Finite State Machine (FSM) และอุปกรณ์ลอจิกโปรแกรมได้ (PLA/PAL)
5. **ประยุกต์ใช้งาน:** เชื่อมต่อระบบดิจิทัลกับโลกแอนะล็อก (ADC/DAC) และสื่อสารผ่านโปรโตคอล UART, I2C, SPI

---

## 📅 แผนการสอนฉบับสมบูรณ์ (17 สัปดาห์)

| สัปดาห์ | หัวข้อหลัก | รายละเอียดเนื้อหาเชิงลึก | บทเรียนอ้างอิง | Lab (ปฏิบัติ ~1 ชม.) |
|:---:|:---|:---|:---:|:---|
| **1** | **Number Systems I** | ระบบเลขฐาน, การแปลงฐาน, **Signed Integers (2's Comp)**, **IEEE 754 Floating Point** | [Ch 01](chapters/ch01-number-systems/) | 🔬 Lab 1: แปลงเลขฐานและทศนิยม |
| **2** | **Codes & Arithmetic** | BCD, Gray, Hamming Code, **BCD Addition & Correction (+6)**, Parity | [Ch 01](chapters/ch01-number-systems/) | 🔬 Lab 2: การตรวจจับและแก้ไขข้อผิดพลาด |
| **3** | **Logic Gates & ICs** | เกตพื้นฐาน, **Tri-State Logic**, **Open-Collector**, Fan-out, Prop. Delay | [Ch 02](chapters/ch02-logic-gates/) | 🔬 Lab 3: ต่อวงจรและวัดแรงดันเอาต์พุต |
| **4** | **Boolean Algebra** | กฎบูลีน, DeMorgan, **Shannon’s Expansion**, **Glitch & Hazards** | [Ch 03](chapters/ch03-boolean-algebra/) | 🔬 Lab 4: การกำจัด Glitch ในวงจรเกต |
| **5** | **K-Map Optimization** | ลดรูป SOP/POS, **5-Variable K-Map**, Prime Implicants (PI/EPI) | [Ch 04](chapters/ch04-karnaugh-maps/) | 🔬 Lab 5: ลดรูปวงจรซับซ้อนด้วย K-Map |
| **6** | **Arithmetic Circuits** | Half/Full Adder, **Carry Look-Ahead Adder (CLA)**, วงจรลบ, **ALU Basics** | [Ch 05](chapters/ch05-combinational-circuits/) | 🔬 Lab 6: สร้างวงจรบวกความเร็วสูง |
| **7** | **Data Routing** | MUX/DEMUX, Encoder/Decoder, **Barrel Shifter**, BCD-to-7Seg | [Ch 05](chapters/ch05-combinational-circuits/) | 🔬 Lab 7: ออกแบบวงจรเลือกสัญญาณ |
| **8** | **📝 Midterm Exam** | **ทดสอบความรู้สัปดาห์ที่ 1 - 7 (Combinational Logic)** | — | — |
| **9** | **Latches & Flip-Flops** | SR/D/JK/T, **Race-Around Condition**, **Master-Slave FF**, Metastability | [Ch 06](chapters/ch06-flip-flops/) | 🔬 Lab 8: วิเคราะห์สภาวะกึ่งเสถียร |
| **10** | **Sequential Analysis** | Timing Diagram, Setup/Hold Time, Excitation Table | [Ch 06](chapters/ch06-flip-flops/) | 🔬 Lab 9: วัดเวลาหน่วงในวงจรลำดับ |
| **11** | **Counters** | Async/Sync Counter, **Clock Divider (Prescaler)**, **LFSR (Random)** | [Ch 07](chapters/ch07-counters-registers/) | 🔬 Lab 10: สร้างเครื่องกำเนิดเลขสุ่ม |
| **12** | **Registers** | SISO/SIPO/PISO/PIPO, Universal Shift Register (74194) | [Ch 07](chapters/ch07-counters-registers/) | 🔬 Lab 11: การรับส่งข้อมูลอนุกรม/ขนาน |
| **13** | **FSM Design I** | Moore vs Mealy, State Diagram, **State Reduction (Implication Table)** | [Ch 09](chapters/ch09-fsm/) | 🔬 Lab 12: ออกแบบตรรกะควบคุมตู้สินค้า |
| **14** | **FSM Design II** | **Real-world Apps:** Vending Machine, **Smart Traffic Light Controller** | [Ch 09](chapters/ch09-fsm/) | 🔬 Lab 13: ต่อวงจร FSM ควบคุมแยกไฟแดง |
| **15** | **Memory & PLD** | RAM/ROM, **NAND vs NOR Flash**, **PLA (Elevator)**, **PAL (Microwave)** | [Ch 08](chapters/ch08-memory-pld/) | 🔬 Lab 14: โปรแกรมตรรกะลงบน PLD |
| **16** | **Interfacing & Comm.** | ADC/DAC, **PWM Control**, **Serial Protocols (UART, I2C, SPI)** | [Ch 10](chapters/ch10-digital-interfacing/) | 🔬 Lab 15: สื่อสารระหว่างชิปผ่านบัส |
| **17** | **🚀 Final Project** | **Mini-Project Presentation & Final Exam** | [Summary](chapters/summary.md) | 🎤 นำเสนอโปรเจกต์จบภาคเรียน |

---

## 📚 หนังสืออ้างอิง (Recommended Textbooks)

- **Digital Fundamentals** (11th Edition) — Thomas L. Floyd
- **Digital Design** (6th Edition) — M. Morris Mano & Michael D. Ciletti
- **Digital Systems: Principles and Applications** — Ronald J. Tocci

---

## 🛠️ เครื่องมือและ Simulator

| Simulator | ลิงก์ | การใช้งานหลัก |
|:---|:---|:---|
| **Tinkercad Circuits** | [tinkercad.com](https://www.tinkercad.com/circuits) | ต่อวงจร IC จริง (74xx, 40xx) และ Microcontroller |
| **CircuitVerse** | [circuitverse.org](https://circuitverse.org/) | วาด Logic Gate แบบลาก-วาง (เหมาะสำหรับบทที่ 1-7) |
| **Logisim Evolution** | [GitHub](https://github.com/logisim-evolution/logisim-evolution) | ออกแบบ FSM, Counter และสถาปัตยกรรมคอมพิวเตอร์ |
| **Falstad Circuit** | [falstad.com](https://www.falstad.com/circuit/) | จำลองวงจรแอนะล็อกและดิจิทัลแบบเห็นการไหลของกระแส |

---

## 📂 โครงสร้าง Repository

- `/chapters`: เนื้อหาบทเรียนรายบท (PDF/Markdown) พร้อมภาพประกอบ Matrix/Diagram
- `/labs`: ใบงานปฏิบัติการประจำสัปดาห์ พร้อมเฉลยและไฟล์จำลอง
- `/images`: รวบรวมภาพวงจรและแผนผังทั้งหมดในหลักสูตร

---
> 💡 **Tip:** สำหรับนักศึกษาที่ต้องการศึกษาต่อยอด แนะนำให้ดูที่ไฟล์ `summary.md` เพื่อสรุปสูตรและ Cheat Sheet ทั้งหมดก่อนสอบครับ
