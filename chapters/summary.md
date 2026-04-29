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