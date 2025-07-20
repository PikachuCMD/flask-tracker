📦 ขั้นตอน Deploy Flask Tracker ไปยัง Render.com

1. สร้างบัญชีฟรีที่ https://render.com
2. ไปที่ https://github.com และสร้าง Repository ใหม่ เช่นชื่อว่า "flask-tracker"
3. นำไฟล์ทั้งหมดในโฟลเดอร์นี้ไปใส่ใน GitHub Repository:
   - app.py
   - requirements.txt
   - render.yaml

4. เข้าสู่ระบบ Render แล้วกด "New Web Service"
5. เชื่อมกับ GitHub และเลือก Repository ที่คุณอัปโหลด
6. ระบบจะ Deploy อัตโนมัติ และแสดง URL เช่น:
   https://flask-tracker.onrender.com/update.css

7. ส่งลิงก์นี้ให้ใครกดจากที่ใดก็ได้ — ระบบจะบันทึก IP และที่อยู่ลง click_log.txt

✅ เสร็จสิ้น!
