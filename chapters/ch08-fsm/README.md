# Chapter 8: การออกแบบวงจรเชิงลำดับและ FSM

## Finite State Machine (FSM)

---

<div class="chapter-tab-content" data-tab-name="Concept" data-tab-icon="💡" id="concept" markdown="1">

## 8.1 บทนำ (Introduction)

**เครื่องจักรสถานะจำกัด (Finite State Machine - FSM)** คือแบบจำลองทางคณิตศาสตร์และวงจรลอจิกที่ใช้ควบคุมลำดับการทำงานของระบบดิจิทัล ระบบจะทำงานโดยการเปลี่ยน "สถานะ" (State) ไปตามเงื่อนไขของอินพุตและจังหวะของสัญญาณนาฬิกา (Clock)

จากบทที่ 6 เราทราบว่า Flip-Flop ทำหน้าที่เป็นหน่วยความจำ 1 บิต และจากบทที่ 7 เราเห็นว่า Counter คือวงจรที่เปลี่ยนสถานะตามลำดับที่กำหนด FSM คือแนวคิดที่ขยายจาก Counter ให้กว้างขึ้น กล่าวคือ สถานะถัดไปไม่จำเป็นต้องเป็นเลขถัดไปเสมอ แต่ขึ้นกับอินพุตและกฎของระบบ

<svg viewBox="0 0 760 420" role="img" aria-label="โครงสร้าง FSM: Next-State Logic, Flip-Flops (State Register), Output Logic พร้อมเส้นป้อนกลับ Present State" style="width:100%; max-width:720px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-bd1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Next-State Logic -->
  <rect x="260" y="30" width="240" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="380" y="70" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">Next-State Logic</text>

  <!-- Flip-Flops -->
  <rect x="260" y="180" width="240" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="380" y="208" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">Flip-Flops</text>
  <text x="380" y="226" text-anchor="middle" font-size="12" fill="#1e293b">(State Register)</text>

  <!-- Output Logic -->
  <rect x="260" y="330" width="240" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="380" y="370" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">Output Logic</text>

  <!-- Input X -> Next-State Logic -->
  <text x="60" y="60" font-size="12.5" fill="#0f172a">Input X</text>
  <path d="M100,65 L260,65" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd1)"/>

  <!-- Next-State Logic -> Flip-Flops -->
  <path d="M380,100 L380,180" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd1)"/>
  <text x="450" y="148" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">D / J,K / T</text>

  <!-- Clock -> Flip-Flops -->
  <text x="60" y="220" font-size="12.5" fill="#0f172a">Clock</text>
  <path d="M100,225 L260,225" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd1)"/>

  <!-- Flip-Flops -> Output Logic -->
  <path d="M380,250 L380,330" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd1)"/>
  <text x="410" y="298" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">Q</text>

  <!-- Output Logic -> Output Y -->
  <path d="M500,365 L700,365" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd1)"/>
  <text x="650" y="350" text-anchor="middle" font-size="12.5" fill="#0f172a">Output Y</text>

  <!-- Feedback: Flip-Flops -> Next-State Logic (Present State) -->
  <path d="M260,215 C150,215 150,65 260,65" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd1)"/>
  <text x="150" y="140" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">Present State</text>
</svg>

FSM เป็นหัวใจหลักในการออกแบบ:

- **Control Unit (CU):** ภาคควบคุมใน CPU
- **Communication Protocols:** การรับส่งข้อมูล เช่น USB, Ethernet, SPI
- **Industrial Controllers:** ระบบควบคุมลิฟต์, ตู้หยอดเหรียญ, ไฟจราจร
- **Sequence Detector:** ตรวจจับรูปแบบข้อมูลที่เข้ามาทีละบิต
- **Counter แบบมีเงื่อนไข:** นับขึ้น/นับลง/หยุด/รีเซตตามอินพุต

คำศัพท์สำคัญที่ต้องแยกให้ออก:

| คำศัพท์ | ความหมาย |
|:---|:---|
| **Present State (PS)** | สถานะปัจจุบันที่เก็บอยู่ใน Flip-Flop |
| **Next State (NS)** | สถานะที่จะถูกโหลดเข้า Flip-Flop ในขอบ Clock ถัดไป |
| **State Register** | กลุ่ม Flip-Flop ที่เก็บรหัสสถานะ |
| **Transition** | การเปลี่ยนจากสถานะหนึ่งไปอีกสถานะหนึ่ง |
| **Output Logic** | วงจรที่สร้างเอาต์พุตจาก State และ/หรือ Input |

จุดสำคัญคือ FSM แบบ Synchronous จะเปลี่ยนสถานะเฉพาะที่ขอบ Clock เหมือน Flip-Flop ในบทที่ 6 ดังนั้นการวิเคราะห์ต้องแยกสามช่วงเวลาออกจากกันให้ชัดเจน:

1. **ก่อนขอบ Clock:** วงจรลอจิกคำนวณ Next State จาก Present State และ Input
2. **ที่ขอบ Clock:** Flip-Flop รับค่า Next State กลายเป็น Present State ใหม่
3. **หลังขอบ Clock:** Output เปลี่ยนตามกฎของ Moore หรือ Mealy

> 💡 **จำง่าย:** FSM = (Combinational Logic ที่คำนวณสถานะถัดไป) + (Flip-Flop ที่จดจำสถานะปัจจุบัน) ทำงานร่วมกันทุกขอบ Clock

---

## 8.2 ประเภทของ FSM: Moore vs Mealy Machine

ในการออกแบบวงจรเชิงลำดับ (Sequential Circuit) เราแบ่ง FSM ออกเป็น 2 ประเภทหลักตามลักษณะการเกิดเอาต์พุต

### 1. Moore Machine

**เอาต์พุตขึ้นอยู่กับ "สถานะปัจจุบัน" เท่านั้น** หากอินพุตเปลี่ยนแต่สถานะยังไม่เปลี่ยน เอาต์พุตจะคงเดิมเสมอ

<svg viewBox="0 0 840 280" role="img" aria-label="Moore block diagram: Next-State Logic, State Register, Output Logic ที่รับเฉพาะ Q จาก State Register" style="width:100%; max-width:760px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-bd2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Next-State Logic -->
  <rect x="60" y="70" width="160" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="140" y="100" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Next-State</text>
  <text x="140" y="118" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Logic</text>

  <!-- State Register -->
  <rect x="320" y="70" width="160" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="400" y="100" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">State</text>
  <text x="400" y="118" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Register</text>

  <!-- Output Logic -->
  <rect x="580" y="70" width="160" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="660" y="100" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Output</text>
  <text x="660" y="118" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Logic</text>

  <!-- Input -> Next-State Logic -->
  <text x="15" y="100" font-size="12.5" fill="#0f172a">Input</text>
  <path d="M15,108 L60,108" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd2)"/>

  <!-- Next-State Logic -> State Register -->
  <path d="M220,105 L320,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd2)"/>

  <!-- State Register -> Output Logic (Q) -->
  <path d="M480,105 L580,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd2)"/>
  <text x="530" y="93" text-anchor="middle" font-size="12.5" fill="#0f172a">Q</text>

  <!-- Output Logic -> Output -->
  <path d="M740,105 L820,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd2)"/>
  <text x="780" y="93" text-anchor="middle" font-size="12.5" fill="#0f172a">Output</text>

  <!-- Clock -> State Register -->
  <text x="400" y="215" text-anchor="middle" font-size="12.5" fill="#0f172a">Clock</text>
  <path d="M400,200 L400,140" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd2)"/>

  <!-- Feedback: State Register -> Next-State Logic -->
  <path d="M400,70 L400,40 L140,40 L140,70" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd2)"/>
  <text x="270" y="28" text-anchor="middle" font-size="12.5" fill="#0f172a">feedback (Q)</text>
</svg>

ใน State Diagram ของ Moore จะเขียนเอาต์พุตไว้ในวงกลมสถานะ เช่น `S2 / Y=1` เพราะเอาต์พุตเป็นคุณสมบัติของสถานะนั้นโดยตรง

<svg viewBox="0 0 420 180" role="img" aria-label="Moore ตัวอย่าง: S0/Y=0 วน X=0 และไป S1/Y=1 เมื่อ X=1" style="width:100%; max-width:420px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-sd1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- self-loop on S0 -->
  <path d="M85,66 C60,20 150,20 125,66" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd1)"/>
  <text x="105" y="22" text-anchor="middle" font-size="12.5" fill="#0f172a">X=0</text>

  <!-- S0 -->
  <circle cx="105" cy="100" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="105" y="95" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#1e293b">S0</text>
  <text x="105" y="111" text-anchor="middle" dominant-baseline="central" font-size="12" font-weight="600" fill="#1e293b">Y=0</text>

  <!-- edge S0 -> S1 -->
  <path d="M139,100 L281,100" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd1)"/>
  <text x="210" y="88" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">X=1</text>

  <!-- S1 -->
  <circle cx="315" cy="100" r="34" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5"/>
  <text x="315" y="95" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#1e293b">S1</text>
  <text x="315" y="111" text-anchor="middle" dominant-baseline="central" font-size="12" font-weight="600" fill="#1e293b">Y=1</text>
</svg>

### 2. Mealy Machine

**เอาต์พุตขึ้นอยู่กับ "สถานะปัจจุบัน" และ "อินพุต" พร้อมกัน** เอาต์พุตสามารถเปลี่ยนแปลงได้ทันทีเมื่ออินพุตเปลี่ยน แม้จะยังไม่ถึงขอบสัญญาณนาฬิกา

<svg viewBox="0 0 860 320" role="img" aria-label="Mealy block diagram: Next-State Logic, State Register, Output Logic ที่รับทั้ง Q จาก State Register และ Input โดยตรง" style="width:100%; max-width:760px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-bd3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Next-State Logic -->
  <rect x="80" y="90" width="160" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="160" y="120" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Next-State</text>
  <text x="160" y="138" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Logic</text>

  <!-- State Register -->
  <rect x="340" y="90" width="160" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="420" y="120" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">State</text>
  <text x="420" y="138" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Register</text>

  <!-- Output Logic -->
  <rect x="600" y="90" width="160" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="680" y="120" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Output</text>
  <text x="680" y="138" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">Logic</text>

  <!-- Input -> Next-State Logic -->
  <text x="15" y="120" font-size="12.5" fill="#0f172a">Input</text>
  <path d="M15,128 L80,128" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd3)"/>

  <!-- Next-State Logic -> State Register -->
  <path d="M240,125 L340,125" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd3)"/>

  <!-- State Register -> Output Logic (Q) -->
  <path d="M500,125 L600,125" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd3)"/>
  <text x="550" y="113" text-anchor="middle" font-size="12.5" fill="#0f172a">Q</text>

  <!-- Output Logic -> Output -->
  <path d="M760,125 L840,125" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd3)"/>
  <text x="800" y="113" text-anchor="middle" font-size="12.5" fill="#0f172a">Output</text>

  <!-- Clock -> State Register -->
  <text x="420" y="235" text-anchor="middle" font-size="12.5" fill="#0f172a">Clock</text>
  <path d="M420,220 L420,160" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd3)"/>

  <!-- Feedback: State Register -> Next-State Logic -->
  <path d="M420,90 L420,60 L160,60 L160,90" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd3)"/>
  <text x="290" y="48" text-anchor="middle" font-size="12.5" fill="#0f172a">feedback (Q)</text>

  <!-- Key Mealy difference: Input -> Output Logic directly -->
  <path d="M30,128 L30,280 L680,280 L680,160" fill="none" stroke="#dc2626" stroke-width="2.25" stroke-dasharray="6,4" marker-end="url(#arrow-bd3)"/>
  <text x="355" y="297" text-anchor="middle" font-size="12.5" font-weight="600" fill="#dc2626">Input ส่งตรงเข้า Output Logic (จุดต่างจาก Moore)</text>
</svg>

ใน State Diagram ของ Mealy จะเขียนเอาต์พุตไว้บนลูกศร เช่น `1/0` หมายถึง เมื่ออินพุตเป็น 1 ให้เปลี่ยนตามลูกศรนั้นและเอาต์พุตเป็น 0

<svg viewBox="0 0 420 200" role="img" aria-label="Mealy ตัวอย่าง: S0 ไป S1 ด้วย label 1/0 และ S1 กลับไป S0 ด้วย label 0/1" style="width:100%; max-width:420px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-sd2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- S0 -->
  <circle cx="105" cy="100" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="105" y="100" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#1e293b">S0</text>

  <!-- S1 -->
  <circle cx="315" cy="100" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="315" y="100" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#1e293b">S1</text>

  <!-- S0 -> S1 -->
  <path d="M139,88 L281,88" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd2)"/>
  <text x="210" y="74" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">1/0</text>

  <!-- S1 -> S0 -->
  <path d="M281,112 L139,112" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd2)"/>
  <text x="210" y="134" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">0/1</text>
</svg>

### ตารางเปรียบเทียบ Moore vs Mealy

| คุณสมบัติ | Moore Machine | Mealy Machine |
|:---|:---:|:---:|
| **การเกิดเอาต์พุต** | ขึ้นกับ State อย่างเดียว | ขึ้นกับ State + Input |
| **ตำแหน่งเขียน Output** | ในวงกลมสถานะ | บนลูกศร transition |
| **ความเร็วการตอบสนอง** | ช้ากว่า (ต้องรอสถานะเปลี่ยน) | **เร็วกว่า** (เปลี่ยนตาม Input ทันที) |
| **จำนวนสถานะ (States)** | มักจะมีมากกว่า | มักจะมีน้อยกว่า |
| **ความเสถียรของ Output** | สูงกว่า เพราะผูกกับ Flip-Flop | อาจเกิด Glitch ตามอินพุต |
| **เหมาะกับงาน** | Controller, Traffic Light, Counter | Sequence Detector, Protocol Handshake |

การเลือกใช้จึงขึ้นกับโจทย์ ถ้าต้องการเอาต์พุตนิ่งและอ่านง่าย มักเลือก Moore ถ้าต้องการตอบสนองเร็วและใช้สถานะน้อย มักเลือก Mealy

> ⚠️ ข้อผิดพลาดที่พบบ่อยที่สุดของนักศึกษาใหม่ คือเขียน Output ผิดตำแหน่งระหว่างสองแบบนี้ จำไว้เสมอว่า **Moore เขียนใน State วงกลม** ส่วน **Mealy เขียนบนลูกศร**

---

## 8.3 แผนผังและตารางสถานะ (Diagram & Table)

### 8.3.1 State Diagram (แผนผังสถานะ)

- **วงกลม:** แทนสถานะ (State)
- **ลูกศร:** แทนการเปลี่ยนสถานะ (Transition)
- **เงื่อนไข:** ตัวเลขบนลูกศรคือ Input
- **Moore:** เขียน Output ในวงกลมสถานะ
- **Mealy:** เขียนเป็น `Input/Output` บนลูกศร

### 8.3.2 State Table (ตารางสถานะ)

State Table แสดงความสัมพันธ์ระหว่างสถานะปัจจุบัน (Present State), อินพุต (Input), สถานะถัดไป (Next State) และเอาต์พุต (Output)

| Present State | Input | Next State | Output |
|:---:|:---:|:---:|:---:|
| S0 | 0 | S0 | 0 |
| S0 | 1 | S1 | 0 |
| S1 | 0 | S0 | 1 |
| S1 | 1 | S1 | 0 |

หลังจากมี State Table แล้วจึงทำ **State Assignment** เพื่อแปลงชื่อสถานะ เช่น `S0, S1, S2` ให้เป็นรหัสบิต เช่น `00, 01, 10` จากนั้นจึงใช้ K-Map หาอินพุตของ Flip-Flop

### 8.3.3 ตารางกระตุ้น Flip-Flop (Excitation Table)

ในการออกแบบ FSM เรามักทราบค่า `Q` และ `Q+` ก่อน แล้วต้องย้อนกลับไปหาว่าต้องป้อนอะไรเข้า Flip-Flop จึงจะเกิดการเปลี่ยนนั้น ตารางนี้เรียกว่า Excitation Table

| Q | Q+ | D | T | J | K |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | X |
| 0 | 1 | 1 | 1 | 1 | X |
| 1 | 0 | 0 | 1 | X | 1 |
| 1 | 1 | 1 | 0 | X | 0 |

สำหรับนักศึกษาปี 1 แนะนำให้เริ่มจาก **D Flip-Flop** เพราะตรงไปตรงมาที่สุด

$$D = Q^+$$

ถ้าเลือก JK หรือ T Flip-Flop สมการอาจสั้นลงในบาง Counter แต่ต้องใช้ Excitation Table เพิ่มเติมเหมือนที่เรียนในบทที่ 6 และบทที่ 7

> 💡 เพราะ $D = Q^+$ เสมอ ตาราง Excitation ของ D FF จึงไม่ต้องคิดอะไรเพิ่ม — แค่ "ลอก" คอลัมน์ Next State มาใส่ในคอลัมน์ D ตรง ๆ

---

## 8.4 ขั้นตอนการออกแบบ FSM (Design Process)

การออกแบบ FSM อย่างเป็นระบบมี 7 ขั้นตอนหลัก:

1. **Understand & Diagram:** เข้าใจโจทย์ กำหนดอินพุต/เอาต์พุต และวาด **State Diagram**
2. **State Table:** แปลงแผนผังเป็น **State Table**
3. **State Reduction:** ลดทอนสถานะที่ซ้ำซ้อน ถ้ามี
4. **State Assignment:** กำหนดรหัสเลขฐานสองให้แต่ละสถานะ
5. **Excitation Table:** เลือกชนิด Flip-Flop และสร้างตารางกระตุ้น
6. **K-Map Minimization:** ลดรูปสมการสำหรับ Next-State Logic และ Output Logic
7. **Implementation:** วาดวงจรลอจิกหรือ Block Diagram สุดท้าย

ลำดับงานโดยรวม:

<div class="kmap-flow">
  <div class="kmap-flow__step">
    <div class="kmap-flow__badge">ขั้นตอนที่ 1</div>
    <div class="kmap-flow__title">โจทย์ (Problem)</div>
    <div class="kmap-flow__desc">เริ่มจากการทำความเข้าใจโจทย์ เงื่อนไข และพฤติกรรมที่ต้องการของระบบ</div>
  </div>

  <div class="kmap-flow__arrow">↓</div>

  <div class="kmap-flow__step">
    <div class="kmap-flow__badge">ขั้นตอนที่ 2</div>
    <div class="kmap-flow__title">กำหนด Input / Output / State</div>
    <div class="kmap-flow__desc">ระบุสัญญาณอินพุต เอาต์พุต และสถานะ (State) ที่ระบบจำเป็นต้องจดจำ</div>
  </div>

  <div class="kmap-flow__arrow">↓</div>

  <div class="kmap-flow__step">
    <div class="kmap-flow__badge">ขั้นตอนที่ 3</div>
    <div class="kmap-flow__title">State Diagram</div>
    <div class="kmap-flow__desc">วาดแผนผังสถานะ แสดงการเปลี่ยนสถานะ (Transition) ตามเงื่อนไขอินพุต</div>
  </div>

  <div class="kmap-flow__arrow">↓</div>

  <div class="kmap-flow__step">
    <div class="kmap-flow__badge">ขั้นตอนที่ 4</div>
    <div class="kmap-flow__title">State Table</div>
    <div class="kmap-flow__desc">แปลงแผนผังเป็นตาราง แสดง Present State → Next State และ Output</div>
  </div>

  <div class="kmap-flow__arrow">↓</div>

  <div class="kmap-flow__step">
    <div class="kmap-flow__badge">ขั้นตอนที่ 5</div>
    <div class="kmap-flow__title">State Assignment</div>
    <div class="kmap-flow__desc">เข้ารหัสแต่ละสถานะเป็นเลขฐานสอง เพื่อเก็บใน Flip-Flop</div>
  </div>

  <div class="kmap-flow__arrow">↓</div>

  <div class="kmap-flow__step">
    <div class="kmap-flow__badge">ขั้นตอนที่ 6</div>
    <div class="kmap-flow__title">Excitation Table</div>
    <div class="kmap-flow__desc">เลือกชนิด Flip-Flop และหาค่าอินพุตที่ต้องป้อน (D / J,K / T)</div>
  </div>

  <div class="kmap-flow__arrow">↓</div>

  <div class="kmap-flow__step">
    <div class="kmap-flow__badge">ขั้นตอนที่ 7</div>
    <div class="kmap-flow__title">K-Map และสมการลอจิก</div>
    <div class="kmap-flow__desc">ลดรูปด้วย K-Map เพื่อหาสมการ Next-State Logic และ Output Logic</div>
  </div>

  <div class="kmap-flow__arrow">↓</div>

  <div class="kmap-flow__step">
    <div class="kmap-flow__badge">ขั้นตอนที่ 8</div>
    <div class="kmap-flow__title">วงจรจริง</div>
    <div class="kmap-flow__desc">นำสมการมาต่อ Flip-Flop เข้ากับ Combinational Logic เป็นวงจรสมบูรณ์</div>
  </div>
</div>

### ตัวอย่างที่ 1: Mealy Sequence Detector ตรวจจับลำดับ `101`

**โจทย์:** ออกแบบวงจรที่รับอินพุตทีละบิต `X` และให้เอาต์พุต `Y=1` เมื่อพบลำดับ `101` โดยอนุญาตให้ลำดับซ้อนทับกันได้ (overlap)

ตัวอย่างอินพุต:

```text
X: 1 0 1 0 1
Y: 0 0 1 0 1
        └─101
            └─101  (ซ้อนทับได้)
```

#### (a) ตีความโจทย์ -> กำหนดสถานะ

เราต้องจำว่า "เห็น prefix ของ 101 ไปถึงไหนแล้ว"

| State | ความหมาย |
|:---:|:---|
| S0 | ยังไม่เห็นบิตที่เป็นจุดเริ่มต้นของ `101` |
| S1 | เห็น `1` แล้ว |
| S2 | เห็น `10` แล้ว |

ใช้ Mealy เพราะเมื่ออยู่ที่ `S2` และอินพุตใหม่เป็น `1` แปลว่าเจอ `101` ครบทันที จึงให้ `Y=1` บน transition ได้ ไม่ต้องเพิ่มสถานะพิเศษ

#### (b) วาด State Diagram

<svg viewBox="0 0 760 320" role="img" aria-label="Mealy state diagram สำหรับตรวจจับลำดับ 101: S0, S1, S2 พร้อม self-loop และ back-edge" style="width:100%; max-width:720px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-sd3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- self-loop S0 -->
  <path d="M85,76 C60,30 150,30 125,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd3)"/>
  <text x="105" y="32" text-anchor="middle" font-size="12.5" fill="#0f172a">0/0</text>

  <!-- self-loop S1 -->
  <path d="M385,76 C360,30 450,30 425,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd3)"/>
  <text x="405" y="32" text-anchor="middle" font-size="12.5" fill="#0f172a">1/0</text>

  <!-- S0 -->
  <circle cx="105" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="105" y="110" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#1e293b">S0</text>

  <!-- S1 -->
  <circle cx="405" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="405" y="110" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#1e293b">S1</text>

  <!-- S2 -->
  <circle cx="660" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="660" y="110" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#1e293b">S2</text>

  <!-- S0 -> S1 -->
  <path d="M139,105 L371,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd3)"/>
  <text x="255" y="92" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">1/0</text>

  <!-- S1 -> S2 -->
  <path d="M439,105 L626,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd3)"/>
  <text x="530" y="92" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">0/0</text>

  <!-- S2 -> S0 (back, arc below) -->
  <path d="M635,140 C500,260 200,260 105,144" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd3)"/>
  <text x="370" y="262" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">0/0</text>

  <!-- S2 -> S1 (back, arc below) -->
  <path d="M645,142 C570,220 470,220 412,142" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd3)"/>
  <text x="540" y="200" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">1/1</text>
</svg>

อ่านแผนผัง:

- จาก `S0` ถ้าได้ `1` แปลว่าเริ่มเห็น prefix `1` → ไป `S1`
- จาก `S1` ถ้าได้ `0` แปลว่าเห็น `10` → ไป `S2`
- จาก `S2` ถ้าได้ `1` แปลว่าเห็น `101` → ให้ `Y=1` แล้วกลับไป `S1` เพราะบิต `1` ตัวสุดท้ายอาจเป็นจุดเริ่มของรอบใหม่

#### (c) สร้าง State Table / State Transition Table

| Present State | X | Next State | Y |
|:---:|:---:|:---:|:---:|
| S0 | 0 | S0 | 0 |
| S0 | 1 | S1 | 0 |
| S1 | 0 | S2 | 0 |
| S1 | 1 | S1 | 0 |
| S2 | 0 | S0 | 0 |
| S2 | 1 | S1 | 1 |

#### (d) State Assignment

มี 3 สถานะ ต้องใช้ Flip-Flop อย่างน้อย 2 ตัว เพราะ $2^1 < 3 \le 2^2$

| State | Q1 Q0 |
|:---:|:---:|
| S0 | 00 |
| S1 | 01 |
| S2 | 10 |
| Unused | 11 |

หลังเข้ารหัส:

| Q1 Q0 | X | Q1+ Q0+ | Y |
|:---:|:---:|:---:|:---:|
| 00 | 0 | 00 | 0 |
| 00 | 1 | 01 | 0 |
| 01 | 0 | 10 | 0 |
| 01 | 1 | 01 | 0 |
| 10 | 0 | 00 | 0 |
| 10 | 1 | 01 | 1 |
| 11 | 0 | XX | X |
| 11 | 1 | XX | X |

`11` เป็นสถานะที่ไม่ได้ใช้ จึงใช้เป็น Don't Care ใน K-Map ได้ แต่ในวงจรจริงมักเพิ่ม Reset ให้กลับ `S0`

#### (e) เลือกชนิด Flip-Flop และสร้าง Excitation Table

เลือก **D Flip-Flop** 2 ตัว คือ `D1` ป้อนให้ Flip-Flop ของ `Q1` และ `D0` ป้อนให้ Flip-Flop ของ `Q0`

สำหรับ D Flip-Flop:

| Q | Q+ | D |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

ดังนั้น:

| Q1 Q0 | X | Q1+ | Q0+ | D1 | D0 | Y |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 00 | 0 | 0 | 0 | 0 | 0 | 0 |
| 00 | 1 | 0 | 1 | 0 | 1 | 0 |
| 01 | 0 | 1 | 0 | 1 | 0 | 0 |
| 01 | 1 | 0 | 1 | 0 | 1 | 0 |
| 10 | 0 | 0 | 0 | 0 | 0 | 0 |
| 10 | 1 | 0 | 1 | 0 | 1 | 1 |
| 11 | 0 | X | X | X | X | X |
| 11 | 1 | X | X | X | X | X |

#### (f) หาสมการ Next-State และ Output ด้วย K-map

K-Map ของ `D1`:

```text
          X
Q1Q0   0   1
 00    0   0
 01    1   0
 11    X   X
 10    0   0
```

จัดกลุ่ม `1` ที่แถว `01, X=0` กับ Don't Care ที่แถว `11, X=0`

$$D_1 = Q_0\overline{X}$$

K-Map ของ `D0`:

```text
          X
Q1Q0   0   1
 00    0   1
 01    0   1
 11    X   X
 10    0   1
```

ทั้งคอลัมน์ `X=1` เป็น 1 หรือ Don't Care

$$D_0 = X$$

K-Map ของ `Y`:

```text
          X
Q1Q0   0   1
 00    0   0
 01    0   0
 11    X   X
 10    0   1
```

จัดกลุ่ม `1` ที่แถว `10, X=1` กับ Don't Care ที่แถว `11, X=1`

$$Y = Q_1X$$

#### (g) วาดวงจรสุดท้าย

<svg viewBox="0 0 820 500" role="img" aria-label="วงจรสุดท้ายของ Mealy 101 detector: NOT, AND สำหรับ D1, Y และวงจร D Flip-Flop สองตัวสำหรับ Q1, Q0" style="width:100%; max-width:800px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-bd4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- NOT gate for X -->
  <rect x="150" y="20" width="70" height="40" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="185" y="40" text-anchor="middle" dominant-baseline="central" font-size="12.5" font-weight="600" fill="#0f172a">NOT</text>

  <!-- AND gate for D1 -->
  <rect x="280" y="50" width="70" height="40" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="315" y="70" text-anchor="middle" dominant-baseline="central" font-size="12.5" font-weight="600" fill="#0f172a">AND</text>

  <!-- AND gate for Y -->
  <rect x="280" y="150" width="70" height="40" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="315" y="170" text-anchor="middle" dominant-baseline="central" font-size="12.5" font-weight="600" fill="#0f172a">AND</text>

  <!-- Input labels -->
  <text x="20" y="40" font-size="12.5" fill="#0f172a">X</text>
  <text x="20" y="115" font-size="12.5" fill="#0f172a">Q0</text>
  <text x="20" y="170" font-size="12.5" fill="#0f172a">Q1</text>

  <!-- X -> NOT -->
  <path d="M35,40 L150,40" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <!-- X branch down to D0 -->
  <path d="M40,40 L40,225 L260,225" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <!-- X branch to AND(Y) -->
  <path d="M45,40 L45,170 L280,170" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>

  <!-- NOT -> AND(D1) -->
  <path d="M220,40 L255,40 L255,62 L280,62" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <!-- Q0 -> AND(D1) -->
  <path d="M35,108 L255,108 L255,78 L280,78" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <!-- Q1 -> AND(Y) -->
  <path d="M35,165 L280,165" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>

  <!-- AND(D1) -> D1 -->
  <path d="M350,70 L420,70" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="455" y="65" text-anchor="middle" font-size="12.5" fill="#0f172a">D1 = Q0·X̄</text>

  <!-- D0 label at the wire -->
  <path d="M260,225 L420,225" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="455" y="220" text-anchor="middle" font-size="12.5" fill="#0f172a">D0 = X</text>

  <!-- AND(Y) -> Y -->
  <path d="M350,170 L420,170" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="455" y="165" text-anchor="middle" font-size="12.5" fill="#0f172a">Y = Q1·X</text>

  <!-- DFF Q1 (top, independent) -->
  <rect x="280" y="290" width="240" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="400" y="318" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">DFF (Q1)</text>
  <text x="400" y="336" text-anchor="middle" font-size="11" fill="#1e293b">D1, CLK, RST</text>

  <!-- D1, CLK, RST input arrows for Q1 -->
  <text x="195" y="300" text-anchor="middle" font-size="11.5" fill="#0f172a">D1</text>
  <path d="M215,305 L280,305" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="195" y="330" text-anchor="middle" font-size="11.5" fill="#0f172a">CLK</text>
  <path d="M215,325 L280,325" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="195" y="350" text-anchor="middle" font-size="11.5" fill="#0f172a">RST</text>
  <path d="M215,345 L280,345" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>

  <!-- Q1 output (own wire, no link to DFF Q0) -->
  <path d="M520,325 L600,325" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="635" y="320" text-anchor="middle" font-size="12.5" fill="#0f172a">Q1</text>

  <!-- DFF Q0 (bottom, independent) -->
  <rect x="280" y="400" width="240" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="400" y="428" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">DFF (Q0)</text>
  <text x="400" y="446" text-anchor="middle" font-size="11" fill="#1e293b">D0, CLK, RST</text>

  <!-- D0, CLK, RST input arrows for Q0 -->
  <text x="195" y="410" text-anchor="middle" font-size="11.5" fill="#0f172a">D0</text>
  <path d="M215,415 L280,415" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="195" y="440" text-anchor="middle" font-size="11.5" fill="#0f172a">CLK</text>
  <path d="M215,435 L280,435" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="195" y="460" text-anchor="middle" font-size="11.5" fill="#0f172a">RST</text>
  <path d="M215,455 L280,455" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>

  <!-- Q0 output (own wire, no link to DFF Q1) -->
  <path d="M520,435 L600,435" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd4)"/>
  <text x="635" y="430" text-anchor="middle" font-size="12.5" fill="#0f172a">Q0</text>
</svg>

### ตัวอย่างที่ 2: Moore FSM นับขึ้น `0-3` พร้อม Enable

**โจทย์:** ออกแบบวงจรนับขึ้น `0 → 1 → 2 → 3 → 0` เมื่อ `EN=1` และค้างค่าเดิมเมื่อ `EN=0` ให้เอาต์พุต `Z=1` เฉพาะตอนนับอยู่ที่ 3

ตัวอย่างนี้คือ Synchronous Counter จากบทที่ 7 ที่เขียนในรูป FSM แบบ Moore เพราะเอาต์พุต `Z` ขึ้นกับสถานะนับปัจจุบันเท่านั้น

#### (a) ตีความโจทย์ -> กำหนดสถานะ

| State | ความหมาย | Output Z |
|:---:|:---:|:---:|
| S0 | Count = 0 | 0 |
| S1 | Count = 1 | 0 |
| S2 | Count = 2 | 0 |
| S3 | Count = 3 | 1 |

#### (b) วาด State Diagram

<svg viewBox="0 0 820 320" role="img" aria-label="Moore state diagram ของ counter 0 ถึง 3 พร้อม Enable: S0, S1, S2, S3 พร้อม self-loop EN=0 และ back-edge S3 ไป S0" style="width:100%; max-width:780px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-sd4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- self-loops EN=0 above each node -->
  <path d="M85,76 C60,30 150,30 125,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd4)"/>
  <text x="105" y="32" text-anchor="middle" font-size="12" fill="#0f172a">EN=0</text>

  <path d="M285,76 C260,30 350,30 325,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd4)"/>
  <text x="305" y="32" text-anchor="middle" font-size="12" fill="#0f172a">EN=0</text>

  <path d="M485,76 C460,30 550,30 525,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd4)"/>
  <text x="505" y="32" text-anchor="middle" font-size="12" fill="#0f172a">EN=0</text>

  <path d="M685,76 C660,30 750,30 725,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd4)"/>
  <text x="705" y="32" text-anchor="middle" font-size="12" fill="#0f172a">EN=0</text>

  <!-- States -->
  <circle cx="105" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="105" y="104" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">S0</text>
  <text x="105" y="120" text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="600" fill="#1e293b">Z=0</text>

  <circle cx="305" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="305" y="104" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">S1</text>
  <text x="305" y="120" text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="600" fill="#1e293b">Z=0</text>

  <circle cx="505" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="505" y="104" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">S2</text>
  <text x="505" y="120" text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="600" fill="#1e293b">Z=0</text>

  <circle cx="705" cy="110" r="34" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5"/>
  <text x="705" y="104" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">S3</text>
  <text x="705" y="120" text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="600" fill="#1e293b">Z=1</text>

  <!-- forward edges EN=1 -->
  <path d="M139,105 L271,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd4)"/>
  <text x="205" y="92" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">EN=1</text>

  <path d="M339,105 L471,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd4)"/>
  <text x="405" y="92" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">EN=1</text>

  <path d="M539,105 L671,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd4)"/>
  <text x="605" y="92" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">EN=1</text>

  <!-- back edge S3 -> S0, long arc below -->
  <path d="M685,140 C600,260 210,260 115,144" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd4)"/>
  <text x="400" y="262" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">EN=1</text>
</svg>

#### (c) สร้าง State Table / State Transition Table

| Present State | EN | Next State | Z |
|:---:|:---:|:---:|:---:|
| S0 | 0 | S0 | 0 |
| S0 | 1 | S1 | 0 |
| S1 | 0 | S1 | 0 |
| S1 | 1 | S2 | 0 |
| S2 | 0 | S2 | 0 |
| S2 | 1 | S3 | 0 |
| S3 | 0 | S3 | 1 |
| S3 | 1 | S0 | 1 |

#### (d) State Assignment

ใช้รหัส Binary ตามค่าที่นับจริง เพื่อเชื่อมกับบท Counter ได้ง่าย

| State | Count | Q1 Q0 |
|:---:|:---:|:---:|
| S0 | 0 | 00 |
| S1 | 1 | 01 |
| S2 | 2 | 10 |
| S3 | 3 | 11 |

หลังเข้ารหัส:

| Q1 Q0 | EN | Q1+ Q0+ | Z |
|:---:|:---:|:---:|:---:|
| 00 | 0 | 00 | 0 |
| 00 | 1 | 01 | 0 |
| 01 | 0 | 01 | 0 |
| 01 | 1 | 10 | 0 |
| 10 | 0 | 10 | 0 |
| 10 | 1 | 11 | 0 |
| 11 | 0 | 11 | 1 |
| 11 | 1 | 00 | 1 |

#### (e) เลือกชนิด Flip-Flop และสร้าง Excitation Table

เลือก **D Flip-Flop** 2 ตัว เพราะต้องการสาธิตขั้นตอนเดียวกับตัวอย่างแรก และเห็นชัดว่า `D = Q+`

| Q1 Q0 | EN | D1 | D0 | Z |
|:---:|:---:|:---:|:---:|:---:|
| 00 | 0 | 0 | 0 | 0 |
| 00 | 1 | 0 | 1 | 0 |
| 01 | 0 | 0 | 1 | 0 |
| 01 | 1 | 1 | 0 | 0 |
| 10 | 0 | 1 | 0 | 0 |
| 10 | 1 | 1 | 1 | 0 |
| 11 | 0 | 1 | 1 | 1 |
| 11 | 1 | 0 | 0 | 1 |

#### (f) หาสมการ Next-State และ Output ด้วย K-map

K-Map ของ `D0`:

```text
          EN
Q1Q0   0   1
 00    0   1
 01    1   0
 11    1   0
 10    0   1
```

`Q0` จะ toggle เมื่อ `EN=1` และ hold เมื่อ `EN=0`

$$D_0 = Q_0 \oplus EN = \overline{Q_0}EN + Q_0\overline{EN}$$

K-Map ของ `D1`:

```text
          EN
Q1Q0   0   1
 00    0   0
 01    0   1
 11    1   0
 10    1   1
```

อ่านได้ว่า `Q1` จะ toggle เฉพาะเมื่อ `Q0=1` และ `EN=1`

$$D_1 = Q_1 \oplus (Q_0EN)$$

หรือเขียนเป็น SOP

$$D_1 = Q_1\overline{Q_0} + Q_1\overline{EN} + \overline{Q_1}Q_0EN$$

K-Map ของ `Z`:

```text
          EN
Q1Q0   0   1
 00    0   0
 01    0   0
 11    1   1
 10    0   0
```

เพราะเป็น Moore Output จึงไม่ขึ้นกับ `EN`

$$Z = Q_1Q_0$$

#### (g) วาดวงจรสุดท้าย

<svg viewBox="0 0 820 500" role="img" aria-label="วงจรสุดท้ายของ Moore counter 0 ถึง 3: XOR, AND สำหรับ D0, D1, Z และวงจร D Flip-Flop สองตัวสำหรับ Q1, Q0" style="width:100%; max-width:800px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-bd5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- XOR gate for D0 -->
  <rect x="260" y="20" width="70" height="40" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="295" y="40" text-anchor="middle" dominant-baseline="central" font-size="12.5" font-weight="600" fill="#0f172a">XOR</text>
  <text x="20" y="30" font-size="12.5" fill="#0f172a">Q0</text>
  <text x="20" y="50" font-size="12.5" fill="#0f172a">EN</text>
  <path d="M40,30 L260,30" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <path d="M40,50 L260,50" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <path d="M330,40 L400,40" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="430" y="35" text-anchor="middle" font-size="12.5" fill="#0f172a">D0</text>

  <!-- AND gate (Q0,EN) -->
  <rect x="150" y="110" width="70" height="40" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="185" y="130" text-anchor="middle" dominant-baseline="central" font-size="12.5" font-weight="600" fill="#0f172a">AND</text>
  <text x="20" y="115" font-size="12.5" fill="#0f172a">Q0</text>
  <text x="20" y="145" font-size="12.5" fill="#0f172a">EN</text>
  <path d="M40,115 L150,115" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <path d="M40,145 L150,145" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>

  <!-- XOR gate for D1 -->
  <rect x="320" y="110" width="70" height="40" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="355" y="130" text-anchor="middle" dominant-baseline="central" font-size="12.5" font-weight="600" fill="#0f172a">XOR</text>
  <path d="M220,130 L320,130" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="60" y="100" font-size="12.5" fill="#0f172a">Q1</text>
  <path d="M70,100 L300,100 L300,118 L320,118" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <path d="M390,130 L460,130" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="490" y="125" text-anchor="middle" font-size="12.5" fill="#0f172a">D1</text>

  <!-- AND gate for Z -->
  <rect x="260" y="200" width="70" height="40" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="295" y="220" text-anchor="middle" dominant-baseline="central" font-size="12.5" font-weight="600" fill="#0f172a">AND</text>
  <text x="20" y="205" font-size="12.5" fill="#0f172a">Q1</text>
  <text x="20" y="225" font-size="12.5" fill="#0f172a">Q0</text>
  <path d="M40,205 L260,205" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <path d="M40,225 L260,225" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <path d="M330,220 L400,220" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="430" y="215" text-anchor="middle" font-size="12.5" fill="#0f172a">Z</text>

  <!-- DFF Q1 (top, independent) -->
  <rect x="280" y="290" width="240" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="400" y="318" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">DFF (Q1)</text>
  <text x="400" y="336" text-anchor="middle" font-size="11" fill="#1e293b">D1, CLK, RST</text>

  <!-- D1, CLK, RST input arrows for Q1 -->
  <text x="195" y="300" text-anchor="middle" font-size="11.5" fill="#0f172a">D1</text>
  <path d="M215,305 L280,305" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="195" y="330" text-anchor="middle" font-size="11.5" fill="#0f172a">CLK</text>
  <path d="M215,325 L280,325" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="195" y="350" text-anchor="middle" font-size="11.5" fill="#0f172a">RST</text>
  <path d="M215,345 L280,345" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>

  <!-- Q1 output (own wire, no link to DFF Q0) -->
  <path d="M520,325 L600,325" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="635" y="320" text-anchor="middle" font-size="12.5" fill="#0f172a">Q1</text>

  <!-- DFF Q0 (bottom, independent) -->
  <rect x="280" y="400" width="240" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="400" y="428" text-anchor="middle" font-size="13" font-weight="600" fill="#0f172a">DFF (Q0)</text>
  <text x="400" y="446" text-anchor="middle" font-size="11" fill="#1e293b">D0, CLK, RST</text>

  <!-- D0, CLK, RST input arrows for Q0 -->
  <text x="195" y="410" text-anchor="middle" font-size="11.5" fill="#0f172a">D0</text>
  <path d="M215,415 L280,415" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="195" y="440" text-anchor="middle" font-size="11.5" fill="#0f172a">CLK</text>
  <path d="M215,435 L280,435" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="195" y="460" text-anchor="middle" font-size="11.5" fill="#0f172a">RST</text>
  <path d="M215,455 L280,455" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>

  <!-- Q0 output (own wire, no link to DFF Q1) -->
  <path d="M520,435 L600,435" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-bd5)"/>
  <text x="635" y="430" text-anchor="middle" font-size="12.5" fill="#0f172a">Q0</text>
</svg>

สังเกตว่าตัวอย่างนี้คือ Counter ที่มีเงื่อนไข `EN` ถ้าเอา `EN` ออกและบังคับให้เป็น 1 ตลอด จะได้ MOD-4 Synchronous Up Counter แบบพื้นฐานจากบทที่ 7

> 💡 นี่คือสิ่งที่ทำให้ FSM ทรงพลัง: Counter ที่เคยเรียนในบทที่ 7 ก็คือ Moore FSM ชนิดหนึ่งนั่นเอง เพียงแต่ลำดับสถานะเดินเป็นเส้นตรง (0→1→2→3→0) เท่านั้น

---

## 8.5 เทคนิคการลดทอนสถานะ (State Reduction)

หากเรามีสถานะ 2 ตัวที่:

1. ให้ **Output** เหมือนกันในทุกเงื่อนไขอินพุต
2. เปลี่ยนไปยัง **Next State** เดียวกัน หรือไปยังสถานะที่เทียบเท่ากัน ในทุกเงื่อนไขอินพุต

เราสามารถ **ยุบรวม (Collapse)** สองสถานะนี้เป็นสถานะเดียวได้ เพื่อลดจำนวน Flip-Flop และเกตลอจิก

### แนวคิดพื้นฐาน

สถานะสองตัวเทียบเท่ากันถ้า "มองจากภายนอกแล้วแยกไม่ออก" หมายความว่าไม่ว่าจะป้อนอินพุตลำดับใดต่อจากนี้ เอาต์พุตที่ได้จะเหมือนกันทุกครั้ง

ตัวอย่าง State Table แบบ Moore:

| Present State | X=0 -> NS | X=1 -> NS | Output Y |
|:---:|:---:|:---:|:---:|
| A | A | B | 0 |
| B | C | D | 0 |
| C | A | B | 0 |
| D | C | D | 1 |
| E | A | B | 0 |

ตรวจดู:

- `A`, `C`, และ `E` ให้ Output = 0 เหมือนกัน
- `A` เมื่อ X=0 ไป A, X=1 ไป B
- `C` เมื่อ X=0 ไป A, X=1 ไป B
- `E` เมื่อ X=0 ไป A, X=1 ไป B

ดังนั้น `A`, `C`, `E` เทียบเท่ากันและยุบเป็นสถานะเดียวได้

ตารางหลังลดทอน:

| Present State | X=0 -> NS | X=1 -> NS | Output Y |
|:---:|:---:|:---:|:---:|
| A' | A' | B | 0 |
| B | A' | D | 0 |
| D | A' | D | 1 |

```text
ก่อนลดทอน:  A, B, C, D, E  = 5 states
หลังลดทอน:  A', B, D       = 3 states

จำนวน Flip-Flop แบบ Binary:
  5 states -> ต้องใช้ 3 FF
  3 states -> ใช้ 2 FF
```

### วิธีตรวจแบบเป็นขั้น

1. แบ่งกลุ่มตาม Output ก่อน เช่น กลุ่ม Output=0 และ Output=1
2. ภายในกลุ่มเดียวกัน ตรวจว่าแต่ละอินพุตไปยังกลุ่มเดียวกันหรือไม่
3. ถ้าไม่เหมือนกัน ให้แยกกลุ่ม
4. ทำซ้ำจนกลุ่มไม่เปลี่ยน

> ⚠️ **ข้อควรระวัง:** State Reduction ต้องรักษาพฤติกรรมภายนอกของระบบ ไม่ใช่ลดเพียงเพราะชื่อสถานะดูคล้ายกัน ต้องตรวจทั้ง Output และ Next State ให้ครบทุกเงื่อนไขอินพุตจริง ๆ

---

## 8.6 การกำหนดรหัสสถานะ (State Encoding)

หลังจากกำหนด State แล้ว ต้องเข้ารหัส State เป็นบิตเพื่อเก็บใน Flip-Flop การเลือก encoding มีผลต่อจำนวน Flip-Flop และความซับซ้อนของวงจรลอจิก

| วิธี | ลักษณะ | ข้อดี | ข้อเสีย |
|:---|:---|:---|:---|
| **Binary** | 00, 01, 10, 11 | ใช้ Flip-Flop น้อยที่สุด | วงจร Next-state อาจซับซ้อน |
| **Gray** | 00, 01, 11, 10 | เปลี่ยนทีละ 1 บิต ลด glitch บางกรณี | จำกัดรูปแบบลำดับ |
| **One-Hot** | 0001, 0010, 0100 | วงจรเร็วและง่ายมาก | ใช้ Flip-Flop มากที่สุด |

### จำนวน Flip-Flop ที่ต้องใช้

ถ้ามี `N` สถานะ

$$\text{จำนวน FF แบบ Binary} = \lceil \log_2 N \rceil$$

| จำนวนสถานะ | Binary FF | One-Hot FF |
|:---:|:---:|:---:|
| 2 | 1 | 2 |
| 3-4 | 2 | 3-4 |
| 5-8 | 3 | 5-8 |
| 9-16 | 4 | 9-16 |

### ตัวอย่างผลของ State Assignment

สมมติ FSM มีการเปลี่ยนสถานะเป็นวงรอบ `S0 → S1 → S2 → S3 → S0`

| State | Binary | Gray |
|:---:|:---:|:---:|
| S0 | 00 | 00 |
| S1 | 01 | 01 |
| S2 | 10 | 11 |
| S3 | 11 | 10 |

แบบ Binary มี transition `01 → 10` ที่เปลี่ยน 2 บิตพร้อมกัน ส่วน Gray เปลี่ยนทีละ 1 บิตในทุก transition ของวงรอบนี้ จึงเหมาะกับวงจรบางประเภทที่ไวต่อ glitch

> 💡 อย่างไรก็ตาม ในวิชาเบื้องต้นมักเริ่มจาก Binary เพราะคำนวณจำนวน Flip-Flop ง่าย และเชื่อมกับ Counter ได้ตรงที่สุด

---

## 8.7 ตัวอย่าง: การออกแบบ Sequence Detector "101"

ต้องการออกแบบวงจรที่ให้เอาต์พุต $Y=1$ เมื่อตรวจพบลำดับอินพุต $X$ เป็น `1` → `0` → `1`

หัวข้อนี้สรุปความต่างระหว่าง Moore และ Mealy สำหรับโจทย์เดียวกัน

**🔬 ทดลองการทำงานและเปรียบเทียบสถานะ (Interactive Moore vs Mealy Sequence Detector):**

{% include fsm-demo.html %}

---

### เปรียบเทียบจำนวนสถานะ

- **Moore:** ต้องการ 4 สถานะ (`S0, S1, S2, S3`) เพราะต้องมีสถานะหนึ่งเพื่อบอกว่า "เจอครบแล้ว" และให้ `Y=1`
- **Mealy:** ต้องการ 3 สถานะ (`S0, S1, S2`) เพราะให้ `Y=1` ได้ทันทีบน transition ที่เจอบิตสุดท้าย

### Moore Version ของ `101`

```text
S0/Y=0 : ยังไม่เจออะไร
S1/Y=0 : เจอ 1
S2/Y=0 : เจอ 10
S3/Y=1 : เจอ 101 ครบแล้ว
```

<svg viewBox="0 0 820 360" role="img" aria-label="Moore state diagram สำหรับตรวจจับ 101: S0, S1, S2, S3 พร้อม self-loop และ back-edges หลายเส้น" style="width:100%; max-width:780px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-sd5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- self-loop S0 (X=0) -->
  <path d="M85,76 C60,30 150,30 125,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd5)"/>
  <text x="105" y="32" text-anchor="middle" font-size="12.5" fill="#0f172a">0</text>

  <!-- self-loop S1 (X=1) -->
  <path d="M285,76 C260,30 350,30 325,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd5)"/>
  <text x="305" y="32" text-anchor="middle" font-size="12.5" fill="#0f172a">1</text>

  <!-- States -->
  <circle cx="105" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="105" y="104" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">S0</text>
  <text x="105" y="120" text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="600" fill="#1e293b">Y=0</text>

  <circle cx="305" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="305" y="104" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">S1</text>
  <text x="305" y="120" text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="600" fill="#1e293b">Y=0</text>

  <circle cx="505" cy="110" r="34" fill="#eef2ff" stroke="#6366f1" stroke-width="2.5"/>
  <text x="505" y="104" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">S2</text>
  <text x="505" y="120" text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="600" fill="#1e293b">Y=0</text>

  <circle cx="705" cy="110" r="34" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5"/>
  <text x="705" y="104" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">S3</text>
  <text x="705" y="120" text-anchor="middle" dominant-baseline="central" font-size="11.5" font-weight="600" fill="#1e293b">Y=1</text>

  <!-- S0 -> S1 (X=1) -->
  <path d="M139,105 L271,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd5)"/>
  <text x="205" y="92" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">1</text>

  <!-- S1 -> S2 (X=0) -->
  <path d="M339,105 L471,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd5)"/>
  <text x="405" y="92" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">0</text>

  <!-- S2 -> S3 (X=1) -->
  <path d="M539,105 L671,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd5)"/>
  <text x="605" y="92" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">1</text>

  <!-- S2 -> S0 (X=0), arc below -->
  <path d="M490,142 C420,230 180,230 118,144" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd5)"/>
  <text x="305" y="232" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">0</text>

  <!-- S3 -> S1 (X=1), arc below, long -->
  <path d="M685,140 C600,280 380,280 318,144" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd5)"/>
  <text x="500" y="285" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">1</text>

  <!-- S3 -> S2 (X=0), arc below, shorter -->
  <path d="M695,142 C640,190 570,190 518,142" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd5)"/>
  <text x="610" y="192" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">0</text>
</svg>

Moore จะได้ `Y=1` หลังจากเข้า `S3` แล้ว ดังนั้นเอาต์พุตมักช้ากว่า Mealy 1 clock แต่เอาต์พุตนิ่งกว่า

### Mealy Version ของ `101`

ตัวอย่างแบบ Mealy ได้ออกแบบครบขั้นตอนในหัวข้อ 8.4 แล้ว สมการสุดท้ายคือ

$$D_1 = Q_0\overline{X}$$

$$D_0 = X$$

$$Y = Q_1X$$

ข้อดีคือใช้เพียง 3 สถานะและให้ `Y=1` ทันทีเมื่ออินพุตตัวสุดท้ายของลำดับมาถึง

### ข้อผิดพลาดที่พบบ่อยในการออกแบบ FSM

| ข้อผิดพลาด | ผลที่เกิดขึ้น | วิธีป้องกัน |
|:---|:---|:---|
| ลืมกำหนดสถานะเริ่มต้น | วงจรเริ่มทำงานจากสถานะสุ่ม | ใส่ Reset ไปยัง `S0` |
| สับสน Present State กับ Next State | สมการ D ผิด | จำว่า D ของ DFF คือ `Q+` |
| เขียน Output ผิดตำแหน่ง | Moore/Mealy ปนกัน | Moore เขียนใน State, Mealy เขียนบนลูกศร |
| ไม่ใส่ transition ครบทุกอินพุต | FSM มีพฤติกรรมไม่กำหนด | ทุก State ต้องมีทางออกครบทุกค่าของ Input |
| ใช้ Don't Care เกินจริง | สถานะ unused อาจหลุดไปติดค้าง | กำหนด reset หรือ recovery path |
| ไม่พิจารณา overlap ใน sequence detector | ตรวจจับลำดับซ้อนทับไม่ได้ | ระบุในโจทย์และออกแบบ prefix ให้ถูก |
| รับอินพุต asynchronous ตรงเข้า FSM | เกิด metastability | ใช้ synchronizer จาก DFF 2 ตัวก่อนเข้า FSM |
| ลืม setup/hold time | Flip-Flop รับค่าผิด | ทำให้สัญญาณนิ่งก่อนขอบ Clock |

---

## 8.8 การใช้งาน FSM ในระบบจริง (Real-world FSM Applications)

FSM เป็นหัวใจของการออกแบบระบบดิจิทัลที่ต้องมีการ "ตัดสินใจเป็นลำดับขั้นตอน" (Sequential Decision Making)

### 8.8.1 ระบบควบคุมไฟจราจรอัจฉริยะ (Smart Traffic Light Controller)

ไฟจราจรเป็น Moore FSM ที่เข้าใจง่าย เพราะสีไฟขึ้นกับสถานะปัจจุบัน ไม่ควรเปลี่ยนทันทีตามสัญญาณ sensor โดยไม่ผ่าน clock หรือ timer

**อินพุต (Inputs):**

- `T_EX` = Timer Expired
- `CAR` = มีรถรอหรือผ่านอยู่

**สถานะ (States):**

- `S0 (GREEN)` ให้ไฟเขียว
- `S1 (YELLOW)` ให้ไฟเหลือง
- `S2 (RED)` ให้ไฟแดง

<svg viewBox="0 0 680 540" role="img" aria-label="Moore state diagram ของไฟจราจร: GREEN, YELLOW, RED จัดเป็นรูปสามเหลี่ยม พร้อม self-loop และ transition ตามเงื่อนไข CAR และ T_EX" style="width:100%; max-width:640px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-sd6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- self-loop GREEN -->
  <path d="M150,76 C125,30 215,30 190,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd6)"/>
  <text x="170" y="30" text-anchor="middle" font-size="11.5" fill="#0f172a">CAR=1 ∧ T_EX=0</text>

  <!-- self-loop YELLOW -->
  <path d="M555,76 C530,30 620,30 595,76" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd6)"/>
  <text x="575" y="30" text-anchor="middle" font-size="11.5" fill="#0f172a">T_EX=0</text>

  <!-- self-loop RED -->
  <path d="M340,444 C315,494 405,494 380,444" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd6)"/>
  <text x="360" y="508" text-anchor="middle" font-size="11.5" fill="#0f172a">T_EX=0</text>

  <!-- GREEN -->
  <circle cx="170" cy="110" r="38" fill="#dcfce7" stroke="#16a34a" stroke-width="2.5"/>
  <text x="170" y="110" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">GREEN</text>

  <!-- YELLOW -->
  <circle cx="575" cy="110" r="38" fill="#fef9c3" stroke="#ca8a04" stroke-width="2.5"/>
  <text x="575" y="110" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">YELLOW</text>

  <!-- RED -->
  <circle cx="360" cy="410" r="38" fill="#fee2e2" stroke="#dc2626" stroke-width="2.5"/>
  <text x="360" y="410" text-anchor="middle" dominant-baseline="central" font-size="13.5" font-weight="600" fill="#1e293b">RED</text>

  <!-- GREEN -> YELLOW -->
  <path d="M208,103 L537,103" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd6)"/>
  <text x="372" y="90" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">CAR=0 ∨ T_EX=1</text>

  <!-- YELLOW -> RED -->
  <path d="M558,144 L391,381" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd6)"/>
  <text x="510" y="260" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">T_EX=1</text>

  <!-- RED -> GREEN (back) -->
  <path d="M329,381 L191,141" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sd6)"/>
  <text x="220" y="260" text-anchor="middle" font-size="12.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">T_EX=1</text>
</svg>

| Current State | Input Conditions | Next State | Lights (G,Y,R) |
|:---:|:---|:---:|:---:|
| GREEN | CAR=1 และ T_EX=0 | GREEN | 1,0,0 |
| GREEN | CAR=0 หรือ T_EX=1 | YELLOW | 1,0,0 |
| YELLOW | T_EX=0 | YELLOW | 0,1,0 |
| YELLOW | T_EX=1 | RED | 0,1,0 |
| RED | T_EX=0 | RED | 0,0,1 |
| RED | T_EX=1 | GREEN | 0,0,1 |

แนวคิดเดียวกันนี้ใช้ได้กับ Controller ใน CPU, เครื่องซักผ้า, Elevator, Keyboard Scanner และ Protocol Receiver บน FPGA/CPLD

### 8.8.2 แนวทางออกแบบ FSM ให้ใช้งานจริง

| ประเด็น | แนวทาง |
|:---|:---|
| Reset | ระบุสถานะเริ่มต้นเสมอ เช่น `S0` |
| Clock | ใช้ clock เดียวกันกับ Flip-Flop ทุกตัวถ้าเป็น synchronous FSM |
| Input ภายนอก | ผ่าน synchronizer ก่อนเข้า FSM |
| Unused State | กำหนดให้กลับ `S0` หรือ state ปลอดภัย |
| Output ที่ไปควบคุมโหลดจริง | ถ้าเป็น Mealy และเสี่ยง glitch ให้ register output เพิ่ม |
| การทดสอบ | จำลองทุก state และทุก input combination |

</div>

<div class="chapter-tab-content" data-tab-name="Interactive Sim" data-tab-icon="🎮" id="sim" markdown="1">

## Interactive Simulators (ห้องทดลอง Finite State Machines)

เครื่องมือจำลองเหล่านี้ออกแบบมาเพื่อช่วยสร้างความเข้าใจผ่านการโต้ตอบและลงมือเล่น (Simulate-First)

### 1. ตัวจำลอง Sequence Detector "101" (FSM Sequence Detector Simulator)
ทดลองป้อนลำดับอินพุต (Input Sequence) 0/1 ทีละบิตเพื่อดูการเคลื่อนที่ผ่านแต่ละสถานะของ FSM แบบ Mealy และ Moore:

{% include fsm-demo.html %}

---

### 2. ลิงก์สู่เครื่องมือวาดและจำลอง FSM ภายนอก (FSM Designers)
- [FSM Designer - Online Finite State Machine Designer](https://madebyevan.com/fsm/) (สามารถคลิกวาดวงกลม สร้าง transition แล้วกดเล่นทดลองนำเข้าข้อมูลเพื่อดูบิตและสถานะเปลี่ยนได้ทันที)

</div>

<div class="chapter-tab-content" data-tab-name="Waveform / Truth Table" data-tab-icon="📊" id="waveform" markdown="1">

## Reference Tables (แนวทางการเปรียบเทียบและการออกแบบ FSM)

สรุปแนวทางความแตกต่างและการเลือกใช้โครงสร้าง FSM:

### 1. เปรียบเทียบ Mealy vs Moore Machines

| คุณสมบัติ | Moore Machine | Mealy Machine |
|---|---|---|
| **ความสัมพันธ์เอาต์พุต** | ขึ้นกับ **สถานะปัจจุบัน (Present State)** เท่านั้น | ขึ้นกับ **สถานะปัจจุบัน** และ **อินพุตปัจจุบัน** |
| **จำนวนสถานะ (States)** | มักจะมีจำนวนสถานะ **มากกว่า** (เนื่องจากต้องเพิ่มสถานะสำหรับเอาต์พุต) | มักจะมีจำนวนสถานะ **น้อยกว่า** |
| **การตอบสนองอินพุต** | ตอบสนองช้ากว่า 1 คาบเวลา (รอจังหวะ Clock) | ตอบสนองได้รวดเร็วทันทีในคาบเวลาเดียวกัน |
| **เสถียรภาพ (Stability)** | เอาต์พุตเสถียรและไม่มี Glitch | เอาต์พุตอาจเกิด Glitch (สัญญาณรบกวนชั่วขณะ) เมื่ออินพุตเปลี่ยนแปลง |

</div>

<div class="chapter-tab-content" data-tab-name="Challenge" data-tab-icon="🏆" id="challenge" markdown="1">

## แบบฝึกหัดท้ายบท

1. จงอธิบายว่าทำไม Mealy Machine ถึงมีแนวโน้มที่จะเกิด Glitch ที่เอาต์พุตได้ง่ายกว่า Moore Machine?

   **เฉลยแนวคิด:** Mealy Output ขึ้นกับ Input โดยตรง ถ้า Input เปลี่ยนหรือมี noise เอาต์พุตอาจเปลี่ยนทันทีผ่าน combinational logic ส่วน Moore Output ขึ้นกับ Flip-Flop State จึงเปลี่ยนเฉพาะหลัง clock edge และนิ่งกว่า

2. ออกแบบ Sequence Detector สำหรับตรวจจับรหัส `1101` แบบ Mealy โดยอนุญาต overlap

   **เฉลยแนวคิด:** กำหนด state เป็น prefix ที่พบแล้ว: `S0` ยังไม่เจอ, `S1` เจอ `1`, `S2` เจอ `11`, `S3` เจอ `110` เมื่ออยู่ `S3` และ X=1 ให้ `Y=1` แล้วกลับไป state ที่แทน prefix `1` เพื่อรองรับ overlap

3. ออกแบบ Sequence Detector สำหรับตรวจจับรหัส `101` แบบ Moore แล้วเปรียบเทียบกับ Mealy ในหัวข้อ 8.4

   **เฉลยแนวคิด:** Moore ต้องเพิ่ม state `S3/Y=1` สำหรับ "เจอครบแล้ว" จึงใช้ 4 states ส่วน Mealy ใช้ 3 states เพราะให้ `Y=1` บน transition จาก `S2` เมื่อ X=1 ได้ทันที

4. ออกแบบ FSM นับขึ้น `0 → 1 → 2 → 3 → 0` โดยใช้ T Flip-Flop แทน D Flip-Flop

   **เฉลยแนวคิด:** ใช้ state assignment `00,01,10,11` เหมือนตัวอย่าง 8.4 สำหรับ MOD-4 counter เมื่อ EN=1 จะได้ `T0=EN` และ `T1=Q0EN` ถ้าไม่มี EN ให้แทน `EN=1` จึงได้ `T0=1`, `T1=Q0`

5. จาก State Table ต่อไปนี้ จงลดทอนสถานะถ้าทำได้

   | Present State | X=0 | X=1 | Y |
   |:---:|:---:|:---:|:---:|
   | A | A | B | 0 |
   | B | C | D | 1 |
   | C | A | B | 0 |
   | D | C | D | 1 |

   **เฉลยแนวคิด:** `A` และ `C` เทียบเท่ากัน เพราะให้ Y=0 และเมื่อ X=0 ไป A, X=1 ไป B เหมือนกัน ส่วน `B` และ `D` ให้ Y=1 และไปยังกลุ่มเดียวกัน จึงยุบได้เป็น 2 states: `{A,C}` และ `{B,D}`

6. ออกแบบ Moore FSM สำหรับไฟจราจร 3 สถานะ `GREEN → YELLOW → RED → GREEN` โดยเปลี่ยนสถานะเมื่อ `T=1` และค้างสถานะเมื่อ `T=0`

   **เฉลยแนวคิด:** กำหนด `S0=GREEN`, `S1=YELLOW`, `S2=RED`; output เป็น `G,Y,R` ตาม state; state table มีเงื่อนไข `T=0` hold ทุก state และ `T=1` ไป state ถัดไป ใช้ 2 D Flip-Flop เข้ารหัส 3 state และกำหนด unused state `11` ให้กลับ `S0`

</div>
