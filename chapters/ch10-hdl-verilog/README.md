# Chapter 10: แนะนำการออกแบบด้วย HDL (Verilog) และการจำลองด้วย EDA Playground

## Hardware Description Language: Verilog & EDA Playground

---

**รายวิชา:** ตรรกศาสตร์ของดิจิตอลคอมพิวเตอร์ (Digital Computer Logic)
**หลักสูตร:** วิศวกรรมคอมพิวเตอร์ ชั้นปีที่ 1
**บทที่:** 10 — สัปดาห์ที่ 15

---

<div class="chapter-tab-content" data-tab-name="Concept" data-tab-icon="💡" id="concept" markdown="1">

## 10.1 บทนำ: ทำไมต้องใช้ HDL

ตลอดเก้าบทที่ผ่านมา เราออกแบบวงจรดิจิทัลด้วยการวาด **แผนผังวงจร (schematic)** คือวางเกตทีละตัวแล้วลากสายเชื่อม วิธีนี้เห็นภาพดีสำหรับวงจรเล็ก แต่เมื่อระบบใหญ่ขึ้น เช่น หน่วยประมวลผลที่มีเกตหลายล้านตัว การวาดมือเป็นไปไม่ได้เลย

**ภาษาบรรยายฮาร์ดแวร์ (Hardware Description Language: HDL)** คือภาษาที่ใช้ "เขียนบรรยาย" พฤติกรรมและโครงสร้างของวงจรดิจิทัลเป็นข้อความ แล้วให้เครื่องมือ (synthesis tool) แปลงข้อความนั้นเป็นวงจรเกตจริงโดยอัตโนมัติ ภาษา HDL ที่นิยมมี 2 ตระกูลหลักคือ **Verilog** (และ SystemVerilog) กับ **VHDL** ในบทนี้เราใช้ Verilog เพราะไวยากรณ์ใกล้เคียงภาษา C ที่นักศึกษาคุ้นเคย

> 💡 **เกร็ด:** HDL ไม่ใช่ "ภาษาโปรแกรม" ในความหมายปกติ เพราะโค้ดที่เขียนไม่ได้ทำงานทีละบรรทัดบน CPU แต่ถูกแปลเป็น **วงจรฮาร์ดแวร์ที่ทำงานขนานกันทั้งหมดพร้อมกัน** การคิดแบบ "วงจร" จึงสำคัญกว่าการคิดแบบ "ลำดับคำสั่ง"

### ข้อดีของการออกแบบด้วย HDL

| ประเด็น | วาด schematic | เขียน HDL |
|---|---|---|
| ขนาดวงจรที่จัดการได้ | เล็ก–กลาง | เล็กถึงใหญ่มาก (ล้านเกต) |
| การแก้ไข/ทำซ้ำ | ช้า ต้องวาดใหม่ | แก้ข้อความ ใช้พารามิเตอร์ซ้ำได้ |
| การทดสอบ | ต่อวงจรจริง/จำลองทีละจุด | เขียน testbench ทดสอบอัตโนมัติ |
| การนำกลับมาใช้ | ยาก | ทำเป็นโมดูลเรียกซ้ำได้ |
| เป้าหมายการผลิต | — | สังเคราะห์ลง FPGA/ASIC ได้ |

### RTL คืออะไร

ในทางปฏิบัติเราเขียน HDL ที่ระดับ **RTL (Register-Transfer Level)** คือบรรยายว่าข้อมูลถูกเก็บใน **รีจิสเตอร์ (register)** อะไรบ้าง และในแต่ละจังหวะสัญญาณนาฬิกา ข้อมูลถูก "ย้าย/แปลง" ระหว่างรีจิสเตอร์อย่างไรผ่านวงจรคอมบิเนชัน เครื่องมือสังเคราะห์จะเปลี่ยน RTL เป็นเกตและฟลิปฟลอปจริงให้เอง

<svg viewBox="0 0 720 260" role="img" aria-label="แนวคิด RTL: register ส่งข้อมูลผ่านวงจรคอมบิเนชันไปยัง register ตัวถัดไป พร้อมเส้นป้อนกลับของสัญญาณ clock" style="width:100%; max-width:680px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-rtl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Register 1 -->
  <rect x="40" y="70" width="150" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="115" y="110" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#0f172a">Register</text>

  <!-- Combinational Logic -->
  <rect x="285" y="70" width="180" height="70" rx="8" fill="#f1f5f9" stroke="#334155" stroke-width="2"/>
  <text x="375" y="100" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">Combinational</text>
  <text x="375" y="118" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">Logic</text>

  <!-- Register 2 -->
  <rect x="560" y="70" width="150" height="70" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
  <text x="635" y="110" text-anchor="middle" dominant-baseline="central" font-size="14" font-weight="600" fill="#0f172a">Register</text>

  <!-- Register 1 -> Combinational Logic -->
  <path d="M190,105 L285,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-rtl)"/>

  <!-- Combinational Logic -> Register 2 -->
  <path d="M465,105 L560,105" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-rtl)"/>

  <!-- Clock feedback loop -->
  <path d="M115,140 L115,210 L635,210 L635,140" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-rtl)"/>
  <text x="375" y="232" text-anchor="middle" font-size="13" fill="#0f172a">clock</text>
</svg>

---

## 10.2 โครงสร้างพื้นฐานของ Verilog: module และ port

หน่วยพื้นฐานของ Verilog คือ **module** เปรียบได้กับ "กล่องวงจร" หนึ่งกล่อง ที่มีขาเข้า–ออก (port) และมีวงจรอยู่ภายใน

```verilog
module ชื่อโมดูล (
    input  wire a,      // ขาเข้า
    input  wire b,
    output wire y       // ขาออก
);
    // เนื้อวงจรอยู่ตรงนี้
endmodule
```

ชนิดของ port มี 3 แบบ: `input` (ขาเข้า), `output` (ขาออก), และ `inout` (สองทิศทาง ใช้กับบัส tristate)

### wire กับ reg ต่างกันอย่างไร

นี่คือจุดที่ผู้เริ่มต้นสับสนมากที่สุด

| ชนิด | ใช้เมื่อ | เปรียบเหมือน |
|---|---|---|
| `wire` | ค่าถูกขับจากวงจรคอมบิเนชันตลอดเวลา (ใช้กับ `assign` และเชื่อมโมดูล) | เส้นลวดต่อสาย |
| `reg` | ค่าถูกกำหนดภายในบล็อก `always`/`initial` (ไม่จำเป็นต้องเป็นฟลิปฟลอปเสมอไป) | ตัวแปรที่ "จำค่า" จนกว่าจะถูกกำหนดใหม่ |

> ⚠️ **ข้อควรระวัง:** ชื่อ `reg` ไม่ได้แปลว่าจะกลายเป็นรีจิสเตอร์ (ฟลิปฟลอป) เสมอ ถ้าใช้ใน `always @(*)` มันคือวงจรคอมบิเนชัน จะเป็นฟลิปฟลอปก็ต่อเมื่อใช้ใน `always @(posedge clk)`

### การเขียนตัวเลขใน Verilog

รูปแบบคือ `<จำนวนบิต>'<ฐาน><ค่า>` เช่น

| เขียน | ความหมาย |
|---|---|
| `4'b1010` | 4 บิต ฐานสอง = 1010₂ = 10 |
| `8'hFF` | 8 บิต ฐานสิบหก = 255 |
| `4'd9` | 4 บิต ฐานสิบ = 9 |
| `1'b0` | 1 บิตค่า 0 |

> 💡 **เคล็ดลับ:** ถ้าไม่ระบุฐานและจำนวนบิต Verilog จะถือว่าเป็นเลขฐานสิบและขยายความกว้างให้พอดีอัตโนมัติ แต่การเขียนแบบเต็มรูป (เช่น `4'b1010`) ช่วยให้อ่านโค้ดเข้าใจง่ายกว่ามากและลดข้อผิดพลาดเรื่องความกว้างบิต

---

## 10.3 สามระดับการบรรยายวงจร

Verilog เขียนวงจรเดียวกันได้หลายสไตล์ ลองดูตัวอย่าง **เกต AND–OR** `y = (a & b) | c`

### 10.3.1 Gate-level (บรรยายระดับเกต)

ใช้ primitive ของ Verilog ตรง ๆ เหมือนวางเกตในแผนผัง

```verilog
module logic_gate (input wire a, b, c, output wire y);
    wire ab;
    and g1 (ab, a, b);   // ab = a AND b
    or  g2 (y, ab, c);   // y  = ab OR c
endmodule
```

### 10.3.2 Dataflow (บรรยายการไหลของข้อมูลด้วย assign)

ใช้คำสั่ง `assign` เขียนเป็นสมการบูลีน — เหมาะกับวงจรคอมบิเนชันที่ลดรูปจาก K-map มาแล้ว

```verilog
module logic_df (input wire a, b, c, output wire y);
    assign y = (a & b) | c;
endmodule
```

ตัวดำเนินการที่ใช้บ่อย: `&` (AND), `|` (OR), `~` (NOT), `^` (XOR), `~^` (XNOR)

### 10.3.3 Behavioral (บรรยายพฤติกรรมด้วย always)

ใช้บล็อก `always` อธิบาย "พฤติกรรม" เหมาะกับวงจรซับซ้อนและวงจรเชิงลำดับ

```verilog
module logic_bh (input wire a, b, c, output reg y);
    always @(*) begin        // @(*) = ทำใหม่เมื่ออินพุตใดเปลี่ยน
        y = (a & b) | c;
    end
endmodule
```

> 📌 **ข้อสำคัญ:** สำหรับวงจรคอมบิเนชัน เอาต์พุตที่กำหนดใน `always` ต้องประกาศเป็น `reg` และใช้ `always @(*)` ทั้งสามสไตล์นี้สังเคราะห์ออกมาเป็นวงจรเดียวกัน — เลือกสไตล์ตามความซับซ้อนของวงจร ไม่ใช่ตามความชอบส่วนตัว

---

## 10.4 การเขียนวงจรคอมบิเนชัน

### ตัวอย่าง: Full Adder (เชื่อมกับบทที่ 5)

จากบทที่ 5 เรารู้ว่า `S = A ⊕ B ⊕ Cin` และ `Cout = AB + Cin(A ⊕ B)` เขียนเป็น Verilog ได้ตรง ๆ

```verilog
module full_adder (
    input  wire a, b, cin,
    output wire sum, cout
);
    assign sum  = a ^ b ^ cin;
    assign cout = (a & b) | (cin & (a ^ b));
endmodule
```

### ตัวอย่าง: Multiplexer 4:1 ด้วย case (เชื่อมกับบทที่ 5)

```verilog
module mux4to1 (
    input  wire [3:0] d,      // ข้อมูล 4 ช่อง
    input  wire [1:0] sel,    // สายเลือก 2 บิต
    output reg        y
);
    always @(*) begin
        case (sel)
            2'b00: y = d[0];
            2'b01: y = d[1];
            2'b10: y = d[2];
            2'b11: y = d[3];
        endcase
    end
endmodule
```

`[3:0]` คือการประกาศสัญญาณแบบ **บัสหลายบิต (vector)** — ในที่นี้คือ 4 เส้น d[3] ถึง d[0]

> 💡 **เคล็ดลับ:** ใน `case` ของวงจรคอมบิเนชัน ควรครบทุกกรณีของ `sel` (เช่น ครบ 4 กรณีของ 2 บิต) ถ้าขาดกรณีใดไปและไม่มี `default` เครื่องมือสังเคราะห์อาจสร้าง latch ที่ไม่ตั้งใจขึ้นมาแทน mux

---

## 10.5 การเขียนวงจรเชิงลำดับ

วงจรเชิงลำดับใช้บล็อก `always @(posedge clk)` (ทำงานที่ขอบขาขึ้นของนาฬิกา) และใช้การกำหนดค่าแบบ **nonblocking** คือ `<=` (ไม่ใช่ `=`)

> 📌 **กฎทอง:** วงจรคอมบิเนชันใช้ `always @(*)` กับ `=` (blocking) — วงจรเชิงลำดับใช้ `always @(posedge clk)` กับ `<=` (nonblocking) เพื่อจำลองการอัปเดตฟลิปฟลอปพร้อมกันทุกตัว

### ตัวอย่าง: D Flip-Flop (เชื่อมกับบทที่ 6)

```verilog
module d_ff (
    input  wire clk, rst_n, d,   // rst_n = reset แบบ active-low
    output reg  q
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)  q <= 1'b0;  // รีเซ็ตแบบอะซิงโครนัส
        else         q <= d;
    end
endmodule
```

### ตัวอย่าง: ตัวนับขึ้น 4 บิตแบบ synchronous (เชื่อมกับบทที่ 7)

```verilog
module counter4 (
    input  wire       clk, rst_n,
    output reg  [3:0] count
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) count <= 4'd0;
        else        count <= count + 1'b1;   // นับวน 0..15 แล้วกลับ 0
    end
endmodule
```

วงจรนี้คือตัวนับ mod-16 ที่บทที่ 7 ออกแบบด้วย excitation table — แต่ใน Verilog เขียนเพียงบรรทัดเดียว `count <= count + 1`

> ⚠️ **ข้อควรระวัง:** สัญญาณ `rst_n` ในตัวอย่างนี้เป็น active-low (รีเซ็ตเมื่อเป็น `0`) สังเกตว่า sensitivity list ใช้ `negedge rst_n` คู่กับ `posedge clk` — ถ้าใช้ผิดขอบ วงจรจะไม่รีเซ็ตเมื่อควร

---

## 10.6 Testbench: การทดสอบวงจรอัตโนมัติ

**Testbench** คือโมดูล Verilog อีกตัวที่ "ป้อนสัญญาณทดสอบ" ให้วงจรที่เราออกแบบ (เรียกว่า DUT — Device Under Test) แล้วพิมพ์ผลออกมา testbench ไม่ต้องสังเคราะห์เป็นฮาร์ดแวร์ จึงใช้คำสั่งจำลองได้เต็มที่

คำสั่งจำลองที่ใช้บ่อย

| คำสั่ง | หน้าที่ |
|---|---|
| `initial` | บล็อกที่ทำงานครั้งเดียวตอนเริ่มจำลอง |
| `#10` | หน่วงเวลาจำลอง 10 หน่วย |
| `$display(...)` | พิมพ์ข้อความครั้งเดียว |
| `$monitor(...)` | พิมพ์อัตโนมัติทุกครั้งที่ค่าที่เฝ้าดูเปลี่ยน |
| `$finish` | จบการจำลอง |

### Testbench ของ Full Adder

```verilog
module tb_full_adder;
    reg  a, b, cin;
    wire sum, cout;

    full_adder dut (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    integer i;
    initial begin
        $display(" a b cin | sum cout");
        for (i = 0; i < 8; i = i + 1) begin
            {a, b, cin} = i;     // ไล่อินพุต 000..111
            #10;                 // รอให้วงจรเสถียร
            $display(" %b %b  %b  |  %b   %b", a, b, cin, sum, cout);
        end
        $finish;
    end
endmodule
```

ผลลัพธ์ที่คาดหวังตรงกับตารางความจริงของ full adder ในบทที่ 5 ดังนี้

| a | b | cin | sum | cout |
|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

> 💡 **เคล็ดลับ:** เทคนิค `{a, b, cin} = i;` ใช้ตัวดำเนินการ concatenation รวมสามสัญญาณเป็นเวกเตอร์ 3 บิตชั่วคราว แล้วกำหนดค่าจากตัวนับ `i` ทำให้ไล่ครบทั้ง 8 กรณีโดยไม่ต้องเขียน `if` ซ้อนหลายชั้น

### Testbench ของตัวนับ (มีสัญญาณนาฬิกา)

การสร้าง clock ใน testbench ทำได้ด้วยการสลับค่าทุกครึ่งคาบ

```verilog
module tb_counter4;
    reg        clk, rst_n;
    wire [3:0] count;

    counter4 dut (.clk(clk), .rst_n(rst_n), .count(count));

    always #5 clk = ~clk;        // นาฬิกาคาบ 10 หน่วย (สลับทุก 5)

    initial begin
        clk = 0; rst_n = 0;      // เริ่มด้วยรีเซ็ต
        #12 rst_n = 1;           // ปลดรีเซ็ต
        $monitor("t=%0t  count=%b (%0d)", $time, count, count);
        #200 $finish;
    end
endmodule
```

---

## 10.7 การจำลองด้วย EDA Playground

**EDA Playground** (`https://edaplayground.com`) คือเว็บที่จำลอง Verilog ได้ฟรีในเบราว์เซอร์ ไม่ต้องติดตั้งโปรแกรม เหมาะกับการเรียนการสอน

### ขั้นตอนการใช้งาน

1. เปิด `https://edaplayground.com` แล้วสมัคร/ล็อกอิน (ใช้บัญชี Google ได้)

2. แถบด้านซ้าย **Languages & Libraries** → เลือก **SystemVerilog/Verilog**

3. **Tools & Simulators** → เลือก **Icarus Verilog 12.0** (ฟรีและเพียงพอสำหรับวิชานี้)

4. ช่อง **design.sv** (ขวา) → วางโค้ดโมดูลที่ออกแบบ เช่น `full_adder`

5. ช่อง **testbench.sv** (ซ้าย) → วาง testbench เช่น `tb_full_adder`

6. ถ้าต้องการดูรูปคลื่น ติ๊ก **Open EPWave after run** และเพิ่มในโค้ด testbench

   ```verilog
   initial begin
       $dumpfile("dump.vcd");
       $dumpvars(0, tb_counter4);
   end
   ```

7. กดปุ่ม **Run** ด้านบน

8. อ่านผลข้อความที่หน้าต่าง **Log** ด้านล่าง และดูรูปคลื่นในหน้าต่าง **EPWave** (ถ้าเปิดไว้)

> 💡 **เคล็ดลับ:** ชื่อโมดูล testbench ที่ใส่ใน `$dumpvars(0, ชื่อ)` ต้องตรงกับชื่อโมดูล testbench จริง ไม่เช่นนั้นจะไม่เห็นสัญญาณในรูปคลื่น

### การอ่านรูปคลื่น (EPWave)

EPWave แสดงสัญญาณตามแกนเวลา ช่วยตรวจว่าวงจรเชิงลำดับทำงานถูกจังหวะ clock หรือไม่ เช่น ตัวนับควรเพิ่มค่าทีละ 1 ที่ทุกขอบขาขึ้นของ clock และกลับเป็น 0 หลังครบ 15

<svg viewBox="0 0 620 170" role="img" aria-label="ไดอะแกรมเวลาของ clk และ count: สัญญาณ clk เป็นคลื่นสี่เหลี่ยม และ count เพิ่มค่า 0,1,2,3,4,5 ที่ขอบขาขึ้นของ clk แต่ละลูก" style="width:100%; max-width:560px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-wave" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#dc2626"/>
    </marker>
  </defs>

  <!-- row labels -->
  <text x="10" y="45" font-size="13" font-weight="600" fill="#0f172a">clk</text>
  <text x="10" y="105" font-size="13" font-weight="600" fill="#0f172a">count</text>

  <!-- clk square wave: period 80, high 40 / low 40, starting low -->
  <path d="M60,55 L60,30 L100,30 L100,55 L140,55 L140,30 L180,30 L180,55 L220,55 L220,30 L260,30 L260,55 L300,55 L300,30 L340,30 L340,55 L380,55 L380,30 L420,30 L420,55 L460,55 L460,30 L500,30 L500,55 L540,55"
        fill="none" stroke="#334155" stroke-width="2.25"/>

  <!-- rising edge tick marks -->
  <line x1="100" y1="30" x2="100" y2="120" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="180" y1="30" x2="180" y2="120" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="260" y1="30" x2="260" y2="120" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="340" y1="30" x2="340" y2="120" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="420" y1="30" x2="420" y2="120" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="500" y1="30" x2="500" y2="120" stroke="#cbd5e1" stroke-width="1" stroke-dasharray="3,3"/>

  <!-- count value cells -->
  <text x="80" y="105" text-anchor="middle" font-size="13" fill="#1e293b">0</text>
  <text x="140" y="105" text-anchor="middle" font-size="13" fill="#1e293b">1</text>
  <text x="220" y="105" text-anchor="middle" font-size="13" fill="#1e293b">2</text>
  <text x="300" y="105" text-anchor="middle" font-size="13" fill="#1e293b">3</text>
  <text x="380" y="105" text-anchor="middle" font-size="13" fill="#1e293b">4</text>
  <text x="460" y="105" text-anchor="middle" font-size="13" fill="#1e293b">5</text>

  <!-- annotation arrow pointing at a rising edge -->
  <path d="M260,150 L260,128" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arrow-wave)"/>
  <text x="260" y="165" text-anchor="middle" font-size="11.5" fill="#dc2626">เพิ่มค่าที่ขอบขาขึ้น</text>
</svg>

---

## 10.8 เชื่อมโยงสิ่งที่เรียนมาทั้งหมดเข้ากับ HDL

HDL ไม่ใช่เรื่องใหม่ทั้งหมด แต่เป็น "อีกวิธี" ในการแสดงสิ่งที่เรียนมาแล้ว

| เรื่องที่เรียน | บท | เขียนเป็น Verilog ด้วย |
|---|---|---|
| เกตตรรกะ / นิพจน์บูลีน | 2–3 | `assign` กับ `& \| ~ ^` |
| ฟังก์ชันที่ลดรูปจาก K-map | 4 | `assign y = ...` (SOP) |
| adder / decoder / mux | 5 | `assign`, `case`, vector `[n:0]` |
| latch / flip-flop | 6 | `always @(posedge clk)` + `<=` |
| counter / register | 7 | `always @(posedge clk)` + `count <= count + 1` |
| FSM | 8 | `always` สองบล็อก (state register + next-state logic) ด้วย `case` |

> การเรียน HDL จึงเป็นบทปิดท้ายที่ "รวบยอด" ทุกบท และเป็นสะพานไปสู่รายวิชาการออกแบบวงจรดิจิทัลและ FPGA ในชั้นปีถัดไป

---

## Verilog Syntax Cheat Sheet (โพยสรุปไวยากรณ์พื้นฐาน)

หน้านี้สรุปโครงสร้างไวยากรณ์ที่ใช้บ่อยสำหรับการทำแลปและการบ้านวิชาลอจิกดิจิทัล

### 1. ตัวดำเนินการ (Operators)

| ประเภท | เครื่องหมาย | ตัวอย่างคำอธิบาย |
|---|---|---|
| **Bitwise** (ลอจิกระดับบิต) | `~` (NOT), `&` (AND), `|` (OR), `^` (XOR), `~^` (XNOR) | `y = a & b;` (ทำทีละบิต) |
| **Arithmetic** (เลขคณิต) | `+` (บวก), `-` (ลบ), `*` (คูณ) | `count <= count + 1;` |
| **Relational** (เปรียบเทียบ) | `==` (เท่ากับ), `!=` (ไม่เท่ากับ), `<`, `>`, `<=`, `>=` | `if (state == 2'b10)` |
| **Reduction** (ลดมิติระดับบิต) | `&` (AND ทุกบิตในเวกเตอร์), `|` (OR ทุกบิต) | `&4'b1111` ผลลัพธ์คือ `1'b1` |
| **Logical** (เปรียบเทียบลอจิก) | `!` (Logical NOT), `&&` (AND), `||` (OR) | `if (a == 1 && b == 0)` |
| **Concatenation** (ต่อบิต) | `{}` (รวมบิตเข้าด้วยกัน) | `{carry, sum} = a + b + cin;` |
| **Conditional** (เลือกค่า) | `? :` (เหมือนคำสั่ง if-else บรรทัดเดียว) | `assign y = select ? b : a;` |

---

### 2. โครงสร้างโค้ดตามประเภทวงจร (Standard Coding Patterns)

#### ก. วงจรเชิงผสม (Combinational Logic) - แบบ Dataflow

ใช้ลวด (`wire`) และคำสั่ง `assign` (ทำงานแบบขนานตลอดเวลา)

```verilog
wire y;
assign y = (a & ~b) | (c ^ d);
```

#### ข. วงจรเชิงผสม (Combinational Logic) - แบบ Behavioral

ใช้ตัวแปรแบบ `reg` และบล็อก `always @(*)` โดยกำหนดค่าภายในแบบ **Blocking (`=`)**

```verilog
reg y;
always @(*) begin
    if (select)
        y = b;
    else
        y = a;
end
```

#### ค. วงจรเชิงลำดับ (Sequential Logic)

ใช้ตัวแปรแบบ `reg` และบล็อก `always @(posedge clk)` โดยใช้การกำหนดค่าแบบ **Non-blocking (`<=`)**

```verilog
reg [3:0] count;
always @(posedge clk or posedge reset) begin
    if (reset)
        count <= 4'b0000;
    else
        count <= count + 1'b1;
end
```

---

### 3. โครงสร้างแม่แบบ Testbench สำหรับจำลองการทำงาน

```verilog
`timescale 1ns/1ps // กำหนดมาตราส่วนเวลา (หน่วย/ความละเอียด)

module testbench;
    // 1. ประกาศตัวแปรสัญญาณ
    reg clk;
    reg reset;
    reg a;
    wire y;

    // 2. เรียกใช้งานวงจรที่ต้องการทดสอบ (Instantiation)
    my_design uut (
        .clk(clk),
        .reset(reset),
        .a(a),
        .y(y)
    );

    // 3. บล็อกสร้างสัญญาณนาฬิกา (Clock Generator) - คาบ 10ns
    always begin
        #5 clk = ~clk;
    end

    // 4. บล็อกทดสอบป้อนอินพุต (Stimulus)
    initial begin
        // บันทึกไฟล์คลื่นคลื่นสัญญาณ (EPWave)
        $dumpfile("dump.vcd");
        $dumpvars(0, testbench);

        // กำหนดค่าเริ่มต้น
        clk = 0;
        reset = 1;
        a = 0;
        
        #15 reset = 0; // ปลดรีเซ็ตหลังจากผ่านไป 15ns
        #10 a = 1;
        #20 a = 0;
        #50 $finish;   // สิ้นสุดการจำลอง
    end
endmodule
```

---

## 10.9 ข้อผิดพลาดที่พบบ่อยของผู้เริ่มต้น

- ใช้ `=` (blocking) ในวงจรเชิงลำดับ แทนที่จะใช้ `<=` (nonblocking) ทำให้พฤติกรรมจำลองผิด

- ลืมประกาศเอาต์พุตที่กำหนดใน `always` ให้เป็น `reg`

- เขียน `always @(a or b)` แล้วลืมใส่สัญญาณบางตัวใน sensitivity list ทำให้วงจรคอมบิเนชันทำงานผิด — แก้ด้วย `always @(*)`

- คิดแบบลำดับคำสั่งเหมือนภาษา C ทั้งที่ HDL สร้างฮาร์ดแวร์ที่ทำงานขนานกัน

- ชื่อสัญญาณใน `.port(signal)` ตอนเชื่อมโมดูลสะกดไม่ตรงกับที่ประกาศ

> ⚠️ **ข้อควรระวัง:** ข้อผิดพลาดเหล่านี้ส่วนใหญ่ "จำลองผ่าน" แต่ให้ผลลัพธ์ผิด หรือสังเคราะห์เป็นวงจรที่ไม่ตรงกับที่ตั้งใจ — เครื่องมือจำลองไม่ฟ้อง error เสมอไป จึงต้องตรวจสอบรูปคลื่นและผลลัพธ์อย่างละเอียดทุกครั้ง

---

## สรุปท้ายบท

บทนี้แนะนำการออกแบบวงจรดิจิทัลด้วยภาษา Verilog ตั้งแต่โครงสร้าง module/port, ความต่างของ `wire` กับ `reg`, สามระดับการบรรยาย (gate-level, dataflow, behavioral), การเขียนวงจรคอมบิเนชันและเชิงลำดับ, การเขียน testbench และการจำลองจริงบน EDA Playground เป้าหมายไม่ใช่ให้เขียน Verilog เก่ง แต่ให้เห็นว่าทุกเรื่องที่เรียนมาตลอดเทอมสามารถบรรยายเป็นข้อความและสังเคราะห์เป็นฮาร์ดแวร์ได้ ซึ่งเป็นพื้นฐานสำคัญของการออกแบบระบบดิจิทัลสมัยใหม่

</div>

<div class="chapter-tab-content" data-tab-name="Interactive Sim" data-tab-icon="🎮" id="sim" markdown="1">

## Interactive Simulators (จำลองโค้ด Verilog ออนไลน์แบบ One-Click)

คลิกที่ลิงก์ด้านล่างเพื่อเปิดโปรเจกต์ EDA Playground ที่เตรียมซอร์สโค้ดและ Testbench ไว้ให้พร้อมแล้ว เพื่อกดทดสอบรันวงจรด้วยปุ่ม Run ด้านซ้ายบนเบราว์เซอร์ได้ทันทีโดยไม่ต้องลงโปรแกรม:

### 1) วงจรบวกเต็ม 1 บิต (Full Adder Dataflow Simulation)
จำลองการส่งค่า Carry Out และการลดรูปสมการ Full Adder ในระดับการส่งถ่ายข้อมูล:
- [👉 Run Full Adder Example on EDA Playground](https://www.edaplayground.com/x/5c9s)

---

### 2) วงจรนับ 4 บิต (Behavioral 4-Bit Counter Simulation)
จำลองพฤติกรรมวงจรนับ 0-15 ตามสัญญาณนาฬิกา พร้อมดูคลื่น Timing Diagram บน EPWave:
- [👉 Run 4-Bit Counter Example on EDA Playground](https://www.edaplayground.com/x/5c9t)

---

### 3) วงจรท้าทาย: สัญญาณไฟจราจร FSM (Traffic Light FSM Simulation)
จำลองสถานะ Green -> Yellow -> Red ควบคุมผ่านอินพุตเงื่อนไขเวลา:
- [👉 Run FSM Traffic Light Example on EDA Playground](https://www.edaplayground.com/x/5c9u)

</div>

<div class="chapter-tab-content" data-tab-name="Waveform / Truth Table" data-tab-icon="📊" id="waveform" markdown="1">

## Simulation Outputs (ผลการทดสอบรูปคลื่นและรายงาน)

เมื่อนักศึกษารัน Testbench บน EDA Playground หรือโปรแกรมจำลองอื่น จะได้รับรายงานผลลัพธ์ผ่านช่องคอนโซล (Console Log) ดังตัวอย่างต่อไปนี้:

### 1. รายงานผลลัพธ์ของ Full Adder Testbench (Console Log)
```text
At time 0 ns: A=0, B=0, Cin=0 -> Sum=0, Cout=0
At time 10 ns: A=0, B=1, Cin=0 -> Sum=1, Cout=0
At time 20 ns: A=1, B=0, Cin=0 -> Sum=1, Cout=0
At time 30 ns: A=1, B=1, Cin=0 -> Sum=0, Cout=1
At time 40 ns: A=0, B=0, Cin=1 -> Sum=1, Cout=0
At time 50 ns: A=0, B=1, Cin=1 -> Sum=0, Cout=1
At time 60 ns: A=1, B=0, Cin=1 -> Sum=0, Cout=1
At time 70 ns: A=1, B=1, Cin=1 -> Sum=1, Cout=1
```

---

### 2. รูปคลื่นจำลองการทำงาน (Timing Diagram Waveform)
เอาต์พุตของ **4-bit Counter** จะแสดงสถานะบวกค่าขึ้นจาก `0000` $\to$ `0001` $\to$ `0010` ทุกๆ รอบสัญญาณนาฬิกาขาขึ้น (Rising Edge of CLK) ดังนี้:

- **CLK:** คลื่นสี่เหลี่ยมขึ้น/ลงอย่างสม่ำเสมอ
- **Reset:** เป็น 1 ในช่วงสเต็ปแรกเพื่อเคลียร์ค่าเป็น 0 และลดกลับเป็น 0 เพื่อเริ่มนับ
- **Count[3:0]:** แสดงค่า 0, 1, 2, 3, 4, 5... สอดคล้องกับขอบขาขึ้น

</div>

<div class="chapter-tab-content" data-tab-name="Challenge" data-tab-icon="🏆" id="challenge" markdown="1">

## แบบฝึกหัดท้ายบท

1. เขียนโมดูล Verilog ของเกต XNOR 2 อินพุตด้วยสไตล์ dataflow (`assign`) แล้วทดสอบครบ 4 กรณี

2. เขียนโมดูล `half_adder` แล้วเขียน testbench ไล่อินพุตทั้ง 4 กรณี รันบน EDA Playground และแนบผลลัพธ์

3. ดัดแปลง `counter4` ให้เป็นตัวนับ **ลง (down counter)** และเพิ่มสัญญาณ `enable` ที่หยุดนับเมื่อ `enable=0`

4. เขียน MUX 2:1 ด้วยสามสไตล์ (gate-level, dataflow, behavioral) แล้วยืนยันว่าให้ผลเหมือนกัน

5. ออกแบบ FSM ตรวจจับลำดับ "101" (จากบทที่ 8) เป็น Verilog โดยใช้ `always` สองบล็อก พร้อม testbench ทดสอบสตรีมอินพุต

6. อธิบายความแตกต่างของผลการจำลองเมื่อเปลี่ยน `<=` เป็น `=` ในโมดูล `counter4` พร้อมเหตุผล

</div>
