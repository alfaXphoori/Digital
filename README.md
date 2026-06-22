# ลอจิกและดิจิทัล (Logic and Digital)

> รายวิชา **3(2-2-5)** — ทฤษฎี 2 ชม. / ปฏิบัติ 2 ชม. / ศึกษาด้วยตนเอง 5 ชม. ต่อสัปดาห์
> หลักสูตรวิศวกรรมศาสตรบัณฑิต สาขาวิชาวิศวกรรมเมคคาทรอนิกส์ — ชั้นปีที่ 1 ภาคการศึกษาที่ 2
>
> 📋 ดูแผนการจัดการเรียนรู้รายสัปดาห์ฉบับเต็ม (CLO/LLO, การวัดประเมินผล): **[weekly-lesson-plan.md](weekly-lesson-plan.md)**

## แผนการสอน (15 สัปดาห์)

| สัปดาห์ที่ | หัวข้อการเรียน | รายละเอียดเนื้อหา | ไฟล์อ้างอิง |
|:---:|:---|:---|:---|
| **1** | **บทนำรายวิชาและระบบดิจิทัล** | สัญญาณแอนะล็อกกับดิจิทัล, หลักการระบบดิจิทัล, ระบบเลขฐาน (2, 8, 10, 16), รหัสดิจิทัล (BCD, Gray, ASCII) | [Number Systems](chapters/ch01-number-systems/) |
| **2** | **เลขคณิตในระบบดิจิทัล** | การบวก/ลบเลขฐานสอง, คอมพลีเมนต์ 1's และ 2's, การแทนเลขมีเครื่องหมาย | [Number Systems](chapters/ch01-number-systems/) |
| **3** | **ลอจิกเกตพื้นฐาน** | สัญลักษณ์และตารางความจริงของ AND, OR, NOT, NAND, NOR, XOR, XNOR, การอ่านดาต้าชีต IC 74xx | [Logic Gates](chapters/ch02-logic-gates/) |
| **4** | **คุณสมบัติดิจิทัลไอซีและการเชื่อมต่อลอจิกเกต** | ตระกูล TTL/CMOS, ระดับแรงดันลอจิก, fan-in/fan-out, noise margin, propagation delay, ตัวต้านทาน pull-up/down | [Logic Gates](chapters/ch02-logic-gates/) |
| **5** | **พีชคณิตบูลีนและการลดรูปสมการลอจิก** | ทฤษฎีบทพีชคณิตบูลีน, ทฤษฎีบทเดอมอร์แกน, การลดรูปสมการด้วยพีชคณิต | [Boolean Algebra](chapters/ch03-boolean-algebra/) |
| **6** | **แผนผังคาร์โนห์ (Karnaugh Map)** | K-Map 2–4 ตัวแปร, รูปแบบ SOP/POS, เงื่อนไข don't-care | [Karnaugh Maps](chapters/ch04-karnaugh-maps/) |
| **7** | **การออกแบบวงจรคอมบิเนชัน** | ขั้นตอนการออกแบบจากโจทย์สู่วงจร, การใช้เกตสากล (NAND-only / NOR-only), การแปลงรูปวงจร | [Combinational Circuits](chapters/ch05-combinational-circuits/) |
| **8** | **วงจรคำนวณทางคณิตศาสตร์** | Half/Full Adder, วงจรบวกขนานและวงจรลบ, การใช้ไอซี 7483 | [Combinational Circuits](chapters/ch05-combinational-circuits/) |
| **—** | **🟧 สอบกลางภาค (Midterm Exam)** | **ครอบคลุมเนื้อหาสัปดาห์ที่ 1–8 \| สัดส่วน 20%** | - |
| **9** | **วงจรเปรียบเทียบ เข้ารหัส ถอดรหัส และภาคแสดงผล** | Comparator, Encoder/Decoder, การขับ 7-segment display | [Combinational Circuits](chapters/ch05-combinational-circuits/) |
| **10** | **วงจรมัลติเพล็กซ์และดีมัลติเพล็กซ์** | หลักการ MUX/DEMUX, การสร้างฟังก์ชันลอจิกด้วย MUX | [Combinational Circuits](chapters/ch05-combinational-circuits/) |
| **11** | **วงจรกำเนิดสัญญาณนาฬิกาและมัลติไวเบรเตอร์** | สัญญาณนาฬิกาและ duty cycle, มัลติไวเบรเตอร์ astable/monostable, ไอซีไทเมอร์ 555 | [Digital Interfacing](chapters/ch10-digital-interfacing/) |
| **12** | **แลตช์และฟลิปฟลอป** | SR Latch, Gated Latch, ฟลิปฟลอป D/JK/T, Clock, Trigger และตารางสถานะ | [Flip-Flops](chapters/ch06-flip-flops/) |
| **13** | **การออกแบบวงจรซีเควนเชียลและวงจรนับ** | หลักการออกแบบวงจรซีเควนเชียล, วงจรนับ asynchronous และ synchronous, ตัวนับ mod-N | [Counters & Registers](chapters/ch07-counters-registers/) |
| **14** | **วงจรเลื่อนข้อมูล (Shift Register)** | โหมด SISO/SIPO/PISO/PIPO, Universal shift register, การประยุกต์ใช้งาน | [Counters & Registers](chapters/ch07-counters-registers/) |
| **15** | **วงจรแปลงสัญญาณและหน่วยความจำ** | การแปลงสัญญาณ DAC/ADC, ความละเอียดและอัตราการสุ่ม, โครงสร้างและคุณสมบัติหน่วยความจำ RAM/ROM | [Memory & PLD](chapters/ch08-memory-pld/) · [Digital Interfacing](chapters/ch10-digital-interfacing/) |
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

