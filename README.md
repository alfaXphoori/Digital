# ลอจิกและดิจิทัล (Logic and Digital)

> รายวิชา **3(2-2-5)** — ทฤษฎี 2 ชม. / ปฏิบัติ 2 ชม. / ศึกษาด้วยตนเอง 5 ชม. ต่อสัปดาห์
> หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมเมคคาทรอนิกส์ — ชั้นปีที่ 1 ภาคการศึกษาที่ 2
>
> 📋 ดูแผนการจัดการเรียนรู้รายสัปดาห์ฉบับเต็ม (CLO/LLO, การวัดประเมินผล): **[weekly-lesson-plan.md](weekly-lesson-plan.md)**

## แผนการสอน (15 สัปดาห์)

| สัปดาห์ที่ | หัวข้อการเรียน | รายละเอียดเนื้อหา | ไฟล์อ้างอิง |
|:---:|:---|:---|:---|
| **1** | **บทนำรายวิชาและระบบตัวเลข** | สัญญาณแอนะล็อก/ดิจิทัล, ระบบเลขฐาน (2, 8, 10, 16), รหัส BCD/Gray/ASCII | [Number Systems](chapters/ch01-number-systems/) |
| **2** | **เลขคณิตในระบบดิจิทัล** | การบวก/ลบเลขฐานสอง, คอมพลีเมนต์ 1's และ 2's, การแทนเลขมีเครื่องหมาย | [Number Systems](chapters/ch01-number-systems/) |
| **3** | **เกตตรรกะและนิพจน์ตรรกะ** | AND, OR, NOT, NAND, NOR, XOR, XNOR, ตารางความจริง, เกตสากล, ดาต้าชีต IC 74xx | [Logic Gates](chapters/ch02-logic-gates/) |
| **4** | **คุณสมบัติดิจิทัลไอซีและการเชื่อมต่อ** | TTL/CMOS, ระดับแรงดันลอจิก, fan-in/fan-out, noise margin, propagation delay | [Logic Gates](chapters/ch02-logic-gates/) |
| **5** | **พีชคณิตบูลีนและการลดรูปสมการ** | ทฤษฎีบทพีชคณิตบูลีน, ทฤษฎีบทเดอมอร์แกน, SOP/POS | [Boolean Algebra](chapters/ch03-boolean-algebra/) |
| **6** | **ผังคาร์โนห์ (Karnaugh Map)** | K-Map 2–4 ตัวแปร, รูปแบบ SOP/POS, เงื่อนไข don't-care | [Karnaugh Maps](chapters/ch04-karnaugh-maps/) |
| **7** | **วงจรคอมบิเนชันและวงจรคำนวณ** | ขั้นตอนการออกแบบ, เกตสากล, Half/Full Adder, วงจรบวก/ลบ, ไอซี 7483 | [Combinational Circuits](chapters/ch05-combinational-circuits/) |
| **8** | **วงจรเปรียบเทียบ ถอด/ลงรหัส และมัลติเพล็กเซอร์** | Comparator, Encoder/Decoder, 7-segment, MUX/DEMUX และการสร้างฟังก์ชันด้วย MUX | [Combinational Circuits](chapters/ch05-combinational-circuits/) |
| **—** | **🟧 สอบกลางภาค (Midterm Exam)** | **ครอบคลุมเนื้อหาสัปดาห์ที่ 1–8 \| สัดส่วน 20%** | - |
| **9** | **สัญญาณนาฬิกาและแลตช์** | Clock, duty cycle, มัลติไวเบรเตอร์/ไอซี 555, SR/Gated Latch | [Flip-Flops](chapters/ch06-flip-flops/) |
| **10** | **ฟลิปฟลอป** | ฟลิปฟลอป D/JK/T, Trigger, ตารางสถานะ/ตารางกระตุ้น, timing diagram | [Flip-Flops](chapters/ch06-flip-flops/) |
| **11** | **วงจรนับและเรจิสเตอร์** | ตัวนับ asynchronous/synchronous, mod-N, โครงสร้างเรจิสเตอร์, โหมด SISO/SIPO/PISO/PIPO | [Counters & Registers](chapters/ch07-counters-registers/) |
| **12** | **หน่วยความจำ PLD และการแปลงสัญญาณ** | RAM/ROM, PLD, DAC/ADC, ความละเอียดและอัตราการสุ่มตัวอย่าง (Resolution & Sampling Rate) | [Memory & Interfacing](chapters/ch08-memory-interfacing/) |
| **13** | **แนะนำ HDL: Verilog + EDA Playground** | module/port, assign/always, testbench, การจำลองบน EDA Playground | [Verilog HDL](chapters/ch09-hdl-verilog/) |
| **14** | **สถาปัตยกรรมคอมพิวเตอร์และหน่วยประมวลผลกลางเบื้องต้น** | โครงสร้าง CPU, Von Neumann, Instruction Cycle, 8-bit ALU/PC Verilog | [Computer Architecture](chapters/ch10-computer-architecture/) |
| **15** | **โครงงานย่อยและการประยุกต์ใช้งาน / สรุปทบทวนรายวิชา** | นำเสนอ Mini-Project, บูรณาการระบบดิจิทัล, สรุปและเตรียมสอบปลายภาค | [Summary](chapters/summary.md) |
| **—** | **🟧 สอบปลายภาค (Final Exam)** | **ครอบคลุมเนื้อหาสัปดาห์ที่ 9–15 \| สัดส่วน 25%** | [summary.md](chapters/summary.md) |

---

## 📊 เกณฑ์การวัดและประเมินผล

| รายการประเมิน | สัดส่วน (%) | CLO ที่สัมพันธ์ |
|:---|:---:|:---|
| จิตพิสัย การเข้าเรียนและการมีส่วนร่วมในชั้นเรียน | 10 | CLO4 |
| ใบงานและแบบฝึกหัด | 30 | CLO1, CLO2, CLO3 |
| สอบปฏิบัติ | 15 | CLO3, CLO4 |
| สอบกลางภาค | 20 | CLO1, CLO2 |
| สอบปลายภาค | 25 | CLO2, CLO3 |
| **รวม** | **100** | |

---

## 🛠️ Simulator ที่ใช้ในวิชา

| Simulator | ลิงก์ | ใช้สำหรับ |
|:---|:---|:---|
| **Tinkercad Circuits** | [tinkercad.com/circuits](https://www.tinkercad.com/circuits) | ต่อวงจร IC จริง (7408, 7432, 7473, 4511), Lab หลักของวิชา |
| **CircuitVerse** | [circuitverse.org](https://circuitverse.org/) | วาด Logic Gate ลาก-วาง, เหมาะ Lab สัปดาห์ 1–7 |
<!-- ซ่อนไว้ก่อน
| **Logisim Evolution** | [github.com/logisim-evolution](https://github.com/logisim-evolution/logisim-evolution/releases) | ออกแบบ FSM, Counter, Memory (Desktop App) |
| **Falstad Circuit Sim** | [falstad.com/circuit](https://www.falstad.com/circuit/) | จำลองวงจรแบบเห็นกระแสไหล animation |
-->

---

