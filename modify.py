import re
import os

# 1. Update kmap-3var.html
html3 = open('_includes/kmap-3var.html', 'r').read()

# Swap headers
html3 = html3.replace(
    '<span class="kmap-diag-lbl kmap-diag-lbl--bc">BC</span>\n          <span class="kmap-diag-lbl kmap-diag-lbl--a">A</span>',
    '<span class="kmap-diag-lbl kmap-diag-lbl--bc">AB</span>\n          <span class="kmap-diag-lbl kmap-diag-lbl--a">C</span>'
)

new_m3 = [0, 2, 6, 4, 1, 3, 7, 5]
counter = [0]
def repl3(match):
    m_val = new_m3[counter[0]]
    counter[0] += 1
    return f'<div class="kmap-cell kmap-cell--interactive" data-index="{m_val}">\n          <span class="kmap-minterm-idx">m{m_val}</span>\n          <span class="kmap-cell-val">0</span>\n        </div>'

html3 = re.sub(r'<div class="kmap-cell kmap-cell--interactive" data-index="\d+">\s*<span class="kmap-minterm-idx">m\d+</span>\s*<span class="kmap-cell-val">0</span>\s*</div>', repl3, html3)

open('_includes/kmap-3var.html', 'w').write(html3)


# 2. Update kmap-4var.html
html4 = open('_includes/kmap-4var.html', 'r').read()
html4 = html4.replace(
    '<span class="kmap-diag-lbl kmap-diag-lbl--bc">CD</span>\n          <span class="kmap-diag-lbl kmap-diag-lbl--a">AB</span>',
    '<span class="kmap-diag-lbl kmap-diag-lbl--bc">AB</span>\n          <span class="kmap-diag-lbl kmap-diag-lbl--a">CD</span>'
)
# Headers
html4 = html4.replace('Row 0 header (AB=00)', 'Row 0 header (CD=00)')
html4 = html4.replace('Row 1 header (AB=01)', 'Row 1 header (CD=01)')
html4 = html4.replace('Row 2 header (AB=11)', 'Row 2 header (CD=11)')
html4 = html4.replace('Row 3 header (AB=10)', 'Row 3 header (CD=10)')
html4 = html4.replace('The Grid (AB is row, CD is column)', 'The Grid (CD is row, AB is column)')

new_m4 = [
    0, 4, 12, 8,
    1, 5, 13, 9,
    3, 7, 15, 11,
    2, 6, 14, 10
]
counter4 = [0]
def repl4(match):
    m_val = new_m4[counter4[0]]
    counter4[0] += 1
    return f'<div class="kmap-cell kmap-cell--interactive" data-index="{m_val}">\n          <span class="kmap-minterm-idx">m{m_val}</span>\n          <span class="kmap-cell-val">0</span>\n        </div>'

html4 = re.sub(r'<div class="kmap-cell kmap-cell--interactive" data-index="\d+">\s*<span class="kmap-minterm-idx">m\d+</span>\s*<span class="kmap-cell-val">0</span>\s*</div>', repl4, html4)

open('_includes/kmap-4var.html', 'w').write(html4)

# 3. Update footer.html
footer = open('_includes/footer.html', 'r').read()

# For 3-var: replace ALL_GROUPS_3VAR entirely
new_groups_3var = """    const ALL_GROUPS_3VAR = [
      // Size 8
      { cells: [0, 1, 2, 3, 4, 5, 6, 7], rows: [0, 1], cols: [0, 1, 2, 3], term: "1", html: "1", explanation: "ทุกช่องในตารางเป็น 1 หรือ X ทำให้ลดรูปเหลือ 1 (วงจรส่งออกเป็นจริงเสมอ)" },

      // Size 4
      { cells: [0, 2, 6, 4], rows: [0], cols: [0, 1, 2, 3], term: "C̅", html: '<span class="kmap-bar">C</span>', explanation: "ครอบคลุมแถวบนทั้งหมด (C=0) ทำให้ตัวแปร A, B ตัดกันออกหมด เหลือเพียง C̅" },
      { cells: [1, 3, 7, 5], rows: [1], cols: [0, 1, 2, 3], term: "C", html: 'C', explanation: "ครอบคลุมแถวล่างทั้งหมด (C=1) ทำให้ตัวแปร A, B ตัดกันออกหมด เหลือเพียง C" },
      { cells: [0, 2, 1, 3], rows: [0, 1], cols: [0, 1], term: "A̅", html: '<span class="kmap-bar">A</span>', explanation: "ครอบคลุมคอลัมน์ 00 และ 01 ทั้งสองแถว (C เปลี่ยน, B เปลี่ยน) เหลือ A คงที่ที่ 0 (A̅)" },
      { cells: [2, 6, 3, 7], rows: [0, 1], cols: [1, 2], term: "B", html: 'B', explanation: "ครอบคลุมคอลัมน์ 01 และ 11 ทั้งสองแถว (C เปลี่ยน, A เปลี่ยน) เหลือ B คงที่ที่ 1 (B)" },
      { cells: [6, 4, 7, 5], rows: [0, 1], cols: [2, 3], term: "A", html: 'A', explanation: "ครอบคลุมคอลัมน์ 11 และ 10 ทั้งสองแถว (C เปลี่ยน, B เปลี่ยน) เหลือ A คงที่ที่ 1 (A)" },
      { cells: [4, 0, 5, 1], rows: [0, 1], cols: [0, 3], term: "B̅", html: '<span class="kmap-bar">B</span>', explanation: "ครอบคลุมคอลัมน์ 10 และ 00 (วนขอบซ้าย-ขวา) ทั้งสองแถว (C เปลี่ยน, A เปลี่ยน) เหลือ B คงที่ที่ 0 (B̅)" },

      // Size 2 (Horizontal)
      { cells: [0, 2], rows: [0], cols: [0, 1], term: "A̅C̅", html: '<span class="kmap-bar">A</span><span class="kmap-bar">C</span>', explanation: "จัดกลุ่ม m0, m2 ในแถว C=0 (C̅) และคอลัมน์ 00, 01 (B เปลี่ยน) เหลือ A คงที่ที่ 0 (A̅)" },
      { cells: [2, 6], rows: [0], cols: [1, 2], term: "BC̅", html: 'B<span class="kmap-bar">C</span>', explanation: "จัดกลุ่ม m2, m6 ในแถว C=0 (C̅) และคอลัมน์ 01, 11 (A เปลี่ยน) เหลือ B คงที่ที่ 1 (B)" },
      { cells: [6, 4], rows: [0], cols: [2, 3], term: "AC̅", html: 'A<span class="kmap-bar">C</span>', explanation: "จัดกลุ่ม m6, m4 ในแถว C=0 (C̅) และคอลัมน์ 11, 10 (B เปลี่ยน) เหลือ A คงที่ที่ 1 (A)" },
      { cells: [4, 0], rows: [0], cols: [0, 3], term: "B̅C̅", html: '<span class="kmap-bar">B</span><span class="kmap-bar">C</span>', explanation: "จัดกลุ่ม m4, m0 (วนขอบซ้าย-ขวา) ในแถว C=0 (C̅) และคอลัมน์ 10, 00 (A เปลี่ยน) เหลือ B คงที่ที่ 0 (B̅)" },
      { cells: [1, 3], rows: [1], cols: [0, 1], term: "A̅C", html: '<span class="kmap-bar">A</span>C', explanation: "จัดกลุ่ม m1, m3 ในแถว C=1 (C) และคอลัมน์ 00, 01 (B เปลี่ยน) เหลือ A คงที่ที่ 0 (A̅)" },
      { cells: [3, 7], rows: [1], cols: [1, 2], term: "BC", html: 'BC', explanation: "จัดกลุ่ม m3, m7 ในแถว C=1 (C) และคอลัมน์ 01, 11 (A เปลี่ยน) เหลือ B คงที่ที่ 1 (B)" },
      { cells: [7, 5], rows: [1], cols: [2, 3], term: "AC", html: 'AC', explanation: "จัดกลุ่ม m7, m5 ในแถว C=1 (C) และคอลัมน์ 11, 10 (B เปลี่ยน) เหลือ A คงที่ที่ 1 (A)" },
      { cells: [5, 1], rows: [1], cols: [0, 3], term: "B̅C", html: '<span class="kmap-bar">B</span>C', explanation: "จัดกลุ่ม m5, m1 (วนขอบซ้าย-ขวา) ในแถว C=1 (C) และคอลัมน์ 10, 00 (A เปลี่ยน) เหลือ B คงที่ที่ 0 (B̅)" },

      // Size 2 (Vertical)
      { cells: [0, 1], rows: [0, 1], cols: [0], term: "A̅B̅", html: '<span class="kmap-bar">A</span><span class="kmap-bar">B</span>', explanation: "จัดกลุ่ม m0, m1 ในคอลัมน์ AB=00 (A̅B̅) ทั้งสองแถว (C เปลี่ยนจาก 0->1 ถูกตัดออก)" },
      { cells: [2, 3], rows: [0, 1], cols: [1], term: "A̅B", html: '<span class="kmap-bar">A</span>B', explanation: "จัดกลุ่ม m2, m3 ในคอลัมน์ AB=01 (A̅B) ทั้งสองแถว (C เปลี่ยนจาก 0->1 ถูกตัดออก)" },
      { cells: [6, 7], rows: [0, 1], cols: [2], term: "AB", html: 'AB', explanation: "จัดกลุ่ม m6, m7 ในคอลัมน์ AB=11 (AB) ทั้งสองแถว (C เปลี่ยนจาก 0->1 ถูกตัดออก)" },
      { cells: [4, 5], rows: [0, 1], cols: [3], term: "AB̅", html: 'A<span class="kmap-bar">B</span>', explanation: "จัดกลุ่ม m4, m5 ในคอลัมน์ AB=10 (AB̅) ทั้งสองแถว (C เปลี่ยนจาก 0->1 ถูกตัดออก)" },

      // Size 1
      { cells: [0], rows: [0], cols: [0], term: "A̅B̅C̅", html: '<span class="kmap-bar">A</span><span class="kmap-bar">B</span><span class="kmap-bar">C</span>', explanation: "ช่อง m0 (แถว C=0, คอลัมน์ AB=00) ไม่สามารถจับกลุ่มร่วมกับช่องข้างเคียงใดๆ ได้" },
      { cells: [2], rows: [0], cols: [1], term: "A̅BC̅", html: '<span class="kmap-bar">A</span>B<span class="kmap-bar">C</span>', explanation: "ช่อง m2 (แถว C=0, คอลัมน์ AB=01) ไม่สามารถจับกลุ่มร่วมกับช่องข้างเคียงใดๆ ได้" },
      { cells: [6], rows: [0], cols: [2], term: "ABC̅", html: 'AB<span class="kmap-bar">C</span>', explanation: "ช่อง m6 (แถว C=0, คอลัมน์ AB=11) ไม่สามารถจับกลุ่มร่วมกับช่องข้างเคียงใดๆ ได้" },
      { cells: [4], rows: [0], cols: [3], term: "AB̅C̅", html: 'A<span class="kmap-bar">B</span><span class="kmap-bar">C</span>', explanation: "ช่อง m4 (แถว C=0, คอลัมน์ AB=10) ไม่สามารถจับกลุ่มร่วมกับช่องข้างเคียงใดๆ ได้" },
      { cells: [1], rows: [1], cols: [0], term: "A̅B̅C", html: '<span class="kmap-bar">A</span><span class="kmap-bar">B</span>C', explanation: "ช่อง m1 (แถว C=1, คอลัมน์ AB=00) ไม่สามารถจับกลุ่มร่วมกับช่องข้างเคียงใดๆ ได้" },
      { cells: [3], rows: [1], cols: [1], term: "A̅BC", html: '<span class="kmap-bar">A</span>BC', explanation: "ช่อง m3 (แถว C=1, คอลัมน์ AB=01) ไม่สามารถจับกลุ่มร่วมกับช่องข้างเคียงใดๆ ได้" },
      { cells: [7], rows: [1], cols: [2], term: "ABC", html: 'ABC', explanation: "ช่อง m7 (แถว C=1, คอลัมน์ AB=11) ไม่สามารถจับกลุ่มร่วมกับช่องข้างเคียงใดๆ ได้" },
      { cells: [5], rows: [1], cols: [3], term: "AB̅C", html: 'A<span class="kmap-bar">B</span>C', explanation: "ช่อง m5 (แถว C=1, คอลัมน์ AB=10) ไม่สามารถจับกลุ่มร่วมกับช่องข้างเคียงใดๆ ได้" }
    ];"""

footer = re.sub(r'    const ALL_GROUPS_3VAR = \[\n.*?\n    \];', new_groups_3var, footer, flags=re.DOTALL)

# For 4-var: replace rows and cols logic
old_row_logic = """        // Rows (AB)
        if (rSet.length === 1) {
          const r = rSet[0];
          if (r === 0) { termParts.push("A̅", "B̅"); htmlParts.push('<span class="kmap-bar">A</span>', '<span class="kmap-bar">B</span>'); expParts.push("A=0 (A̅)", "B=0 (B̅)"); }
          else if (r === 1) { termParts.push("A̅", "B"); htmlParts.push('<span class="kmap-bar">A</span>', 'B'); expParts.push("A=0 (A̅)", "B=1 (B)"); }
          else if (r === 2) { termParts.push("A", "B"); htmlParts.push('A', 'B'); expParts.push("A=1 (A)", "B=1 (B)"); }
          else if (r === 3) { termParts.push("A", "B̅"); htmlParts.push('A', '<span class="kmap-bar">B</span>'); expParts.push("A=1 (A)", "B=0 (B̅)"); }
        } else if (rSet.length === 2) {
          if (rSet.includes(0) && rSet.includes(1)) { termParts.push("A̅"); htmlParts.push('<span class="kmap-bar">A</span>'); expParts.push("A=0 (A̅)"); }
          else if (rSet.includes(2) && rSet.includes(3)) { termParts.push("A"); htmlParts.push('A'); expParts.push("A=1 (A)"); }
          else if (rSet.includes(0) && rSet.includes(3)) { termParts.push("B̅"); htmlParts.push('<span class="kmap-bar">B</span>'); expParts.push("B=0 (B̅)"); }
          else if (rSet.includes(1) && rSet.includes(2)) { termParts.push("B"); htmlParts.push('B'); expParts.push("B=1 (B)"); }
        }"""
new_row_logic = """        // Rows (CD)
        if (rSet.length === 1) {
          const r = rSet[0];
          if (r === 0) { termParts.push("C̅", "D̅"); htmlParts.push('<span class="kmap-bar">C</span>', '<span class="kmap-bar">D</span>'); expParts.push("C=0 (C̅)", "D=0 (D̅)"); }
          else if (r === 1) { termParts.push("C̅", "D"); htmlParts.push('<span class="kmap-bar">C</span>', 'D'); expParts.push("C=0 (C̅)", "D=1 (D)"); }
          else if (r === 2) { termParts.push("C", "D"); htmlParts.push('C', 'D'); expParts.push("C=1 (C)", "D=1 (D)"); }
          else if (r === 3) { termParts.push("C", "D̅"); htmlParts.push('C', '<span class="kmap-bar">D</span>'); expParts.push("C=1 (C)", "D=0 (D̅)"); }
        } else if (rSet.length === 2) {
          if (rSet.includes(0) && rSet.includes(1)) { termParts.push("C̅"); htmlParts.push('<span class="kmap-bar">C</span>'); expParts.push("C=0 (C̅)"); }
          else if (rSet.includes(2) && rSet.includes(3)) { termParts.push("C"); htmlParts.push('C'); expParts.push("C=1 (C)"); }
          else if (rSet.includes(0) && rSet.includes(3)) { termParts.push("D̅"); htmlParts.push('<span class="kmap-bar">D</span>'); expParts.push("D=0 (D̅)"); }
          else if (rSet.includes(1) && rSet.includes(2)) { termParts.push("D"); htmlParts.push('D'); expParts.push("D=1 (D)"); }
        }"""
footer = footer.replace(old_row_logic, new_row_logic)

old_col_logic = """        // Columns (CD)
        if (cSet.length === 1) {
          const c = cSet[0];
          if (c === 0) { termParts.push("C̅", "D̅"); htmlParts.push('<span class="kmap-bar">C</span>', '<span class="kmap-bar">D</span>'); expParts.push("C=0 (C̅)", "D=0 (D̅)"); }
          else if (c === 1) { termParts.push("C̅", "D"); htmlParts.push('<span class="kmap-bar">C</span>', 'D'); expParts.push("C=0 (C̅)", "D=1 (D)"); }
          else if (c === 2) { termParts.push("C", "D"); htmlParts.push('C', 'D'); expParts.push("C=1 (C)", "D=1 (D)"); }
          else if (c === 3) { termParts.push("C", "D̅"); htmlParts.push('C', '<span class="kmap-bar">D</span>'); expParts.push("C=1 (C)", "D=0 (D̅)"); }
        } else if (cSet.length === 2) {
          if (cSet.includes(0) && cSet.includes(1)) { termParts.push("C̅"); htmlParts.push('<span class="kmap-bar">C</span>'); expParts.push("C=0 (C̅)"); }
          else if (cSet.includes(2) && cSet.includes(3)) { termParts.push("C"); htmlParts.push('C'); expParts.push("C=1 (C)"); }
          else if (cSet.includes(0) && cSet.includes(3)) { termParts.push("D̅"); htmlParts.push('<span class="kmap-bar">D</span>'); expParts.push("D=0 (D̅)"); }
          else if (cSet.includes(1) && cSet.includes(2)) { termParts.push("D"); htmlParts.push('D'); expParts.push("D=1 (D)"); }
        }"""
new_col_logic = """        // Columns (AB)
        if (cSet.length === 1) {
          const c = cSet[0];
          if (c === 0) { termParts.push("A̅", "B̅"); htmlParts.push('<span class="kmap-bar">A</span>', '<span class="kmap-bar">B</span>'); expParts.push("A=0 (A̅)", "B=0 (B̅)"); }
          else if (c === 1) { termParts.push("A̅", "B"); htmlParts.push('<span class="kmap-bar">A</span>', 'B'); expParts.push("A=0 (A̅)", "B=1 (B)"); }
          else if (c === 2) { termParts.push("A", "B"); htmlParts.push('A', 'B'); expParts.push("A=1 (A)", "B=1 (B)"); }
          else if (c === 3) { termParts.push("A", "B̅"); htmlParts.push('A', '<span class="kmap-bar">B</span>'); expParts.push("A=1 (A)", "B=0 (B̅)"); }
        } else if (cSet.length === 2) {
          if (cSet.includes(0) && cSet.includes(1)) { termParts.push("A̅"); htmlParts.push('<span class="kmap-bar">A</span>'); expParts.push("A=0 (A̅)"); }
          else if (cSet.includes(2) && cSet.includes(3)) { termParts.push("A"); htmlParts.push('A'); expParts.push("A=1 (A)"); }
          else if (cSet.includes(0) && cSet.includes(3)) { termParts.push("B̅"); htmlParts.push('<span class="kmap-bar">B</span>'); expParts.push("B=0 (B̅)"); }
          else if (cSet.includes(1) && cSet.includes(2)) { termParts.push("B"); htmlParts.push('B'); expParts.push("B=1 (B)"); }
        }"""
footer = footer.replace(old_col_logic, new_col_logic)

# Replace coordToMinterm arrays in footer
old_coord = """      const rowMinterms = [
        [0, 1, 3, 2],
        [4, 5, 7, 6],
        [12, 13, 15, 14],
        [8, 9, 11, 10]
      ];"""
new_coord = """      const rowMinterms = [
        [0, 4, 12, 8],
        [1, 5, 13, 9],
        [3, 7, 15, 11],
        [2, 6, 14, 10]
      ];"""
footer = footer.replace(old_coord, new_coord)

# Replace mIdx in updateGridDisplay for 3var
old_mIdx_3var = "const mIdx = [0, 1, 3, 2, 4, 5, 7, 6];"
new_mIdx_3var = "const mIdx = [0, 2, 6, 4, 1, 3, 7, 5];"
footer = footer.replace(old_mIdx_3var, new_mIdx_3var)

open('_includes/footer.html', 'w').write(footer)
