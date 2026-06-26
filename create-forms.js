/**
 * Google Apps Script for creating Week 1 and Week 2 assignment submission forms.
 * Copy this code and run it at https://script.google.com
 */
function createAssignmentForms() {
  const assignments = [
    {
      week: 1,
      title: "ส่งงานสัปดาห์ที่ 1: บทนำรายวิชาและระบบดิจิทัล",
      desc: "ช่องทางการส่งใบงานวิชา ลอจิกและดิจิทัล\n\nใบงานที่ 1 — รู้จักชุดทดลอง/เครื่องมือวัด และฝึกแทนค่า–นับในเลขฐานต่าง ๆ\nกำหนดตั้งชื่อไฟล์: รหัสนักศึกษา_ชื่อ_lab01.pdf (ตัวอย่าง: 6701001_สมชาย_lab01.pdf)\n\n⚠️ สำคัญ: โปรดเพิ่มคำถามประเภท 'อัปโหลดไฟล์' (File Upload) ในหน้านี้ด้วยตนเองเพื่อใช้รับไฟล์ของนักศึกษา (เนื่องจาก Google Apps Script ไม่อนุญาตให้สร้างคำถามแนบไฟล์ผ่าน Code)",
      filenameExample: "รหัสนักศึกษา_ชื่อ_lab01.pdf"
    },
    {
      week: 2,
      title: "ส่งงานสัปดาห์ที่ 2: เลขคณิตในระบบดิจิทัลและรหัสดิจิทัล",
      desc: "ช่องทางการส่งใบงานวิชา ลอจิกและดิจิทัล\n\nใบงานที่ 2 — การคำนวณเลขฐานสอง (บวก/ลบด้วยคอมพลีเมนต์) และรหัส BCD/Gray/Parity\nกำหนดตั้งชื่อไฟล์: รหัสนักศึกษา_ชื่อ_lab02.pdf (ตัวอย่าง: 6701001_สมชาย_lab02.pdf)\n\n⚠️ สำคัญ: โปรดเพิ่มคำถามประเภท 'อัปโหลดไฟล์' (File Upload) ในหน้านี้ด้วยตนเองเพื่อใช้รับไฟล์ของนักศึกษา (เนื่องจาก Google Apps Script ไม่อนุญาตให้สร้างคำถามแนบไฟล์ผ่าน Code)",
      filenameExample: "รหัสนักศึกษา_ชื่อ_lab02.pdf"
    }
  ];

  assignments.forEach(assign => {
    let form = FormApp.create(assign.title);
    form.setTitle(assign.title)
        .setDescription(assign.desc)
        .setCollectEmail(true)
        .setAllowResponseEdits(true);

    // 1. รหัสนักศึกษา
    let idItem = form.addTextItem();
    idItem.setTitle("รหัสนักศึกษา")
          .setRequired(true);
    let idValidation = FormApp.createTextValidation()
      .requireTextContainsPattern("^\\d+$")
      .setHelpText("กรุณากรอกรหัสนักศึกษาเป็นตัวเลขเท่านั้น")
      .build();
    idItem.setValidation(idValidation);

    // 2. ชื่อ-นามสกุล
    let nameItem = form.addTextItem();
    nameItem.setTitle("ชื่อ-นามสกุล")
            .setRequired(true);

    // 3. หมู่เรียน
    let secItem = form.addListItem();
    secItem.setTitle("หมู่เรียน")
           .setChoiceValues(["กลุ่ม 1", "กลุ่ม 2"])
           .setRequired(true);

    // Section instruction to add File Upload manually
    let section = form.addPageBreakItem();
    section.setTitle("ส่วนอัปโหลดไฟล์ (โปรดกดเพิ่มคำถามประเภท File Upload ตรงนี้ด้วยตนเอง)")
           .setHelpText("1. กดปุ่มบวก (+) เพื่อเพิ่มคำถามใหม่ด้านล่างหัวข้อนี้\n2. เลือกประเภทคำถามเป็น 'อัปโหลดไฟล์' (File Upload)\n3. ตั้งชื่อว่า 'อัปโหลดใบงาน'\n4. เปิดใช้งานคำสั่ง 'จำเป็น' (Required)");

    Logger.log("=========================================");
    Logger.log("สัปดาห์ที่ " + assign.week + ": " + assign.title);
    Logger.log("ลิงก์แก้ไขฟอร์ม (Edit Link): " + form.getEditUrl());
    Logger.log("ลิงก์สำหรับส่งให้นักศึกษา (Published Link): " + form.getPublishedUrl());
  });
  Logger.log("=========================================");
}
