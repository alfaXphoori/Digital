# Summary: สรุปภาพรวมวิชา Digital Logic

วิชา Digital Logic (ลอจิกดิจิทัล) เป็นพื้นฐานสำคัญของวิศวกรรมคอมพิวเตอร์และระบบสมองกลฝังตัว โดยแบ่งเนื้อหาหลักออกเป็น 2 ส่วนใหญ่ ๆ คือ วงจรเชิงผสม (Combinational Logic) และ วงจรเชิงลำดับ (Sequential Logic)

---

## 1. เนื้อหาหลักที่เรียน

### 1.1 พื้นฐาน (Fundamentals)
- **ระบบเลขฐาน:** การแปลงเลขฐาน 2, 8, 10, 16, ทศนิยม IEEE 754 และการคำนวณ (Binary Arithmetic / 2's Complement)
- **รหัสดิจิทัล:** BCD, Gray Code, ASCII, Unicode และการตรวจจับข้อผิดพลาด (Parity, Hamming Code)
- **ลอจิกเกต:** AND, OR, NOT, NAND, NOR, XOR, XNOR (พร้อมเรื่อง Tri-State, Open-Collector)

### 1.2 วงจรเชิงผสม (Combinational Logic)
- **การลดรูป:** Boolean Algebra, DeMorgan's Theorem, Shannon's Expansion และ K-Map (รวมถึง 5 ตัวแปร)
- **วงจรคำนวณ:** Adder (Ripple Carry, CLA), Subtractor, Comparator, ALU
- **วงจรจัดการข้อมูล:** Encoder, Decoder, Multiplexer (MUX), Demultiplexer (DEMUX), Barrel Shifter

### 1.3 วงจรเชิงลำดับ (Sequential Logic)
- **หน่วยความจำพื้นฐาน:** Latches และ Flip-Flops (SR, D, JK, T) รวมปัญหา Race-Around และ Metastability
- **ตัวนับและรีจิสเตอร์:** Async/Sync Counter, Clock Divider, Shift Registers (SISO, SIPO, PISO, PIPO), LFSR
- **การออกแบบระบบ:** Finite State Machines (FSM) - Moore และ Mealy Machines พร้อมเทคนิค State Reduction

### 1.4 ระบบขั้นสูง (Advanced Systems)
- **หน่วยความจำ:** RAM (SRAM, DRAM) และ ROM (PROM, EPROM, EEPROM, NAND/NOR Flash)
- **อุปกรณ์ลอจิกโปรแกรมได้:** PLA, PAL, CPLD และ FPGA
- **การเชื่อมต่อ:** ADC (Analog-to-Digital) และ DAC (Digital-to-Analog) พร้อม Serial Protocols (UART, I2C, SPI)

---

## 2. สูตรลัดและตารางสรุปที่สำคัญ (Cheat Sheet)

### ลอจิกเกตพื้นฐาน

| Gate | Output = 1 เมื่อ... | สมการ |
|:---:|:---|:---:|
| **AND** | ทุกอินพุตเป็น 1 | $Y = AB$ |
| **OR** | มีอินพุตใดอินพุตหนึ่งเป็น 1 | $Y = A+B$ |
| **NOT** | อินพุตเป็น 0 | $Y = \bar{A}$ |
| **NAND**| อินพุตไม่เป็น 1 พร้อมกันหมด | $Y = \overline{AB}$ |
| **NOR** | ทุกอินพุตเป็น 0 | $Y = \overline{A+B}$ |
| **XOR** | อินพุตต่างกัน | $Y = A \oplus B$ |
| **XNOR**| อินพุตเหมือนกัน | $Y = A \odot B$ |

### เอกลักษณ์บูลีน (Boolean Identities) ที่ใช้บ่อย

- **Double Negation:** $\bar{\bar{A}} = A$
- **DeMorgan:** $\overline{AB} = \bar{A} + \bar{B}$ และ $\overline{A+B} = \bar{A}\cdot\bar{B}$
- **Absorption:** $A + AB = A$ และ $A(A+B) = A$
- **Complement:** $A + \bar{A} = 1$ และ $A \cdot \bar{A} = 0$
- **Distributive:** $A + BC = (A+B)(A+C)$  *(ใช้บ่อยมากในการลดรูป!)*

---

## 3. ตารางสรุปไอซี (IC Reference)

| IC | หน้าที่ | ประเภท |
|:---:|:---|:---|
| **7408** | Quad 2-input AND | Logic Gate |
| **7432** | Quad 2-input OR | Logic Gate |
| **7404** | Hex Inverter (NOT) | Logic Gate |
| **7400** | Quad 2-input NAND | Logic Gate |
| **7402** | Quad 2-input NOR | Logic Gate |
| **7486** | Quad 2-input XOR | Logic Gate |
| **7483** | 4-bit Binary Full Adder | Arithmetic |
| **74138** | 3-to-8 Decoder / DEMUX | Data Routing |
| **74151** | 8:1 Multiplexer | Data Routing |
| **7473** | Dual JK Flip-Flop | Sequential |
| **7474** | Dual D Flip-Flop | Sequential |
| **7490** | Decade Counter (MOD-10) | Counter |
| **74194** | 4-bit Universal Shift Register | Register |
| **4511** | BCD to 7-Segment Decoder | Display |

---

## 4. แหล่งเรียนรู้เพิ่มเติม (Resources)

- **Simulator:** 
  - [Tinkercad Circuits](https://www.tinkercad.com/circuits) (วงจร IC จริง)
  - [CircuitVerse](https://circuitverse.org/) (วาด Logic Gate ง่ายๆ)
- **หนังสือแนะนำ:**
  - *Digital Fundamentals* โดย Thomas L. Floyd
  - *Digital Design* โดย M. Morris Mano
- **คอร์สออนไลน์:**
  - [Coursera: Digital Systems: From Logic Gates to Processors](https://www.coursera.org/learn/digital-systems)

---

> 🚀 **ความสำเร็จในการเรียน:** คือการเข้าใจหลักการและสามารถ "ออกแบบ" วงจรเพื่อแก้ปัญหาจริงในระดับฮาร์ดแวร์ได้ ขอให้สนุกกับการเรียน Digital Logic ครับ!

---

## 5. ลิงก์บทเรียน

- [บทที่ 1 ระบบตัวเลขและรหัส](ch01-number-systems/)
- [บทที่ 2 เกตตรรกะและคุณสมบัติดิจิทัลไอซี](ch02-logic-gates/)
- [บทที่ 3 พีชคณิตบูลีน](ch03-boolean-algebra/)
- [บทที่ 4 ผังคาร์โนห์](ch04-karnaugh-maps/)
- [บทที่ 5 วงจรคอมบิเนชันและการประยุกต์](ch05-combinational-circuits/)
- [บทที่ 6 สัญญาณนาฬิกาและฟลิปฟลอป](ch06-flip-flops/)
- [บทที่ 7 วงจรนับและเรจิสเตอร์](ch07-counters-registers/)
- [บทที่ 8 การออกแบบวงจรเชิงลำดับและ FSM](ch08-fsm/)
- [บทที่ 9 หน่วยความจำ PLD และการแปลงสัญญาณ ADC/DAC](ch09-memory-interfacing/)
- [บทที่ 10 แนะนำ HDL: Verilog และ EDA Playground](ch10-hdl-verilog/)
- [บทที่ 11 สถาปัตยกรรมคอมพิวเตอร์และหน่วยประมวลผลกลางเบื้องต้น](ch11-computer-architecture/)

## 6. ลิงก์ปฏิบัติการ (16 แลป)

- [Lab 1 — ระบบตัวเลขและการแปลงเลขฐาน](../labs/lab01-number-systems.html)
- [Lab 2 — รหัสดิจิทัล (BCD, Gray)](../labs/lab02-digital-codes.html)
- [Lab 3 — เกตตรรกะ](../labs/lab03-logic-gates.html)
- [Lab 4 — กฎเดอมอร์แกน](../labs/lab04-demorgan.html)
- [Lab 5 — ผังคาร์โนห์](../labs/lab05-kmap.html)
- [Lab 6 — วงจรบวก](../labs/lab06-adder.html)
- [Lab 7 — วงจรขับ 7-segment](../labs/lab07-7segment.html)
- [Lab 8 — SR Latch](../labs/lab08-sr-latch.html)
- [Lab 9 — JK Flip-Flop](../labs/lab09-jk-flipflop.html)
- [Lab 10 — วงจรนับแบบ Ripple](../labs/lab10-ripple-counter.html)
- [Lab 11 — Shift Register](../labs/lab11-shift-register.html)
- [Lab 12 — การออกแบบ FSM](../labs/lab12-fsm-design.html)
- [Lab 13 — การสร้าง FSM](../labs/lab13-fsm-implementation.html)
- [Lab 14 — ROM Logic](../labs/lab14-rom-logic.html)
- [Lab 15 — โปรเจกต์ย่อย](../labs/lab15-mini-project.html)
- [Lab 16 — Verilog Simulation บน EDA Playground](../labs/lab16-verilog-eda.html)

## 7. เอกสารที่เกี่ยวข้อง

- [ตารางตำแหน่งขาไอซี (IC Pinouts Reference)](../labs/ic-pinouts.html)
- [แผนการจัดการเรียนรู้รายสัปดาห์ (ฉบับเต็ม)](../weekly-lesson-plan.html)
- [กลับหน้าแรกรายวิชา](../)