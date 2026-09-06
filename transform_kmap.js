const fs = require('fs');
const content = fs.readFileSync('_includes/footer.html', 'utf8');

// We want to transform ALL_GROUPS_3VAR and ALL_GROUPS_4VAR

function swap4VarTerm(term) {
  // Swap A <-> C, B <-> D
  return term.replace(/A/g, 'X').replace(/C/g, 'A').replace(/X/g, 'C')
             .replace(/B/g, 'Y').replace(/D/g, 'B').replace(/Y/g, 'D');
}

function swap4VarHtml(html) {
  return swap4VarTerm(html);
}

function swap4VarExplanation(exp) {
  // Replace A with C, B with D, C with A, D with B
  let res = exp.replace(/A/g, 'X').replace(/C/g, 'A').replace(/X/g, 'C')
               .replace(/B/g, 'Y').replace(/D/g, 'B').replace(/Y/g, 'D');
  // Swap "แถว" (row) and "คอลัมน์" (column)
  res = res.replace(/แถว/g, 'TEMPROW').replace(/คอลัมน์/g, 'แถว').replace(/TEMPROW/g, 'คอลัมน์');
  // Swap "บน/ล่าง" with "ซ้าย/ขวา"
  res = res.replace(/บน/g, 'TEMPTOP').replace(/ซ้าย/g, 'บน').replace(/TEMPTOP/g, 'ซ้าย');
  res = res.replace(/ล่าง/g, 'TEMPBOT').replace(/ขวา/g, 'ล่าง').replace(/TEMPBOT/g, 'ขวา');
  return res;
}

// Map old minterm to new minterm for 4-var (swap AB and CD)
// old physical cell had ABCD. New physical cell has CDAB.
// So the minterm number in the physical cell changes from ABCD to CDAB.
// Wait! If the physical cell stays exactly the same, the `cells` array should NOT change!
// Because `cells` array uses PHYSICAL indices! 
// Wait, no. The cells array uses MINTERM indices in the original code!
// Let's verify this!
