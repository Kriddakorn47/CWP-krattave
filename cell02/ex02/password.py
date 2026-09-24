# ตัวแปรเก็บรหัสผ่านตามโจทย์
correct_password = "Python is awesome"

# รับรหัสผ่านที่ผู้ใช้พิมพ์เข้ามา
user_input = input()

# ตรวจสอบเงื่อนไข
if user_input == correct_password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")