original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# นำเฉพาะค่าที่มากกว่า 5 มาบวก 2 แล้วแปลงเป็น set เพื่อลบค่าซ้ำ
new_array = {x + 2 for x in original_array if x > 5}

print(original_array)
print(new_array)