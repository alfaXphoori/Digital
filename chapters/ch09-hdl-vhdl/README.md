# Chapter 9: การออกแบบด้วย VHDL และการจำลองด้วย vhdl.ai

## Hardware Description Language: VHDL & VHDLive (vhdl.ai)

---

**รายวิชา:** ตรรกศาสตร์ของดิจิตอลคอมพิวเตอร์ (Digital Computer Logic)
**หลักสูตร:** วิศวกรรมเมคคาทรอนิกส์ ชั้นปีที่ 1
**บทที่:** 9 — สัปดาห์ที่ 13

---

<div class="chapter-tab-content" data-tab-name="Concept" data-tab-icon="💡" id="concept" markdown="1">

## 9.1 บทนำ: การออกแบบวงจรดิจิทัลด้วย VHDL

ตลอดแปดบทที่ผ่านมา เราออกแบบวงจรดิจิทัลด้วยการวาด **แผนผังวงจร (schematic)** คือวางเกตทีละตัวแล้วลากสายเชื่อม วิธีนี้เห็นภาพดีสำหรับวงจรเล็ก แต่เมื่อระบบใหญ่ขึ้น เช่น หน่วยประมวลผลที่มีเกตหลายล้านตัว การวาดมือเป็นไปไม่ได้เลย

**ภาษาบรรยายฮาร์ดแวร์ (Hardware Description Language: HDL)** คือภาษาที่ใช้ "เขียนบรรยาย" พฤติกรรมและโครงสร้างของวงจรดิจิทัลเป็นข้อความ แล้วให้เครื่องมือแปลงข้อความนั้นเป็นวงจรเกตจริงโดยอัตโนมัติ ในบทนี้เราใช้ **VHDL** (VHSIC Hardware Description Language) ร่วมกับโปรแกรมจำลองบนเว็บ [vhdl.ai](https://vhdl.ai/vhdlive) ซึ่งไม่ต้องติดตั้งโปรแกรมใด ๆ

เหตุผลที่วิศวกรควรรู้จักและอ่าน VHDL ออก

| ประเด็น | เหตุผล |
|---|---|
| **งานภาครัฐ/การบิน/ยุโรป** | โครงการด้านอวกาศ การบิน และงานทหาร นิยม VHDL เพราะตรวจสอบชนิดข้อมูลเข้มงวด ปลอดภัยสูง |
| **โค้ดเก่าในโรงงาน** | ระบบควบคุมจำนวนมากเขียนด้วย VHDL มาตั้งแต่ยุค 1990 และยังใช้งานอยู่ |
| **เครื่องมือมาตรฐาน** | Vivado / Quartus / GHDL รองรับ VHDL อย่างสมบูรณ์ และสังเคราะห์ลง FPGA ได้จริง |
| **คิดแบบฮาร์ดแวร์จริง** | VHDL บังคับให้คิดถึงชนิดข้อมูล ขนาดบิต และทิศทางสัญญาณอย่างชัดเจน |

> 💡 **ข้อความสำคัญที่สุดของบทนี้** — VHDL **บรรยายวงจร** ไม่ใช่ **ลำดับคำสั่ง** โค้ดทุกบรรทัดที่อยู่ระหว่าง `begin` กับ `end architecture` ทำงาน **พร้อมกันทั้งหมด** สลับลำดับบรรทัดแล้ววงจรไม่เปลี่ยน

### เส้นทางของโค้ด (design flow)

```text
เขียน RTL  →  Testbench + Simulation  →  Synthesis  →  Place & Route  →  FPGA
   ▲                    ▲
   └────── วันนี้อยู่ที่สองกล่องนี้ ──────┘
```

วันนี้เราหยุดที่ **simulation** ส่วนกล่องที่เหลือมีไว้ให้เห็นภาพว่าข้อความที่พิมพ์จะกลายเป็นวงจรจริงได้อย่างไร

---

## 9.2 entity กับ architecture: กล่องวงจรหนึ่งกล่อง

ไฟล์ VHDL ทุกไฟล์มีสองส่วนเสมอ

- **`entity`** = **หน้าตาของกล่อง** มีขาอะไรบ้าง เข้าหรือออก กว้างกี่บิต
- **`architecture`** = **สิ่งที่อยู่ในกล่อง** วงจรข้างในทำงานอย่างไร

<svg viewBox="0 0 700 250" role="img" aria-label="ไดอะแกรมแสดงว่า entity คือกรอบกล่องพร้อมขาสัญญาณเข้า a b และขาออก y ส่วน architecture คือวงจรที่อยู่ภายในกล่อง" style="width:100%; max-width:660px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-ent" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- entity box -->
  <rect x="200" y="55" width="300" height="140" rx="10" fill="#eef2ff" stroke="#4f46e5" stroke-width="2.5"/>
  <text x="350" y="42" text-anchor="middle" font-size="14" font-weight="700" fill="#4f46e5">entity — หน้าตาของกล่อง (port)</text>

  <!-- architecture inner box -->
  <rect x="240" y="88" width="220" height="80" rx="8" fill="#ffffff" stroke="#334155" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="350" y="122" text-anchor="middle" font-size="13.5" font-weight="600" fill="#0f172a">architecture</text>
  <text x="350" y="142" text-anchor="middle" font-size="12.5" fill="#475569">y &lt;= a and b;</text>

  <!-- input pins -->
  <path d="M90,100 L200,100" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-ent)"/>
  <path d="M90,150 L200,150" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-ent)"/>
  <text x="80" y="104" text-anchor="end" font-size="13" font-weight="600" fill="#0f172a">a : in</text>
  <text x="80" y="154" text-anchor="end" font-size="13" font-weight="600" fill="#0f172a">b : in</text>

  <!-- output pin -->
  <path d="M500,125 L610,125" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-ent)"/>
  <text x="620" y="129" font-size="13" font-weight="600" fill="#0f172a">y : out</text>

  <text x="350" y="222" text-anchor="middle" font-size="12.5" fill="#64748b">entity ตัวเดียวมีได้หลาย architecture — วงจรเดียวกัน เขียนได้หลายสไตล์</text>
</svg>

```vhdl
library ieee;                       -- ต้องมีทุกไฟล์
use ieee.std_logic_1164.all;        -- เพื่อใช้ชนิด std_logic

entity and2 is
  port ( a, b : in  std_logic;      -- ขาเข้า
         y    : out std_logic );    -- ขาออก
end entity;

architecture rtl of and2 is         -- "rtl" คือชื่อ architecture ตั้งเองได้
begin
  y <= a and b;                     -- <= คือ "ต่อสายจากขวาไปซ้าย"
end architecture;
```

### สามจุดที่นักศึกษาสะดุดบ่อยที่สุดในสามบรรทัดแรก

1. **`library ieee; use ieee.std_logic_1164.all;` ลืมไม่ได้** — ถ้าไม่ประกาศ จะไม่รู้จักชนิด `std_logic` เลยและคอมไพล์ไม่ผ่านทันที
2. **`<=` ไม่ใช่ "น้อยกว่าหรือเท่ากับ"** — ในบริบทของสัญญาณ มันคือการ **ต่อสาย/ขับค่า** เทียบได้กับ `assign` ของ Verilog
3. **ชื่อ architecture ตั้งเองได้** — นิยมใช้ `rtl`, `behavioral`, `structural` ตามสไตล์ที่เขียนข้างใน

| Verilog | VHDL |
|---|---|
| `module and2 (...); ... endmodule` | `entity and2 is ... end entity;` + `architecture ... end architecture;` |
| `assign y = a & b;` | `y <= a and b;` |
| `input wire a` | `a : in std_logic` |
| `output wire y` | `y : out std_logic` |

---

## 9.3 ชนิดข้อมูลที่ต้องรู้เพียงสามอย่าง

### std_logic — สายไฟหนึ่งเส้น

`std_logic` มี **9 ค่า** แต่ในวิชานี้ใช้จริงเพียงไม่กี่ค่า

| ค่า | ความหมาย | เจอเมื่อไร |
|:---:|---|---|
| `'0'` `'1'` | ลอจิกต่ำ / สูง | ตลอดเวลา |
| `'U'` | Uninitialized — ยังไม่เคยถูกกำหนดค่า | ช่วงต้นการจำลองก่อน reset |
| `'X'` | Unknown — ขัดแย้งกัน | มีคนขับสายเดียวกันสองทาง (หัวข้อ 9.11) |
| `'Z'` | High impedance — ลอย | บัสสามสถานะ (บทที่ 2) |
| `'-'` | Don't care | ใช้ตอนสังเคราะห์ (บทที่ 4) |

> ⚠️ **ทำไมช่วงแรกของ waveform ถึงเป็นสีแดงหรือเขียนว่า `U`?** เพราะ `std_logic` ที่ยังไม่ถูกกำหนดค่าเริ่มต้นจะเป็น `'U'` ไม่ใช่ `'0'` นี่ไม่ใช่บั๊ก แต่คือการเตือนว่า "ฟลิปฟลอปจริงก็ไม่รู้ว่าตัวเองเก็บค่าอะไรก่อนถูกรีเซ็ต" — เป็นเหตุผลว่าทำไมวงจรจริงต้องมีสาย reset

### std_logic_vector — สายไฟหลายเส้นมัดรวมกัน

```vhdl
signal d : std_logic_vector(3 downto 0);   -- สายไฟ 4 เส้น: d(3) d(2) d(1) d(0)
```

`3 downto 0` คือ **สายไฟ 4 เส้น** ไม่ใช่ array ในภาษาโปรแกรม `d(0)` คือเส้นที่ 0 เขียนค่าทั้งก้อนด้วยเครื่องหมายอัญประกาศคู่ เช่น `d <= "1010";` (สายเส้นเดียวใช้อัญประกาศเดี่ยว `'1'`)

### unsigned / signed — เมื่อต้องการบวกเลข

**`std_logic_vector` บวกเลขไม่ได้** เพราะมันคือ "มัดสายไฟ" ไม่ใช่ "ตัวเลข" ถ้าจะบวกต้องแปลงเป็น `unsigned` หรือ `signed` จากไลบรารีมาตรฐาน `numeric_std`

```vhdl
use ieee.numeric_std.all;

signal cnt : unsigned(3 downto 0);
...
cnt <= cnt + 1;                    -- บวกได้ เพราะเป็น unsigned
q   <= std_logic_vector(cnt);      -- แปลงกลับตอนส่งออกขา
```

> 📌 **ห้ามใช้ `std_logic_arith` หรือ `std_logic_unsigned`** ที่เห็นในโค้ดเก่าตามอินเทอร์เน็ต ทั้งสองตัวเป็นของเฉพาะผู้ผลิต ไม่ใช่มาตรฐาน IEEE และทำให้โค้ดย้ายเครื่องมือไม่ได้ — ใช้ **`numeric_std`** เท่านั้น

---

## 9.4 ตัวอย่าง 0 — เกตพื้นฐาน

**สอน:** `entity`/`architecture` ครั้งแรก, operator พื้นฐาน, ความหมายของ `<=`, ดู waveform ครั้งแรก

### ขั้นที่ 1 — เกตเดียว (ให้พิมพ์ตามทีละบรรทัด)

ใช้โค้ด `and2` ในหัวข้อ 9.2 ได้เลย ให้นักศึกษาพิมพ์เองทั้งหมด อย่าให้คัดลอกวาง เพราะครั้งแรกคือครั้งเดียวที่จะได้จำโครงไฟล์

### ขั้นที่ 2 — รวมทุกเกตไว้ในโมดูลเดียว

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity gates is
  port ( a, b : in  std_logic;
         y_and, y_or, y_not, y_nand, y_nor, y_xor, y_xnor : out std_logic );
end entity;

architecture rtl of gates is
begin
  y_and  <= a and b;
  y_or   <= a or b;
  y_not  <= not a;
  y_nand <= a nand b;
  y_nor  <= a nor b;
  y_xor  <= a xor b;
  y_xnor <= a xnor b;
end architecture;
```

**Testbench** (อาจารย์เตรียมให้ ยังไม่ต้องอธิบายละเอียด เก็บไว้อธิบายในตัวอย่าง 1)

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_gates is end entity;

architecture sim of tb_gates is
  signal a, b : std_logic;
  signal y_and, y_or, y_not, y_nand, y_nor, y_xor, y_xnor : std_logic;
begin
  uut: entity work.gates
    port map (a, b, y_and, y_or, y_not, y_nand, y_nor, y_xor, y_xnor);

  process begin
    a <= '0'; b <= '0'; wait for 10 ns;
    a <= '0'; b <= '1'; wait for 10 ns;
    a <= '1'; b <= '0'; wait for 10 ns;
    a <= '1'; b <= '1'; wait for 10 ns;
    wait;
  end process;
end architecture;
```

### จุดที่ต้องเน้น

- **7 บรรทัดใน `gates` คือเกต 7 ตัวที่วางอยู่บนบอร์ดพร้อมกัน** ไม่มีบรรทัดไหน "ทำงานก่อน" — ลองสลับลำดับบรรทัดแล้วรันใหม่ ผลเหมือนเดิมทุกประการ
- **VHDL มี operator ครบทุกเกต** ทั้ง `and or not nand nor xor xnor` เป็นคำสงวนหมด ไม่ต้องประกอบเอง (ต่างจาก Verilog ที่ไม่มี `nand` เป็น operator)
- **Operator ตรรกะทุกตัวมีลำดับความสำคัญเท่ากัน จึงต้องใส่วงเล็บเสมอ**

```vhdl
y <= a and b or c;        -- ❌ คอมไพล์ไม่ผ่าน
y <= (a and b) or c;      -- ✅ ถูกต้อง
```

ข้อความ error จริงจาก GHDL คือ

```text
error: only one type of logical operators may be used to combine relation
  y <= a and b or c;
               ^
```

> 🔎 **ให้โชว์ error นี้ในคาบจริง** — นี่คือจุดที่ VHDL ต่างจาก Verilog ชัดที่สุด VHDL ไม่ยอมเดาใจเราว่า `and` มาก่อน `or` แต่บังคับให้เขียนให้ชัด ปรัชญานี้คือเหตุผลที่งานความปลอดภัยสูงเลือก VHDL

**ลองด้วยตนเอง:** เขียน `y <= (a and b) or ((not a) and c);` แล้วทายก่อนดู waveform ว่านี่คือวงจรอะไร
(คำตอบ: **mux 2:1** ที่มี `a` เป็นสายเลือก — ซึ่งเชื่อมไปยังตัวอย่าง 2 พอดี)

---

## 9.5 ตัวอย่าง 1 — Half Adder

**สอน:** การตั้งชื่อวงจรจากวงจรย่อย, อ่าน testbench ให้เข้าใจ, `assert`

เปิดหัวข้อนี้ด้วยการวาด half adder จาก XOR + AND บนกระดาน แล้วชี้ว่าโค้ดข้างล่างคือ **เกตสองตัวจากตัวอย่าง 0 ที่ถูกนำมาตั้งชื่อใหม่** — นี่คือครั้งแรกที่เรา "ห่อวงจรย่อยเป็นกล่องใหม่" ซึ่งจะกลายเป็นการประกอบโมดูลในตัวอย่าง 4

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity half_adder is
  port ( a, b  : in  std_logic;
         sum   : out std_logic;
         carry : out std_logic );
end entity;

architecture rtl of half_adder is
begin
  sum   <= a xor b;   -- ทำงานพร้อมกัน สลับบรรทัดผลเหมือนเดิม
  carry <= a and b;
end architecture;
```

### Testbench template (ใช้โครงนี้ทั้งคาบ)

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_half_adder is end entity;      -- โต๊ะทดลอง ไม่มีขา

architecture sim of tb_half_adder is
  signal a, b, sum, carry : std_logic;
begin
  uut: entity work.half_adder port map (a, b, sum, carry);

  process begin
    a <= '0'; b <= '0'; wait for 10 ns;
    a <= '0'; b <= '1'; wait for 10 ns;
    a <= '1'; b <= '0'; wait for 10 ns;
    a <= '1'; b <= '1'; wait for 10 ns;
    assert (sum = '0' and carry = '1')
      report "1+1 should give carry" severity error;
    wait;   -- หยุดกระบวนการนี้ถาวร = จบ simulation
  end process;
end architecture;
```

### จุดที่ต้องเน้น

| สิ่งที่เห็นในโค้ด | ความหมาย |
|---|---|
| `entity tb_half_adder is end entity;` | testbench **ไม่มี port** เพราะเป็นโต๊ะทดลอง ไม่ใช่วงจรที่จะเอาไปลงชิป |
| `uut: entity work.half_adder port map (...)` | `uut` = unit under test คือการหยิบวงจรมาวางบนโต๊ะแล้วต่อสาย |
| `wait for 10 ns;` | ใช้ได้ **เฉพาะใน testbench** วงจรจริงสังเคราะห์คำสั่งนี้ไม่ได้ |
| `assert ... report ... severity error;` | ให้ simulator ตรวจคำตอบแทนสายตาเรา — สำคัญมากเมื่อวงจรใหญ่ขึ้น |
| `wait;` บรรทัดสุดท้าย | ไม่มีบรรทัดนี้ process จะวนกลับไปทำซ้ำตั้งแต่ต้นไม่รู้จบ |

> ⚠️ **ข้อความใน `report "..."` ต้องเป็นภาษาอังกฤษล้วน** VHDL รับเฉพาะอักขระ ASCII ในสตริง (comment เขียนไทยได้) ถ้าพิมพ์ภาษาไทยลงไป จะได้ error จริงว่า
> ```text
> error: invalid character not allowed, even in a string
> ```

> 💡 **assert ผ่านแล้วเงียบ** — ถ้ารันแล้ว log ไม่ขึ้นอะไรเลย แปลว่าผ่านหมด ไม่ใช่ว่าไม่ได้รัน ถ้าอยากเห็นผลเป็นตาราง ให้ใช้ testbench แบบพิมพ์ตารางในแท็บ **Interactive Sim**

**ลองเอง:** เพิ่มขา `cin` ให้กลายเป็น **full adder** แล้วเขียน `assert` ให้ครบทั้ง 8 กรณี

---

## 9.6 ตัวอย่าง 2 — Mux 4:1 สองสไตล์

**สอน:** `std_logic_vector`, `with-select`, `process` + `case`, sensitivity list

วงจรเดียวกันเขียนได้สองสไตล์ และ **สังเคราะห์ออกมาเป็น mux ตัวเดียวกันเป๊ะ** — ให้เห็นว่าสไตล์คือเรื่องการอ่านง่าย ไม่ใช่เรื่องวงจร

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity mux4 is
  port ( d   : in  std_logic_vector(3 downto 0);
         sel : in  std_logic_vector(1 downto 0);
         y   : out std_logic );
end entity;

-- สไตล์ A: concurrent statement
architecture style_a of mux4 is
begin
  with sel select
    y <= d(0) when "00",
         d(1) when "01",
         d(2) when "10",
         d(3) when others;      -- others ขาดไม่ได้
end architecture;

-- สไตล์ B: process (พฤติกรรมเดียวกัน วงจรเดียวกัน)
architecture style_b of mux4 is
begin
  process(d, sel)               -- sensitivity list ต้องมีทุก input ที่อ่าน
  begin
    case sel is
      when "00"   => y <= d(0);
      when "01"   => y <= d(1);
      when "10"   => y <= d(2);
      when others => y <= d(3);
    end case;
  end process;
end architecture;
```

### Testbench

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_mux4 is end entity;

architecture sim of tb_mux4 is
  signal d   : std_logic_vector(3 downto 0) := "1010";  -- d(3)=1 d(2)=0 d(1)=1 d(0)=0
  signal sel : std_logic_vector(1 downto 0);
  signal y   : std_logic;
begin
  -- ระบุ architecture ที่จะทดสอบในวงเล็บ เปลี่ยนเป็น style_b แล้วรันซ้ำ ผลต้องเหมือนกัน
  uut: entity work.mux4(style_a) port map (d => d, sel => sel, y => y);

  process begin
    sel <= "00"; wait for 10 ns;
    assert y = d(0) report "sel=00 should select d(0)" severity error;
    sel <= "01"; wait for 10 ns;
    assert y = d(1) report "sel=01 should select d(1)" severity error;
    sel <= "10"; wait for 10 ns;
    assert y = d(2) report "sel=10 should select d(2)" severity error;
    sel <= "11"; wait for 10 ns;
    assert y = d(3) report "sel=11 should select d(3)" severity error;

    d <= "0101"; wait for 10 ns;   -- เปลี่ยน d ขณะ sel ค้างที่ 11 → y ต้องตาม d(3) ทันที
    assert y = '0' report "y must follow d(3) when d changes" severity error;
    wait;
  end process;
end architecture;
```

> 📌 **ถ้าไม่ระบุ `(style_a)`** simulator จะเลือก architecture ที่ **วิเคราะห์ล่าสุด** (ตัวที่อยู่ล่างสุดในไฟล์) นักศึกษาจะงงมากว่าทำไมแก้ `style_a` แล้วผลไม่เปลี่ยน — นี่คือความสามารถที่ Verilog ไม่มี และเป็นเหตุผลที่ VHDL เหมาะกับการเทียบสองสถาปัตยกรรมในไฟล์เดียว

### จุดที่ต้องเน้น

- **`3 downto 0` คือสายไฟ 4 เส้น** ไม่ใช่ array ในภาษาโปรแกรม `d(0)` คือเส้นที่ 0
- **`process` ยังเป็นวงจร concurrent เมื่อมองจากข้างนอก** ข้างในแค่เขียนเรียงบรรทัดให้อ่านง่าย ทั้งไฟล์มี `process` กี่ตัวก็ทำงานพร้อมกันหมด
- **ลบ `when others` ออกให้ดู** → คอมไพเลอร์ฟ้องทันที ข้อความจริงคือ

  ```text
  error: missing choice(s)
      y <= d(0) when "00",
                ^
  ```

  เพราะ `std_logic` มี 9 ค่า การไล่ `"00" "01" "10" "11"` จึงยัง **ไม่ครบทุกกรณี** ในสายตาของ VHDL

- **ตัด `d` ออกจาก sensitivity list ให้ดู** → simulation ให้ค่าค้าง (stale) แต่ synthesis ยังได้วงจรถูก นี่คือความไม่ตรงกันที่อันตรายที่สุดของวงจรคอมบิเนชัน ผลรันจริงเทียบกันอยู่ในแท็บ **Waveform / Truth Table**

> ⭐ **ทางแก้ของ VHDL-2008: `process(all)`** — เขียนแค่นี้แล้วเครื่องมือใส่สัญญาณทุกตัวที่อ่านให้เองอัตโนมัติ ลืมไม่ได้อีกต่อไป (เทียบเท่า `always @(*)` ของ Verilog) **ให้ใช้ `process(all)` กับวงจรคอมบิเนชันเสมอ** และเก็บ sensitivity list แบบเขียนเองไว้ใช้กับวงจรเชิงลำดับเท่านั้น

**ลองเอง:** เขียน decoder 2:4 ด้วยสไตล์ที่ถนัด (เอาต์พุตเป็น `std_logic_vector(3 downto 0)`)

---

## 9.7 ตัวอย่าง 3 — ฟลิปฟลอป D / T / JK

**สอน:** `rising_edge`, asynchronous reset, enable, signal ภายใน

> ⭐ **ข้อความหลักของช่วงนี้:** ทุก `process` ที่มี `rising_edge(clk)` คือ **ฟลิปฟลอปหนึ่งชุด** และฟลิปฟลอปทุกชนิดคือ **D-FF ตัวเดียวกัน ต่างกันแค่ลอจิกหน้าขา D**

### D flip-flop

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity dff is
  port ( clk, rst, en, d : in  std_logic;
         q               : out std_logic );
end entity;

architecture rtl of dff is
begin
  process(clk, rst)
  begin
    if rst = '1' then                 -- asynchronous reset: ไม่รอ clock
      q <= '0';
    elsif rising_edge(clk) then       -- ทุกอย่างในบล็อกนี้กลายเป็นฟลิปฟลอป
      if en = '1' then
        q <= d;                       -- ไม่มี else → ค่าเดิมค้าง = หน่วยความจำ
      end if;
    end if;
  end process;
end architecture;
```

> 📌 **sensitivity list ของวงจรเชิงลำดับมีแค่ `(clk, rst)`** ห้ามใส่ `d` หรือ `en` เพราะฟลิปฟลอปจะไม่สนใจอินพุตเลยจนกว่าจะถึงขอบนาฬิกา นี่คือกรณีเดียวที่ sensitivity list "ไม่ครบ" แล้วถูกต้อง — และเป็นเหตุผลว่าทำไม `process(all)` ใช้กับวงจรเชิงลำดับไม่ได้

### T flip-flop

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tff is
  port ( clk, rst, t : in  std_logic;
         q           : out std_logic );
end entity;

architecture rtl of tff is
  signal q_int : std_logic := '0';   -- signal ภายใน เพื่ออ่านค่าปัจจุบันกลับมาใช้
begin
  process(clk, rst)
  begin
    if rst = '1' then q_int <= '0';
    elsif rising_edge(clk) then
      if t = '1' then q_int <= not q_int; end if;
    end if;
  end process;
  q <= q_int;                        -- ต่อออกขาจริง
end architecture;
```

> ⚠️ **ทำไมต้องมี `q_int` ทั้งที่มี `q` อยู่แล้ว?** เพราะใน **VHDL-93** อ่านค่าจากขา `out` ไม่ได้ ข้อความ error จริงคือ `error: port "q" cannot be read`
> ใน **VHDL-2008** กฎนี้ถูกยกเลิกแล้ว เขียน `q <= not q;` ตรง ๆ ได้เลยและคอมไพล์ผ่าน — แต่ **ให้เขียนแบบมี `q_int` ต่อไป** เพราะโค้ดจะย้ายไปใช้กับเครื่องมือหรือมาตรฐานเก่าได้โดยไม่ต้องแก้ และอ่านแล้วเห็นชัดว่าอะไรคือสถานะภายใน อะไรคือขาออก

### JK flip-flop (โครงเดียวกับ T-FF ต่างแค่ลอจิกใน `rising_edge`)

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity jkff is
  port ( clk, rst, j, k : in  std_logic;
         q              : out std_logic );
end entity;

architecture rtl of jkff is
  signal q_int : std_logic := '0';
begin
  process(clk, rst)
  begin
    if rst = '1' then q_int <= '0';
    elsif rising_edge(clk) then
      case j & k is                        -- & คือ "ต่อสาย j กับ k เป็น 2 บิต"
        when "00"   => null;                 -- hold  (null = ไม่ทำอะไร)
        when "01"   => q_int <= '0';         -- reset
        when "10"   => q_int <= '1';         -- set
        when others => q_int <= not q_int;   -- toggle
      end case;
    end if;
  end process;
  q <= q_int;
end architecture;
```

> ⚠️ **`case j & k is` ต้องใช้ VHDL-2008 เท่านั้น** ถ้าตั้งมาตรฐานเป็น VHDL-93 จะได้ error จริงว่า
> ```text
> error: can't resolve overload for operator "&"
>       case j & k is
>              ^
> ```
> ตรวจช่อง **Std** ใน vhdl.ai ให้เป็น **VHDL-2008** ก่อนรัน (หัวข้อ 9.9)

### Testbench ของวงจรที่มีสัญญาณนาฬิกา — ของใหม่ 3 อย่าง

| บรรทัด | ทำหน้าที่อะไร |
|---|---|
| `signal clk : std_logic := '0';` | ต้องมีค่าเริ่มต้น ไม่งั้น `not 'U'` = `'U'` ตลอด นาฬิกาจะไม่มีวันวิ่ง |
| `clk <= not clk after 5 ns when not done;` | สร้างนาฬิกาที่วิ่งเองจนกว่า `done` เป็นจริง คาบ 10 ns = 100 MHz |
| `wait until rising_edge(clk); wait for 1 ns;` | รอขอบนาฬิกา แล้วถอยมาอ่านผล 1 ns ให้ค่าใหม่ปรากฏก่อนตรวจ |
| `std.env.stop;` | หยุด simulation (VHDL-2008) |

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_dff is end entity;

architecture sim of tb_dff is
  signal clk  : std_logic := '0';      -- ต้องมีค่าเริ่มต้น
  signal rst, en, d, q : std_logic;
  signal done : boolean := false;
begin
  uut: entity work.dff port map (clk => clk, rst => rst, en => en, d => d, q => q);

  clk <= not clk after 5 ns when not done;   -- คาบ 10 ns = 100 MHz

  process begin
    rst <= '1'; en <= '0'; d <= '0';
    wait for 12 ns;
    assert q = '0' report "reset should clear q" severity error;

    rst <= '0'; en <= '1'; d <= '1';
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '1' report "q should follow d=1" severity error;

    d <= '0';
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '0' report "q should follow d=0" severity error;

    en <= '0'; d <= '1';                 -- en=0 → q ต้องค้างค่าเดิม
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '0' report "q must hold when en=0" severity error;

    done <= true;
    std.env.stop;
    wait;
  end process;
end architecture;
```

testbench ของ T-FF และ JK-FF ใช้โครงเดียวกันทุกประการ ดูฉบับเต็มในแท็บ **Interactive Sim**

### จุดที่ต้องเน้น

1. **`q` เปลี่ยนที่ขอบขาขึ้นเท่านั้น** ระหว่างขอบ `d` จะกระพริบอย่างไรก็ไม่มีผล
2. **`rising_edge(clk)` ต่างจาก `if clk = '1'`** อย่างหลังได้ **latch** ไม่ใช่ flip-flop และเครื่องมือสังเคราะห์จะฟ้องจริงว่า
   ```text
   error: latch infered for net "q" (use --latches)
   ```
3. **ค่าที่กำหนดให้ signal ยังไม่เปลี่ยนทันทีในบรรทัดถัดไป** — signal อัปเดตเมื่อ process หยุดรอ นี่คือจุดต่างที่ชัดที่สุดระหว่าง `signal` กับ `variable` (และคือเหตุผลเดียวกับที่ Verilog ใช้ `<=` ในวงจรเชิงลำดับ)
4. **ให้เทียบ waveform ของ T-FF กับบิตต่ำสุดของ counter ในตัวอย่าง 4** จะเห็นว่าเหมือนกันทุกประการ

**ลองเอง:** เพิ่มขา `set` แบบ asynchronous ให้ D-FF แล้วตัดสินใจว่า `rst` หรือ `set` ชนะเมื่อมาพร้อมกัน (ใบ้: ใครอยู่ใน `if` ตัวแรก คนนั้นชนะ)

---

## 9.8 ตัวอย่าง 4 — จากฟลิปฟลอปสู่รีจิสเตอร์

**สอน:** การประกอบโมดูลด้วย `port map`, structural vs behavioral, `numeric_std`

ทั้ง shift register และ counter คือ **ฟลิปฟลอป 4 ตัว + ลอจิกหน้าขา D** ต่างกันแค่สมการหน้าขา D เท่านั้น

<svg viewBox="0 0 760 210" role="img" aria-label="ไดอะแกรมชิฟต์รีจิสเตอร์ 4 บิต ประกอบจากดีฟลิปฟลอปสี่ตัวต่ออนุกรม โดยเอาต์พุตของตัวหนึ่งเป็นอินพุตของตัวถัดไป และมีสายนาฬิการ่วมกันทุกตัว" style="width:100%; max-width:720px; height:auto; display:block; margin:1.25rem auto; font-family:'Segoe UI',system-ui,sans-serif;">
  <defs>
    <marker id="arrow-sr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- four flip-flops -->
  <g>
    <rect x="110" y="45" width="110" height="80" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
    <text x="165" y="72" text-anchor="middle" font-size="12.5" font-weight="700" fill="#4f46e5">ff0</text>
    <text x="122" y="100" font-size="11.5" fill="#334155">D</text>
    <text x="208" y="100" text-anchor="end" font-size="11.5" fill="#334155">Q</text>

    <rect x="270" y="45" width="110" height="80" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
    <text x="325" y="72" text-anchor="middle" font-size="12.5" font-weight="700" fill="#4f46e5">ff1</text>
    <text x="282" y="100" font-size="11.5" fill="#334155">D</text>
    <text x="368" y="100" text-anchor="end" font-size="11.5" fill="#334155">Q</text>

    <rect x="430" y="45" width="110" height="80" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
    <text x="485" y="72" text-anchor="middle" font-size="12.5" font-weight="700" fill="#4f46e5">ff2</text>
    <text x="442" y="100" font-size="11.5" fill="#334155">D</text>
    <text x="528" y="100" text-anchor="end" font-size="11.5" fill="#334155">Q</text>

    <rect x="590" y="45" width="110" height="80" rx="8" fill="#eef2ff" stroke="#4f46e5" stroke-width="2"/>
    <text x="645" y="72" text-anchor="middle" font-size="12.5" font-weight="700" fill="#4f46e5">ff3</text>
    <text x="602" y="100" font-size="11.5" fill="#334155">D</text>
    <text x="688" y="100" text-anchor="end" font-size="11.5" fill="#334155">Q</text>
  </g>

  <!-- signal chain -->
  <path d="M40,85 L110,85" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sr)"/>
  <text x="36" y="78" text-anchor="end" font-size="12" font-weight="600" fill="#0f172a">sin</text>
  <path d="M220,85 L270,85" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sr)"/>
  <text x="245" y="76" text-anchor="middle" font-size="11" fill="#64748b">s(0)</text>
  <path d="M380,85 L430,85" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sr)"/>
  <text x="405" y="76" text-anchor="middle" font-size="11" fill="#64748b">s(1)</text>
  <path d="M540,85 L590,85" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sr)"/>
  <text x="565" y="76" text-anchor="middle" font-size="11" fill="#64748b">s(2)</text>
  <path d="M700,85 L745,85" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow-sr)"/>
  <text x="722" y="76" text-anchor="middle" font-size="11" fill="#64748b">s(3)</text>

  <!-- shared clock line -->
  <path d="M40,170 L700,170" fill="none" stroke="#dc2626" stroke-width="2"/>
  <path d="M165,170 L165,125" fill="none" stroke="#dc2626" stroke-width="1.75" marker-end="url(#arrow-sr)"/>
  <path d="M325,170 L325,125" fill="none" stroke="#dc2626" stroke-width="1.75" marker-end="url(#arrow-sr)"/>
  <path d="M485,170 L485,125" fill="none" stroke="#dc2626" stroke-width="1.75" marker-end="url(#arrow-sr)"/>
  <path d="M645,170 L645,125" fill="none" stroke="#dc2626" stroke-width="1.75" marker-end="url(#arrow-sr)"/>
  <text x="36" y="174" text-anchor="end" font-size="12" font-weight="600" fill="#dc2626">clk</text>
  <text x="380" y="196" text-anchor="middle" font-size="11.5" fill="#dc2626">ฟลิปฟลอปทุกตัวใช้นาฬิกาเส้นเดียวกัน = synchronous</text>
</svg>

### Shift register 4 บิต แบบ structural (ประกอบจาก `dff` ของตัวอย่าง 3)

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity shift4 is
  port ( clk, rst, en, sin : in  std_logic;
         q                 : out std_logic_vector(3 downto 0) );
end entity;

architecture structural of shift4 is
  signal s : std_logic_vector(3 downto 0);
begin
  ff0: entity work.dff port map (clk, rst, en, sin,  s(0));
  ff1: entity work.dff port map (clk, rst, en, s(0), s(1));
  ff2: entity work.dff port map (clk, rst, en, s(1), s(2));
  ff3: entity work.dff port map (clk, rst, en, s(2), s(3));
  q <= s;
end architecture;
```

**โค้ดสี่บรรทัดนี้คือรูป SVG ข้างบนตรง ๆ** — `ff0` ถึง `ff3` คือกล่องสี่กล่อง และ `s(0)`..`s(2)` คือสายที่เชื่อมระหว่างกล่อง

### Shift register แบบ behavioral (วงจรเดียวกัน เขียนบรรทัดเดียว)

```vhdl
architecture rtl of shift4 is
  signal s : std_logic_vector(3 downto 0) := (others => '0');
begin
  process(clk, rst)
  begin
    if rst = '1' then s <= (others => '0');
    elsif rising_edge(clk) then
      if en = '1' then s <= s(2 downto 0) & sin; end if;   -- เลื่อนซ้าย ป้อน sin เข้าบิต 0
    end if;
  end process;
  q <= s;
end architecture;
```

> 🔎 **อ่านบรรทัดหัวใจให้ออก** `s <= s(2 downto 0) & sin;` แปลว่า "เอาสามบิตล่างของค่าเดิม มาต่อท้ายด้วย `sin` แล้วเก็บกลับเข้าไป" — บิตบนสุดหล่นหายไป นี่คือการเลื่อนซ้ายพอดี
> ผลรันจริงของทั้งสอง architecture **เหมือนกันทุกจังหวะนาฬิกา** (ดูแท็บ Waveform)

### Counter 4 บิต (โครงเดียวกัน เปลี่ยนสมการหน้าขา D เป็น +1)

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;          -- ต้องมี เพื่อใช้ unsigned และ +

entity counter4 is
  port ( clk, rst, en : in  std_logic;
         q            : out std_logic_vector(3 downto 0) );
end entity;

architecture rtl of counter4 is
  signal cnt : unsigned(3 downto 0) := (others => '0');
begin
  process(clk, rst)
  begin
    if rst = '1' then cnt <= (others => '0');
    elsif rising_edge(clk) then
      if en = '1' then cnt <= cnt + 1; end if;   -- ล้นกลับเป็น 0 เองเมื่อพ้น 15
    end if;
  end process;
  q <= std_logic_vector(cnt);      -- แปลงกลับตอนส่งออกขา
end architecture;
```

### จุดที่ต้องเน้น

| ประเด็น | สาระ |
|---|---|
| **structural vs behavioral** | structural ทำให้เห็นชัดว่า "โค้ดคือแผนผังวงจร" แต่งานจริงเขียน behavioral แล้วให้เครื่องมือสังเคราะห์สร้างฟลิปฟลอปเอง |
| **port map สองแบบ** | แบบเรียงตำแหน่ง `(clk, rst, en, sin, s(0))` ใช้สอนได้ แต่งานจริงควรใช้แบบระบุชื่อ `(clk => clk, d => sin, ...)` เพื่อไม่ต่อสายผิด |
| **`(others => '0')`** | แปลว่า "ทุกบิตเป็น 0" โดยไม่ผูกกับความกว้าง เปลี่ยนรีจิสเตอร์เป็น 8 บิตก็ไม่ต้องแก้บรรทัดนี้ |
| **การนับต้องผ่าน `unsigned`** | `std_logic_vector` บวกเลขไม่ได้ ต้องแปลงไปกลับด้วย `numeric_std` |
| **`for ... loop` ใน testbench** | ใช้นับจำนวนลูกนาฬิกาได้สะดวก เช่น `for i in 1 to 5 loop wait until rising_edge(clk); end loop;` |

---

## 9.9 การจำลองด้วย vhdl.ai (VHDLive)

**vhdl.ai** คือเว็บที่จำลอง VHDL ได้ฟรีในเบราว์เซอร์ ส่วนที่เราใช้ชื่อ **VHDLive** เปิดได้ที่ [vhdl.ai/vhdlive](https://vhdl.ai/vhdlive) — **ไม่ต้องติดตั้งโปรแกรม และไม่ต้องสมัครสมาชิกก็ใช้ simulator ได้**

> ⭐ **จุดที่น่าสนใจทางเทคนิค:** VHDLive ไม่ได้เขียน simulator ขึ้นใหม่ แต่นำ **GHDL** ซึ่งเป็น simulator มาตรฐานโอเพนซอร์สตัวเดียวกับที่ใช้ในงานจริง มาคอมไพล์เป็น **WebAssembly** ให้รันในเบราว์เซอร์ (มี **NVC** ให้เลือกเป็น backend สำรองด้วย) แปลว่าโค้ดที่รันผ่านที่นี่ จะรันผ่านบนเครื่องจริงเหมือนกัน — **การจำลองทั้งหมดเกิดขึ้นในเครื่องของนักศึกษาเอง ไม่ต้องรอคิวเซิร์ฟเวอร์**

### ขั้นตอนการใช้งานในคาบ

1. เปิด [vhdl.ai/vhdlive](https://vhdl.ai/vhdlive) (แนะนำกดปุ่ม **Fullscreen** เพื่อให้พื้นที่เขียนโค้ดกว้างขึ้น)
2. แผง **Files** ด้านซ้าย — กด **New file…** แล้วตั้งชื่อ **โดยไม่ต้องพิมพ์ `.vhd`** (ช่องกรอกเขียนว่า *Entity / file name (without .vhd)*) ตั้งชื่อไฟล์ให้ตรงกับชื่อ entity เช่น `dff`, `tb_dff`
3. วางโค้ดวงจรไว้ไฟล์หนึ่ง และ testbench ไว้อีกไฟล์หนึ่ง — **ถ้ามีหลาย entity เช่น `dff` กับ `shift4` จะวางรวมไฟล์เดียวกันก็ได้**
4. ตั้งค่าแถบด้านบนให้ครบ 3 ช่อง

   | ช่อง | ค่าที่ต้องตั้ง | ถ้าตั้งผิดจะเกิดอะไร |
   |---|---|---|
   | **Top Entity** | ชื่อ entity ของ **testbench** เช่น `tb_dff` | รันแล้วไม่มีอะไรเกิดขึ้น หรือฟ้องหา entity ไม่เจอ |
   | **Std:** | **VHDL-2008** | `case j & k`, `process(all)`, `std.env.stop` ใช้ไม่ได้ทันที |
   | **Stop:** | เช่น `200` `ns` (มีปุ่ม **+100ns** กดเพิ่มทีละ 10 ลูกนาฬิกา และมีชุด preset ให้เลือก) | waveform ขาดกลางคัน หรือรันนานเกินจำเป็น |

   > 🚨 **ช่อง Std สำคัญที่สุดและพลาดกันทุกปี** — ค่าตั้งต้นของเว็บคือ **VHDL-93c** ไม่ใช่ VHDL-2008 ถ้าไม่เปลี่ยน โค้ดในบทนี้จะคอมไพล์ไม่ผ่านตั้งแต่ JK flip-flop เป็นต้นไป **ให้เปลี่ยนเป็น VHDL-2008 เป็นอย่างแรกทุกครั้งที่เปิดโปรเจ็กต์ใหม่**

5. กดปุ่ม **Simulate ▶** — แถบสถานะจะขึ้น *Compiled — running simulation...* ถ้าโค้ดผิดจะขึ้น **Compile failed** พร้อมบรรทัดที่ผิด
6. อ่านผลที่แผง **Console** ด้านล่าง — ข้อความจาก `assert`/`report` ที่ไม่ผ่านจะโผล่ที่นี่ **ถ้าเงียบแปลว่าผ่านหมด**
7. ดูรูปคลื่นที่แท็บ **Waveform** — ใช้ช่อง **Filter signals…** กรองเฉพาะสัญญาณของ `uut` และเปลี่ยน radix ของ vector เป็น binary เพื่อให้เห็นทีละบิต

### ปุ่มที่ควรรู้เพิ่มอีกสี่ปุ่ม

| ปุ่ม | ใช้ทำอะไร |
|---|---|
| **Examples** | คลังตัวอย่างสำเร็จรูป (มี `AND_GATE`, `Decoder2to4`, `Comparator4Bit` ฯลฯ พร้อม testbench) ใช้เทียบกับโค้ดตัวเองได้ |
| **Share / ZIP** → **⇗ Share project…** | สร้างลิงก์โปรเจ็กต์ — **ใช้ลิงก์นี้ส่งงาน** และในเมนูเดียวกันมีปุ่มดาวน์โหลดทั้งโปรเจ็กต์เป็นไฟล์ ZIP |
| **Open .vhd file…** | เปิดไฟล์ `.vhd` จากเครื่องขึ้นมาแก้ต่อ (ใช้ตอนทำงานต่อจากคาบที่แล้ว) |
| **Export waveform as PNG / SVG** | บันทึกรูปคลื่นเป็นภาพ สำหรับแนบในรายงาน |

> 💡 **โปรเจ็กต์ถูกบันทึกอัตโนมัติลงเบราว์เซอร์ทุก 0.5 วินาที** (มีข้อความ *Project autosaves to your browser every 500ms*) แต่นั่นคือเก็บไว้ในเครื่องตัวเองเท่านั้น — **ถ้าล้างข้อมูลเบราว์เซอร์หรือเปลี่ยนเครื่อง งานจะหาย** ให้กด **⇗ Share** เก็บลิงก์ไว้ หรือดาวน์โหลดโปรเจ็กต์เป็น ZIP ทุกครั้งที่ทำเสร็จ

> ⚠️ **ข้อควรระวังก่อนถึงคาบสอน** VHDLive ยังมีป้าย **Beta** กำกับอยู่ ตำแหน่งปุ่มอาจเปลี่ยนตามเวอร์ชัน ให้อาจารย์ทดลองรันโค้ดทั้ง 5 ชุดก่อนเข้าสอนหนึ่งรอบเสมอ และเตรียมแผนสำรองไว้ (เช่น ติดตั้ง GHDL บนเครื่องของห้องปฏิบัติการ ซึ่งใช้โค้ดชุดเดียวกันได้โดยไม่ต้องแก้)

### ถ้าอยากรันบนเครื่องตัวเอง

โค้ดทุกชุดในบทนี้รันด้วย GHDL บนเครื่องได้ทันทีด้วยสามคำสั่ง

```bash
ghdl -a --std=08 design.vhd testbench.vhd   # analyse: ตรวจไวยากรณ์
ghdl -e --std=08 tb_dff                      # elaborate: ประกอบวงจร
ghdl -r --std=08 tb_dff --vcd=wave.vcd       # run: จำลองและบันทึกรูปคลื่น
```

ไฟล์ `wave.vcd` ที่ได้ เปิดดูรูปคลื่นได้ด้วย **GTKWave** หรือ **Surfer**

---

## 9.10 VHDL ↔ Verilog: ตารางเทียบไวยากรณ์

หน้านี้คือโพยเทียบไวยากรณ์ระหว่างภาษา VHDL และ Verilog **แนวคิดเหมือนกันหมด เปลี่ยนแค่คำ**

| สิ่งที่ต้องการ | Verilog | VHDL |
|---|---|---|
| ประกาศกล่องวงจร | `module m(...); ... endmodule` | `entity m is ... end entity;` + `architecture` |
| ขาเข้า / ขาออก | `input wire a` / `output reg y` | `a : in std_logic` / `y : out std_logic` |
| บัส 4 บิต | `wire [3:0] d` | `signal d : std_logic_vector(3 downto 0)` |
| ค่าคงที่ | `4'b1010` / `1'b0` | `"1010"` / `'0'` |
| ต่อสายแบบ concurrent | `assign y = a & b;` | `y <= a and b;` |
| AND / OR / NOT / XOR | `&` `\|` `~` `^` | `and` `or` `not` `xor` |
| NAND / NOR / XNOR | `~(a & b)` ฯลฯ | `nand` `nor` `xnor` (มีให้ตรง ๆ) |
| ต่อบิต (concatenate) | `{a, b}` | `a & b` |
| บล็อกคอมบิเนชัน | `always @(*)` | `process(all)` |
| บล็อกเชิงลำดับ | `always @(posedge clk)` | `process(clk)` + `if rising_edge(clk)` |
| การกำหนดค่าในบล็อก | `<=` (nonblocking) / `=` (blocking) | `<=` (signal) / `:=` (variable) |
| เลือกกรณี | `case (sel) ... endcase` | `case sel is ... end case;` |
| กรณีที่เหลือ | `default:` | `when others =>` |
| ประกอบโมดูลย่อย | `dff u0 (.clk(clk), .d(d), .q(q));` | `u0: entity work.dff port map (clk => clk, d => d, q => q);` |
| หน่วงเวลาใน testbench | `#10;` | `wait for 10 ns;` |
| สร้างนาฬิกา | `always #5 clk = ~clk;` | `clk <= not clk after 5 ns;` |
| ตรวจคำตอบ | `if (...) $display("ERROR");` | `assert ... report "..." severity error;` |
| จบการจำลอง | `$finish;` | `std.env.stop;` |
| บันทึกรูปคลื่น | `$dumpfile` / `$dumpvars` | ตั้งค่าที่ simulator (`--vcd=`) ไม่ต้องเขียนในโค้ด |
| หมายเหตุ (comment) | `// ...` | `-- ...` |

> 📌 **ความต่างที่สำคัญที่สุดสามข้อ**
> 1. **VHDL ตรวจชนิดข้อมูลเข้มงวดกว่ามาก** — เอา `std_logic_vector` ไปบวกเลขตรง ๆ ไม่ได้ ต้องแปลงชนิดก่อน ในขณะที่ Verilog ปล่อยผ่านเงียบ ๆ ข้อนี้ทำให้ VHDL เขียนช้ากว่า แต่จับบั๊กได้ตั้งแต่ตอนคอมไพล์
> 2. **VHDL แยก `entity` กับ `architecture`** จึงมีหลายสถาปัตยกรรมต่อหนึ่งหน้าตากล่องได้ (เหมือน `style_a`/`style_b` ในหัวข้อ 9.6) Verilog ทำแบบนี้ไม่ได้
> 3. **VHDL ไม่มี `wire`/`reg` ให้สับสน** มีแต่ `signal` อย่างเดียว — ความสับสนอันดับหนึ่งของผู้เริ่มต้น Verilog จึงหายไปเลย

---

## 9.11 ข้อผิดพลาดที่พบบ่อย (พร้อมข้อความจริงจาก simulator)

ทุกข้อความ error ในตารางนี้ได้จากการรัน GHDL จริง ไม่ใช่ข้อความที่แต่งขึ้น

| # | ความผิดพลาด | ข้อความ/อาการจริง | ทางแก้ |
|:---:|---|---|---|
| 1 | ลืมวงเล็บ `a and b or c` | `error: only one type of logical operators may be used to combine relation` | ใส่วงเล็บเสมอ `(a and b) or c` |
| 2 | `with-select` ไม่มี `when others` | `error: missing choice(s)` | ปิดท้ายด้วย `when others` ทุกครั้ง |
| 3 | ลืมสัญญาณใน sensitivity list | ไม่มี error แต่ผลจำลอง **ค้างค่าเดิม** ขณะที่ synthesis ได้วงจรถูก | ใช้ `process(all)` กับวงจรคอมบิเนชัน |
| 4 | `case j & k` ขณะตั้ง Std เป็น VHDL-93 | `error: can't resolve overload for operator "&"` | ตั้ง **Std = VHDL-2008** |
| 5 | อ่านค่าจากขา `out` ใน VHDL-93 | `error: port "q" cannot be read` | ใช้ signal ภายใน (`q_int`) แล้วค่อยต่อออกขา |
| 6 | พิมพ์ภาษาไทยใน `report "..."` | `error: invalid character not allowed, even in a string` | ข้อความ report ใช้ ASCII เท่านั้น (comment ไทยได้) |
| 7 | ใช้ `if clk = '1'` แทน `rising_edge(clk)` | `error: latch infered for net "q"` ตอนสังเคราะห์ | ใช้ `rising_edge(clk)` เท่านั้น |
| 8 | ขับ signal เดียวจากสองที่ (multiple drivers) | **ไม่มี error** แต่ค่ากลายเป็น `'X'` เมื่อสองฝั่งไม่ตรงกัน | ให้ signal หนึ่งตัวมีที่เขียนที่เดียว |
| 9 | ลืมค่าเริ่มต้นของ `clk` ใน testbench | นาฬิกาเป็น `'U'` ตลอด ไม่มีขอบเลย | `signal clk : std_logic := '0';` |
| 10 | ใส่ `wait for` / `after` ในไฟล์วงจร | จำลองผ่าน แต่สังเคราะห์ไม่ได้ | หน่วงเวลาจริงต้องทำด้วยตัวนับกับนาฬิกา |
| 11 | ลืม `wait;` ปิดท้าย process ของ testbench | จำลองวนซ้ำไม่รู้จบ | ปิดท้ายด้วย `wait;` หรือ `std.env.stop;` |
| 12 | Top Entity ไม่ตรงกับชื่อ entity ของ testbench | กด Simulate แล้วไม่มีอะไรเกิดขึ้น | ตั้ง Top Entity ให้ตรงตัวอักษรทุกตัว |

> ⚠️ **ข้อ 8 อันตรายที่สุดในตารางนี้** เพราะไม่มีใครฟ้อง — ผลจำลองจริงเมื่อขับ `y` ทั้ง `y <= a and b;` และ `y <= a or b;` พร้อมกันคือ
> ```text
> a=1 b=0 -> y = 'X'      ← สองฝั่งขัดกัน ได้ค่า Unknown
> a=1 b=1 -> y = '1'      ← บังเอิญตรงกัน จึงดูเหมือนไม่มีปัญหา
> ```
> สังเกตว่าบางกรณีมันก็ "ดูปกติ" นี่คือบั๊กที่ซ่อนตัวเก่งที่สุด และในฮาร์ดแวร์จริงคือการลัดวงจรระหว่างเอาต์พุตสองตัว

---

## 9.12 สรุปท้ายบท

บทนี้พาเขียน VHDL ตั้งแต่โครง `entity`/`architecture`, ชนิด `std_logic`, วงจรคอมบิเนชันสองสไตล์, ฟลิปฟลอปสามชนิด, ไปจนถึงการประกอบฟลิปฟลอปเป็นชิฟต์รีจิสเตอร์และตัวนับ พร้อมจำลองจริงบน vhdl.ai

**สามสิ่งที่ควรติดตัวไปจากบทนี้**

1. **`process` ที่มี `rising_edge(clk)` คือฟลิปฟลอป** ส่วน `process` ที่ไม่มี คือวงจรคอมบิเนชัน — แค่รู้สองข้อนี้ก็อ่าน VHDL ของจริงออกแล้วครึ่งหนึ่ง (หัวข้อ 9.7)
2. **VHDL จู้จี้เรื่องชนิดข้อมูลเพราะตั้งใจ** การที่ `std_logic_vector` บวกเลขไม่ได้ ไม่ใช่ความไม่สะดวก แต่คือการบังคับให้เราบอกให้ชัดว่ากำลังมองสายไฟมัดนี้เป็นตัวเลขแบบใด (หัวข้อ 9.3)
3. **ภาษาเปลี่ยน แต่วงจรไม่เปลี่ยน** — วงจรที่เขียนด้วย VHDL สังเคราะห์ได้ฟลิปฟลอปและลอจิกเกตจริง สิ่งที่เรียนมาตั้งแต่บทที่ 2 ถึงบทที่ 8 จึงยังเป็นความรู้ที่ใช้ได้เสมอไม่ว่าจะบรรยายด้วยภาษาใด

</div>

<div class="chapter-tab-content" data-tab-name="Interactive Sim" data-tab-icon="🎮" id="sim" markdown="1">

## 🎮 ชุดโค้ดพร้อมรัน (Copy → Paste → Simulate)

โค้ดทุกชุดในหน้านี้ **คอมไพล์และรันผ่านจริงด้วย GHDL 6.0.0 (`--std=08`)** ซึ่งเป็น simulator ตัวเดียวกับที่ vhdl.ai นำไปคอมไพล์เป็น WebAssembly — ผลลัพธ์ที่แสดงในแท็บถัดไปคือผลที่ออกมาจริง ไม่ใช่ผลที่คาดเดา

### ตั้งค่าก่อนกด Simulate ทุกครั้ง

| ช่อง | ค่า |
|---|---|
| **Top Entity** | ชื่อ entity ของ testbench ในชุดนั้น (เช่น `tb_gates`) |
| **Std:** | `VHDL-2008` (ค่าตั้งต้นคือ VHDL-93c ต้องเปลี่ยนเองทุกครั้ง) |
| **Stop:** | `100` ns สำหรับชุดที่ 1–2 · `200` ns สำหรับชุดที่ 3–5 |

> 💡 **ทำไมไม่มีลิงก์สำเร็จรูปให้กด?** เพราะลิงก์ share ผูกกับเบราว์เซอร์ของผู้สร้างและหายได้เมื่อล้างข้อมูล การคัดลอกโค้ดวางเองจึงแน่นอนกว่า และได้ฝึกพิมพ์ไปในตัว

---

### ชุดที่ 1 — เกตพื้นฐานทั้งเจ็ด (Top Entity = `tb_gates`)

**ไฟล์ `gates`**

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity gates is
  port ( a, b : in  std_logic;
         y_and, y_or, y_not, y_nand, y_nor, y_xor, y_xnor : out std_logic );
end entity;

architecture rtl of gates is
begin
  y_and  <= a and b;
  y_or   <= a or b;
  y_not  <= not a;
  y_nand <= a nand b;
  y_nor  <= a nor b;
  y_xor  <= a xor b;
  y_xnor <= a xnor b;
end architecture;
```

**ไฟล์ `tb_gates`** — ฉบับพิมพ์ตารางความจริงออกทาง Console

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use std.textio.all;

entity tb_gates is end entity;

architecture sim of tb_gates is
  signal a, b : std_logic;
  signal y_and, y_or, y_not, y_nand, y_nor, y_xor, y_xnor : std_logic;
begin
  uut: entity work.gates
    port map (a, b, y_and, y_or, y_not, y_nand, y_nor, y_xor, y_xnor);

  process
    variable l : line;
  begin
    write(l, string'(" a   b  | AND   OR   NOT   NAND   NOR   XOR   XNOR"));
    writeline(output, l);
    write(l, string'("--------+-----------------------------------------"));
    writeline(output, l);

    for i in 0 to 3 loop
      a <= '0' when i < 2 else '1';          -- conditional assignment ของ VHDL-2008
      b <= '0' when (i mod 2) = 0 else '1';
      wait for 10 ns;
      write(l, string'(" "));
      write(l, std_logic'image(a)(2));      write(l, string'("   "));
      write(l, std_logic'image(b)(2));      write(l, string'("  |  "));
      write(l, std_logic'image(y_and)(2));  write(l, string'("    "));
      write(l, std_logic'image(y_or)(2));   write(l, string'("    "));
      write(l, std_logic'image(y_not)(2));  write(l, string'("     "));
      write(l, std_logic'image(y_nand)(2)); write(l, string'("     "));
      write(l, std_logic'image(y_nor)(2));  write(l, string'("     "));
      write(l, std_logic'image(y_xor)(2));  write(l, string'("     "));
      write(l, std_logic'image(y_xnor)(2));
      writeline(output, l);
    end loop;
    wait;
  end process;
end architecture;
```

> 🔎 **`std_logic'image(a)` คืนสตริง `'1'` พร้อมอัญประกาศ** จึงต้องหยิบตัวอักษรที่ตำแหน่ง `(2)` ออกมาเพียงตัวเดียว เทคนิคนี้ใช้ซ้ำได้ทุก testbench ที่อยากพิมพ์ตาราง

---

### ชุดที่ 2 — Half Adder (Top Entity = `tb_half_adder`)

**ไฟล์ `half_adder`**

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity half_adder is
  port ( a, b  : in  std_logic;
         sum   : out std_logic;
         carry : out std_logic );
end entity;

architecture rtl of half_adder is
begin
  sum   <= a xor b;
  carry <= a and b;
end architecture;
```

**ไฟล์ `tb_half_adder`**

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use std.textio.all;

entity tb_half_adder is end entity;

architecture sim of tb_half_adder is
  signal a, b, sum, carry : std_logic;
begin
  uut: entity work.half_adder port map (a, b, sum, carry);

  process
    variable l : line;
  begin
    write(l, string'(" a   b  | sum  carry"));  writeline(output, l);
    write(l, string'("--------+-----------"));  writeline(output, l);
    for i in 0 to 3 loop
      a <= '0' when i < 2 else '1';
      b <= '0' when (i mod 2) = 0 else '1';
      wait for 10 ns;
      write(l, string'(" "));
      write(l, std_logic'image(a)(2));     write(l, string'("   "));
      write(l, std_logic'image(b)(2));     write(l, string'("  |  "));
      write(l, std_logic'image(sum)(2));   write(l, string'("     "));
      write(l, std_logic'image(carry)(2));
      writeline(output, l);
    end loop;
    assert (sum = '0' and carry = '1')
      report "1+1 should give carry" severity error;
    wait;
  end process;
end architecture;
```

---

### ชุดที่ 3 — Mux 4:1 สองสไตล์เทียบกัน (Top Entity = `tb_mux4_print`)

วางทั้งสอง architecture ไว้ไฟล์เดียวกันตามโค้ดในหัวข้อ 9.6 แล้วใช้ testbench นี้ **เรียกทั้งสองสไตล์พร้อมกัน** เพื่อพิสูจน์ว่าให้ผลเหมือนกันทุกกรณี

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;
use std.textio.all;

entity tb_mux4_print is end entity;

architecture sim of tb_mux4_print is
  signal d    : std_logic_vector(3 downto 0) := "1010";
  signal sel  : std_logic_vector(1 downto 0);
  signal y_a  : std_logic;
  signal y_b  : std_logic;
begin
  ua: entity work.mux4(style_a) port map (d => d, sel => sel, y => y_a);
  ub: entity work.mux4(style_b) port map (d => d, sel => sel, y => y_b);

  process
    variable l : line;
  begin
    write(l, string'("  d      sel | style_a  style_b   match"));  writeline(output, l);
    write(l, string'("-------------+--------------------------"));  writeline(output, l);
    for k in 0 to 7 loop
      d   <= "1010" when k < 4 else "0101";
      sel <= std_logic_vector(to_unsigned(k mod 4, 2));
      wait for 10 ns;
      write(l, string'(" "));
      write(l, d);                           write(l, string'("   "));
      write(l, sel);                         write(l, string'("  |    "));
      write(l, std_logic'image(y_a)(2));     write(l, string'("        "));
      write(l, std_logic'image(y_b)(2));     write(l, string'("       "));
      if y_a = y_b then write(l, string'("yes")); else write(l, string'("NO")); end if;
      writeline(output, l);
    end loop;
    wait;
  end process;
end architecture;
```

> 🧪 **การทดลองที่ต้องทำในคาบ** คัดลอก `mux4` อีกชุดหนึ่ง เปลี่ยนชื่อเป็น `mux4_bad` แล้ว **ลบ `d` ออกจาก sensitivity list** (เหลือ `process(sel)`) จากนั้นรันเทียบกับ `process(all)` — ผลจริงอยู่ในแท็บ Waveform หัวข้อที่ 6

---

### ชุดที่ 4 — ฟลิปฟลอป D / T / JK (Top Entity = `tb_dff`, `tb_tff`, `tb_jkff`)

วาง `dff`, `tff`, `jkff` จากหัวข้อ 9.7 ไว้ในไฟล์ `ff` ไฟล์เดียว แล้วสลับ Top Entity เพื่อรันทีละตัว

**ไฟล์ `tb_tff`**

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_tff is end entity;

architecture sim of tb_tff is
  signal clk  : std_logic := '0';
  signal rst, t, q : std_logic;
  signal done : boolean := false;
begin
  uut: entity work.tff port map (clk => clk, rst => rst, t => t, q => q);

  clk <= not clk after 5 ns when not done;

  process begin
    rst <= '1'; t <= '0';
    wait for 12 ns;
    rst <= '0';

    t <= '1';                            -- toggle ทุกขอบ: 0 → 1 → 0 → 1
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '1' report "first toggle should give 1" severity error;
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '0' report "second toggle should give 0" severity error;
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '1' report "third toggle should give 1" severity error;

    t <= '0';                            -- t=0 ต้องค้าง
    wait until rising_edge(clk); wait for 1 ns;
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '1' report "q must hold when t=0" severity error;

    done <= true;
    std.env.stop;
    wait;
  end process;
end architecture;
```

**ไฟล์ `tb_jkff`**

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_jkff is end entity;

architecture sim of tb_jkff is
  signal clk  : std_logic := '0';
  signal rst, j, k, q : std_logic;
  signal done : boolean := false;
begin
  uut: entity work.jkff port map (clk => clk, rst => rst, j => j, k => k, q => q);

  clk <= not clk after 5 ns when not done;

  process begin
    rst <= '1'; j <= '0'; k <= '0';
    wait for 12 ns;
    rst <= '0';

    j <= '1'; k <= '0';                  -- set
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '1' report "jk=10 should set" severity error;

    j <= '0'; k <= '0';                  -- hold
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '1' report "jk=00 should hold" severity error;

    j <= '0'; k <= '1';                  -- reset
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '0' report "jk=01 should reset" severity error;

    j <= '1'; k <= '1';                  -- toggle สองครั้ง
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '1' report "jk=11 first toggle" severity error;
    wait until rising_edge(clk); wait for 1 ns;
    assert q = '0' report "jk=11 second toggle" severity error;

    done <= true;
    std.env.stop;
    wait;
  end process;
end architecture;
```

`tb_dff` ฉบับ assert อยู่ในหัวข้อ 9.7 แล้ว ส่วนฉบับพิมพ์ตารางต่อลูกนาฬิกาใช้โค้ดนี้

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use std.textio.all;

entity tb_dff_print is end entity;

architecture sim of tb_dff_print is
  signal clk  : std_logic := '0';
  signal rst, en, d, q : std_logic;
  signal done : boolean := false;

  type stim_t is record
    r, e, dd : std_logic;
  end record;
  type stim_arr is array (natural range <>) of stim_t;
  constant stim : stim_arr := (          -- (rst, en, d) ของแต่ละลูกนาฬิกา
    ('1', '0', '0'),
    ('0', '1', '1'),
    ('0', '1', '0'),
    ('0', '0', '1'),
    ('0', '0', '0'),
    ('0', '1', '1'),
    ('1', '1', '1') );
begin
  uut: entity work.dff port map (clk => clk, rst => rst, en => en, d => d, q => q);
  clk <= not clk after 5 ns when not done;

  process
    variable l : line;
  begin
    write(l, string'(" edge   rst  en   d  |  q"));   writeline(output, l);
    write(l, string'("---------------------+----"));  writeline(output, l);
    for i in stim'range loop
      rst <= stim(i).r;  en <= stim(i).e;  d <= stim(i).dd;
      wait until rising_edge(clk);
      wait for 1 ns;
      write(l, string'("  #"));            write(l, i + 1);
      write(l, string'("     "));
      write(l, std_logic'image(rst)(2));   write(l, string'("    "));
      write(l, std_logic'image(en)(2));    write(l, string'("   "));
      write(l, std_logic'image(d)(2));     write(l, string'("  |  "));
      write(l, std_logic'image(q)(2));
      writeline(output, l);
    end loop;
    done <= true;
    std.env.stop;
    wait;
  end process;
end architecture;
```

---

### ชุดที่ 5 — Shift Register + Counter (Top Entity = `tb_shift4` / `tb_counter4`)

วาง `dff` (จากชุดที่ 4), `shift4` ทั้งสอง architecture และ `counter4` ไว้ในไฟล์เดียวกันได้ ตามโค้ดในหัวข้อ 9.8

**ไฟล์ `tb_shift4`** — สลับ `(rtl)` เป็น `(structural)` แล้วรันซ้ำ ผลต้องเท่ากันทุกบรรทัด

```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity tb_shift4 is end entity;

architecture sim of tb_shift4 is
  signal clk  : std_logic := '0';
  signal rst, en, sin : std_logic;
  signal q    : std_logic_vector(3 downto 0);
  signal done : boolean := false;
begin
  uut: entity work.shift4(rtl) port map (clk => clk, rst => rst, en => en, sin => sin, q => q);

  clk <= not clk after 5 ns when not done;

  process begin
    rst <= '1'; en <= '0'; sin <= '0';
    wait for 12 ns;
    assert q = "0000" report "reset should clear register" severity error;

    rst <= '0'; en <= '1';
    sin <= '1'; wait until rising_edge(clk); wait for 1 ns;   -- 0001
    sin <= '0'; wait until rising_edge(clk); wait for 1 ns;   -- 0010
    sin <= '1'; wait until rising_edge(clk); wait for 1 ns;   -- 0101
    sin <= '1'; wait until rising_edge(clk); wait for 1 ns;   -- 1011
    assert q = "1011" report "after shifting 1,0,1,1 q should be 1011" severity error;

    en <= '0'; sin <= '0';
    wait until rising_edge(clk); wait for 1 ns;
    assert q = "1011" report "register must hold when en=0" severity error;

    done <= true;
    std.env.stop;
    wait;
  end process;
end architecture;
```

**ไฟล์ `tb_counter4`**

```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_counter4 is end entity;

architecture sim of tb_counter4 is
  signal clk  : std_logic := '0';
  signal rst, en : std_logic;
  signal q    : std_logic_vector(3 downto 0);
  signal done : boolean := false;
begin
  uut: entity work.counter4 port map (clk => clk, rst => rst, en => en, q => q);

  clk <= not clk after 5 ns when not done;

  process begin
    rst <= '1'; en <= '0';
    wait for 12 ns;
    assert q = "0000" report "reset should clear counter" severity error;

    rst <= '0'; en <= '1';
    for i in 1 to 5 loop                 -- นับ 5 ครั้ง
      wait until rising_edge(clk);
    end loop;
    wait for 1 ns;
    assert unsigned(q) = 5 report "after 5 clocks q should be 5" severity error;

    for i in 6 to 16 loop                -- นับต่อจนครบ 16 → ล้นกลับ 0
      wait until rising_edge(clk);
    end loop;
    wait for 1 ns;
    assert q = "0000" report "counter should wrap to 0 after 16 clocks" severity error;

    en <= '0';
    wait until rising_edge(clk); wait for 1 ns;
    assert q = "0000" report "counter must hold when en=0" severity error;

    done <= true;
    std.env.stop;
    wait;
  end process;
end architecture;
```

> 📌 **`unsigned(q) = 5` เทียบกับตัวเลขได้ตรง ๆ** เมื่อประกาศ `use ieee.numeric_std.all;` — สะดวกกว่าการเขียน `q = "0101"` มากเมื่อวงจรกว้างหลายบิต

---

### 🧪 ภารกิจประจำคาบ

1. รันชุดที่ 1 แล้วเทียบตารางที่ได้กับตารางความจริงในบทที่ 2 — ตรงกันครบทั้ง 7 เกตไหม
2. รันชุดที่ 3 สองรอบ โดยเปลี่ยน `uut` จาก `style_a` เป็น `style_b` — ผลต่างกันหรือไม่ และบอกอะไรเราเกี่ยวกับ "สไตล์การเขียน"
3. รันชุดที่ 4 แล้วเปิดแท็บ Waveform เทียบ `q` ของ T-FF กับบิต `q(0)` ของ counter ในชุดที่ 5
4. ในชุดที่ 5 เปลี่ยน `shift4(rtl)` เป็น `shift4(structural)` แล้วยืนยันว่าผลเท่ากันทุกบรรทัด
5. ลองเปลี่ยน `rising_edge(clk)` เป็น `clk = '1'` ในชุดที่ 4 แล้วอธิบายว่ารูปคลื่นเปลี่ยนไปอย่างไร และทำไมจึงเรียกว่า latch

</div>

<div class="chapter-tab-content" data-tab-name="Waveform / Truth Table" data-tab-icon="📊" id="waveform" markdown="1">

## 📊 ผลการจำลองจริง (Verified Simulation Outputs)

ผลทั้งหมดในหน้านี้มาจากการรันโค้ดในแท็บ Interactive Sim ด้วย **GHDL 6.0.0** จริง (`--std=08`) ไม่ใช่ผลที่เขียนคาดไว้

### 1. เกตพื้นฐานทั้งเจ็ด — Console

```text
 a   b  | AND   OR   NOT   NAND   NOR   XOR   XNOR
--------+-----------------------------------------
 0   0  |  0    0    1     1     1     0     1
 0   1  |  0    1    1     1     0     1     0
 1   0  |  0    1    0     1     0     1     0
 1   1  |  1    1    0     0     0     0     1
```

> 🔎 **อ่านตารางนี้ให้เป็นสามอย่าง** — คอลัมน์ NOT ไม่สนใจ `b` เลยเพราะ `y_not <= not a;` · คอลัมน์ NAND เป็นส่วนกลับของ AND ทุกแถว · XNOR เป็น `1` เมื่ออินพุตเหมือนกัน จึงใช้เป็นวงจร "เท่ากันหรือไม่" ได้ (ตรงกับ comparator ในบทที่ 5)

---

### 2. Half Adder — Console

```text
 a   b  | sum  carry
--------+-----------
 0   0  |  0     0
 0   1  |  1     0
 1   0  |  1     0
 1   1  |  0     1
```

ตรงกับตารางความจริงของ half adder ในบทที่ 5 ทุกแถว — `sum` คือ XOR และ `carry` คือ AND

---

### 3. Mux 4:1 — สองสไตล์ให้ผลเท่ากันทุกกรณี

```text
  d      sel | style_a  style_b   match
-------------+--------------------------
 1010   00  |    0        0       yes
 1010   01  |    1        1       yes
 1010   10  |    0        0       yes
 1010   11  |    1        1       yes
 0101   00  |    1        1       yes
 0101   01  |    0        0       yes
 0101   10  |    1        1       yes
 0101   11  |    0        0       yes
```

> ⭐ **นี่คือหลักฐานว่า `with-select` กับ `process + case` คือวงจรเดียวกัน** ทั้งสองสไตล์ให้ผลตรงกันทั้ง 8 กรณี สไตล์จึงเป็นเรื่องความอ่านง่าย ไม่ใช่เรื่องฮาร์ดแวร์ — เลือกสไตล์ตามความซับซ้อนของวงจร ไม่ใช่ตามความชอบ

---

### 4. D Flip-Flop — ค่า q ที่ทุกลูกนาฬิกา

```text
 edge   rst  en   d  |  q
---------------------+----
  #1     1    0   0  |  0
  #2     0    1   1  |  1
  #3     0    1   0  |  0
  #4     0    0   1  |  0     ← en=0: d=1 แต่ q ไม่ขยับ
  #5     0    0   0  |  0
  #6     0    1   1  |  1     ← en=1: กลับมารับค่าอีกครั้ง
  #7     1    1   1  |  0     ← rst=1: ล้างทันทีแม้ d=1 en=1
```

**สามสิ่งที่ผลนี้ยืนยัน**

1. **`en` คือประตูของหน่วยความจำ** แถว #4–#5 อินพุต `d` เปลี่ยนไปมาแต่ `q` ไม่ขยับเลย นี่คือ "การจำ" ที่แท้จริง
2. **reset แบบ asynchronous ชนะทุกอย่าง** แถว #7 แม้ `en=1` และ `d=1` ผลก็ยังเป็น `0` เพราะ `rst` อยู่ใน `if` ตัวแรก
3. **ค่าเปลี่ยนที่ขอบนาฬิกาเท่านั้น** ไม่มีแถวใดที่ `q` เปลี่ยนโดยไม่มีขอบนาฬิกา (ยกเว้น reset)

---

### 5. Shift Register 4 บิต — เลื่อนบิตทีละลูกนาฬิกา

ป้อน `sin` เป็นลำดับ `1, 0, 1, 1` แล้วปิด `en` (ตารางนี้ได้จาก testbench แบบพิมพ์ตาราง ซึ่งดัดแปลงจาก `tb_dff_print` ในชุดที่ 4 ส่วน `tb_shift4` แบบ `assert` ในชุดที่ 5 ตรวจค่าชุดเดียวกันนี้แบบเงียบ ๆ)

```text
 edge   en  sin |   q
----------------+-------
  #1     1    1  |  0001
  #2     1    0  |  0010
  #3     1    1  |  0101
  #4     1    1  |  1011
  #5     0    0  |  1011     ← en=0 ค้างค่าเดิม
  #6     0    0  |  1011
```

> 🔎 **ดูบิตเดินจากขวาไปซ้าย** เลข `1` ตัวแรกที่เข้ามาในลูกที่ #1 อยู่ที่ `q(0)` พอถึงลูกที่ #4 มันเดินไปถึง `q(3)` พอดี — ใช้เวลา 4 ลูกนาฬิกาในการเดินผ่านรีจิสเตอร์ 4 บิต ตรงกับเวลาหน่วงของ SISO ในบทที่ 7
> **รันตารางนี้ซ้ำโดยเปลี่ยนเป็น `shift4(structural)` ได้ผลเหมือนกันทุกบรรทัด** ยืนยันว่า "ต่อ D-FF สี่ตัวด้วยมือ" กับ "เขียนสมการเลื่อนบิตบรรทัดเดียว" คือวงจรเดียวกัน

---

### 6. sensitivity list ที่ลืมใส่ — บั๊กที่ไม่มีใครฟ้อง

วงจรเดียวกันสองตัว ตัวหนึ่งเขียน `process(sel)` (ลืม `d`) อีกตัวเขียน `process(all)` ป้อน `sel = "11"` ค้างไว้ แล้วเปลี่ยนเฉพาะ `d`

```text
   d      sel | process(sel)  process(all)
--------------+----------------------------
  1010   11  |      1             1
  0101   11  |      1             0
```

> ⚠️ **แถวที่สองคือหัวใจ** `d(3)` เปลี่ยนจาก `1` เป็น `0` แล้ว แต่ฝั่ง `process(sel)` ยัง **ค้างค่าเดิมที่ `1`** เพราะ process ไม่ถูกปลุก ในขณะที่ `process(all)` ตอบ `0` ถูกต้อง
> ที่อันตรายคือ **ตอนสังเคราะห์เป็นวงจรจริง เครื่องมือไม่สนใจ sensitivity list เลย** วงจรบนชิปจะทำงานถูก แต่ผลจำลองผิด — แปลว่าเราจะ "ทดสอบผ่าน" ทั้งที่วงจรจริงทำอีกอย่าง หรือ "ทดสอบไม่ผ่าน" ทั้งที่วงจรจริงถูก ทั้งสองทางคือฝันร้าย
> **ทางแก้มีทางเดียว: ใช้ `process(all)` กับวงจรคอมบิเนชันทุกครั้ง**

---

### 7. Counter 4 บิต — นับครบรอบและล้นกลับ

เปิด `en` ค้างไว้ 17 ลูกนาฬิกาแล้วปิดในลูกที่ 18 (ตารางจาก testbench แบบพิมพ์ตาราง ค่าเดียวกับที่ `tb_counter4` ในชุดที่ 5 ใช้ `assert` ตรวจ)

```text
 edge |  q (bin)  q (dec)
------+------------------
  # 1  |   0001      1
  # 2  |   0010      2
  # 3  |   0011      3
  # 4  |   0100      4
  # 5  |   0101      5
  # 6  |   0110      6
  # 7  |   0111      7
  # 8  |   1000      8
  # 9  |   1001      9
  #10  |   1010      10
  #11  |   1011      11
  #12  |   1100      12
  #13  |   1101      13
  #14  |   1110      14
  #15  |   1111      15
  #16  |   0000      0   <- wrap
  #17  |   0001      1
  #18  |   0001      1   <- en=0 hold
```

**สามสิ่งที่ผลนี้ยืนยัน**

1. **นับขึ้นทีละ 1 ทุกลูกนาฬิกา** ลูกละ 10 ns ตามคาบที่ตั้งไว้ (`after 5 ns` สองครั้ง)
2. **ล้นกลับเป็น 0 เองที่ลูกที่ 16** เพราะ `cnt` กว้าง 4 บิต `1111 + 1` จึงตัดบิตทดทิ้ง — นี่คือตัวนับ mod-16 แบบเดียวกับบทที่ 7 ไม่ต้องเขียนเงื่อนไขรีเซ็ตเอง
3. **`en = 0` หยุดค้างค่าเดิม** แถวที่ 18 ค่ายังเป็น 1 เท่าเดิม

> 🔎 **ให้นักศึกษาสังเกตคอลัมน์ `q(0)`** — มันสลับ `0/1` ทุกลูกนาฬิกา ซึ่งคือ **T flip-flop ที่ `t = 1` ตลอดเวลา** เป๊ะ ๆ ตามที่บอกไว้ในหัวข้อ 9.7 ส่วน `q(1)` สลับทุก 2 ลูก `q(2)` ทุก 4 ลูก และ `q(3)` ทุก 8 ลูก — นี่คือการหารความถี่ที่เรียนในบทที่ 7

---

### 8. Multiple drivers — บั๊กที่ซ่อนตัวเก่งที่สุด

ขับ `y` จากสองบรรทัดพร้อมกัน (`y <= a and b;` และ `y <= a or b;`)

```text
a=1 b=0 -> y = 'X'      ← สองฝั่งขัดกัน ได้ Unknown
a=1 b=1 -> y = '1'      ← บังเอิญตรงกัน จึงดูเหมือนไม่มีปัญหา
```

> ⚠️ **VHDL ไม่ฟ้อง error เลย** เพราะ `std_logic` เป็นชนิดที่มี resolution function คือ "มีหลายคนขับสายเดียวกันได้ แล้วค่อยตัดสินว่าได้ค่าอะไร" ซึ่งจำเป็นสำหรับบัสสามสถานะ (บทที่ 2) แต่กลายเป็นกับดักเมื่อเราเผลอเขียนซ้ำ
> **กฎง่าย ๆ:** signal หนึ่งตัว มีที่เขียนที่เดียวเสมอ ถ้าเห็น `'X'` โผล่ใน waveform ให้ค้นหาชื่อ signal นั้นในโค้ดว่ามีกี่ที่ที่เขียนถึงมัน

</div>

<div class="chapter-tab-content" data-tab-name="Challenge" data-tab-icon="🏆" id="challenge" markdown="1">

## 🏆 แบบฝึกหัดท้ายบท

### ภาคที่ 1: ไวยากรณ์และวงจรคอมบิเนชัน

**ข้อ 1 — เกตจากตัวอย่าง 0**
เขียน entity `my_gate` ที่ทำหน้าที่ XNOR โดย **ห้ามใช้ operator `xnor`** (ใบ้: `not (a xor b)`) พร้อม testbench ไล่ครบ 4 กรณี แล้วแนบผล Console

**ข้อ 2 — Full Adder**
ขยาย `half_adder` ในหัวข้อ 9.5 ให้มีขา `cin` กลายเป็น full adder
- เขียน `assert` ให้ครบทั้ง 8 กรณี
- เทียบสมการที่เขียนกับสมการในบทที่ 5 ว่าตรงกันหรือไม่

**ข้อ 3 — วงเล็บที่หายไป**
พิมพ์ `y <= a and b or c;` ลงไปจริง ๆ แล้วกด Simulate
- คัดลอกข้อความ error ที่ได้มาแปะในรายงาน
- อธิบายว่าทำไม VHDL จึงไม่ยอมเดาลำดับความสำคัญให้เรา และข้อดีของการไม่เดาคืออะไร

**ข้อ 4 — Decoder 2:4**
เขียน decoder 2:4 (เอาต์พุต `std_logic_vector(3 downto 0)` แบบ active-high) ด้วย **ทั้งสองสไตล์** คือ `with-select` และ `process(all) + case` ไว้ในไฟล์เดียวกันเป็นสอง architecture แล้วเขียน testbench ตัวเดียวที่เรียกทั้งสองพร้อมกันและพิมพ์คำว่า `MISMATCH` ถ้าผลไม่ตรงกัน

**ข้อ 5 — จาก K-map สู่ VHDL**
เลือกสมการที่ลดรูปแล้วจากบทที่ 4 มาหนึ่งข้อ เขียนเป็น concurrent statement บรรทัดเดียว แล้วเขียน testbench ไล่อินพุตครบทุกกรณีเพื่อยืนยันว่าตรงกับตารางความจริงต้นฉบับ

---

### ภาคที่ 2: วงจรเชิงลำดับ

**ข้อ 6 — D-FF ที่มีทั้ง set และ reset**
เพิ่มขา `set` แบบ asynchronous ให้ `dff`
- ตัดสินใจว่า `rst` หรือ `set` ชนะเมื่อมาพร้อมกัน แล้วอธิบายว่าโค้ดบรรทัดใดเป็นตัวตัดสิน
- เขียน testbench ที่ทดสอบกรณี `rst = set = '1'` พร้อมกันด้วย

**ข้อ 7 — latch กับ flip-flop เห็นด้วยตา**
คัดลอก `dff` มาอีกชุด เปลี่ยน `rising_edge(clk)` เป็น `clk = '1'` แล้วรันด้วย testbench เดียวกัน
- เปรียบเทียบ waveform ของทั้งสองตัว ต่างกันตรงไหน
- ถ้า `d` เปลี่ยนค่ากลางช่วงที่ `clk = '1'` แต่ละตัวตอบสนองอย่างไร
- อธิบายว่าทำไมวงจร synchronous จึงห้ามใช้ latch

**ข้อ 8 — JK-FF ครบทุกกรณี**
ขยาย `tb_jkff` ให้ไล่ `jk` ครบทั้ง 4 ค่า ค่าละ 2 ลูกนาฬิกา (รวม 8 ลูก) แล้วพิมพ์ตาราง `edge | j k | q` ออกทาง Console เทียบกับตารางคุณลักษณะของ JK-FF ในบทที่ 6

**ข้อ 9 — Ring counter 4 บิต**
สร้าง ring counter ที่ reset แล้วได้ `"0001"` จากนั้นวนเป็น `0010 → 0100 → 1000 → 0001` ไปเรื่อย ๆ
- เขียนทั้งแบบ structural (ต่อ `dff` สี่ตัว) และแบบ behavioral
- ต้องระวังอะไรเป็นพิเศษตอน reset และเพราะเหตุใดถ้าเผลอ reset เป็น `"0000"` วงจรจะตายค้างตลอดกาล

**ข้อ 10 — Ripple counter เทียบ synchronous counter**
สร้าง ripple counter 4 บิตจาก `tff` สี่ตัวแบบ structural (เอาต์พุตของตัวก่อนหน้าเป็นนาฬิกาของตัวถัดไป)
- เทียบ waveform กับ `counter4` ในหัวข้อ 9.8
- อธิบายว่าทำไมในทางปฏิบัติจึงไม่นิยม (ใบ้: เอาต์พุตแต่ละบิตไม่เปลี่ยนพร้อมกัน เกิด glitch ระหว่างทาง)

**ข้อ 11 — BCD counter นับขึ้น/ลง**
เขียนตัวนับ 0–9 พร้อมขา `dir` เลือกทิศทาง (`1` = นับขึ้น, `0` = นับลง)
- นับขึ้นถึง 9 แล้วต้องกลับไป 0 · นับลงถึง 0 แล้วต้องกลับไป 9
- เขียน testbench ที่ทดสอบการวนกลับทั้งสองทิศทาง

---

### ภาคที่ 3: เชื่อมโยงกับบทก่อนหน้า

**ข้อ 12 — VHDL เทียบ Verilog บรรทัดต่อบรรทัด**
เลือกวงจรหนึ่งวงจร (เช่น `counter4` หรือ `mux4to1`) แล้วเปรียบเทียบการเขียนด้วย VHDL กับไวยากรณ์ Verilog ในตารางหัวข้อ 9.10
- ทำตารางเทียบทีละบรรทัดว่าบรรทัดใดของ Verilog กลายเป็นบรรทัดใดของ VHDL
- บรรทัดใดที่ VHDL ต้องเขียนยาวกว่า และเขียนยาวกว่าเพื่อแลกกับอะไร

**ข้อ 13 — ระบบเตือนในรถยนต์ (จากบทที่ 8 หัวข้อ 8.15.1)**
เขียนวงจร `car_warning` เป็น VHDL
$$P_1 = K \cdot D \qquad P_2 = K\overline{S} \qquad P_3 = L \cdot D \cdot \overline{K} \qquad \text{BUZZER} = P_1 + P_2 + P_3$$
- ประกาศ product term ทั้งสามเป็น `signal` ภายใน เพื่อให้เห็นการแชร์เทอมแบบเดียวกับแถวของ PLA
- เขียน testbench ไล่อินพุตครบทั้ง 16 กรณี แล้วนับว่ามีกี่กรณีที่ buzzer ดัง
- เทียบผลกับตารางสถานการณ์ในบทที่ 8 ว่าตรงกันทุกแถวหรือไม่

**ข้อ 14 — 🌟 โจทย์บูรณาการ: ไฟจราจรทางข้าม**
นำโจทย์ไฟจราจรทางข้ามจากบทที่ 8 มาเขียนเป็น VHDL
1. ใช้ `type state_t is (GREEN, YELLOW, RED, WALK);` เป็นชนิดข้อมูลของสถานะ (ความสามารถที่ Verilog ไม่มี — ทำให้ waveform แสดงชื่อสถานะเป็นตัวอักษรแทนเลขฐานสอง)
2. สร้างตัวนับเวลาภายใน entity เพื่อสร้างสัญญาณ "ครบเวลา" เอง — **ห้ามใช้ `wait for` หรือ `after` ในไฟล์วงจร**
3. เก็บการกดปุ่มคนข้ามด้วยฟลิปฟลอปเพิ่ม 1 ตัว (set เมื่อกด, clear เมื่อได้ข้ามแล้ว)
4. เขียน testbench ที่กดปุ่มกลางไฟเขียว แล้วตรวจว่าระบบจำการกดไว้จนถึงรอบถัดไป
5. แนบภาพ waveform ที่แสดงครบหนึ่งรอบ (ใช้ปุ่ม **Export waveform as PNG**)

---

## 📤 การส่งงานและเกณฑ์ให้คะแนน

**วิธีส่ง:** ทำใน [vhdl.ai/vhdlive](https://vhdl.ai/vhdlive) แล้วกด **⇗ Share project…** ส่งลิงก์ที่ได้ พร้อมแนบภาพ waveform และผล Console ที่แสดงว่าวงจรทำงานถูกต้อง

> ⚠️ **ก่อนส่ง ให้เปิดลิงก์ที่ได้ในหน้าต่างไม่ระบุตัวตน (incognito) หนึ่งครั้ง** เพื่อยืนยันว่าคนอื่นเปิดดูได้จริง — งานที่เปิดได้เฉพาะเครื่องตัวเองจะถือว่ายังไม่ได้ส่ง และควรดาวน์โหลดโปรเจ็กต์เป็น ZIP เก็บสำรองไว้เสมอ

| หัวข้อประเมิน | คะแนน | เกณฑ์ |
|---|:---:|---|
| **คอมไพล์ผ่านและสังเคราะห์ได้** | 3 | ไม่มี `wait for` / `after` ในไฟล์วงจร · ไม่มี latch โดยไม่ตั้งใจ · ไม่มี multiple drivers |
| **พฤติกรรมถูกต้องตามโจทย์** | 4 | ตรวจจาก waveform และผล Console ครบทุกกรณีที่โจทย์ระบุ |
| **Testbench ครอบคลุม** | 2 | ต้องทดสอบอย่างน้อย: reset · กรณีปกติ · กรณีขอบ (ล้น/วนกลับ/ค้างค่า) |
| **อธิบายวงจรเป็นภาษาคน 2–3 บรรทัด** | 1 | บอกได้ว่าวงจรที่เขียนกลายเป็นฟลิปฟลอปกี่ตัว และลอจิกหน้าขา D คืออะไร |
| **รวม** | **10** | |

</div>
