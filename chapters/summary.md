# Summary: สรุปภาพรวมวิชา Digital Logic

วิชา Digital Logic (ลอจิกดิจิทัล) เป็นพื้นฐานสำคัญของวิศวกรรมคอมพิวเตอร์และระบบสมังฝังตัว โดยแบ่งเนื้อหาหลักออกเป็น 2 ส่วนใหญ่ ๆ คือ วงจรเชิงผสม (Combinational Logic) และ วงจรเชิงลำดับ (Sequential Logic)

---

## 1. เนื้อหาหลักที่เรียน

### 1.1 พื้นฐาน (Fundamentals)
- **ระบบเลขฐาน:** การแปลงเลขฐาน 2, 8, 10, 16 และการคำนวณ (Binary Arithmetic)
- **รหัสดิจิทัล:** BCD, Gray Code, ASCII, Unicode และการตรวจจับข้อผิดพลาด (Parity, Hamming Code)
- **ลอจิกเกต:** AND, OR, NOT, NAND, NOR, XOR, XNOR

### 1.2 วงจรเชิงผสม (Combinational Logic)
- **การลดรูป:** Boolean Algebra, De Morgan's Theorem และ Karnaugh Maps (K-Map)
- **วงจรคำนวณ:** Adder, Subtractor, Comparator
- **วงจรจัดการข้อมูล:** Encoder, Decoder, Multiplexer (MUX), Demultiplexer (DEMUX)

### 1.3 วงจรเชิงลำดับ (Sequential Logic)
- **หน่วยความจำพื้นฐาน:** Latches และ Flip-Flops (SR, D, JK, T)
- **ตัวนับและรีจิสเตอร์:** Ripple Counter, Synchronous Counter, Shift Registers (SISO, SIPO, PISO, PIPO)
- **การออกแบบระบบ:** Finite State Machines (FSM) - Moore และ Mealy Machines

### 1.4 ระบบขั้นสูง (Advanced Systems)
- **หน่วยความจำ:** RAM (SRAM, DRAM) และ ROM (PROM, EPROM, EEPROM, Flash)
- **อุปกรณ์ลอจิกโปรแกรมได้:** PLA, PAL, CPLD และ FPGA
- **การเชื่อมต่อ:** ADC (Analog-to-Digital) และ DAC (Digital-to-Analog)

---

## 2. สูตรลัดและตารางสรุปที่สำคัญ (Cheat Sheet)

### ลอจิกเกตพื้นฐาน

| Gate | Output = 1 เมื่อ... | สมการ |
|:---:|:---|:---:|
| **AND** | ทุกอินพุตเป็น 1 | $Y = AB$ |
| **OR** | มีอินพุตใดอินพุตหนึ่งเป็น 1 | $Y = A+B$ |
| **NOT** | อินพุตเป็น 0 | $Y = \bar{A}$ |
| **XOR** | อินพุตต่างกัน | $Y = A \oplus B$ |
| **XNOR** | อินพุตเหมือนกัน | $Y = A \odot B$ |

### เอกลักษณ์บูลีน (Boolean Identities)ที่ใช้บ่อย

- **Double Negation:** $\bar{\bar{A}} = A$
- **De Morgan:** $\overline{AB} = \bar{A} + \bar{B}$ และ $\overline{A+B} = \bar{A}\bar{B}$
- **Absorption:** $A + AB = A$ และ $A(A+B) = A$
- **Complement:** $A + \bar{A} = 1$ และ $A\bar{A} = 0$
- **Distributive:** $A + BC = (A+B)(A+C)$

---

## 3. ตารางสรุปไอซี (IC Reference)

| IC | หน้าที่ | ประเภท |
|:---:|:---|:---|
| **7408** | Quad 2-input AND | Logic Gate |
| **7432** | Quad 2-input OR | Logic Gate |
| **7404** | Hex Inverter (NOT) | Logic Gate |
| **7483** | 4-bit Binary Full Adder | Arithmetic |
| **74138** | 3-to-8 Decoder / DEMUX | Data Routing |
| **74151** | 8:1 Multiplexer | Data Routing |
| **7473** | Dual JK Flip-Flop | Sequential |
| **7474** | Dual D Flip-Flop | Sequential |
| **7490** | Decade Counter (0-9) | Counter |
| **74194** | 4-bit Universal Shift Register | Register |
| **4511** | BCD to 7-Segment Decoder | Display |

---

## 4. แหล่งเรียนรู้เพิ่มเติม (Resources)

- **Simulator:** [Tinkercad Circuits](https://www.tinkercad.com/circuits)
- **หนังสือแนะนำ:**
  - *Digital Fundamentals* โดย Thomas L. Floyd
  - *Digital Design* โดย M. Morris Mano
- **คอร์สออนไลน์:**
  - [Coursera: Digital Systems: From Logic Gates to Processors](https://www.coursera.org/learn/digital-systems)
  - [edX: Computation Structures - Part 1: Digital Circuits](https://www.edx.org/course/computation-structures-part-1-digital-circuits)

---

> 🚀 **ความสำเร็จในการเรียน:** คือการเข้าใจหลักการและสามารถ "ออกแบบ" วงจรเพื่อแก้ปัญหาจริงได้ ขอให้โชคดีกับการสอบและการทำ Mini-Project!
