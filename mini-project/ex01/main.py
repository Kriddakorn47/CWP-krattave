# main.py

import sys
from checkmate import checkmate, print_pretty_board


def main():
    # 1. เช็กว่าผู้ใช้ส่งชื่อไฟล์มาไหม (ถ้าไม่ส่งเลย พิมพ์ Error)
    if len(sys.argv) < 2:
        print("Error")
        return

    # 2. วนลูปอ่านทุกไฟล์ที่ส่งเข้ามาทาง Command Line
    for filepath in sys.argv[1:]:
        try:
            # เปิดอ่านไฟล์กระดาน
            with open(filepath, 'r') as f:
                board_str = f.read()

            # (Creative Bonus) พิมพ์ชื่อไฟล์และกระดานสัญลักษณ์หมากรุก
            print(f"=== {filepath} ===")
            print_pretty_board(board_str)

            # (Bonus Part 1) เช็กผลลัพธ์ว่า In Check หรือไม่
            checkmate(board_str)
            print()  # เว้นบรรทัดระหว่างแต่ละไฟล์

        except Exception:
            # ถ้าเปิดไฟล์ไม่ได้ หรือไฟล์ไม่มีอยู่จริง ให้พิมพ์ Error
            print("Error")

if __name__ == "__main__":
    main()