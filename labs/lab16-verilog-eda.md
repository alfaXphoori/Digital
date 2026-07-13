# 🔬 Lab 16: Verilog Simulation บน EDA Playground
## วัตถุประสงค์
- เขียนโมดูล Verilog สำหรับวงจรดิจิทัลพื้นฐานได้
- เขียน Testbench เพื่อทดสอบโมดูลได้
- รัน Simulation บน EDA Playground ได้
- อ่านผลจาก Console และ Waveform ด้วย EPWave ได้
- เชื่อมโยง Full Adder และ Counter ที่เคยต่อด้วย IC จริงกับ HDL
---
## อุปกรณ์/เครื่องมือ
| เครื่องมือ | รายละเอียด |
|:---|:---|
| EDA Playground | https://www.edaplayground.com |
| Simulator | Icarus Verilog หรือ Verilator |
| Waveform Viewer | เปิด **Open EPWave after run** |
| เอกสารประกอบ | บทที่ 5 Full Adder, บทที่ 7 Counter, บทที่ 10 Verilog HDL |
---
## ส่วนที่ 1: ทำความรู้จัก EDA Playground UI (10 นาที)
### ขั้นตอน
1. เปิดเว็บ **https://www.edaplayground.com**
2. ใช้ช่อง **design.sv** สำหรับใส่ Verilog module ที่ออกแบบ
3. ใช้ช่อง **testbench.sv** สำหรับใส่ code จำลอง input และตรวจ output
4. เลือกภาษาเป็น **SystemVerilog/Verilog**
5. เลือก Simulator เป็น **Icarus Verilog** หรือ **Verilator**
6. เปิด **Open EPWave after run** แล้วกด **Run**
| รายการ | ค่าที่ใช้ |
|:---|:---|
| Simulator | |
| เปิด EPWave after run? | |
| Run สำเร็จหรือไม่? | |
| เห็น Console output หรือไม่? | |
---
## ส่วนที่ 2: Lab ย่อย A — Full Adder (Combinational) (25 นาที)
Full Adder เป็นวงจรจาก **บทที่ 5** ที่เคยต่อด้วย IC Gate จริง ในส่วนนี้จะเขียนด้วย Verilog แทนการต่อสายบน Breadboard
### design.sv
```verilog
module full_adder(
    input  wire a,
    input  wire b,
    input  wire cin,
    output wire sum,
    output wire cout
);
    assign sum  = a ^ b ^ cin;
    assign cout = (a & b) | (a & cin) | (b & cin);
endmodule
```
### testbench.sv
```verilog
module testbench;
    reg a, b, cin;
    wire sum, cout;
    integer i;

    full_adder uut (.a(a), .b(b), .cin(cin), .sum(sum), .cout(cout));

    initial begin
        $dumpfile("full_adder.vcd");
        $dumpvars(0, testbench);
        $display("Time | a b cin | cout sum");
        $monitor("%4t | %b %b  %b  |   %b    %b", $time, a, b, cin, cout, sum);

        for (i = 0; i < 8; i = i + 1) begin
            {a, b, cin} = i;
            #10;
        end

        $display("Full Adder simulation finished.");
        $finish;
    end
endmodule
```
### ขั้นตอนการทดลอง
1. วาง code ทั้งสองไฟล์ให้ถูกช่อง แล้วกด **Run**
2. ดู Console ว่าไล่ครบ 8 กรณีหรือไม่
3. เปิด EPWave แล้วเพิ่มสัญญาณ `a`, `b`, `cin`, `sum`, `cout`
4. เปรียบเทียบ waveform กับตารางความจริงของ Full Adder
| a | b | cin | sum ที่คาดหวัง | cout ที่คาดหวัง | sum จาก Simulation | cout จาก Simulation | ถูกต้อง? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 0 | 0 | 0 | | | |
| 0 | 0 | 1 | 1 | 0 | | | |
| 0 | 1 | 0 | 1 | 0 | | | |
| 0 | 1 | 1 | 0 | 1 | | | |
| 1 | 0 | 0 | 1 | 0 | | | |
| 1 | 0 | 1 | 0 | 1 | | | |
| 1 | 1 | 0 | 0 | 1 | | | |
| 1 | 1 | 1 | 1 | 1 | | | |
📸 **Screenshot Console และ EPWave ของ Full Adder**
---
## ส่วนที่ 3: Lab ย่อย B — 4-bit Counter (Sequential) (35 นาที)
Counter เป็นวงจรจาก **บทที่ 7** ที่เคยต่อด้วย Flip-Flop จริง ใน Verilog จะเขียนพฤติกรรมด้วย `always @(posedge clk)`
### design.sv
```verilog
module counter4(
    input  wire clk,
    input  wire rst,
    output reg  [3:0] q
);
    always @(posedge clk) begin
        if (rst) q <= 4'b0000;
        else q <= q + 1'b1;
    end
endmodule
```
### testbench.sv
```verilog
module testbench;
    reg clk, rst;
    wire [3:0] q;

    counter4 uut (.clk(clk), .rst(rst), .q(q));

    initial clk = 0;
    always #5 clk = ~clk;

    initial begin
        $dumpfile("counter4.vcd");
        $dumpvars(0, testbench);
        $display("Time | rst clk | q");
        $monitor("%4t |  %b   %b  | %b (%0d)", $time, rst, clk, q, q);

        rst = 1;
        #12;
        rst = 0;
        #160;
        rst = 1;
        #10;
        rst = 0;
        #50;

        $display("Counter simulation finished.");
        $finish;
    end
endmodule
```
### ขั้นตอนการทดลอง
1. วาง code ใหม่ใน **design.sv** และ **testbench.sv**
2. กด **Run** แล้วดู Console ว่า `q` เพิ่มค่าทีละ 1 หลังปล่อย reset
3. เปิด EPWave แล้วเพิ่มสัญญาณ `clk`, `rst`, `q`
4. ขยาย waveform เพื่อดูว่า `q` เปลี่ยนเฉพาะที่ขอบขาขึ้นของ `clk`
5. สังเกตว่าเมื่อ `rst = 1` ค่า `q` กลับเป็น `0000`
| Clock Rising Edge | rst | q ที่คาดหวัง | q จาก Simulation | Decimal | ถูกต้อง? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Reset | 1 | 0000 | | 0 | |
| 1 | 0 | 0001 | | 1 | |
| 2 | 0 | 0010 | | 2 | |
| 3 | 0 | 0011 | | 3 | |
| 4 | 0 | 0100 | | 4 | |
| 5 | 0 | 0101 | | 5 | |
| 6 | 0 | 0110 | | 6 | |
| 7 | 0 | 0111 | | 7 | |
| 8 | 0 | 1000 | | 8 | |
| 15 | 0 | 1111 | | 15 | |
| 16 | 0 | 0000 | | 0 | |
| Reset อีกครั้ง | 1 | 0000 | | 0 | |
📸 **Screenshot EPWave ที่เห็น `clk`, `rst`, `q` ชัดเจน**
---
## ส่วนที่ 4: วิเคราะห์ Waveform (10 นาที)
| สัญญาณ | สิ่งที่ต้องสังเกตใน EPWave |
|:---|:---|
| `clk` | เปลี่ยนทุก 5 time units ทำให้คาบเท่ากับ 10 time units |
| `rst` | เมื่อเป็น 1 ทำให้ Counter กลับ 0000 |
| `q[3:0]` | เปลี่ยนเฉพาะที่ขอบขาขึ้นของ clock |
| `sum`, `cout` | เปลี่ยนตาม input ทันทีเพราะเป็น combinational logic |
**คำถาม:** Full Adder กับ Counter ต่างกันอย่างไรเมื่อดูจาก waveform?
คำตอบ: _________________________________________________________
---
## ส่วนที่ 5: Debugging Guide (5 นาที)
| ปัญหา | ตรวจสอบ |
|:---|:---|
| กด Run แล้ว module ไม่พบ | ชื่อ module ใน design ตรงกับชื่อที่เรียกใน testbench หรือไม่ |
| EPWave ไม่เปิด | ติ๊ก **Open EPWave after run** แล้วหรือยัง |
| Waveform ว่าง | มี `$dumpfile` และ `$dumpvars` ใน testbench หรือไม่ |
| Counter ไม่เพิ่มค่า | มี `always #5 clk = ~clk;` หรือไม่ |
| Counter ไม่ reset | ต่อสัญญาณ `rst` เข้ากับ module ถูกชื่อหรือไม่ |
---
## คำถามท้าย Lab
1. `wire` กับ `reg` ใน Verilog ใช้ต่างกันอย่างไร? ______________________________________
2. ทำไมวงจร Counter จึงต้องมีสัญญาณ `reset`? ______________________________________
3. ใน sequential logic เหตุใดจึงนิยมใช้ non-blocking assignment (`<=`)? ______________________________________
4. Blocking assignment (`=`) กับ non-blocking assignment (`<=`) ต่างกันอย่างไร? ______________________________________
5. การดู waveform ช่วยให้ debug วงจรดิจิทัลได้ดีกว่าดู Console อย่างเดียวอย่างไร? ______________________________________
---
## งานท้าทาย (Optional / Bonus) ⭐
1. เขียนโมดูล **2-to-1 MUX** ด้วย `assign` แล้วสร้าง testbench ทดสอบครบทุกกรณี
2. เขียนโมดูล **D Flip-Flop** ด้วย `always @(posedge clk)` พร้อม reset
3. แก้ Counter ให้เป็น **MOD-10 Counter** นับ 0 ถึง 9 แล้ววนกลับ 0
---
## การส่งงาน
> 📋 **ส่งงานผ่าน Google Form**
### ขั้นตอน
1. ถ่าย Screenshot หน้า EDA Playground ของ Full Adder และ Counter
2. ถ่าย Screenshot Console output และ EPWave ของทั้ง 2 lab ย่อย
3. กรอกตารางผลการทดลองและคำถามท้าย Lab
### Checklist ก่อนกด Submit
- [ ] Full Adder simulation รันครบ 8 กรณี
- [ ] ตาราง Full Adder กรอกครบ
- [ ] Counter simulation เห็น `clk`, `rst`, `q`
- [ ] ตาราง Counter กรอกครบ
- [ ] Screenshot Console และ EPWave ครบ
- [ ] ตอบคำถามท้าย Lab ครบ
