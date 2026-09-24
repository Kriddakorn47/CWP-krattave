import sys

# 1. ตรวจสอบว่ามี Argument ส่งเข้ามาหรือไม่
if len(sys.argv) > 1:
    print("none")
    sys.exit()

# 2. ใช้ while loop 2 ตัวในการวนสร้างตารางสูตรคูณ
i = 0
while i <= 10:
    j = 0
    line = f"Table de {i}:"
    while j <= 10:
        line += f" {i * j}"
        j += 1
    print(line)
    i += 1