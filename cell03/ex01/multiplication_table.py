# รับค่าตัวเลขจากผู้ใช้
num = int(input("Enter a number\n"))

# ลูปคูณตั้งแต่ 0 ถึง 9 (range(10) จะได้ค่า 0, 1, 2, ..., 9)
for i in range(10):
    print(f"{i} x {num} = {i * num}")