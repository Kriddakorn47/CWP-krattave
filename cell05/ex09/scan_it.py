import sys
import re

# เช็กว่าจำนวนพารามิเตอร์ไม่เท่ากับ 2 หรือไม่ (sys.argv[0] คือชื่อโปรแกรม รวมแล้วต้องเป็น 3)
if len(sys.argv) != 3:
    print("none")
else:
    key = sys.argv[1]
    word = sys.argv[2]
    
    res = re.findall(key, word)
    
    # ถ้าพบคำหลัก (res ไม่เป็น List บล็อกว่าง) ให้แสดงจำนวน ถ้าหาไม่เจอให้แสดง none
    if res:
        print(len(res))
    else:
        print("none")