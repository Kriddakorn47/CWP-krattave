# 1. กำหนด Array เริ่มต้น
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# 2. วนลูปสร้าง Array ใหม่โดยนำค่าเดิมมาบวก 2
new_array = [x + 2 for x in original_array]

# 3. แสดงผล Array ทั้งสอง
print("Original array:", original_array)
print("New array:", new_array)