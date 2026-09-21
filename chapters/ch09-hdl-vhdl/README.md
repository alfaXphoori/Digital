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

### คลังตัวอย่างวงจรใน vhdl.ai (Built-in Example Library)

ในเว็บ [vhdl.ai/vhdlive](https://vhdl.ai/vhdlive) มีปุ่ม **Examples** ที่รวมตัวอย่างวงจรดิจิทัลมาตรฐานไว้ถึง **35 ตัวอย่าง** ครอบคลุมตั้งแต่เกตพื้นฐาน วงจรคอมบิเนชัน ไปจนถึงตัวขับจอภาพกราฟิก VGA และระบบคอมพิวเตอร์ RISC-V SoC ขนาดใหญ่ โดยไฟล์ทั้งหมดถูกรวบรวมและจัดหมวดหมู่อยู่ในโฟลเดอร์ [`vhdl-ai-examples/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples):

| หมวดหมู่ (Category) | จำนวน | ตัวอย่างเด่นใน vhdl.ai | บทเรียนดิจิทัลที่เชื่อมโยง | โฟลเดอร์ซอร์สโค้ดในโปรเจกต์ |
|---|:---:|---|:---:|---|
| **1. Logic Gates** | 7 | AND, OR, NOT, NAND, NOR, XOR, XNOR Gate | บทที่ 2 เกตตรรกะ | [`01-logic-gates/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates) |
| **2. MUX / deMUX** | 5 | 2:1, 4:1, 8:1 MUX และ 1:2, 1:4 deMUX | บทที่ 5 วงจรเชิงจัดหมู่ | [`02-mux-demux/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux) |
| **3. Decoders & Encoders** | 3 | 2:4 Decoder, 3:8 Decoder, 8:3 Priority Encoder | บทที่ 5 วงจรเชิงจัดหมู่ | [`03-decoders-encoders/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders) |
| **4. Display Drivers** | 1 | BCD to 7-Segment Display Driver | บทที่ 8 การต่อประสาน | [`04-display-drivers/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/04-display-drivers) |
| **5. Code Converters** | 2 | Binary to Gray, Gray to Binary (4 บิต) | บทที่ 1 ระบบตัวเลข | [`05-code-converters/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/05-code-converters) |
| **6. Comparators** | 2 | 4-bit Magnitude Comparator, 8-bit Comparator | บทที่ 5 วงจรเชิงจัดหมู่ | [`06-comparators/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/06-comparators) |
| **7. Arithmetic** | 5 | Half Adder, Full Adder, 4-bit RCA, Subtractor, Add/Sub | บทที่ 5 วงจรคำนวณ | [`07-arithmetic/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic) |
| **8. Code Templates** | 4 | Entity (Register), Testbench, Package (Bus), FSM | บทที่ 9 โครงสร้าง VHDL | [`10-templates/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/10-templates) |
| **9. VGA / Display** | 4 | Color Bars, Checkerboard, XOR Pattern, Bouncing Ball | กราฟิก TinyTapeout | [`08-vga-display/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display) |
| **10. CPUs & SoCs** | 6 | mini-RISC, Ben Eater SAP-1, RPU RISC-V, lxp32, NEORV32, Microwatt | บทที่ 10 สถาปัตยกรรม | [`09-cpus-socs/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/09-cpus-socs) |

> 💡 **วิธีเปิดใช้งานใน vhdl.ai:** เมื่อเปิดหน้าเว็บ [vhdl.ai/vhdlive](https://vhdl.ai/vhdlive) ให้คลิกปุ่ม **Examples** บนแถบเครื่องมือ ระบบจะแสดงเมนูตัวอย่างทั้งหมดให้เลือกเปิด ซึ่งจะโหลดไฟล์วงจรพร้อม Testbench และตั้งค่า Top Entity ให้อัตโนมัติ

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


---

## 📚 คลังตัวอย่างวงจรฉบับสมบูรณ์จาก vhdl.ai (VHDLive Examples Catalog)

หัวข้อนี้รวบรวมซอร์สโค้ด VHDL และ Testbench ฉบับสมบูรณ์ของทุกตัวอย่างจากคลัง [vhdl.ai](https://vhdl.ai/vhdlive) จัดหมวดหมู่อย่างเป็นระบบ พร้อมระบุค่าคอนฟิกสำหรับการจำลอง และเชื่อมโยงไปยังทฤษฎีในบทเรียนดิจิทัลที่เกี่ยวข้อง ไฟล์ทั้งหมดถูกบันทึกไว้ในโฟลเดอร์ [`vhdl-ai-examples/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples) ของบทนี้

### หมวดที่ 1: เกตลอจิกพื้นฐาน (Logic Gates — ครบ 7 เกต)

*สอดคล้องกับ: **บทที่ 2 เกตตรรกะและพีชคณิตบูลีน***

ใน vhdl.ai มีการแยกเกตพื้นฐานออกเป็นโมดูลเดี่ยวพร้อม Testbench ครบทั้ง 7 ชนิด เหมาะสำหรับการเริ่มต้นฝึกคอมไพล์และดูรูปคลื่น waveform ของแต่ละเกตอย่างเจาะลึก:

#### 1.1 AND Gate (2-input AND gate)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `AND_GATE_tb` | [`vhdl-ai-examples/01-logic-gates/and-gate/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/and-gate) |
| **Std** | `VHDL-2008` (หรือ VHDL-93) | ไฟล์วงจร: [`AND_GATE.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/and-gate/AND_GATE.vhd) |
| **Stop** | `50 ns` | ไฟล์ Testbench: [`AND_GATE_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/and-gate/AND_GATE_tb.vhd) |

**ไฟล์ `AND_GATE.vhd` (Entity & Architecture)**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity AND_GATE is
    Port (
        A : in  STD_LOGIC;   -- Input A
        B : in  STD_LOGIC;   -- Input B
        Y : out STD_LOGIC    -- Output Y = A AND B
    );
end AND_GATE;

architecture Behavioral of AND_GATE is
begin
    -- Compute AND of inputs A and B
    Y <= A and B;
end Behavioral;
```

**ไฟล์ `AND_GATE_tb.vhd` (Testbench)**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity AND_GATE_tb is
end AND_GATE_tb;

architecture Behavioral of AND_GATE_tb is
    signal A, B, Y : std_logic;  -- Signals to drive DUT and capture output
begin
    -- Instantiate the Device Under Test (DUT)
    uut: entity work.AND_GATE
        port map (
            A => A,
            B => B,
            Y => Y
        );

    -- Stimulus process to test all input combinations
    stim_proc: process
    begin
        A <= '0'; B <= '0';   -- Test case 0 AND 0
        wait for 10 ns;
        A <= '0'; B <= '1';   -- Test case 0 AND 1
        wait for 10 ns;
        A <= '1'; B <= '0';   -- Test case 1 AND 0
        wait for 10 ns;
        A <= '1'; B <= '1';   -- Test case 1 AND 1
        wait for 10 ns;
        wait; -- Stop simulation here
    end process;
end Behavioral;
```

#### 1.2 OR Gate (2-input OR gate)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `OR_GATE_tb` | [`vhdl-ai-examples/01-logic-gates/or-gate/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/or-gate) |
| **Std** | `VHDL-2008` (หรือ VHDL-93) | ไฟล์วงจร: [`OR_GATE.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/or-gate/OR_GATE.vhd) |
| **Stop** | `50 ns` | ไฟล์ Testbench: [`OR_GATE_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/or-gate/OR_GATE_tb.vhd) |

**ไฟล์ `OR_GATE.vhd` (Entity & Architecture)**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY OR_GATE IS
    PORT (
        A : IN STD_LOGIC;   -- Input A
        B : IN STD_LOGIC;   -- Input B
        Y : OUT STD_LOGIC   -- Output Y = A OR B
    );
END OR_GATE;

ARCHITECTURE Behavioral OF OR_GATE IS
begin
    -- Compute OR of inputs A and B
    Y <= A or B;
END Behavioral;
```

**ไฟล์ `OR_GATE_tb.vhd` (Testbench)**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY OR_GATE_tb IS
END OR_GATE_tb;

ARCHITECTURE Behavioral OF OR_GATE_tb IS
    SIGNAL A, B, Y : STD_LOGIC;  -- Signals to drive DUT and capture output
BEGIN
    -- Instantiate the Device Under Test (DUT)
    uut : ENTITY work.OR_GATE
        PORT MAP(
            A => A,
            B => B,
            Y => Y
        );

    -- Stimulus process to test all input combinations
    stim_proc : PROCESS
    BEGIN
        A <= '0';
        B <= '0';  -- Test case 0 OR 0
        WAIT FOR 10 ns;

        A <= '0';
        B <= '1';  -- Test case 0 OR 1
        WAIT FOR 10 ns;

        A <= '1';
        B <= '0';  -- Test case 1 OR 0
        WAIT FOR 10 ns;

        A <= '1';
        B <= '1';  -- Test case 1 OR 1
        WAIT FOR 10 ns;

        WAIT; -- Stop simulation here
    END PROCESS;
END behavioral;
```

#### 1.3 NOT Gate (1-input inverter)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `NOT_GATE_tb` | [`vhdl-ai-examples/01-logic-gates/not-gate/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/not-gate) |
| **Std** | `VHDL-2008` (หรือ VHDL-93) | ไฟล์วงจร: [`NOT_GATE.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/not-gate/NOT_GATE.vhd) |
| **Stop** | `50 ns` | ไฟล์ Testbench: [`NOT_GATE_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/not-gate/NOT_GATE_tb.vhd) |

**ไฟล์ `NOT_GATE.vhd` (Entity & Architecture)**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY NOT_GATE IS
    PORT (
        A : IN STD_LOGIC;   -- Input A
        Y : OUT STD_LOGIC   -- Output Y = NOT A
    );
END NOT_GATE;

ARCHITECTURE behavioural OF NOT_GATE IS
BEGIN
    -- Compute inversion of input A
    Y <= NOT A;
END behavioural;
```

**ไฟล์ `NOT_GATE_tb.vhd` (Testbench)**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY NOT_GATE_tb IS
END NOT_GATE_tb;

ARCHITECTURE behavioural OF NOT_GATE_tb IS
    SIGNAL A, Y : STD_LOGIC;  -- Signals to drive DUT and capture output
BEGIN
    -- Instantiate the Device Under Test (DUT)
    uut : ENTITY work.NOT_GATE
        PORT MAP(
            A => A,
            Y => Y
        );

    -- Stimulus process to test all input values
    stim_proc : PROCESS
    BEGIN
        A <= '0';  -- Test case: NOT 0
        WAIT FOR 10 ns;

        A <= '1';  -- Test case: NOT 1
        WAIT FOR 10 ns;

        WAIT; -- Stop simulation here
    END PROCESS;
END behavioural;
```

#### 1.4 NAND Gate (2-input NAND gate)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `NAND_GATE_tb` | [`vhdl-ai-examples/01-logic-gates/nand-gate/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/nand-gate) |
| **Std** | `VHDL-2008` (หรือ VHDL-93) | ไฟล์วงจร: [`NAND_GATE.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/nand-gate/NAND_GATE.vhd) |
| **Stop** | `50 ns` | ไฟล์ Testbench: [`NAND_GATE_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/nand-gate/NAND_GATE_tb.vhd) |

**ไฟล์ `NAND_GATE.vhd` (Entity & Architecture)**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_Logic_1164.ALL;

ENTITY NAND_GATE IS
    PORT (
        A : IN STD_LOGIC;   -- Input A
        B : IN STD_LOGIC;   -- Input B
        Y : OUT STD_LOGIC   -- Output Y = A NAND B
    );
END NAND_GATE;

ARCHITECTURE behavioural OF NAND_GATE IS
BEGIN
    -- Compute NAND of inputs A and B
    Y <= A NAND B;
END behavioural;
```

**ไฟล์ `NAND_GATE_tb.vhd` (Testbench)**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY NAND_GATE_tb IS
END NAND_GATE_tb;

ARCHITECTURE behavioural OF NAND_GATE_tb IS
    SIGNAL A, B, Y : STD_LOGIC;  -- Signals to drive DUT and capture output
BEGIN
    -- Instantiate the Device Under Test (DUT)
    uut : ENTITY work.NAND_GATE
        PORT MAP(
            A => A,
            B => B,
            Y => Y
        );

    -- Stimulus process to test all input combinations
    stim_proc : PROCESS
    BEGIN
        a <= '0';
        b <= '0';  -- Test case 0 NAND 0
        WAIT FOR 10 ns;

        a <= '0';
        b <= '1';  -- Test case 0 NAND 1
        WAIT FOR 10 ns;

        a <= '1';
        b <= '0';  -- Test case 1 NAND 0
        WAIT FOR 10 ns;

        a <= '1';
        b <= '1';  -- Test case 1 NAND 1
        WAIT FOR 10 ns;

        WAIT; -- Stop simulation here
    END PROCESS;
END behavioural;
```

#### 1.5 NOR Gate (2-input NOR gate)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `NOR_GATE_tb` | [`vhdl-ai-examples/01-logic-gates/nor-gate/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/nor-gate) |
| **Std** | `VHDL-2008` (หรือ VHDL-93) | ไฟล์วงจร: [`NOR_GATE.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/nor-gate/NOR_GATE.vhd) |
| **Stop** | `50 ns` | ไฟล์ Testbench: [`NOR_GATE_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/nor-gate/NOR_GATE_tb.vhd) |

**ไฟล์ `NOR_GATE.vhd` (Entity & Architecture)**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY NOR_GATE IS
    PORT (
        A : IN STD_LOGIC;   -- Input A
        B : IN STD_LOGIC;   -- Input B
        Y : OUT STD_LOGIC   -- Output Y = A NOR B
    );
END NOR_GATE;

ARCHITECTURE Behavioural OF NOR_GATE IS
BEGIN
    -- Compute NOR of inputs A and B
    y <= A NOR b;
END Behavioural;
```

**ไฟล์ `NOR_GATE_tb.vhd` (Testbench)**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY NOR_GATE_tb IS
END NOR_GATE_tb;

ARCHITECTURE Behavioural OF NOR_GATE_tb IS
    SIGNAL A, B, Y : STD_LOGIC;  -- Signals to drive DUT and capture output
BEGIN
    -- Instantiate the Device Under Test (DUT)
    uut :
    ENTITY work.NOR_GATE
        PORT MAP(
            A => A,
            B => B,
            Y => Y
        );

    -- Stimulus process to test all input combinations
    stim_proc : PROCESS
    BEGIN
        A <= '0';
        B <= '0';  -- Test case 0 NOR 0
        WAIT FOR 10 ns;

        A <= '0';
        B <= '1';  -- Test case 0 NOR 1
        WAIT FOR 10 ns;

        A <= '1';
        B <= '0';  -- Test case 1 NOR 0
        WAIT FOR 10 ns;

        A <= '1';
        B <= '1';  -- Test case 1 NOR 1
        WAIT FOR 10 ns;

        WAIT; -- Stop simulation here
    END PROCESS;
END Behavioural;
```

#### 1.6 XOR Gate (2-input XOR gate)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `XOR_GATE_tb` | [`vhdl-ai-examples/01-logic-gates/xor-gate/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/xor-gate) |
| **Std** | `VHDL-2008` (หรือ VHDL-93) | ไฟล์วงจร: [`XOR_GATE.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/xor-gate/XOR_GATE.vhd) |
| **Stop** | `50 ns` | ไฟล์ Testbench: [`XOR_GATE_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/xor-gate/XOR_GATE_tb.vhd) |

**ไฟล์ `XOR_GATE.vhd` (Entity & Architecture)**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity XOR_GATE is
    Port (
        A : in  STD_LOGIC;   -- Input A
        B : in  STD_LOGIC;   -- Input B
        Y : out STD_LOGIC    -- Output Y = A XOR B
    );
end XOR_GATE;

architecture Behavioral of XOR_GATE is
begin
    -- Compute XOR of inputs A and B
    Y <= A xor B;
end Behavioral;
```

**ไฟล์ `XOR_GATE_tb.vhd` (Testbench)**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity XOR_GATE_tb is
end XOR_GATE_tb;

architecture Behavioral of XOR_GATE_tb is
    signal A, B, Y : std_logic;  -- Signals to drive DUT and capture output
begin
    -- Instantiate the Device Under Test (DUT)
    uut: entity work.XOR_GATE
        port map (
            A => A,
            B => B,
            Y => Y
        );

    -- Stimulus process to test all input combinations
    stim_proc: process
    begin
        A <= '0'; B <= '0';  -- Test case 0 XOR 0
        wait for 10 ns;

        A <= '0'; B <= '1';  -- Test case 0 XOR 1
        wait for 10 ns;

        A <= '1'; B <= '0';  -- Test case 1 XOR 0
        wait for 10 ns;

        A <= '1'; B <= '1';  -- Test case 1 XOR 1
        wait for 10 ns;

        wait; -- Stop simulation here
    end process;
end Behavioral;
```

#### 1.7 XNOR Gate (2-input XNOR gate)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `XNOR_GATE_tb` | [`vhdl-ai-examples/01-logic-gates/xnor-gate/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/xnor-gate) |
| **Std** | `VHDL-2008` (หรือ VHDL-93) | ไฟล์วงจร: [`XNOR_GATE.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/xnor-gate/XNOR_GATE.vhd) |
| **Stop** | `50 ns` | ไฟล์ Testbench: [`XNOR_GATE_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/01-logic-gates/xnor-gate/XNOR_GATE_tb.vhd) |

**ไฟล์ `XNOR_GATE.vhd` (Entity & Architecture)**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity XNOR_GATE is
    Port (
        A : in  STD_LOGIC;   -- Input A
        B : in  STD_LOGIC;   -- Input B
        Y : out STD_LOGIC    -- Output Y = A XNOR B
    );
end XNOR_GATE;

architecture Behavioral of XNOR_GATE is
begin
    -- Compute XNOR of inputs A and B
    Y <= A xnor B;
end Behavioral;
```

**ไฟล์ `XNOR_GATE_tb.vhd` (Testbench)**
```vhdl
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity XNOR_GATE_tb is
end XNOR_GATE_tb;

architecture Behavioral of XNOR_GATE_tb is
    signal A, B, Y : std_logic;  -- Signals to drive DUT and capture output
begin
    -- Instantiate the Device Under Test (DUT)
    uut: entity work.XNOR_GATE
        port map (
            A => A,
            B => B,
            Y => Y
        );

    -- Stimulus process to test all input combinations
    stim_proc: process
    begin
        A <= '0'; B <= '0';  -- Test case 0 XNOR 0
        wait for 10 ns;

        A <= '0'; B <= '1';  -- Test case 0 XNOR 1
        wait for 10 ns;

        A <= '1'; B <= '0';  -- Test case 1 XNOR 0
        wait for 10 ns;

        A <= '1'; B <= '1';  -- Test case 1 XNOR 1
        wait for 10 ns;

        wait; -- Stop simulation here
    end process;
end Behavioral;
```

### หมวดที่ 2: วงจรมัลติเพล็กเซอร์และดีมัลติเพล็กเซอร์ (MUX / deMUX — 5 วงจร)

*สอดคล้องกับ: **บทที่ 5 วงจรเชิงจัดหมู่ (Combinational Circuits)***

ตัวเลือกสัญญาณ (Multiplexer) ทำหน้าที่เลือกข้อมูลเข้าหลายสายส่งออกไปยังสายสัญญาณปลายทางเพียงสายเดียวตามรหัสควบคุม `sel` ส่วนดีมัลติเพล็กเซอร์ (Demultiplexer) กระจายข้อมูลจาก 1 สายไปยังปลายทางหลายช่องสัญญาณ:

#### 2.1 2-to-1 MUX (2-to-1 multiplexer)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `MUX2to1_tb` | [`vhdl-ai-examples/02-mux-demux/2-to-1-mux/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/2-to-1-mux) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`2to1_MUX.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/2-to-1-mux/2to1_MUX.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`2to1_MUX_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/2-to-1-mux/2to1_MUX_tb.vhd) |

**ไฟล์ `2to1_MUX.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY MUX2to1 IS
    PORT (
        A : IN STD_LOGIC;  -- Input 0
        B : IN STD_LOGIC;  -- Input 1
        S : IN STD_LOGIC;  -- Select signal
        Y : OUT STD_LOGIC  -- Output, selected input
    );
END MUX2to1;

ARCHITECTURE Behavioural OF MUX2to1 IS
BEGIN
    -- Process to implement 2-to-1 multiplexer
    PROCESS (A, B, S)
    BEGIN
        IF S <= '0' THEN
            Y <= A;  -- When select is 0, output A
        ELSE
            Y <= B;  -- When select is 1, output B
        END IF;
    END PROCESS;

END Behavioural;
```

**ไฟล์ `2to1_MUX_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY MUX2to1_tb IS
END MUX2to1_tb;

ARCHITECTURE test OF MUX2to1_tb IS
    SIGNAL A, B, S, Y : STD_LOGIC;  -- Signals to drive DUT and capture output
BEGIN
    -- Instantiate the Device Under Test (DUT)
    uut : ENTITY work.MUX2to1
        PORT MAP(
            A => A,
            B => B,
            S => S,
            Y => Y
        );

    -- Stimulus process to test all input combinations
    stimulus_proc : PROCESS
    BEGIN
        -- Select = 0 test cases
        A <= '0'; B <= '0'; S <= '0';  -- Expect Y = 0
        WAIT FOR 2 ns;

        A <= '0'; B <= '1'; S <= '0';  -- Expect Y = 0
        WAIT FOR 2 ns;

        A <= '1'; B <= '0'; S <= '0';  -- Expect Y = 1
        WAIT FOR 2 ns;

        A <= '1'; B <= '1'; S <= '0';  -- Expect Y = 1
        WAIT FOR 2 ns;

        -- Select = 1 test cases
        A <= '0'; B <= '0'; S <= '1';  -- Expect Y = 0
        WAIT FOR 2 ns;

        A <= '0'; B <= '1'; S <= '1';  -- Expect Y = 1
        WAIT FOR 2 ns;

        A <= '1'; B <= '0'; S <= '1';  -- Expect Y = 0
        WAIT FOR 2 ns;

        A <= '1'; B <= '1'; S <= '1';  -- Expect Y = 1
        WAIT FOR 2 ns;

        WAIT; -- Stop simulation here
    END PROCESS;
END test;
```

#### 2.2 4-to-1 MUX (4-to-1 multiplexer)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `MUX4to1_tb` | [`vhdl-ai-examples/02-mux-demux/4-to-1-mux/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/4-to-1-mux) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`4to1_MUX.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/4-to-1-mux/4to1_MUX.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`4to1_MUX_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/4-to-1-mux/4to1_MUX_tb.vhd) |

**ไฟล์ `4to1_MUX.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY MUX4to1 IS
    PORT (
        A : IN STD_LOGIC;              -- Input 0
        B : IN STD_LOGIC;              -- Input 1
        C : IN STD_LOGIC;              -- Input 2
        D : IN STD_LOGIC;              -- Input 3
        S : IN STD_LOGIC_VECTOR(1 DOWNTO 0); -- 2-bit select signal
        Y : OUT STD_LOGIC              -- Output, selected input
    );
END MUX4to1;

ARCHITECTURE behavioural OF MUX4to1 IS
BEGIN
    -- Process to implement 4-to-1 multiplexer
    PROCESS (A, B, C, D, S)
    BEGIN
        -- Default assignment prevents Y from being 'U'
        Y <= '0';

        -- Select which input to output based on S
        IF S = "00" THEN
            Y <= A;  -- Select input A
        ELSIF S = "01" THEN
            Y <= B;  -- Select input B
        ELSIF S = "10" THEN
            Y <= C;  -- Select input C
        ELSIF S = "11" THEN
            Y <= D;  -- Select input D
        END IF;
    END PROCESS;
END behavioural;
```

**ไฟล์ `4to1_MUX_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY MUX4to1_tb IS
END MUX4to1_tb;

ARCHITECTURE test OF MUX4to1_tb IS
    -- Signals to drive the DUT
    SIGNAL A, B, C, D, Y : STD_LOGIC := '0';
    SIGNAL S : STD_LOGIC_VECTOR(1 DOWNTO 0) := "00";
BEGIN
    -- Instantiate the Device Under Test (DUT)
    uut : ENTITY work.MUX4to1
        PORT MAP(
            A => A,
            B => B,
            C => C,
            D => D,
            S => S,
            Y => Y
        );

    -- Stimulus process to test the MUX
    stim_proc : PROCESS
        VARIABLE inputs : STD_LOGIC_VECTOR(3 DOWNTO 0); -- For generating all input combinations
    BEGIN
        -- Manual test for readability
        A <= '1'; B <= '0'; C <= '1'; D <= '0'; S <= "00"; WAIT FOR 10 ns;
        S <= "01"; WAIT FOR 10 ns;
        S <= "10"; WAIT FOR 10 ns;
        S <= "11"; WAIT FOR 10 ns;

        -- Automatic exhaustive testing
        FOR s_int IN 0 TO 3 LOOP  -- Loop over all select values
            FOR i IN 0 TO 15 LOOP  -- Loop over all possible 4-bit input combinations
                inputs := STD_LOGIC_VECTOR(to_unsigned(i, 4));
                A <= inputs(3);  -- Map MSB to input A
                B <= inputs(2);
                C <= inputs(1);
                D <= inputs(0);  -- Map LSB to input D
                S <= STD_LOGIC_VECTOR(to_unsigned(s_int, 2));
                WAIT FOR 1 ns;  -- Small delay for simulation
            END LOOP;
        END LOOP;

        WAIT;  -- Stop simulation here
    END PROCESS;
END test;
```

#### 2.3 8-to-1 MUX (8-to-1 multiplexer)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `MUX8to1_tb` | [`vhdl-ai-examples/02-mux-demux/8-to-1-mux/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/8-to-1-mux) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`MUX8to1.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/8-to-1-mux/MUX8to1.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`MUX8to1_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/8-to-1-mux/MUX8to1_tb.vhd) |

**ไฟล์ `MUX8to1.vhd`**
```vhdl
-- ======================================================
-- Project : 91_8to1_MUX
-- File    : MUX8to1.vhd
-- Author  : Ahmad Nabil
-- Function: 8-to-1 Multiplexer
-- ======================================================

LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY MUX8to1 IS
    PORT (
        D : IN STD_LOGIC_VECTOR (7 DOWNTO 0); -- 8 data inputs (D0-D7)
        S : IN STD_LOGIC_VECTOR (2 DOWNTO 0); -- 3-bit select signal
        Y : OUT STD_LOGIC                     -- Output, selected input
    );
END MUX8to1;

ARCHITECTURE behaviour OF MUX8to1 IS
BEGIN
    -- Multiplexer logic using 'with-select-when'
    WITH S SELECT
        Y <= D(0) WHEN "000",  -- Select D0
             D(1) WHEN "001",  -- Select D1
             D(2) WHEN "010",  -- Select D2
             D(3) WHEN "011",  -- Select D3
             D(4) WHEN "100",  -- Select D4
             D(5) WHEN "101",  -- Select D5
             D(6) WHEN "110",  -- Select D6
             D(7) WHEN "111",  -- Select D7
             '0'  WHEN OTHERS; -- Default output to prevent 'U'
END behaviour;
```

**ไฟล์ `MUX8to1_tb.vhd`**
```vhdl
-- ======================================================
-- Project : 91_8to1_MUX
-- File    : MUX8to1_tb.vhd
-- Author  : Ahmad Nabil
-- Function: 8-to-1 Multiplexer Test Bench
-- ======================================================

LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY MUX8to1_tb IS
END MUX8to1_tb;

ARCHITECTURE test OF MUX8to1_tb IS
    SIGNAL D : STD_LOGIC_VECTOR(7 DOWNTO 0) := "10101010"; -- Test pattern for inputs
    SIGNAL S : STD_LOGIC_VECTOR(2 DOWNTO 0) := (OTHERS => '0'); -- Select lines initialized to 0
    SIGNAL Y : STD_LOGIC; -- Output signal
BEGIN
    -- Instantiate the 8-to-1 MUX DUT
    uut : ENTITY work.MUX8to1
        PORT MAP(
            D => D,
            S => S,
            Y => Y
        );

    -- Stimulus process to drive select inputs
    stim_proc : PROCESS
    BEGIN
        FOR i IN 0 TO 7 LOOP
            S <= STD_LOGIC_VECTOR(to_unsigned(i, 3)); -- Set select lines to choose each input
            WAIT FOR 1 ns;                             -- Small delay for observation
        END LOOP;
        WAIT; -- Stop simulation here
    END PROCESS;
END test;
```

#### 2.4 1-to-2 deMUX (1-to-2 demultiplexer)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `deMUX1to2_tb` | [`vhdl-ai-examples/02-mux-demux/1-to-2-demux/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/1-to-2-demux) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`deMUX1to2.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/1-to-2-demux/deMUX1to2.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`deMUX1to2_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/1-to-2-demux/deMUX1to2_tb.vhd) |

**ไฟล์ `deMUX1to2.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

ENTITY deMUX1to2 IS
    PORT (
         D  : IN STD_LOGIC_VECTOR(7 downto 0);  -- 8-bit input signal
         O1 : OUT STD_LOGIC_VECTOR(7 downto 0); -- Output 1, receives D when S=0
         O2 : OUT STD_LOGIC_VECTOR(7 downto 0); -- Output 2, receives D when S=1
         S  : IN STD_LOGIC                       -- Select signal
    );
END deMUX1to2;

ARCHITECTURE behaviour OF deMUX1to2 IS
BEGIN
    -- Assign D to O1 if S=0, else zero
    O1 <= D WHEN S = '0' ELSE "00000000";

    -- Assign D to O2 if S=1, else zero
    O2 <= D WHEN S = '1' ELSE "00000000"; 
END behaviour;
```

**ไฟล์ `deMUX1to2_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

ENTITY deMUX1to2_tb IS
END deMUX1to2_tb;

ARCHITECTURE test OF deMUX1to2_tb IS
    SIGNAL D  : STD_LOGIC_VECTOR(7 DOWNTO 0); -- Test input
    SIGNAL O1 : STD_LOGIC_VECTOR(7 DOWNTO 0); -- DUT output 1
    SIGNAL O2 : STD_LOGIC_VECTOR(7 DOWNTO 0); -- DUT output 2
    SIGNAL S  : STD_LOGIC;                     -- DUT select signal
BEGIN
    -- Instantiate the DUT
    dut : ENTITY work.deMUX1to2
        PORT MAP(
            D  => D,
            O1 => O1,
            O2 => O2,
            S  => S
        );

    -- Stimulus process to exhaustively test all input combinations
    stim_proc : PROCESS
    BEGIN
        -- Loop through all 8-bit values for D (0 to 255)
        FOR i IN 0 TO 255 LOOP
            D <= STD_LOGIC_VECTOR(to_unsigned(i, 8));

            -- Apply select S=0, output should go to O1
            S <= '0';
            WAIT FOR 1 ns;

            -- Apply select S=1, output should go to O2
            S <= '1';
            WAIT FOR 1 ns;
        END LOOP;

        -- Stop simulation
        WAIT;
    END PROCESS;
END test;
```

#### 2.5 1-to-4 deMUX (1-to-4 demultiplexer)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `deMUX1to4_tb` | [`vhdl-ai-examples/02-mux-demux/1-to-4-demux/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/1-to-4-demux) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`deMUX1to4.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/1-to-4-demux/deMUX1to4.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`deMUX1to4_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/02-mux-demux/1-to-4-demux/deMUX1to4_tb.vhd) |

**ไฟล์ `deMUX1to4.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;

----------------------------------------------------------------

ENTITY deMUX1to4 IS
    PORT (
        D  : IN  STD_LOGIC;                   -- Input signal
        S  : IN  STD_LOGIC_VECTOR(1 DOWNTO 0);-- 2-bit select signal
        O1 : OUT STD_LOGIC;                    -- Output 1
        O2 : OUT STD_LOGIC;                    -- Output 2
        O3 : OUT STD_LOGIC;                    -- Output 3
        O4 : OUT STD_LOGIC                     -- Output 4
    );
END deMUX1to4;

----------------------------------------------------------------

ARCHITECTURE behaviour OF deMUX1to4 IS
BEGIN
    PROCESS (S, D)
    BEGIN
        -- Default output values to avoid latches
        O1 <= '0';
        O2 <= '0';
        O3 <= '0';
        O4 <= '0';

        -- Route input D to the selected output based on S
        CASE S IS
            WHEN "00" =>
                O1 <= D;
            WHEN "01" =>
                O2 <= D;
            WHEN "10" =>
                O3 <= D;
            WHEN "11" =>
                O4 <= D;
            WHEN OTHERS =>
                NULL;  -- outputs remain '0' for invalid select values
        END CASE;
    END PROCESS;
END behaviour;
```

**ไฟล์ `deMUX1to4_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

----------------------------------------------------------------

ENTITY deMUX1to4_tb IS
END deMUX1to4_tb;

----------------------------------------------------------------

ARCHITECTURE test OF deMUX1to4_tb IS

    SIGNAL D : STD_LOGIC;                      -- Input signal for DUT
    SIGNAL S : STD_LOGIC_VECTOR(1 DOWNTO 0);   -- 2-bit select signal for DUT
    SIGNAL O1, O2, O3, O4 : STD_LOGIC;         -- Outputs from DUT

BEGIN
    -- Instantiate the DUT
    DUT : ENTITY work.deMUX1to4
        PORT MAP(
            D  => D,
            S  => S,
            O1 => O1,
            O2 => O2,
            O3 => O3,
            O4 => O4
        );

    -- Stimulus process to test all combinations of D and S
    stim_proc : PROCESS
    BEGIN
        -- Test with D=0
        D <= '0';
        S <= "00"; WAIT FOR 1 ns;
        S <= "01"; WAIT FOR 1 ns;
        S <= "10"; WAIT FOR 1 ns;
        S <= "11"; WAIT FOR 1 ns;

        -- Test with D=1
        D <= '1';
        S <= "00"; WAIT FOR 1 ns;
        S <= "01"; WAIT FOR 1 ns;
        S <= "10"; WAIT FOR 1 ns;
        S <= "11"; WAIT FOR 1 ns;

        WAIT;  -- stop simulation
    END PROCESS;

END test;
```

### หมวดที่ 3: วงจรถอดรหัสและเข้ารหัส (Decoders & Encoders — 3 วงจร)

*สอดคล้องกับ: **บทที่ 5 วงจรเชิงจัดหมู่ (Combinational Circuits)***

วงจรถอดรหัส (Decoder) แปลงรหัส $n$ บิตเป็น $2^n$ เส้นเอาต์พุตพร้อมขาควบคุม `EN` (Enable) ส่วนวงจรเข้ารหัสแบบมีลำดับความสำคัญ (Priority Encoder) ตรวจจับอินพุตที่มีลำดับสูงสุดและแปลงเป็นรหัสฐานสอง พร้อมบิตสถานะว่ามีอินพุตใดทำงานหรือไม่:

#### 3.1 2-to-4 Decoder (2-to-4 line decoder with enable)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `Decoder2to4_tb` | [`vhdl-ai-examples/03-decoders-encoders/2-to-4-decoder/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/2-to-4-decoder) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`Decoder2to4.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/2-to-4-decoder/Decoder2to4.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`Decoder2to4_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/2-to-4-decoder/Decoder2to4_tb.vhd) |

**ไฟล์ `Decoder2to4.vhd`**
```vhdl
-- ====================================================
-- Project: 2-to-4 Decoder
-- File   : Decoder2to4.vhd
-- Author : Ahmad Nabil (TheChipMaker)
-- Desc   : Simple line decoder with enable input
-- ====================================================

LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY Decoder2to4 IS
    PORT (
        A  : IN  STD_LOGIC_VECTOR (1 DOWNTO 0);  -- 2-bit input address
        EN : IN  STD_LOGIC;                       -- Enable signal
        Y  : OUT STD_LOGIC_VECTOR (3 DOWNTO 0)   -- 4-bit output
    );
END Decoder2to4;

ARCHITECTURE behaviour OF Decoder2to4 IS
BEGIN
    PROCESS (A, EN)
    BEGIN
        -- Only decode when enable is active
        IF (EN = '1') THEN
            CASE A IS
                WHEN "00" => Y <= "0001";  -- output line 0 active
                WHEN "01" => Y <= "0010";  -- output line 1 active
                WHEN "10" => Y <= "0100";  -- output line 2 active
                WHEN "11" => Y <= "1000";  -- output line 3 active
                WHEN OTHERS => Y <= (OTHERS => '0'); -- default case
            END CASE;
        ELSIF (EN = '0') THEN
            Y <= "0000";  -- disable all outputs if EN is 0
        END IF;
    END PROCESS;
END behaviour;
```

**ไฟล์ `Decoder2to4_tb.vhd`**
```vhdl
-- ====================================================
-- Project: 2-to-4 Decoder
-- File   : Decoder2to4_tb.vhd
-- Author : Ahmad Nabil (TheChipMaker)
-- Desc   : Simple 2-to-4 testbench for a line decoder with enable input
-- ====================================================

LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY Decoder2to4_tb IS
END Decoder2to4_tb;

ARCHITECTURE test OF Decoder2to4_tb IS

    SIGNAL A  : STD_LOGIC_VECTOR (1 DOWNTO 0);  -- input address for DUT
    SIGNAL EN : STD_LOGIC;                       -- enable signal for DUT
    SIGNAL Y  : STD_LOGIC_VECTOR (3 DOWNTO 0);  -- output from DUT

BEGIN

    -- Instantiate the DUT
    uut : ENTITY work.Decoder2to4
        PORT MAP(
            A  => A,
            EN => EN,
            Y  => Y
        );

    -- Stimulus process
    stim_proc : PROCESS
    BEGIN
        -- Test with enable = 0 (all outputs should remain 0)
        EN <= '0';
        A <= "00"; WAIT FOR 1 ns;
        A <= "01"; WAIT FOR 1 ns;
        A <= "10"; WAIT FOR 1 ns;
        A <= "11"; WAIT FOR 1 ns;

        -- Test with enable = 1 (decoder should activate corresponding output)
        EN <= '1';
        A <= "00"; WAIT FOR 1 ns;
        A <= "01"; WAIT FOR 1 ns;
        A <= "10"; WAIT FOR 1 ns;
        A <= "11"; WAIT FOR 1 ns;

        WAIT;  -- stop simulation
    END PROCESS;
END test;
```

#### 3.2 3-to-8 Decoder (3-to-8 line decoder with enable)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `Decoder3to8_tb` | [`vhdl-ai-examples/03-decoders-encoders/3-to-8-decoder/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/3-to-8-decoder) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`Decoder3to8.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/3-to-8-decoder/Decoder3to8.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`Decoder3to8_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/3-to-8-decoder/Decoder3to8_tb.vhd) |

**ไฟล์ `Decoder3to8.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY Decoder3to8 IS
    PORT (
        A  : IN  STD_LOGIC_VECTOR (2 DOWNTO 0);  -- 3-bit input address
        EN : IN  STD_LOGIC;                       -- Enable signal
        Y  : OUT STD_LOGIC_VECTOR (7 DOWNTO 0)   -- 8-bit output
    );
END Decoder3to8;

ARCHITECTURE Behavioral OF Decoder3to8 IS
BEGIN
    PROCESS (A, EN)
    BEGIN
        -- Only decode when enable is active
        IF (EN = '1') THEN
            CASE A IS
                WHEN "000" => Y <= "00000001"; -- output 0 active
                WHEN "001" => Y <= "00000010"; -- output 1 active
                WHEN "010" => Y <= "00000100"; -- output 2 active
                WHEN "011" => Y <= "00001000"; -- output 3 active
                WHEN "100" => Y <= "00010000"; -- output 4 active
                WHEN "101" => Y <= "00100000"; -- output 5 active
                WHEN "110" => Y <= "01000000"; -- output 6 active
                WHEN "111" => Y <= "10000000"; -- output 7 active
                WHEN OTHERS => Y <= "00000000"; -- default case
            END CASE;
        ELSE
            Y <= "00000000"; -- disable all outputs if EN = 0
        END IF;
    END PROCESS;
END Behavioral;
```

**ไฟล์ `Decoder3to8_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

ENTITY Decoder3to8_tb IS
END Decoder3to8_tb;

ARCHITECTURE test OF Decoder3to8_tb IS
    SIGNAL A  : STD_LOGIC_VECTOR (2 DOWNTO 0);  -- input address for DUT
    SIGNAL EN : STD_LOGIC;                       -- enable signal for DUT
    SIGNAL Y  : STD_LOGIC_VECTOR (7 DOWNTO 0);  -- output from DUT

BEGIN

    -- Instantiate the DUT
    dut : ENTITY work.Decoder3to8
        PORT MAP(
            A  => A,
            EN => EN,
            Y  => Y
        );

    -- Stimulus process
    stim_proc : PROCESS
    BEGIN
        -- Test with enable = 0 (all outputs should remain 0)
        EN <= '0';
        FOR i IN 1 TO 8 LOOP
            A <= STD_LOGIC_VECTOR(to_unsigned(i, 3));
            WAIT FOR 1 ns;
        END LOOP;

        -- Test with enable = 1 (decoder should activate corresponding output)
        EN <= '1';
        FOR i IN 1 TO 8 LOOP
            A <= STD_LOGIC_VECTOR(to_unsigned(i, 3));
            WAIT FOR 1 ns;
        END LOOP;

        WAIT;  -- stop simulation
    END PROCESS;
END test;
```

#### 3.3 8-to-3 Priority Encoder (8-to-3 priority encoder)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `PriorityEncoder8to3_tb` | [`vhdl-ai-examples/03-decoders-encoders/8-to-3-priority-encoder/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/8-to-3-priority-encoder) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`PriorityEncoder8to3.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/8-to-3-priority-encoder/PriorityEncoder8to3.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`PriorityEncoder8to3_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/03-decoders-encoders/8-to-3-priority-encoder/PriorityEncoder8to3_tb.vhd) |

**ไฟล์ `PriorityEncoder8to3.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

ENTITY PriorityEncoder8to3 IS
    PORT (
        A : IN  STD_LOGIC_VECTOR(7 DOWNTO 0);  -- 8-bit input signals
        Y : OUT STD_LOGIC_VECTOR(2 DOWNTO 0);  -- 3-bit output representing highest priority input index
        V : OUT STD_LOGIC                       -- Valid flag: '1' if at least one input is high
    );
END PriorityEncoder8to3;

ARCHITECTURE Behaviour OF PriorityEncoder8to3 IS
BEGIN
    process(A)
        variable found : BOOLEAN;  -- flag to indicate first/highest input found
    begin
        V <= '0';                 -- default: no valid input
        Y <= "000";               -- default output
        found := FALSE;

        -- Check inputs from highest (7) to lowest (0) for priority encoding
        for i in 7 downto 0 loop
            if (A(i) = '1') and not found then
                Y <= std_logic_vector(to_unsigned(i, 3)); -- assign index to output
                V <= '1';                                  -- set valid flag
                found := TRUE;                             -- mark highest input found
            end if;
        end loop;
    end process;
END Behaviour;
```

**ไฟล์ `PriorityEncoder8to3_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

ENTITY PriorityEncoder8to3_tb IS
END PriorityEncoder8to3_tb;

-------------------------------------------------------
ARCHITECTURE test OF PriorityEncoder8to3_tb IS
    -- Signals to connect to DUT
    SIGNAL A : STD_LOGIC_VECTOR(7 DOWNTO 0) := (OTHERS => '0');  -- input
    SIGNAL Y : STD_LOGIC_VECTOR(2 DOWNTO 0);                     -- output from DUT
    SIGNAL V : STD_LOGIC;                                        -- valid flag from DUT
BEGIN
    -- Instantiate the DUT
    uut : ENTITY work.PriorityEncoder8to3
        PORT MAP(
            A => A,
            Y => Y,
            V => V
        );

    -- Stimulus process
    stim_proc : PROCESS
    BEGIN

        -- Test each single high input for priority detection
        FOR i IN 7 DOWNTO 0 LOOP
            A <= (OTHERS => '0');  -- clear all inputs
            A(i) <= '1';           -- set only current input high
            WAIT FOR 1 ns;
        END LOOP;

        -- Test multiple-high inputs (verify priority of highest index)
        A <= "10101010";  -- highest active input should be 7
        WAIT FOR 10 ns;
        A <= "01010101";  -- highest active input should be 6
        WAIT FOR 10 ns;
        A <= "00000000";  -- no inputs active, V should be 0
        WAIT FOR 10 ns;

        WAIT;  -- stop simulation
    END PROCESS;
END test;
```

### หมวดที่ 4: ตัวขับจอแสดงผล 7 ส่วน (Display Drivers — 1 วงจร)

*สอดคล้องกับ: **บทที่ 5 และบทที่ 8 การต่อประสานกับอุปกรณ์ภายนอก***

วงจรแปลงรหัส BCD (0–9) เป็นสัญญาณควบคุมหลอด LED 7 ส่วน (`a` ถึง `g`) สำหรับแสดงผลตัวเลขบนหน้าจอแสดงผลดิจิทัล:

#### 4.1 7-Segment Driver (BCD to 7-segment display driver)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `sevenSeg_tb` | [`vhdl-ai-examples/04-display-drivers/7-segment-driver/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/04-display-drivers/7-segment-driver) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`sevenSeg.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/04-display-drivers/7-segment-driver/sevenSeg.vhd) |
| **Stop** | `120 ns` | ไฟล์ Testbench: [`sevenSeg_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/04-display-drivers/7-segment-driver/sevenSeg_tb.vhd) |

**ไฟล์ `sevenSeg.vhd`**
```vhdl
--                  a
--             ____________
--            │            │
--          f │            │ b
--            │            │
--            │____________│
--            │     g      │
--            │            │
--         e  │            │ c
--            │            │
--             ‾‾‾‾‾‾‾‾‾‾‾‾
--                   d
--
--      Segment mapping (active high):
--      MSB  a   b   c   d   e   f
--      MSB  0   0   0   0   0   0
--
-- 0:       a(1) b(1) c(1) d(1) e(1) f(1) g(0)       (1111110)
-- 1:       a(0) b(1) c(1) d(0) e(0) f(0) g(0)       (0110000)
-- 2:       a(1) b(1) c(0) d(1) e(1) f(0) g(1)       (1101101)
-- 3:       a(1) b(1) c(1) d(1) e(0) f(0) g(1)       (1111001)
-- 4:       a(0) b(1) c(1) d(0) e(0) f(1) g(1)       (0110011)
-- 5:       a(1) b(0) c(1) d(1) e(0) f(1) g(1)       (1011011)
-- 6:       a(1) b(0) c(1) d(1) e(1) f(1) g(1)       (1011111)
-- 7:       a(1) b(1) c(1) d(0) e(0) f(0) g(0)       (1110000)
-- 8:       a(1) b(1) c(1) d(1) e(1) f(1) g(1)       (1111111)
-- 9:       a(1) b(1) c(1) d(1) e(0) f(1) g(1)       (1111011)
-- Other:   a(0) b(0) c(0) d(0) e(0) f(0) g(0)       (0000000)
--
--
--
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY sevenSeg IS
    PORT (
        A : IN  STD_LOGIC_VECTOR(3 DOWNTO 0); -- 4-bit input representing hexadecimal digit (0–15)
        Y : OUT STD_LOGIC_VECTOR(6 DOWNTO 0)  -- 7-segment output (a–g)
    );
END sevenSeg;

----------------------------------------------
ARCHITECTURE Behaviour OF sevenSeg IS
BEGIN

    PROCESS (A)
    BEGIN
        -- Map input digit to 7-segment display encoding
        CASE A IS
            WHEN "0000" => Y <= "1111110"; -- 0
            WHEN "0001" => Y <= "0110000"; -- 1
            WHEN "0010" => Y <= "1101101"; -- 2
            WHEN "0011" => Y <= "1111001"; -- 3
            WHEN "0100" => Y <= "0110011"; -- 4
            WHEN "0101" => Y <= "1011011"; -- 5
            WHEN "0110" => Y <= "1011111"; -- 6
            WHEN "0111" => Y <= "1110000"; -- 7
            WHEN "1000" => Y <= "1111111"; -- 8
            WHEN "1001" => Y <= "1111011"; -- 9
            WHEN OTHERS => Y <= "0000000"; -- invalid input, turn off display
        END CASE;

    END PROCESS;

END Behaviour;
```

**ไฟล์ `sevenSeg_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.STD_LOGIC_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

ENTITY sevenSeg_tb IS
END sevenSeg_tb;

ARCHITECTURE Test OF sevenSeg_tb IS

    -- DUT signals
    SIGNAL A : STD_LOGIC_VECTOR(3 DOWNTO 0); -- input to seven-segment decoder
    SIGNAL Y : STD_LOGIC_VECTOR(6 DOWNTO 0); -- output from decoder

BEGIN

    -- Instantiate the Unit Under Test (UUT)
    uut: ENTITY work.sevenSeg
        PORT MAP (
            A => A,
            Y => Y
        );

    -- Stimulus process
    stim_proc: PROCESS
    BEGIN
        -- Apply all possible 4-bit input values (0–15)
        FOR i IN 0 TO 15 LOOP
            A <= STD_LOGIC_VECTOR(to_unsigned(i, 4));
            WAIT FOR 1 ns; -- short delay to observe output
        END LOOP;
        WAIT; -- stop simulation
    END PROCESS;

END Test;
```

### หมวดที่ 5: วงจรแปลงรหัส (Code Converters — 2 วงจร)

*สอดคล้องกับ: **บทที่ 1 ระบบตัวเลขและรหัสดิจิทัล***

รหัส Gray มีจุดเด่นคือค่าที่ติดกันจะเปลี่ยนสถานะเพียง 1 บิตเท่านั้น จึงป้องกันความผิดพลาดจากการเปลี่ยนระดับสัญญาณพร้อมกัน (glitch) ในอุปกรณ์วัดตำแหน่งเชิงมุม:

#### 5.1 Binary to Gray (4-bit binary to Gray code converter)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `BinaryToGray_tb` | [`vhdl-ai-examples/05-code-converters/binary-to-gray/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/05-code-converters/binary-to-gray) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`BinaryToGray.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/05-code-converters/binary-to-gray/BinaryToGray.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`BinaryToGray_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/05-code-converters/binary-to-gray/BinaryToGray_tb.vhd) |

**ไฟล์ `BinaryToGray.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY BinaryToGray IS
    GENERIC (
        N : INTEGER := 4 -- width of binary input (default 4 bits)
    );
    PORT (
        B : IN  STD_LOGIC_VECTOR (N - 1 DOWNTO 0); -- Binary input
        G : OUT STD_LOGIC_VECTOR (N - 1 DOWNTO 0)  -- Gray code output
    );
END BinaryToGray;

-----------------------------------------------------

ARCHITECTURE behaviour OF BinaryToGray IS
BEGIN
    b_proc : PROCESS (B)
    BEGIN
        -- MSB of Gray code = MSB of binary input
        G(N - 1) <= B(N - 1);

        -- Generate remaining Gray bits
        FOR i IN N - 2 DOWNTO 0 LOOP -- MSB already processed
            -- Each Gray bit (except MSB) = XOR of binary bit with next higher-order bit
            G(i) <= B(i + 1) XOR B(i);
        END LOOP;

    END PROCESS b_proc;

END behaviour;
```

**ไฟล์ `BinaryToGray_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY BinaryToGray_tb IS
END BinaryToGray_tb;

------------------------------------------------------
ARCHITECTURE Test OF BinaryToGray_tb IS

    CONSTANT N : INTEGER := 4; -- width of input/output
    SIGNAL B : STD_LOGIC_VECTOR (N - 1 DOWNTO 0); -- Binary input to DUT
    SIGNAL G : STD_LOGIC_VECTOR (N - 1 DOWNTO 0); -- Gray output from DUT
BEGIN
    -- Instantiate the DUT
    dut : ENTITY work.BinaryToGray
        GENERIC MAP(
            N => N
        )
    PORT MAP(
        B => B,
        G => G
    );

    -- Stimulus process
    stim_process : PROCESS
    BEGIN
        -- Test all possible binary input values (0 to 2^N-1)
        FOR i IN 0 TO 2 ** N - 1 LOOP
            B <= STD_LOGIC_VECTOR(to_unsigned(i, 4));
            WAIT FOR 1 ns; -- small delay to observe output
        END LOOP;
    END PROCESS;
END Test;
```

#### 5.2 Gray to Binary (4-bit Gray code to binary converter)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `GrayToBinary_tb` | [`vhdl-ai-examples/05-code-converters/gray-to-binary/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/05-code-converters/gray-to-binary) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`GrayToBinary.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/05-code-converters/gray-to-binary/GrayToBinary.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`GrayToBinary_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/05-code-converters/gray-to-binary/GrayToBinary_tb.vhd) |

**ไฟล์ `GrayToBinary.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY GrayToBinary IS
    GENERIC (
        N : INTEGER := 4 -- width of input/output (default 4 bits)
    );
    PORT (
        G : IN  STD_LOGIC_VECTOR (N - 1 DOWNTO 0); -- Gray code input
        B : OUT STD_LOGIC_VECTOR (N - 1 DOWNTO 0)  -- Binary output
    );
END GrayToBinary;

----------------------------------------------------------

ARCHITECTURE Behaviour OF GrayToBinary IS
BEGIN    
    PROCESS (G)
        -- Variable to hold intermediate binary calculation
        VARIABLE B_var : STD_LOGIC_VECTOR(N - 1 DOWNTO 0);
    BEGIN
        -- MSB of binary = MSB of Gray code
        B_var(N - 1) := G(N - 1);

        -- Compute remaining binary bits
        FOR i IN N - 2 DOWNTO 0 LOOP
            -- Each binary bit = XOR of previous binary bit and corresponding Gray bit
            B_var(i) := B_var(i + 1) XOR G(i);
        END LOOP;

        -- Update output signal
        B <= B_var;
    END PROCESS;
END Behaviour;
```

**ไฟล์ `GrayToBinary_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY GrayToBinary_tb IS
END GrayToBinary_tb;

-----------------------------------------------------------

ARCHITECTURE Test OF GrayToBinary_tb IS
    CONSTANT N : INTEGER := 4; -- width of input/output
    SIGNAL G : STD_LOGIC_VECTOR(N-1 DOWNTO 0); -- Gray input to DUT
    SIGNAL B : STD_LOGIC_VECTOR(N-1 DOWNTO 0); -- Binary output from DUT
BEGIN
    -- Instantiate DUT
    DUT: ENTITY work.GrayToBinary
        GENERIC MAP (N => N)
        PORT MAP (
            G => G,
            B => B
        );

    -- Stimulus + self-check process
    stim_proc: PROCESS
        -- Variables to compute expected binary output
        VARIABLE B_expected_var : STD_LOGIC_VECTOR(N-1 DOWNTO 0);
        VARIABLE i_var : INTEGER;
    BEGIN
        -- Loop through all possible Gray code inputs
        FOR i_var IN 0 TO 2**N - 1 LOOP
            G <= STD_LOGIC_VECTOR(to_unsigned(i_var, N)); -- Apply Gray input
            WAIT FOR 1 ns;  -- wait for combinational logic to settle

            -- Compute expected binary output
            B_expected_var(N-1) := G(N-1); -- MSB
            FOR j IN N-2 DOWNTO 0 LOOP
                B_expected_var(j) := B_expected_var(j+1) XOR G(j);
            END LOOP;

            -- Compare DUT output with expected
            ASSERT (B = B_expected_var)
                REPORT "Mismatch! Gray=" & INTEGER'IMAGE(to_integer(unsigned(G))) &
                       " Expected Binary=" & INTEGER'IMAGE(to_integer(unsigned(B_expected_var))) &
                       " Got=" & INTEGER'IMAGE(to_integer(unsigned(B)))
                SEVERITY ERROR;
        END LOOP;

        -- Report success
        REPORT "All test cases PASSED." SEVERITY NOTE;
        WAIT; -- stop simulation
    END PROCESS;

END Test;
```

### หมวดที่ 6: วงจรเปรียบเทียบขนาด (Comparators — 2 วงจร)

*สอดคล้องกับ: **บทที่ 5 วงจรเชิงจัดหมู่ (Combinational Circuits)***

วงจรเปรียบเทียบขนาดของเลขฐานสองสองจำนวน ($A$ และ $B$) ให้เอาต์พุตสามสถานะ: มากกว่า ($A > B$), น้อยกว่า ($A < B$) และเท่ากัน ($A = B$):

#### 6.1 4-bit Comparator (4-bit magnitude comparator (A>B, A<B, A=B))

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `Comparator4Bit_tb` | [`vhdl-ai-examples/06-comparators/4-bit-comparator/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/06-comparators/4-bit-comparator) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`Comparator4Bit.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/06-comparators/4-bit-comparator/Comparator4Bit.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`Comparator4Bit_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/06-comparators/4-bit-comparator/Comparator4Bit_tb.vhd) |

**ไฟล์ `Comparator4Bit.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

ENTITY Comparator4Bit IS
    PORT (
        A : IN STD_LOGIC_VECTOR(3 DOWNTO 0); -- First 4-bit input
        B : IN STD_LOGIC_VECTOR(3 DOWNTO 0); -- Second 4-bit input

        A_gt_B : OUT STD_LOGIC; -- High if A > B
        A_lt_B : OUT STD_LOGIC; -- High if A < B
        A_eq_B : OUT STD_LOGIC  -- High if A = B
    );
END Comparator4Bit;
----------------------------------------------------
ARCHITECTURE Behaviour OF Comparator4Bit IS
BEGIN
    PROCESS (A, B)
        -- Variables to hold integer equivalents of inputs for comparison
        VARIABLE A_int, B_int : INTEGER;
    BEGIN
        -- Convert std_logic_vector to integer
        A_int := to_integer(unsigned(A));
        B_int := to_integer(unsigned(B));

        -- Compare values and set outputs accordingly
        IF A_int > B_int THEN
            A_gt_B <= '1';
            A_lt_B <= '0';
            A_eq_B <= '0';
        ELSIF A_int < B_int THEN
            A_gt_B <= '0';
            A_lt_B <= '1';
            A_eq_B <= '0';
        ELSE 
            A_gt_B <= '0';
            A_lt_B <= '0';
            A_eq_B <= '1';
        END IF;
    END PROCESS;
END Behaviour;
```

**ไฟล์ `Comparator4Bit_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.NUMERIC_STD.ALL;

ENTITY Comparator4Bit_tb IS
END Comparator4Bit_tb;

ARCHITECTURE Test OF Comparator4Bit_tb IS
    -- Testbench signals for DUT inputs
    SIGNAL A : STD_LOGIC_VECTOR(3 DOWNTO 0);
    SIGNAL B : STD_LOGIC_VECTOR(3 DOWNTO 0);

    -- Testbench signals for DUT outputs
    SIGNAL A_gt_B : STD_LOGIC;
    SIGNAL A_lt_B : STD_LOGIC;
    SIGNAL A_eq_B : STD_LOGIC;

    -- Helper function to convert std_logic_vector to string for reporting
    FUNCTION to_string(v : STD_LOGIC_VECTOR) RETURN STRING IS
        VARIABLE s : STRING(1 TO v'LENGTH);
    BEGIN
        FOR i IN v'RANGE LOOP
            IF v(i) = '0' THEN
                s(i - v'LOW + 1) := '0';
            ELSE
                s(i - v'LOW + 1) := '1';
            END IF;
        END LOOP;
        RETURN s;
    END FUNCTION;

BEGIN
    -- Instantiate DUT
    DUT : ENTITY work.Comparator4Bit
        PORT MAP(
            A => A,
            B => B,
            A_gt_B => A_gt_B,
            A_lt_B => A_lt_B,
            A_eq_B => A_eq_B
        );

    -- Self-checking stimulus process
    stim_proc : PROCESS
        -- Variables to store expected outputs
        VARIABLE expected_gt, expected_lt, expected_eq : STD_LOGIC;
    BEGIN
        -- Exhaustively test all combinations of 4-bit inputs
        FOR i IN 0 TO 15 LOOP
            FOR j IN 0 TO 15 LOOP
                A <= STD_LOGIC_VECTOR(to_unsigned(i, 4)); -- Apply test input A
                B <= STD_LOGIC_VECTOR(to_unsigned(j, 4)); -- Apply test input B
                WAIT FOR 1 ns;

                -- Compute expected outputs
                IF i > j THEN
                    expected_gt := '1';
                    expected_lt := '0';
                    expected_eq := '0';
                ELSIF i < j THEN
                    expected_gt := '0';
                    expected_lt := '1';
                    expected_eq := '0';
                ELSE
                    expected_gt := '0';
                    expected_lt := '0';
                    expected_eq := '1';
                END IF;

                -- Check DUT outputs and report
                IF (A_gt_B /= expected_gt) OR (A_lt_B /= expected_lt) OR (A_eq_B /= expected_eq) THEN
                    REPORT "FAIL: A=" & to_string(A) & " B=" & to_string(B) & " --> DUT outputs incorrect"
                        SEVERITY ERROR;
                ELSE
                    REPORT "PASS: A=" & to_string(A) & " B=" & to_string(B) & " --> DUT outputs correct";
                END IF;

            END LOOP;
        END LOOP;

        WAIT; -- stop simulation
    END PROCESS stim_proc;

END Test;
```

#### 6.2 8-bit Comparator (8-bit magnitude comparator)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `Comparator8Bit_tb` | [`vhdl-ai-examples/06-comparators/8-bit-comparator/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/06-comparators/8-bit-comparator) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`Comparator8Bit.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/06-comparators/8-bit-comparator/Comparator8Bit.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`Comparator8Bit_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/06-comparators/8-bit-comparator/Comparator8Bit_tb.vhd) |

**ไฟล์ `Comparator8Bit.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY Comparator8Bit IS
    PORT (
        A : IN STD_LOGIC_VECTOR(7 DOWNTO 0);  -- 8-bit input A
        B : IN STD_LOGIC_VECTOR(7 DOWNTO 0);  -- 8-bit input B

        A_gt_B : OUT STD_LOGIC;               -- High if A > B
        A_lt_B : OUT STD_LOGIC;               -- High if A < B
        A_eq_B : OUT STD_LOGIC                -- High if A = B
    );
END Comparator8Bit;

-----------------------------------------------------------

ARCHITECTURE Behaviour OF Comparator8Bit IS
BEGIN
    PROCESS (A, B)                            -- Combinational process sensitive to A and B
        VARIABLE A_int, B_int : INTEGER;     -- Variables to hold integer equivalents of inputs
    BEGIN
        A_int := to_integer(unsigned(A));    -- Convert A vector to integer
        B_int := to_integer(unsigned(B));    -- Convert B vector to integer

        -- Compare values and drive outputs accordingly
        IF (A_int > B_int) THEN
            A_gt_B <= '1';
            A_lt_B <= '0';
            A_eq_B <= '0';
        ELSIF (A_int < B_int) THEN
            A_gt_B <= '0';
            A_lt_B <= '1';
            A_eq_B <= '0';
        ELSE
            A_gt_B <= '0';
            A_lt_B <= '0';
            A_eq_B <= '1';
        END IF;
    END PROCESS;                             -- End of combinational comparison

END Behaviour;
```

**ไฟล์ `Comparator8Bit_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY Comparator8Bit_tb IS
END Comparator8Bit_tb;

---------------------------------------------
ARCHITECTURE Test OF Comparator8Bit_tb IS

    -- Testbench signals for DUT inputs
    SIGNAL A, B : STD_LOGIC_VECTOR(7 DOWNTO 0);   
    -- Testbench signals for DUT outputs
    SIGNAL A_gt_B, A_lt_B, A_eq_B : STD_LOGIC;    

BEGIN

    -- Instantiate DUT
    DuT : ENTITY work.Comparator8Bit                 
        PORT MAP(
            A => A,
            B => B,
            A_gt_B => A_gt_B,
            A_lt_B => A_lt_B,
            A_eq_B => A_eq_B
        );

    stim_proc : PROCESS                              -- Stimulus process
        VARIABLE expected_A_gt_B, expected_A_lt_B, expected_A_eq_B : STD_LOGIC;  -- Expected outputs
    BEGIN
        -- Sweep all combinations of 8-bit inputs
        FOR i IN 0 TO 255 LOOP                      -- Sweep A from 0 to 255
            A <= STD_LOGIC_VECTOR(to_unsigned(i, 8));
            FOR j IN 0 TO 255 LOOP                  -- Sweep B from 0 to 255
                B <= STD_LOGIC_VECTOR(to_unsigned(j, 8));
                WAIT FOR 1 ns;                      -- Wait for combinational outputs to settle

                -- Compute expected outputs
                IF i > j THEN                        
                    expected_A_gt_B := '1';
                    expected_A_lt_B := '0';
                    expected_A_eq_B := '0';
                ELSIF i < j THEN
                    expected_A_gt_B := '0';
                    expected_A_lt_B := '1';
                    expected_A_eq_B := '0';
                ELSE
                    expected_A_gt_B := '0';
                    expected_A_lt_B := '0';
                    expected_A_eq_B := '1';
                END IF;

                -- Self-check using assertions; report mismatch if DUT output is incorrect
                ASSERT expected_A_gt_B = A_gt_B
                REPORT "Mismatch at A=" & integer'image(i) & ", B=" & integer'image(j) & " : A_gt_B incorrect"
                    SEVERITY ERROR;

                ASSERT expected_A_lt_B = A_lt_B
                REPORT "Mismatch at A=" & integer'image(i) & ", B=" & integer'image(j) & " : A_lt_B incorrect"
                    SEVERITY ERROR;

                ASSERT expected_A_eq_B = A_eq_B
                REPORT "Mismatch at A=" & integer'image(i) & ", B=" & integer'image(j) & " : A_eq_B incorrect"
                    SEVERITY ERROR;

            END LOOP;
        END LOOP;

        WAIT;                                       -- Stop simulation indefinitely
    END PROCESS;

END Test;
```

### หมวดที่ 7: วงจรคำนวณเลขคณิต (Arithmetic Circuits — 5 วงจร)

*สอดคล้องกับ: **บทที่ 5 วงจรบวกและวงจรลบเลขคณิต***

หัวใจสำคัญของ ALU ในซีพียู คือวงจรบวกและลบเลขฐานสอง ใน vhdl.ai มีตั้งแต่ Half Adder, Full Adder จนถึง 4-bit Ripple Carry Adder, Subtractor และ Adder/Subtractor ที่รวมทั้งสองโหมดไว้ในโมดูลเดียว:

#### 7.1 Half Adder (1-bit half adder (sum + carry))

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `HalfAdder_tb` | [`vhdl-ai-examples/07-arithmetic/half-adder/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/half-adder) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`HalfAdder.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/half-adder/HalfAdder.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`HalfAdder_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/half-adder/HalfAdder_tb.vhd) |

**ไฟล์ `HalfAdder.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY HalfAdder IS
    PORT (
        A : IN STD_LOGIC;    -- First input
        B : IN STD_LOGIC;    -- Second input
        S : OUT STD_LOGIC;   -- Sum output (A XOR B)
        C : OUT STD_LOGIC    -- Carry output (A AND B)
    );
END HalfAdder;

-----------------------------------------------
ARCHITECTURE Behaviour OF HalfAdder IS
BEGIN
    PROCESS (A, B)  -- Triggered whenever A or B changes
    BEGIN
        S <= A XOR B; -- Sum
        C <= A AND B; -- Carry
    END PROCESS;
END Behaviour;
```

**ไฟล์ `HalfAdder_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY HalfAdder_tb IS
END HalfAdder_tb;

ARCHITECTURE Test OF HalfAdder_tb IS
    SIGNAL A, B, S, C : STD_LOGIC;  -- Signals to connect to DUT
BEGIN
    DuT : ENTITY work.HalfAdder
        PORT MAP(
            A => A,
            B => B,
            S => S,
            C => C
        );

    stim_proc : PROCESS
        VARIABLE expected_S, expected_C : STD_LOGIC; -- For self-check
    BEGIN
        -- Test 0 + 0
        A <= '0'; B <= '0';
        expected_S := '0'; expected_C := '0';
        WAIT FOR 1 ns;
        ASSERT (S = expected_S AND C = expected_C)
            REPORT "Error: Half Adder failed for A=0 B=0" SEVERITY ERROR;

        -- Test 0 + 1
        A <= '0'; B <= '1';
        expected_S := '1'; expected_C := '0';
        WAIT FOR 1 ns;
        ASSERT (S = expected_S AND C = expected_C)
            REPORT "Error: Half Adder failed for A=0 B=1" SEVERITY ERROR;

        -- Test 1 + 0
        A <= '1'; B <= '0';
        expected_S := '1'; expected_C := '0';
        WAIT FOR 1 ns;
        ASSERT (S = expected_S AND C = expected_C)
            REPORT "Error: Half Adder failed for A=1 B=0" SEVERITY ERROR;

        -- Test 1 + 1
        A <= '1'; B <= '1';
        expected_S := '0'; expected_C := '1';
        WAIT FOR 1 ns;
        ASSERT (S = expected_S AND C = expected_C)
            REPORT "Error: Half Adder failed for A=1 B=1" SEVERITY ERROR;

        -- End simulation
        WAIT;
    END PROCESS;
END Test;
```

#### 7.2 Full Adder (1-bit full adder with carry-in)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `FullAdder_tb` | [`vhdl-ai-examples/07-arithmetic/full-adder/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/full-adder) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`FullAdder.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/full-adder/FullAdder.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`FullAdder_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/full-adder/FullAdder_tb.vhd) |

**ไฟล์ `FullAdder.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY FullAdder IS
    PORT (
        A    : IN STD_LOGIC;
        B    : IN STD_LOGIC;
        Cin  : IN STD_LOGIC;
        Sum  : OUT STD_LOGIC;
        Cout : OUT STD_LOGIC
    );
END FullAdder;

----------------------------------------------------
ARCHITECTURE Behaviour OF FullAdder IS
BEGIN
    Sum  <= A XOR B XOR Cin;
    Cout <= (A AND B) OR (Cin AND (A XOR B));
END Behaviour;
```

**ไฟล์ `FullAdder_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY FullAdder_tb IS
END FullAdder_tb;

----------------------------------------------------
ARCHITECTURE Test OF FullAdder_tb IS
    SIGNAL A, B, Cin  : STD_LOGIC;
    SIGNAL Sum, Cout  : STD_LOGIC;
BEGIN

    -- Instantiate the DUT
    DuT : ENTITY work.FullAdder
        PORT MAP(
            A    => A,
            B    => B,
            Cin  => Cin,
            Sum  => Sum,
            Cout => Cout
        );

    -- Stimulus and self-check process
    stim_proc : PROCESS
        VARIABLE vec : STD_LOGIC_VECTOR(2 DOWNTO 0);
        VARIABLE expected_Sum, expected_Cout : STD_LOGIC;
    BEGIN
        -- Loop through all 8 input combinations (A,B,Cin)
        FOR i IN 0 TO 7 LOOP
            vec := STD_LOGIC_VECTOR(to_unsigned(i, 3));

            -- Drive DUT inputs
            A   <= vec(2);
            B   <= vec(1);
            Cin <= vec(0);

            WAIT FOR 1 ns;  -- allow DUT outputs to update

            -- Compute expected outputs
            expected_Sum  := vec(2) XOR vec(1) XOR vec(0);
            expected_Cout := (vec(2) AND vec(1)) OR (vec(0) AND (vec(2) XOR vec(1)));

            -- Assertions to check correctness
            ASSERT Sum = expected_Sum
                REPORT "Error in Sum at input " & STD_LOGIC'IMAGE(vec(2)) & STD_LOGIC'IMAGE(vec(1)) & STD_LOGIC'IMAGE(vec(0))
                SEVERITY ERROR;

            ASSERT Cout = expected_Cout
                REPORT "Error in Cout at input " & STD_LOGIC'IMAGE(vec(2)) & STD_LOGIC'IMAGE(vec(1)) & STD_LOGIC'IMAGE(vec(0))
                SEVERITY ERROR;

            REPORT "Test " & integer'image(i) & " passed!" SEVERITY NOTE;
        END LOOP;

        WAIT; -- stop simulation
    END PROCESS stim_proc;

END Test;
```

#### 7.3 4-bit Ripple Carry Adder (4-bit ripple carry adder)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `RCA4Bit_tb` | [`vhdl-ai-examples/07-arithmetic/4-bit-ripple-carry-adder/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-ripple-carry-adder) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`RCA4Bit.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-ripple-carry-adder/RCA4Bit.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`RCA4Bit_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-ripple-carry-adder/RCA4Bit_tb.vhd) |

**ไฟล์ `RCA4Bit.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY RCA4Bit IS
    PORT (
        A : IN STD_LOGIC_VECTOR(3 DOWNTO 0);  -- 4-bit input operand A
        B : IN STD_LOGIC_VECTOR(3 DOWNTO 0);  -- 4-bit input operand B
        Cin : IN STD_LOGIC;                   -- Carry-in input
        S : OUT STD_LOGIC_VECTOR(3 DOWNTO 0); -- 4-bit sum output
        Cout : OUT STD_LOGIC                  -- Carry-out output
    );
END RCA4Bit;

ARCHITECTURE Behaviour OF RCA4Bit IS
BEGIN
    PROCESS(A, B, Cin)  -- Combinational process sensitive to inputs
        VARIABLE c : STD_LOGIC_VECTOR(4 DOWNTO 0); -- Internal carry chain
    BEGIN
        -- Initialize carry-in
        c(0) := Cin;

        -- Ripple-carry logic: compute carry propagation
        c(1) := (A(0) AND B(0)) OR (c(0) AND (A(0) XOR B(0)));
        c(2) := (A(1) AND B(1)) OR (c(1) AND (A(1) XOR B(1)));
        c(3) := (A(2) AND B(2)) OR (c(2) AND (A(2) XOR B(2)));
        c(4) := (A(3) AND B(3)) OR (c(3) AND (A(3) XOR B(3)));

        -- Compute sum bits using XOR with carry-in
        S(0) <= A(0) XOR B(0) XOR c(0);
        S(1) <= A(1) XOR B(1) XOR c(1);
        S(2) <= A(2) XOR B(2) XOR c(2);
        S(3) <= A(3) XOR B(3) XOR c(3);

        -- Output final carry-out
        Cout <= c(4);
    END PROCESS;
END Behaviour;
```

**ไฟล์ `RCA4Bit_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY RCA4Bit_tb IS
END RCA4Bit_tb;

ARCHITECTURE Test OF RCA4Bit_tb IS
    -- Signals to connect to DUT
    SIGNAL A    : STD_LOGIC_VECTOR(3 DOWNTO 0); -- Operand A
    SIGNAL B    : STD_LOGIC_VECTOR(3 DOWNTO 0); -- Operand B
    SIGNAL Cin  : STD_LOGIC;                    -- Carry-in
    SIGNAL S    : STD_LOGIC_VECTOR(3 DOWNTO 0); -- Sum output
    SIGNAL Cout : STD_LOGIC;                    -- Carry-out
BEGIN
    -- Instantiate Device Under Test (DUT)
    DuT : ENTITY work.RCA4Bit
        PORT MAP(
            A => A,
            B => B,
            Cin => Cin,
            S => S,
            Cout => Cout
        );

    -- Stimulus and verification process
    stim_proc : PROCESS
        VARIABLE expected_S    : STD_LOGIC_VECTOR(4 DOWNTO 0); -- Expected sum (5 bits: sum + carry)
        VARIABLE expected_Cout : STD_LOGIC;                    -- Expected carry-out
        VARIABLE error_count   : INTEGER := 0;                 -- Counter for errors
    BEGIN
        -- Loop through all input combinations of A and B
        FOR i IN 0 TO 15 LOOP
            A   <= STD_LOGIC_VECTOR(to_unsigned(i, 4));
            Cin <= '0'; -- Test only Cin = 0 here

            FOR j IN 0 TO 15 LOOP
                B <= STD_LOGIC_VECTOR(to_unsigned(j, 4));

                -- Compute expected result
                expected_S := STD_LOGIC_VECTOR(to_unsigned(i + j, 5));

                -- Expected carry based on overflow
                IF (i + j) > 15 THEN
                    expected_Cout := '1';
                ELSE
                    expected_Cout := '0';
                END IF;

                WAIT FOR 1 ns; -- Allow DUT to update

                -- Compare sum output with expected value
                IF S /= expected_S(3 DOWNTO 0) THEN
                    REPORT "SUM mismatch: A=" & INTEGER'image(i) &
                           " B=" & INTEGER'image(j) &
                           " Expected=" & INTEGER'image(to_integer(unsigned(expected_S(3 DOWNTO 0)))) &
                           " Got=" & INTEGER'image(to_integer(unsigned(S)))
                           SEVERITY ERROR;
                    error_count := error_count + 1;
                END IF;

                -- Compare carry-out with expected carry
                IF Cout /= expected_Cout THEN
                    REPORT "CARRY mismatch: A=" & INTEGER'image(i) &
                           " B=" & INTEGER'image(j) &
                           " Expected=" & STD_LOGIC'image(expected_Cout) &
                           " Got=" & STD_LOGIC'image(Cout)
                           SEVERITY ERROR;
                    error_count := error_count + 1;
                END IF;
            END LOOP;
        END LOOP;

        -- Final report after all tests
        IF error_count = 0 THEN
            REPORT "All test cases passed successfully!" SEVERITY NOTE;
        ELSE
            REPORT "Simulation finished with " & INTEGER'image(error_count) & " errors." SEVERITY ERROR;
        END IF;

        WAIT; -- End simulation
    END PROCESS;
END Test;
```

#### 7.4 4-bit Subtractor (4-bit binary subtractor)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `Subtractor_4Bit_tb` | [`vhdl-ai-examples/07-arithmetic/4-bit-subtractor/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-subtractor) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`Subtractor_4Bit.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-subtractor/Subtractor_4Bit.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`Subtractor_4Bit_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-subtractor/Subtractor_4Bit_tb.vhd) |

**ไฟล์ `Subtractor_4Bit.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

-- 4-bit Subtractor top-level entity
ENTITY Subtractor_4Bit IS
    PORT (
        A : IN STD_LOGIC_VECTOR(3 DOWNTO 0);  -- Minuend input
        B : IN STD_LOGIC_VECTOR(3 DOWNTO 0);  -- Subtrahend input
        D : OUT STD_LOGIC_VECTOR(3 DOWNTO 0); -- Difference output
        Bout : OUT STD_LOGIC                  -- Final borrow output
    );
END Subtractor_4Bit;

ARCHITECTURE Behavioural OF Subtractor_4Bit IS
    -- Declare the 1-bit Full Subtractor component
    COMPONENT FullSubtractor IS
        PORT (
            A_1bit : IN STD_LOGIC;    -- Single bit from A
            B_1bit : IN STD_LOGIC;    -- Single bit from B
            Bin_1bit : IN STD_LOGIC;  -- Borrow-in from previous stage
            D_1bit : OUT STD_LOGIC;   -- Single-bit difference output
            Bout_1bit : OUT STD_LOGIC -- Borrow-out to next stage
        );
    END COMPONENT;

    SIGNAL borrow_chain : STD_LOGIC_VECTOR(4 DOWNTO 0); -- Borrow propagation chain
BEGIN
    borrow_chain(0) <= '0'; -- Initial borrow-in is 0

    -- Instantiate Full Subtractors for each bit, connecting borrow chain
    FS0 : FullSubtractor PORT MAP(
        A_1bit => A(0),
        B_1bit => B(0),
        Bin_1bit => borrow_chain(0),
        D_1bit => D(0),
        Bout_1bit => borrow_chain(1)
    );
    FS1 : FullSubtractor PORT MAP(
        A_1bit => A(1),
        B_1bit => B(1),
        Bin_1bit => borrow_chain(1),
        D_1bit => D(1),
        Bout_1bit => borrow_chain(2)
    );
    FS2 : FullSubtractor PORT MAP(
        A_1bit => A(2),
        B_1bit => B(2),
        Bin_1bit => borrow_chain(2),
        D_1bit => D(2),
        Bout_1bit => borrow_chain(3)
    );
    FS3 : FullSubtractor PORT MAP(
        A_1bit => A(3),
        B_1bit => B(3),
        Bin_1bit => borrow_chain(3),
        D_1bit => D(3),
        Bout_1bit => borrow_chain(4)
    );

    Bout <= borrow_chain(4); -- Final borrow output
END Behavioural;

-- ========================
-- Full Subtractor Module
-- ========================

LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

-- 1-bit Full Subtractor entity
ENTITY FullSubtractor IS
    PORT (
        A_1bit : IN STD_LOGIC;    -- Minuend bit
        B_1bit : IN STD_LOGIC;    -- Subtrahend bit
        Bin_1bit : IN STD_LOGIC;  -- Borrow-in
        D_1bit : OUT STD_LOGIC;   -- Difference bit
        Bout_1bit : OUT STD_LOGIC -- Borrow-out
    );
END FullSubtractor;

ARCHITECTURE Behavioural OF FullSubtractor IS
BEGIN
    -- Difference equation: D = A XOR B XOR Bin
    D_1bit <= A_1bit XOR B_1bit XOR Bin_1bit;

    -- Borrow-out equation: Bout = (~A AND B) OR ((~(A XOR B)) AND Bin)
    Bout_1bit <= (NOT A_1bit AND B_1bit) OR (NOT (A_1bit XOR B_1bit) AND Bin_1bit);
END Behavioural;
```

**ไฟล์ `Subtractor_4Bit_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.NUMERIC_STD.ALL; -- Needed for to_unsigned conversion

-- Testbench for 4-bit subtractor
ENTITY Subtractor_4Bit_tb IS
END Subtractor_4Bit_tb;

ARCHITECTURE Test OF Subtractor_4Bit_tb IS
    -- Signals to connect to DUT
    SIGNAL A : STD_LOGIC_VECTOR(3 DOWNTO 0);   -- Minuend input
    SIGNAL B : STD_LOGIC_VECTOR(3 DOWNTO 0);   -- Subtrahend input
    SIGNAL D : STD_LOGIC_VECTOR(3 DOWNTO 0);   -- Difference output
    SIGNAL Bout : STD_LOGIC;                   -- Borrow output
BEGIN
    -- Instantiate the Device Under Test (DUT)
    DuT : ENTITY work.Subtractor_4Bit
        PORT MAP(
            A => A,
            B => B,
            D => D,
            Bout => Bout
        );

    -- Stimulus process: applies all input combinations and checks results
    stim_proc : PROCESS
        VARIABLE expected_D : STD_LOGIC_VECTOR(3 DOWNTO 0); -- Expected difference
        VARIABLE expected_Bout : STD_LOGIC;                 -- Expected borrow
        VARIABLE mismatch_found : BOOLEAN := FALSE;        -- Flag to track errors
    BEGIN
        -- Loop over all possible A and B combinations (4-bit)
        FOR i IN 0 TO 15 LOOP
            A <= STD_LOGIC_VECTOR(to_unsigned(i, 4));
            FOR j IN 0 TO 15 LOOP
                B <= STD_LOGIC_VECTOR(to_unsigned(j, 4));
                WAIT FOR 1 ns;  -- Small delay to allow signals to propagate

                -- Compute expected results
                expected_D := STD_LOGIC_VECTOR(to_unsigned(((i - j) MOD 16), 4));
                IF i < j THEN
                    expected_Bout := '1';
                ELSE
                    expected_Bout := '0';
                END IF;

                -- Check if DUT output matches expected
                IF D /= expected_D OR expected_Bout /= Bout THEN
                    mismatch_found := TRUE;
                    REPORT "Mismatch for A=" & INTEGER'image(i) &
                           " B=" & INTEGER'image(j)
                           SEVERITY ERROR;
                END IF;
            END LOOP;
        END LOOP;

        -- Report success if no mismatches found
        IF NOT mismatch_found THEN
            REPORT "All test cases passed successfully!" SEVERITY NOTE;
        END IF;

        WAIT; -- Stop simulation
    END PROCESS;

END Test;
```

#### 7.5 4-bit Add/Sub (4-bit adder/subtractor with mode select)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `Adder_Subtractor_4Bit_tb` | [`vhdl-ai-examples/07-arithmetic/4-bit-add-sub/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-add-sub) |
| **Std** | `VHDL-2008` | ไฟล์วงจร: [`Adder_Subtractor_4Bit.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-add-sub/Adder_Subtractor_4Bit.vhd) |
| **Stop** | `100 ns` | ไฟล์ Testbench: [`Adder_Subtractor_4Bit_tb.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/07-arithmetic/4-bit-add-sub/Adder_Subtractor_4Bit_tb.vhd) |

**ไฟล์ `Adder_Subtractor_4Bit.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

-- ========================
-- Top-level 4-bit Adder-Subtractor
-- ========================
ENTITY Adder_Subtractor_4Bit IS
    PORT (
        A      : IN  STD_LOGIC_VECTOR(3 DOWNTO 0); -- 4-bit input A
        B      : IN  STD_LOGIC_VECTOR(3 DOWNTO 0); -- 4-bit input B
        Sub    : IN  STD_LOGIC;                     -- Control: 0 = Add, 1 = Subtract
        S      : OUT STD_LOGIC_VECTOR(3 DOWNTO 0); -- 4-bit sum/difference output
        CB_out : OUT STD_LOGIC                      -- Carry-out (addition) / Borrow-out (subtraction)
    );
END Adder_Subtractor_4Bit;

ARCHITECTURE Behaviour OF Adder_Subtractor_4Bit IS
    -- Carry/Borrow propagation chain: CB_chain(0) is initial carry/borrow, CB_chain(4) is final carry/borrow
    SIGNAL CB_chain : STD_LOGIC_VECTOR(4 DOWNTO 0);

    -- Modified B for subtraction (B XOR Sub)
    SIGNAL B_mod : STD_LOGIC_VECTOR(3 DOWNTO 0);

    -- Full Adder Component Declaration
    COMPONENT FullAdder IS
        PORT (
            A_1bit   : IN  STD_LOGIC; -- 1-bit input A
            B_1bit   : IN  STD_LOGIC; -- 1-bit input B (or modified for subtraction)
            Cin_1bit : IN  STD_LOGIC; -- Carry-in / Borrow-in
            S_1bit   : OUT STD_LOGIC; -- 1-bit sum/difference output
            Cout_1bit: OUT STD_LOGIC  -- Carry-out / Borrow-out
        );
    END COMPONENT;

BEGIN
    -- ================================
    -- Prepare B_mod for subtraction
    -- If Sub = 1, B is complemented (B XOR 1 = ~B)
    -- If Sub = 0, B_mod = B (B XOR 0 = B)
    -- ================================
    B_mod(0) <= B(0) XOR Sub;
    B_mod(1) <= B(1) XOR Sub;
    B_mod(2) <= B(2) XOR Sub;
    B_mod(3) <= B(3) XOR Sub;

    -- Initial carry-in = Sub (0 for addition, 1 for subtraction to implement two's complement)
    CB_chain(0) <= Sub;

    -- ================================
    -- Instantiate 4 Full Adders
    -- Each Full Adder handles one bit, chain carries/borrows through CB_chain
    -- ================================
    FAS0 : FullAdder PORT MAP(
        A_1bit   => A(0),
        B_1bit   => B_mod(0),
        Cin_1bit => CB_chain(0),
        S_1bit   => S(0),
        Cout_1bit=> CB_chain(1)
    );

    FAS1 : FullAdder PORT MAP(
        A_1bit   => A(1),
        B_1bit   => B_mod(1),
        Cin_1bit => CB_chain(1),
        S_1bit   => S(1),
        Cout_1bit=> CB_chain(2)
    );

    FAS2 : FullAdder PORT MAP(
        A_1bit   => A(2),
        B_1bit   => B_mod(2),
        Cin_1bit => CB_chain(2),
        S_1bit   => S(2),
        Cout_1bit=> CB_chain(3)
    );

    FAS3 : FullAdder PORT MAP(
        A_1bit   => A(3),
        B_1bit   => B_mod(3),
        Cin_1bit => CB_chain(3),
        S_1bit   => S(3),
        Cout_1bit=> CB_chain(4)
    );

    -- Output final carry/borrow
    CB_out <= CB_chain(4);

END Behaviour;

-- ========================
-- 1-bit Full Adder
-- ========================
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;

ENTITY FullAdder IS
    PORT (
        A_1bit   : IN  STD_LOGIC;  -- 1-bit input A
        B_1bit   : IN  STD_LOGIC;  -- 1-bit input B
        Cin_1bit : IN  STD_LOGIC;  -- Carry-in / Borrow-in
        S_1bit   : OUT STD_LOGIC;  -- 1-bit sum/difference
        Cout_1bit: OUT STD_LOGIC   -- Carry-out / Borrow-out
    );
END FullAdder;

ARCHITECTURE Behaviour OF FullAdder IS
BEGIN
    -- Compute sum/difference
    S_1bit    <= A_1bit XOR B_1bit XOR Cin_1bit;

    -- Compute carry-out / borrow-out
    Cout_1bit <= (A_1bit AND B_1bit) OR (B_1bit AND Cin_1bit) OR (Cin_1bit AND A_1bit);
END Behaviour;
```

**ไฟล์ `Adder_Subtractor_4Bit_tb.vhd`**
```vhdl
LIBRARY IEEE;
USE IEEE.std_logic_1164.ALL;
USE IEEE.numeric_std.ALL;

ENTITY Adder_Subtractor_4Bit_tb IS
END Adder_Subtractor_4Bit_tb;

ARCHITECTURE Test OF Adder_Subtractor_4Bit_tb IS
    -- DUT signals
    SIGNAL A, B      : STD_LOGIC_VECTOR(3 DOWNTO 0);
    SIGNAL Sub       : STD_LOGIC;
    SIGNAL S         : STD_LOGIC_VECTOR(3 DOWNTO 0);
    SIGNAL CB_out    : STD_LOGIC;

    -- Helper unsigned signals for arithmetic
    SIGNAL A_u, B_u, S_u : unsigned(3 DOWNTO 0);
BEGIN
    -- Convert STD_LOGIC_VECTOR to unsigned
    A_u <= unsigned(A);
    B_u <= unsigned(B);
    S_u <= unsigned(S);

    -- Instantiate the 4-bit Adder-Subtractor
    DuT : ENTITY work.Adder_Subtractor_4Bit
        PORT MAP(
            A      => A,
            B      => B,
            Sub    => Sub,
            S      => S,
            CB_out => CB_out
        );

    stim_proc : PROCESS
        VARIABLE expected_S       : unsigned(3 DOWNTO 0);
        VARIABLE expected_CB_out  : STD_LOGIC;
        VARIABLE temp_result      : unsigned(4 DOWNTO 0); -- extra bit for carry/borrow
    BEGIN
        -- ================================
        -- Addition Test
        -- ================================
        Sub <= '0';
        FOR i IN 0 TO 15 LOOP
            A <= std_logic_vector(to_unsigned(i,4));
            FOR j IN 0 TO 15 LOOP
                B <= std_logic_vector(to_unsigned(j,4));
                WAIT FOR 1 ns;

                -- Compute expected sum
                temp_result := resize(A_u,5) + resize(B_u,5); -- 5 bits to catch carry
                expected_CB_out := temp_result(4);            -- carry out
                expected_S := temp_result(3 DOWNTO 0);        -- lower 4 bits

                -- Check results
                IF S_u /= expected_S THEN
                    REPORT "Addition mismatch: A=" & integer'image(i) &
                           " B=" & integer'image(j) &
                           " S=" & integer'image(to_integer(S_u)) &
                           " Expected=" & integer'image(to_integer(expected_S));
                END IF;

                IF CB_out /= expected_CB_out THEN
                    REPORT "Addition carry mismatch: A=" & integer'image(i) &
                           " B=" & integer'image(j) &
                           " CB_out=" & STD_LOGIC'image(CB_out) &
                           " Expected=" & STD_LOGIC'image(expected_CB_out);
                END IF;
            END LOOP;
        END LOOP;

        -- ================================
        -- Subtraction Test
        -- ================================
        Sub <= '1';
        FOR i IN 0 TO 15 LOOP
            A <= std_logic_vector(to_unsigned(i,4));
            FOR j IN 0 TO 15 LOOP
                B <= std_logic_vector(to_unsigned(j,4));
                WAIT FOR 1 ns;

                -- Compute expected difference
                temp_result := resize(A_u,5) - resize(B_u,5); -- 5 bits to catch borrow
                expected_CB_out := not temp_result(4);            -- borrow flag
                expected_S := temp_result(3 DOWNTO 0);        -- lower 4 bits

                -- Check results
                IF S_u /= expected_S THEN
                    REPORT "Subtraction mismatch: A=" & integer'image(i) &
                           " B=" & integer'image(j) &
                           " S=" & integer'image(to_integer(S_u)) &
                           " Expected=" & integer'image(to_integer(expected_S));
                END IF;

                IF CB_out /= expected_CB_out THEN
                    REPORT "Subtraction borrow mismatch: A=" & integer'image(i) &
                           " B=" & integer'image(j) &
                           " CB_out=" & STD_LOGIC'image(CB_out) &
                           " Expected=" & STD_LOGIC'image(expected_CB_out);
                END IF;
            END LOOP;
        END LOOP;

        WAIT; -- stop simulation
    END PROCESS;
END Test;
```

### หมวดที่ 8: เทมเพลตมาตรฐานจาก vhdl.ai (+ New from template…)

*สอดคล้องกับ: **บทที่ 9 โครงสร้างภาษา VHDL มาตรฐาน***

เมื่อคลิกปุ่ม **+ New from template…** บน vhdl.ai โปรแกรมมี 4 โครงสร้างต้นแบบมาตรฐานที่พร้อมให้หยิบไปเขียนต่อทันที บันทึกไว้ที่ [`vhdl-ai-examples/10-templates/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/10-templates):

#### 8.1 Entity Template — โมดูลรีจิสเตอร์พร้อมรีเซ็ตแบบอะซิงโครนัส
แม่แบบมาตรฐานสำหรับวงจร Synchronous Sequential Circuit ที่มีสัญญาณนาฬิกา `clk` และขา `rst` (ไฟล์: [`template_entity.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/10-templates/template_entity.vhd)):
```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity my_entity is
  port (
    clk : in  std_logic;
    rst : in  std_logic;
    d   : in  std_logic_vector(7 downto 0);
    q   : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of my_entity is
begin
  process (clk, rst)
  begin
    if rst = '1' then
      q <= (others => '0');
    elsif rising_edge(clk) then
      q <= d;
    end if;
  end process;
end architecture;
```

#### 8.2 Testbench Template — โครงเทสต์เบนช์สร้างสัญญาณนาฬิกาอัตโนมัติ
แม่แบบจำลองสัญญาณนาฬิกา (Clock Generator) คาบ 10 ns พร้อมจังหวะสร้างพัลส์รีเซ็ตและหยุดการจำลอง (ไฟล์: [`template_testbench.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/10-templates/template_testbench.vhd)):
```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity my_testbench is
end entity;

architecture sim of my_testbench is
  constant CLK_PERIOD : time := 10 ns;
  signal clk : std_logic := '0';
  signal rst : std_logic := '1';
begin
  clk <= not clk after CLK_PERIOD / 2;
  rst <= '1', '0' after 30 ns;

  process
  begin
    wait for 200 ns;
    report "Simulation finished" severity note;
    wait;
  end process;
end architecture;
```

#### 8.3 Package Template — การสร้างแพ็กเกจชนิดข้อมูลเรคคอร์ดและฟังก์ชัน
แม่แบบสำหรับการแบ่งปันชนิดข้อมูลโครงสร้าง (`record`) และฟังก์ชันมาตรฐานในโปรเจกต์ขนาดใหญ่ (ไฟล์: [`template_package.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/10-templates/template_package.vhd)):
```vhdl
library ieee;
use ieee.std_logic_1164.all;

package my_package is
  constant DATA_WIDTH : positive := 32;
  type bus_t is record
    valid : std_logic;
    data  : std_logic_vector(DATA_WIDTH-1 downto 0);
  end record;
  function bit_count(v : std_logic_vector) return natural;
end package;

package body my_package is
  function bit_count(v : std_logic_vector) return natural is
    variable n : natural := 0;
  begin
    for i in v'range loop
      if v(i) = '1' then n := n + 1; end if;
    end loop;
    return n;
  end function;
end package body;
```

#### 8.4 FSM Template — แบบจำลองเครื่องสถานะจำกัด 3 สถานะ (Two-Process FSM)
โครงสร้าง Finite State Machine แบบแยกส่วนคำนวณ State Register ออกจาก Next-State / Output Logic ตามมาตรฐานสากล (ไฟล์: [`template_fsm.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/10-templates/template_fsm.vhd)):
```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity my_fsm is
  port (
    clk   : in  std_logic;
    rst   : in  std_logic;
    start : in  std_logic;
    done  : out std_logic
  );
end entity;

architecture rtl of my_fsm is
  type state_t is (IDLE, RUN, FINISH);
  signal s, s_next : state_t := IDLE;
begin
  process (clk, rst)
  begin
    if rst = '1' then s <= IDLE;
    elsif rising_edge(clk) then s <= s_next;
    end if;
  end process;

  process (s, start)
  begin
    s_next <= s;
    done   <= '0';
    case s is
      when IDLE   => if start = '1' then s_next <= RUN; end if;
      when RUN    => s_next <= FINISH;
      when FINISH => done <= '1'; s_next <= IDLE;
    end case;
  end process;
end architecture;
```
### หมวดที่ 9: วงจรแสดงผลกราฟิก VGA บน TinyTapeout (VGA Demos — 4 วงจร)

*สอดคล้องกับ: **โครงการผลิตชิปจริง TinyTapeout และการสังเคราะห์ฮาร์ดแวร์***

ตัวอย่างกราฟิก VGA บน vhdl.ai ใช้มาตรฐานพินเอาต์ของโครงการ **TinyTapeout** (บอร์ด TinyVGA) เพื่อสร้างสัญญาณภาพความละเอียด 640x480 @ 60Hz ออกจอภาพจริง โค้ดทั้งหมดคอมไพล์ผ่าน `ghdl-yosys-plugin` เป็น CXXRTL แล้วเรนเดอร์สดลงบนแท็บ **VGA** ในเบราว์เซอร์:

#### 9.1 VGA Color Bars (TinyTapeout) (Live 640x480 VGA color bars rendered to a canvas. Click the VGA tab then Build & Run — the VHDL is synthesized through ghdl-yosys-plugin, emitted as CXXRTL, compiled to WASM with emcc, and stepped at ~40 Mcycles/sec for 60 FPS. Toggle ui_in[0..2] to scramble the bar order. Uses the TinyTapeout pinout (clk, rst_n, ui_in[7:0], uo_out[7:0]) with the TinyVGA bit layout, so the same source synthesizes to a real TinyTapeout submission.)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `tt_um_stripes` | [`vhdl-ai-examples/08-vga-display/vga-color-bars-tinytapeout/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display/vga-color-bars-tinytapeout) |
| **วิธีดูผลการทำงาน** | เปิดแท็บ **VGA** แล้วกด **Build & Run** | ไฟล์วงจร: [`tt_um_stripes.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display/vga-color-bars-tinytapeout/tt_um_stripes.vhd) |

**ไฟล์ `tt_um_stripes.vhd`**
```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- TinyTapeout-pinout VGA stripes demo.
-- Generates a 640x480 60Hz signal with vertical color bars.
-- Pinout: uo_out = { hsync, B(0), G(0), R(0), vsync, B(1), G(1), R(1) }
entity tt_um_stripes is
  port (
    clk    : in  std_logic;
    rst_n  : in  std_logic;
    ui_in  : in  std_logic_vector(7 downto 0);
    uo_out : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of tt_um_stripes is
  -- VGA 640x480 @ 60Hz timing, 25.175 MHz pixel clock
  -- H: 96 sync + 48 back + 640 active + 16 front = 800
  -- V: 2 sync + 33 back + 480 active + 10 front = 525
  signal hpos  : unsigned(9 downto 0) := (others => '0');
  signal vpos  : unsigned(9 downto 0) := (others => '0');
  signal hsync : std_logic;
  signal vsync : std_logic;
  signal vis   : std_logic;
  signal r, g, b : unsigned(1 downto 0);
begin
  process(clk, rst_n)
  begin
    if rst_n = '0' then
      hpos <= (others => '0');
      vpos <= (others => '0');
    elsif rising_edge(clk) then
      if hpos = 799 then
        hpos <= (others => '0');
        if vpos = 524 then vpos <= (others => '0');
        else               vpos <= vpos + 1;
        end if;
      else
        hpos <= hpos + 1;
      end if;
    end if;
  end process;

  hsync <= '0' when hpos < 96 else '1';
  vsync <= '0' when vpos < 2  else '1';
  vis   <= '1' when (hpos >= 144 and hpos < 784 and vpos >= 35 and vpos < 515) else '0';

  -- Vertical color bars: 8 bars of 80 px each across 640 active pixels.
  -- Pick R/G/B per band based on bits of (hpos-144)/80 = active_col bits 4..6.
  process(vis, hpos, vpos, ui_in)
    variable band : unsigned(2 downto 0);
    variable ac   : unsigned(9 downto 0);
  begin
    r <= "00"; g <= "00"; b <= "00";
    if vis = '1' then
      ac   := hpos - 144;
      band := ac(6 downto 4) xor unsigned(ui_in(2 downto 0));
      r <= band(2) & band(2);
      g <= band(1) & band(1);
      b <= band(0) & band(0);
    end if;
  end process;

  uo_out <= hsync & b(0) & g(0) & r(0) & vsync & b(1) & g(1) & r(1);
end architecture;
```

#### 9.2 VGA Checkerboard (A clean intro VGA demo: 640x480 60Hz checkerboard from one XOR of two position bits. Adjust square size with ui_in[5:4] (16/32/64/128 px) and tint the dark squares with ui_in[2:0]. Inspired by classic "first VGA design" tutorials at fpga4fun.com and Nandland. Original VHDL.)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `tt_um_checker` | [`vhdl-ai-examples/08-vga-display/vga-checkerboard/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display/vga-checkerboard) |
| **วิธีดูผลการทำงาน** | เปิดแท็บ **VGA** แล้วกด **Build & Run** | ไฟล์วงจร: [`tt_um_checker.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display/vga-checkerboard/tt_um_checker.vhd) |

**ไฟล์ `tt_um_checker.vhd`**
```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- TinyTapeout-pinout VGA checkerboard demo.
-- A clean intro to VGA: just hsync/vsync timing and a 1-bit pattern from
-- two position bits XOR-ed together.
--
-- ui_in[2:0] : sets the dark-square colour (RGB bits)
-- ui_in[5:4] : square size: 00=32px, 01=64px, 10=128px, 11=16px
--
-- Inspired by the classic "your first VGA design" pattern from fpga4fun
-- and Nandland's VGA tutorial.
entity tt_um_checker is
  port (
    clk    : in  std_logic;
    rst_n  : in  std_logic;
    ui_in  : in  std_logic_vector(7 downto 0);
    uo_out : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of tt_um_checker is
  signal hpos : unsigned(9 downto 0) := (others => '0');
  signal vpos : unsigned(9 downto 0) := (others => '0');
  signal hsync, vsync, vis : std_logic;
  signal cell : std_logic;
  signal r, g, b : unsigned(1 downto 0);
begin
  process(clk, rst_n) is
  begin
    if rst_n = '0' then
      hpos <= (others => '0');
      vpos <= (others => '0');
    elsif rising_edge(clk) then
      if hpos = 799 then
        hpos <= (others => '0');
        if vpos = 524 then vpos <= (others => '0');
        else vpos <= vpos + 1;
        end if;
      else hpos <= hpos + 1;
      end if;
    end if;
  end process;

  hsync <= '0' when hpos < 96 else '1';
  vsync <= '0' when vpos < 2  else '1';
  vis   <= '1' when hpos >= 144 and hpos < 784 and vpos >= 35 and vpos < 515 else '0';

  -- Select which position-bit determines the cell sign (i.e., square size).
  process(hpos, vpos, ui_in)
  begin
    case ui_in(5 downto 4) is
      when "00"   => cell <= hpos(5) xor vpos(5);  -- 32 px
      when "01"   => cell <= hpos(6) xor vpos(6);  -- 64 px
      when "10"   => cell <= hpos(7) xor vpos(7);  -- 128 px
      when others => cell <= hpos(4) xor vpos(4);  -- 16 px
    end case;
  end process;

  process(vis, cell, ui_in) is
  begin
    r <= "00"; g <= "00"; b <= "00";
    if vis = '1' then
      if cell = '1' then
        r <= "11"; g <= "11"; b <= "11";       -- light squares: white
      else
        r <= ui_in(0) & ui_in(0);              -- dark squares: ui_in[2:0]
        g <= ui_in(1) & ui_in(1);
        b <= ui_in(2) & ui_in(2);
      end if;
    end if;
  end process;

  uo_out <= hsync & b(0) & g(0) & r(0) & vsync & b(1) & g(1) & r(1);
end architecture;
```

#### 9.3 VGA XOR Texture (The classic pixel(x, y) = (x XOR y) demoscene pattern, in VHDL. A frame counter drifts the pattern when ui_in[0] is high; ui_in[3:1] permutes the RGB channel order for 6 different colour schemes. Pattern is folklore (Hugo Elias\u2019s "tiny demo" page and countless Shadertoy variants). Pure-VHDL TinyTapeout port is original to VHDLive.)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `tt_um_xor_pattern` | [`vhdl-ai-examples/08-vga-display/vga-xor-texture/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display/vga-xor-texture) |
| **วิธีดูผลการทำงาน** | เปิดแท็บ **VGA** แล้วกด **Build & Run** | ไฟล์วงจร: [`tt_um_xor_pattern.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display/vga-xor-texture/tt_um_xor_pattern.vhd) |

**ไฟล์ `tt_um_xor_pattern.vhd`**
```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- TinyTapeout-pinout VGA "XOR texture" — the classic
--     pixel(x, y) = (x XOR y) bit pattern
-- that shows up in graphics tutorials as a stunning result of one of the
-- simplest possible expressions. A frame counter slowly drifts the pattern.
--
-- ui_in[0]   : enable animation
-- ui_in[3:1] : colour permutation
--
-- Credit: this pattern is a folklore demoscene staple. Discussed e.g. in
-- Hugo Elias's "tiny demo" page and countless Shadertoy variants. Pure-VHDL
-- TinyTapeout port is original to VHDLive.
entity tt_um_xor_pattern is
  port (
    clk    : in  std_logic;
    rst_n  : in  std_logic;
    ui_in  : in  std_logic_vector(7 downto 0);
    uo_out : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of tt_um_xor_pattern is
  signal hpos : unsigned(9 downto 0) := (others => '0');
  signal vpos : unsigned(9 downto 0) := (others => '0');
  signal hsync, vsync, vis : std_logic;
  signal frame_ctr : unsigned(7 downto 0) := (others => '0');
  signal r, g, b : unsigned(1 downto 0);
begin
  process(clk, rst_n) is
  begin
    if rst_n = '0' then
      hpos <= (others => '0');
      vpos <= (others => '0');
      frame_ctr <= (others => '0');
    elsif rising_edge(clk) then
      if hpos = 799 then
        hpos <= (others => '0');
        if vpos = 524 then
          vpos <= (others => '0');
          if ui_in(0) = '1' then
            frame_ctr <= frame_ctr + 1;
          end if;
        else
          vpos <= vpos + 1;
        end if;
      else
        hpos <= hpos + 1;
      end if;
    end if;
  end process;

  hsync <= '0' when hpos < 96 else '1';
  vsync <= '0' when vpos < 2  else '1';
  vis   <= '1' when hpos >= 144 and hpos < 784 and vpos >= 35 and vpos < 515 else '0';

  process(vis, hpos, vpos, frame_ctr, ui_in) is
    variable px  : unsigned(9 downto 0);
    variable py  : unsigned(9 downto 0);
    variable val : unsigned(7 downto 0);
    variable rv, gv, bv : unsigned(1 downto 0);
  begin
    rv := "00"; gv := "00"; bv := "00";
    if vis = '1' then
      px := hpos - 144;
      py := vpos - 35;
      val := (px(7 downto 0) + frame_ctr) xor py(7 downto 0);
      -- Spread the 8-bit XOR result across R, G, B 2-bit channels
      case ui_in(3 downto 1) is
        when "001"  => rv := val(7 downto 6); gv := val(3 downto 2); bv := val(5 downto 4);
        when "010"  => rv := val(3 downto 2); gv := val(7 downto 6); bv := val(5 downto 4);
        when "011"  => rv := val(5 downto 4); gv := val(3 downto 2); bv := val(7 downto 6);
        when "100"  => rv := val(3 downto 2); gv := val(5 downto 4); bv := val(7 downto 6);
        when "101"  => rv := val(5 downto 4); gv := val(7 downto 6); bv := val(3 downto 2);
        when others => rv := val(7 downto 6); gv := val(5 downto 4); bv := val(3 downto 2);
      end case;
    end if;
    r <= rv;
    g <= gv;
    b <= bv;
  end process;

  uo_out <= hsync & b(0) & g(0) & r(0) & vsync & b(1) & g(1) & r(1);
end architecture;
```

#### 9.4 VGA Bouncing Ball (A 32x32 sprite bouncing around the 640x480 visible area on a dark blue background. Position updates once per frame on the vsync falling edge. ui_in[0] pauses, ui_in[3:1] selects ball colour. Inspired by classic "first VGA sprite" tutorials (Mike Field, Nandland). Original VHDL.)

| ช่องตั้งค่าใน vhdl.ai | ค่าที่ต้องระบุ | ลิงก์ไฟล์ซอร์สโค้ด |
|---|---|---|
| **Top Entity** | `tt_um_bouncing_ball` | [`vhdl-ai-examples/08-vga-display/vga-bouncing-ball/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display/vga-bouncing-ball) |
| **วิธีดูผลการทำงาน** | เปิดแท็บ **VGA** แล้วกด **Build & Run** | ไฟล์วงจร: [`tt_um_bouncing_ball.vhd`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/08-vga-display/vga-bouncing-ball/tt_um_bouncing_ball.vhd) |

**ไฟล์ `tt_um_bouncing_ball.vhd`**
```vhdl
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

-- TinyTapeout-pinout VGA bouncing-ball demo.
-- A 32x32 white square bounces around the 640x480 visible area, updating
-- position once per frame.
--
-- ui_in[0]   : pause animation
-- ui_in[3:1] : ball colour (R, G, B bit each)
--
-- Inspired by the classic 'first VGA sprite' pattern from FPGA tutorials
-- (Mike Field, Nandland). Original implementation for VHDLive.
entity tt_um_bouncing_ball is
  port (
    clk    : in  std_logic;
    rst_n  : in  std_logic;
    ui_in  : in  std_logic_vector(7 downto 0);
    uo_out : out std_logic_vector(7 downto 0)
  );
end entity;

architecture rtl of tt_um_bouncing_ball is
  constant H_ACT : natural := 640;
  constant V_ACT : natural := 480;
  constant BALL  : natural := 32;

  signal hpos : unsigned(9 downto 0) := (others => '0');
  signal vpos : unsigned(9 downto 0) := (others => '0');
  signal hsync, vsync, vis : std_logic;

  -- Ball top-left position in active-area coords
  signal bx : unsigned(9 downto 0) := to_unsigned(320 - BALL/2, 10);
  signal by : unsigned(9 downto 0) := to_unsigned(240 - BALL/2, 10);
  -- Velocity sign: '0' = moving right/down, '1' = moving left/up
  signal vx_sign : std_logic := '0';
  signal vy_sign : std_logic := '0';
  signal last_vsync : std_logic := '1';

  signal r, g, b : unsigned(1 downto 0);
begin
  -- ── VGA pixel counter ────────────────────────────────────────────────────
  process(clk, rst_n) is
  begin
    if rst_n = '0' then
      hpos <= (others => '0');
      vpos <= (others => '0');
    elsif rising_edge(clk) then
      if hpos = 799 then
        hpos <= (others => '0');
        if vpos = 524 then vpos <= (others => '0');
        else               vpos <= vpos + 1;
        end if;
      else hpos <= hpos + 1;
      end if;
    end if;
  end process;

  hsync <= '0' when hpos < 96 else '1';
  vsync <= '0' when vpos < 2  else '1';
  vis   <= '1' when hpos >= 144 and hpos < 784 and vpos >= 35 and vpos < 515 else '0';

  -- ── Ball physics: advance once per frame on vsync falling edge ───────────
  process(clk, rst_n) is
  begin
    if rst_n = '0' then
      bx <= to_unsigned(320 - BALL/2, 10);
      by <= to_unsigned(240 - BALL/2, 10);
      vx_sign <= '0';
      vy_sign <= '0';
      last_vsync <= '1';
    elsif rising_edge(clk) then
      last_vsync <= vsync;
      if last_vsync = '1' and vsync = '0' and ui_in(0) = '0' then
        -- Horizontal step
        if vx_sign = '0' then       -- moving right
          if bx + BALL >= H_ACT - 1 then
            vx_sign <= '1';
            bx <= bx - 1;
          else
            bx <= bx + 1;
          end if;
        else                         -- moving left
          if bx = 0 then
            vx_sign <= '0';
            bx <= bx + 1;
          else
            bx <= bx - 1;
          end if;
        end if;
        -- Vertical step
        if vy_sign = '0' then       -- moving down
          if by + BALL >= V_ACT - 1 then
            vy_sign <= '1';
            by <= by - 1;
          else
            by <= by + 1;
          end if;
        else                         -- moving up
          if by = 0 then
            vy_sign <= '0';
            by <= by + 1;
          else
            by <= by - 1;
          end if;
        end if;
      end if;
    end if;
  end process;

  -- ── Pixel colour ─────────────────────────────────────────────────────────
  process(vis, hpos, vpos, bx, by, ui_in) is
    variable px : unsigned(9 downto 0);
    variable py : unsigned(9 downto 0);
    variable in_ball : boolean;
  begin
    r <= "00"; g <= "00"; b <= "00";
    if vis = '1' then
      px := hpos - 144;
      py := vpos - 35;
      in_ball := (px >= bx) and (px < bx + BALL) and (py >= by) and (py < by + BALL);
      if in_ball then
        r <= ui_in(1) & ui_in(1);
        g <= ui_in(2) & ui_in(2);
        b <= ui_in(3) & ui_in(3);
      else
        b <= "01";  -- dark blue background
      end if;
    end if;
  end process;

  uo_out <= hsync & b(0) & g(0) & r(0) & vsync & b(1) & g(1) & r(1);
end architecture;
```

### หมวดที่ 10: สถาปัตยกรรมคอมพิวเตอร์และระบบหน่วยประมวลผล (CPUs & SoCs — 6 ระบบ)

*สอดคล้องกับ: **บทที่ 10 สถาปัตยกรรมคอมพิวเตอร์ (Computer Architecture)***

vhdl.ai ได้รวมระบบประมวลผลขนาดใหญ่ระดับ Open-Source เพื่อแสดงให้เห็นว่า VHDL สามารถใช้บรรยายคอมพิวเตอร์และไมโครโปรเซสเซอร์ได้จริง ตั้งแต่สถาปัตยกรรมเพื่อการศึกษาขนาดเล็กไปจนถึง SoC 32 บิตและ 64 บิต โดยซอร์สโค้ดเต็มของทุกระบบถูกจัดเก็บไว้ในโฟลเดอร์ [`vhdl-ai-examples/09-cpus-socs/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/09-cpus-socs/):

#### 10.1 mini-RISC CPU

**คำอธิบาย:** 16-bit RISC CPU พร้อม 16 Registers, 16 Opcodes, RAM, ROM, GPIO peripheral. Testbench รันโปรแกรมคูณเลข (261 x 6) 512 ไซเคิล

- **จำนวนไฟล์ในระบบ:** 6 ไฟล์
- **Top Entity สำหรับจำลอง:** `testbench`
- **โฟลเดอร์ซอร์สโค้ดเต็มทั้งหมด:** [`vhdl-ai-examples/09-cpus-socs/mini-risc/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/09-cpus-socs/mini-risc)

**ตัวอย่างโครงสร้างไฟล์หลัก: `testbench.vhd` (แสดงบางส่วน)**
```vhdl
library ieee;
use ieee.std_logic_1164.all;

entity testbench is
end entity testbench;

architecture bhv of testbench is
  constant clkHalfPeriod : time := 10 ns;
  constant clkFullPeriod : time := clkHalfPeriod * 2;

  component soc is
    port (
      clk : in std_logic;
      nres : in std_logic;

      gpio_a : inout std_logic_vector(15 downto 0));
  end component soc;

  signal simulation_done : boolean := false;
  signal clk_s : std_logic;
  signal nres_s : std_logic;
  signal gpio_a_s : std_logic_vector(15 downto 0);
begin  -- architecture bhv

  clkgen : process is
  begin
    while not simulation_done loop
      clk_s <= '1';
      wait for clkHalfPeriod;
      clk_s <= '0';
      wait for clkHalfPeriod;
    end loop;
    wait;
  end process;

  nresgen : process is
  begin
    nres_s <= '0';
    wait for clkFullPeriod * 2;
    nres_s <= '1';
    wait;
  end process;

  process is
  begin
    simulation_done <= false;
    wait for clkFullPeriod * 512;
    simulation_done <= true;
    wait;
  end process;

  dut : soc
    port map (
      clk => clk_s,
      nres => nres_s,

      gpio_a => gpio_a_s);
end architecture bhv;
```

#### 10.2 Ben Eater 8-bit CPU

**คำอธิบาย:** VHDL Port ของคอมพิวเตอร์ขนมปัง SAP-1 ของ Ben Eater โดย Ken Jordan (MIT License) เชื่อมต่อกับ UART Transmitter

- **จำนวนไฟล์ในระบบ:** 6 ไฟล์
- **Top Entity สำหรับจำลอง:** `system_tb`
- **โฟลเดอร์ซอร์สโค้ดเต็มทั้งหมด:** [`vhdl-ai-examples/09-cpus-socs/ben-eater-8-bit-cpu/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/09-cpus-socs/ben-eater-8-bit-cpu)

**ตัวอย่างโครงสร้างไฟล์หลัก: `cpu.vhd` (แสดงบางส่วน)**
```vhdl
--
-- Based on Ben Eater's build of the SAP breadboard computer and his excellent videos.
-- https://eater.net/
--
-- Copyright (c) 2017 Ken Jordan
--
-- Permission is hereby granted, free of charge, to any person obtaining a copy
-- of this software and associated documentation files (the "Software"), to deal
-- in the Software without restriction, including without limitation the rights
-- to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
-- copies of the Software, and to permit persons to whom the Software is
-- furnished to do so, subject to the following conditions:
--
-- The above copyright notice and this permission notice shall be included in all
-- copies or substantial portions of the Software.
--
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
-- IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
-- FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
-- AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
-- LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
-- OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
-- SOFTWARE.
--

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

ENTITY cpu IS
	PORT(
		clk_i		: IN	STD_LOGIC;
		clk_en_i	: IN	STD_LOGIC;
		rst_i		: IN	STD_LOGIC;
		ram_data_i	: IN	STD_LOGIC_VECTOR(7 downto 0);
		ram_data_o	: OUT	STD_LOGIC_VECTOR(7 downto 0);
		ram_addr_o	: OUT	STD_LOGIC_VECTOR(3 downto 0);
		ram_write_o : OUT	STD_LOGIC;
		hlt_o		: OUT	STD_LOGIC;
		out_val_o	: OUT	STD_LOGIC_VECTOR(7 downto 0);
		debug_sel_i : IN	STD_LOGIC_VECTOR(3 downto 0);
		debug_out_o : OUT	STD_LOGIC_VECTOR(7 downto 0)
	);
END cpu;

ARCHITECTURE RTL OF cpu IS

	-- format a std_logic_vector as binary string (for simulation)
	function to_bin(uslv : UNSIGNED) return STRING is
		variable Value				: UNSIGNED(uslv'length-1 downto 0);
		variable Digit				: UNSIGNED(0 downto 0);
		variable j					: NATURAL;
		variable Result				: STRING(1 to integer(uslv'length));
		constant BIN				: STRING := "01";
	begin
		Value := (others => '0');
		Value(uslv'length-1 downto 0) := uslv;
		j := 0;
		for i in Result'reverse_range loop
			Digit		:= Value(j downto j);
... (ดูต่อในไฟล์เต็ม 521 บรรทัดที่โฟลเดอร์โครงการ)
```

#### 10.3 RPU RISC-V (RV32I)

**คำอธิบาย:** ไมโครโปรเซสเซอร์สถาปัตยกรรมเปิด RISC-V (RV32I) แบบ 3-Stage Pipeline แยกชุด ALU, Decoder และ Register-Set ชัดเจน

- **จำนวนไฟล์ในระบบ:** 15 ไฟล์
- **Top Entity สำหรับจำลอง:** `rpu_core_tb`
- **โฟลเดอร์ซอร์สโค้ดเต็มทั้งหมด:** [`vhdl-ai-examples/09-cpus-socs/rpu-risc-v-rv32i/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/09-cpus-socs/rpu-risc-v-rv32i)

**ตัวอย่างโครงสร้างไฟล์หลัก: `alu_int32_div.vhd` (แสดงบางส่วน)**
```vhdl
----------------------------------------------------------------------------------
-- Project Name: RISC-V CPU
-- Description: ALU unit for 32-bit integer division ops
-- 
----------------------------------------------------------------------------------
-- Copyright 2020  Colin Riley
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--     http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.
----------------------------------------------------------------------------------

library IEEE;
use IEEE.STD_LOGIC_1164.all;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
use IEEE.NUMERIC_STD.all;
library work;
use work.constants.all;

entity alu_int32_div is
    port (
        I_clk : in STD_LOGIC;
        I_exec : in STD_LOGIC;
        I_dividend : in STD_LOGIC_VECTOR (XLEN32M1 downto 0);
        I_divisor : in STD_LOGIC_VECTOR (XLEN32M1 downto 0);
        I_op : in STD_LOGIC_VECTOR (1 downto 0);
        O_dataResult : out STD_LOGIC_VECTOR (XLEN32M1 downto 0);
        O_done : out STD_LOGIC;
        O_int : out std_logic
    );
end alu_int32_div;

architecture Behavioral of alu_int32_div is
    signal s_done : std_logic := '0';
    signal s_int : std_logic := '0';
    signal s_op : std_logic_vector(1 downto 0) := (others => '0');
    signal s_result : std_logic_vector(XLEN32M1 downto 0) := (others => '0');
    signal s_outsign : std_logic := '0';
    signal s_ur : unsigned(XLEN32M1 downto 0) := (others => '0');

    signal s_i : integer := 0;
    signal s_N : unsigned(XLEN32M1 downto 0) := (others => '0');
    signal s_D : unsigned(XLEN32M1 downto 0) := (others => '0');
    signal s_R : unsigned(XLEN32M1 downto 0) := (others => '0');
    signal s_Q : unsigned(XLEN32M1 downto 0) := (others => '0');
    constant STATE_IDLE : integer := 0;
    constant STATE_INFLIGHTU : integer := 1;
    constant STATE_COMPLETE : integer := 2;

    signal s_state : integer := 0;
... (ดูต่อในไฟล์เต็ม 183 บรรทัดที่โฟลเดอร์โครงการ)
```

#### 10.4 lxp32 32-bit CPU

**คำอธิบาย:** ซีพียูไพป์ไลน์ 32 บิตประสิทธิภาพสูง พร้อมตัวควบคุมแคชคำสั่ง (I-Cache), ตัวคูณฮาร์ดแวร์ และบัส Wishbone

- **จำนวนไฟล์ในระบบ:** 36 ไฟล์
- **Top Entity สำหรับจำลอง:** `tb`
- **โฟลเดอร์ซอร์สโค้ดเต็มทั้งหมด:** [`vhdl-ai-examples/09-cpus-socs/lxp32-32-bit-cpu/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/09-cpus-socs/lxp32-32-bit-cpu)

**ตัวอย่างโครงสร้างไฟล์หลัก: `common_pkg.vhd` (แสดงบางส่วน)**
```vhdl
---------------------------------------------------------------------
-- Common package for LXP32 testbenches
--
-- Part of the LXP32 verification environment
--
-- Copyright (c) 2016 by Alex I. Kuznetsov
---------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

package common_pkg is
	type rng_state_type is record
		seed1: positive;
		seed2: positive;
	end record;

	-- Generate a pseudo-random value of integer type from [a;b] range
	-- Output is stored in x
	procedure rand(variable st: inout rng_state_type; a,b: integer; variable x: out integer);
	
	-- Convert std_logic_vector to a hexadecimal string (similar to
	-- the "to_hstring" function from VHDL-2008
	function hex_string(x: std_logic_vector) return string;
end package;
```

#### 10.5 NEORV32 RISC-V SoC

**คำอธิบาย:** ระบบ Dual-Core RISC-V SoC ระดับอุตสาหกรรม (62 ไฟล์ ~24,000 บรรทัด) พร้อม JTAG Debugger, Caches, UART, SPI, DMA, Timers

- **จำนวนไฟล์ในระบบ:** 62 ไฟล์
- **Top Entity สำหรับจำลอง:** `neorv32_tb`
- **โฟลเดอร์ซอร์สโค้ดเต็มทั้งหมด:** [`vhdl-ai-examples/09-cpus-socs/neorv32-risc-v-soc/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/09-cpus-socs/neorv32-risc-v-soc)

**ตัวอย่างโครงสร้างไฟล์หลัก: `neorv32_tb.vhd` (แสดงบางส่วน)**
```vhdl
-- ================================================================================ --
-- NEORV32 - Default Processor Testbench                                            --
-- -------------------------------------------------------------------------------- --
-- The NEORV32 RISC-V Processor - https://github.com/stnolting/neorv32              --
-- Copyright (c) NEORV32 contributors.                                              --
-- Copyright (c) 2020 - 2026 Stephan Nolting. All rights reserved.                  --
-- Licensed under the BSD-3-Clause license, see LICENSE for details.                --
-- SPDX-License-Identifier: BSD-3-Clause                                            --
-- ================================================================================ --

library ieee;
use ieee.std_logic_1164.all;
use ieee.math_real.all;

library neorv32;
use neorv32.neorv32_package.all;

library work;
use work.jtag_dmi_pkg.all;

entity neorv32_tb is
  generic (
    JTAG_TESTS_EN     : boolean                        := true;        -- enable JTAG/DMI tests in testbench
    -- processor --
    CLOCK_FREQUENCY   : natural                        := 100_000_000; -- clock frequency of clk_i in Hz
    DUAL_CORE_EN      : boolean                        := true;        -- enable dual-core homogeneous SMP
    BOOT_MODE_SELECT  : natural range 0 to 2           := 2;           -- boot from pre-initialized IMEM
    BOOT_ADDR_CUSTOM  : std_ulogic_vector(31 downto 0) := x"00000000"; -- custom CPU boot address (if boot_config = 1)
    RISCV_ISA_C       : boolean                        := true;        -- compressed extension
    RISCV_ISA_E       : boolean                        := false;       -- embedded RF extension
    RISCV_ISA_M       : boolean                        := true;        -- mul/div extension
    RISCV_ISA_U       : boolean                        := true;        -- user mode extension
    RISCV_ISA_Zaamo   : boolean                        := true;        -- atomic read-modify-write operations extension
    RISCV_ISA_Zalrsc  : boolean                        := true;        -- atomic reservation-set operations extension
    RISCV_ISA_Zcb     : boolean                        := true;        -- additional code size reduction instructions
    RISCV_ISA_Zba     : boolean                        := true;        -- shifted-add bit-manipulation extension
    RISCV_ISA_Zbb     : boolean                        := true;        -- basic bit-manipulation extension
    RISCV_ISA_Zbc     : boolean                        := true;        -- carry-less multiplication instructions
    RISCV_ISA_Zbkb    : boolean                        := true;        -- bit-manipulation instructions for cryptography
    RISCV_ISA_Zbkc    : boolean                        := true;        -- carry-less multiplication instructions
    RISCV_ISA_Zbkx    : boolean                        := true;        -- cryptography crossbar permutation extension
    RISCV_ISA_Zbs     : boolean                        := true;        -- single-bit bit-manipulation extension
    RISCV_ISA_Zfinx   : boolean                        := true;        -- 32-bit floating-point extension
    RISCV_ISA_Zibi    : boolean                        := true;        -- branch with immediate
    RISCV_ISA_Zicntr  : boolean                        := true;        -- base counters
    RISCV_ISA_Zicond  : boolean                        := true;        -- integer conditional operations
    RISCV_ISA_Zihpm   : boolean                        := true;        -- hardware performance monitors
    RISCV_ISA_Zimop   : boolean                        := true;        -- may-be-operations
    RISCV_ISA_Zknd    : boolean                        := true;        -- cryptography NIST AES decryption extension
    RISCV_ISA_Zkne    : boolean                        := true;        -- cryptography NIST AES encryption extension
    RISCV_ISA_Zknh    : boolean                        := true;        -- cryptography NIST hash extension
    RISCV_ISA_Zksed   : boolean                        := true;        -- ShangMi block cipher extension
    RISCV_ISA_Zksh    : boolean                        := true;        -- ShangMi hash extension
    RISCV_ISA_Zmmul   : boolean                        := true;        -- multiply-only M sub-extension
    RISCV_ISA_Xcfu    : boolean                        := true;        -- custom (instr.) functions unit
    CPU_CONSTT_BR_EN  : boolean                        := false;       -- constant-time branches
    CPU_FAST_MUL_EN   : boolean                        := true;        -- use DSPs for M extension's multiplier
    CPU_FAST_SHIFT_EN : boolean                        := true;        -- use barrel shifter for shift operations
    CPU_RF_ARCH_SEL   : natural range 0 to 3           := 0;           -- register file implementation style select
    IMEM_EN           : boolean                        := true;        -- implement processor-internal instruction memory
... (ดูต่อในไฟล์เต็ม 725 บรรทัดที่โฟลเดอร์โครงการ)
```

#### 10.6 Microwatt POWER ISA CPU

**คำอธิบาย:** หน่วยประมวลผล 64 บิตมาตรฐาน Open POWER ISA ของ IBM โดยเวอร์ชันบน vhdl.ai ถูกปรับแต่งให้ทดสอบผ่านเบราว์เซอร์ได้

- **จำนวนไฟล์ในระบบ:** 55 ไฟล์
- **Top Entity สำหรับจำลอง:** `bit_counter`
- **โฟลเดอร์ซอร์สโค้ดเต็มทั้งหมด:** [`vhdl-ai-examples/09-cpus-socs/microwatt-power-isa-cpu/`](file:///Volumes/ExDisk/Google%20Drive%20Ksu/KSU/Git/Digital/chapters/ch09-hdl-vhdl/vhdl-ai-examples/09-cpus-socs/microwatt-power-isa-cpu)

**ตัวอย่างโครงสร้างไฟล์หลัก: `bitsort.vhdl` (แสดงบางส่วน)**
```vhdl
-- Implements instructions that involve sorting bits,
-- that is, cfuged, pextd and pdepd.
-- Also does bperm, which is somewhat different.
--
-- cfuged: Sort the bits in the mask in RB into 0s at the left, 1s at the right
--         and move the bits in RS in the same fashion to give the result
-- pextd:  Like cfuged but the only use the bits of RS where the
--         corresponding bit in RB is 1
-- pdepd:  Inverse of pextd; take the low-order bits of RS and spread them out
--         to the bit positions which have a 1 in RB
-- bperm:  Select 8 arbitrary bits 

-- NB opc is bits 7-6 of the instruction:
-- 00 = pdepd, 01 = pextd, 10 = cfuged

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library work;
use work.helpers.all;

entity bit_sorter is
    port (
        clk         : in std_ulogic;
        rst         : in std_ulogic;
        rs          : in std_ulogic_vector(63 downto 0);
        rb          : in std_ulogic_vector(63 downto 0);
        go          : in std_ulogic;
        opc         : in std_ulogic_vector(1 downto 0);
        done        : out std_ulogic;
        do_bperm    : in std_ulogic;
        bperm_done  : out std_ulogic;
        result      : out std_ulogic_vector(63 downto 0)
        );
end entity bit_sorter;

architecture behaviour of bit_sorter is

    signal val : std_ulogic_vector(63 downto 0);
    signal st  : std_ulogic;
    signal sd  : std_ulogic;
    signal opr : std_ulogic_vector(1 downto 0);
    signal bc  : unsigned(5 downto 0);
    signal jl  : unsigned(5 downto 0);
    signal jr  : unsigned(5 downto 0);
    signal sr_ml : std_ulogic_vector(63 downto 0);
    signal sr_mr : std_ulogic_vector(63 downto 0);
    signal sr_vl : std_ulogic_vector(63 downto 0);
    signal sr_vr : std_ulogic_vector(63 downto 0);

    signal is_bperm  : std_ulogic;
    signal bpc       : unsigned(2 downto 0);
    signal bp_done   : std_ulogic;
    signal bperm_res : std_ulogic_vector(7 downto 0);
    signal rs_sr     : std_ulogic_vector(63 downto 0);
    signal rb_bp     : std_ulogic_vector(63 downto 0);

begin
    bsort_r: process(clk)
... (ดูต่อในไฟล์เต็ม 149 บรรทัดที่โฟลเดอร์โครงการ)
```



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


---

### 9. วงจรถอดรหัส (Decoder 2:4 และ Decoder 3:8) — ตารางผลลัพธ์

เมื่อเปิดขา `EN = '1'` วงจรถอดรหัสจะขับบิตเอาต์พุตให้เป็น `'1'` เพียงตำแหน่งเดียวที่ตรงกับรหัสดิจิทัลขาเข้า (Active-High):

```text
 EN   A1   A0  |  Y3   Y2   Y1   Y0   ความหมาย
---------------+-------------------------------
  0    X    X  |   0    0    0    0   Disabled
  1    0    0  |   0    0    0    1   เปิดใช้งานช่อง 0
  1    0    1  |   0    0    1    0   เปิดใช้งานช่อง 1
  1    1    0  |   0    1    0    0   เปิดใช้งานช่อง 2
  1    1    1  |   1    0    0    0   เปิดใช้งานช่อง 3
```

---

### 10. วงจรเข้ารหัสแบบลำดับความสำคัญ (8:3 Priority Encoder)

เมื่อมีหลายขาเข้าทำงานพร้อมกัน วงจรจะเลือกแปลงขาที่มีดัชนีสูงที่สุดเป็นรหัส 3 บิต พร้อมขา `Valid = '1'`:

```text
    D7..D0     |  Y2  Y1  Y0  | Valid | บิตลำดับสูงสุดที่ทำงาน
---------------+--------------+-------+-------------------------
 0 0 0 0 0 0 0 0 |   0   0   0  |   0   | ไม่มีอินพุต (Idle)
 0 0 0 0 0 0 0 1 |   0   0   0  |   1   | D0
 0 0 0 0 0 1 0 0 |   0   1   0  |   1   | D2
 0 0 0 1 1 0 1 0 |   1   0   0  |   1   | D4 (ชนะ D3, D1)
 1 0 1 0 1 0 1 0 |   1   1   1  |   1   | D7 (ชนะทุกตัว)
```

---

### 11. BCD to 7-Segment Driver — ตารางแปลงค่าตัวเลข

เอาต์พุตระดับ Active-High (`a` ถึง `g`) สำหรับขับไดโอดเปล่งแสงของจอแสดงผล:

```text
 BCD (D C B A) |  a  b  c  d  e  f  g  | ตัวเลขที่แสดง
---------------+-----------------------+---------------
    0 0 0 0    |  1  1  1  1  1  1  0  |      "0"
    0 0 0 1    |  0  1  1  0  0  0  0  |      "1"
    0 0 1 0    |  1  1  0  1  1  0  1  |      "2"
    0 0 1 1    |  1  1  1  1  0  0  1  |      "3"
    0 1 0 0    |  0  1  1  0  0  1  1  |      "4"
    0 1 0 1    |  1  0  1  1  0  1  1  |      "5"
    0 1 1 0    |  1  0  1  1  1  1  1  |      "6"
    0 1 1 1    |  1  1  1  0  0  0  0  |      "7"
    1 0 0 0    |  1  1  1  1  1  1  1  |      "8"
    1 0 0 1    |  1  1  1  1  0  1  1  |      "9"
```

---

### 12. วงจรแปลงรหัส Gray 4 บิต (Binary ↔ Gray Code)

ยืนยันความสัมพันธ์ $G_3 = B_3, G_2 = B_3 \oplus B_2, G_1 = B_2 \oplus B_1, G_0 = B_1 \oplus B_0$:

```text
 Binary (B3..B0) | Gray (G3..G0) | บิตที่เปลี่ยนจากแถวก่อนหน้า
-----------------+---------------+--------------------------
      0000       |     0000      | -
      0001       |     0001      | G0
      0010       |     0011      | G1
      0011       |     0010      | G0
      0100       |     0110      | G2
      0101       |     0111      | G0
      0110       |     0101      | G1
      0111       |     0100      | G0
      1000       |     1100      | G3
```

---

### 13. วงจรเปรียบเทียบขนาด 4 บิต (4-bit Magnitude Comparator)

```text
    A      B   | A_gt_B  A_lt_B  A_eq_B | สรุปผล
---------------+------------------------+----------
  0101   0011  |    1       0       0   |  5 > 3
  0010   0110  |    0       1       0   |  2 < 6
  1001   1001  |    0       0       1   |  9 = 9
  1111   0000  |    1       0       0   | 15 > 0
```

---

### 14. วงจรบวก/ลบเลข 4 บิต (4-bit Add/Sub)

เมื่อ `M = '0'` วงจรทำงานเป็นตัวบวก ($A + B$) และเมื่อ `M = '1'` วงจรทำงานเป็นตัวลบ ($A - B$) โดยใช้หลักการ 2's complement:

```text
 M |   A     B   |   Sum / Diff   Cout / Bout | ผลลัพธ์ทางคณิตศาสตร์
---+-------------+----------------------------+-----------------------
 0 | 0101  0011  |      1000           0      |  5 + 3 = 8
 0 | 1100  0101  |      0001           1      | 12 + 5 = 17 (ทด 1)
 1 | 0111  0010  |      0101           0      |  7 - 2 = 5
 1 | 0011  0101  |      1110           1      |  3 - 5 = -2 (ยืม 1)
```

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
