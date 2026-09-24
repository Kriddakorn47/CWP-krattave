# 1. กำหนด Array ต้นฉบับตามตัวอย่างโจทย์
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. กรองเฉพาะค่าที่มากกว่า 5 แล้วบวกเพิ่ม 2 เข้าไป
new_array = [x + 2 for x in original_array if x > 5]

# 3. แสดงผล Array ทั้งสอง
print(original_array)
print(new_array)