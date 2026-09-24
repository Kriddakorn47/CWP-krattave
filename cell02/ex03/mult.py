# รับค่าตัวเลข 2 จำนวน
print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())

# คำนวณผลคูณ
result = num1 * num2

# แสดงผลการคูณ
print(f"{num1} x {num2} = {result}")

# ตรวจสอบเงื่อนไขและแสดงผลตามโจทย์กำหนด
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")