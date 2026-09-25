#!/usr/bin/env python3

# (Bonus Part 2)
PIECE_MAP = {
    'K': '♔',  # King
    'Q': '♕',  # Queen
    'R': '♖',  # Rook
    'B': '♗',  # Bishop
    'P': '♟',  # Pawn
    '.': '·'
}

def print_pretty_board(board_str):
    if not isinstance(board_str, str):
        return

    for line in board_str.splitlines():
        pretty_line = ""
        for char in line:
            symbol = PIECE_MAP.get(char, char)
            pretty_line += symbol + " "
        print(pretty_line)
        
def is_piece(char):
    return char == 'P' or char == 'B' or char == 'R' or char == 'Q'


def check_pawn(board, row, col):

    # Pawn (P):
    # . . . . . . .
    # . . . . . . .
    # . . X . X . .
    # . . . P . . .
    # . . . . . . .
    # . . . . . . .
    # . . . . . . .

    # ถ้าอยู่แถวบนสุด จะไม่มีแถวให้ขึ้นไปอีก กินใครไม่ได้
    if row == 0:
        return False

    # ทแยงขึ้นซ้าย = (row - 1, col - 1)
    # ต้องเช็กก่อนว่า col - 1 ไม่หลุดขอบซ้ายของกระดาน
    if col - 1 >= 0:
        if board[row - 1][col - 1] == 'K':
            return True

    # ทแยงขึ้นขวา = (row - 1, col + 1)
    # ต้องเช็กก่อนว่า col + 1 ไม่หลุดขอบขวาของกระดาน
    if col + 1 < len(board):
        if board[row - 1][col + 1] == 'K':
            return True

    # ไม่เจอ K ในทั้งสองช่อง
    return False

def check_bishop(board, row, col):

    # Bishop (B):
    # X . . . . . X
    # . X . . . X .
    # . . X . X . .
    # . . . B . . .
    # . . X . X . .
    # . X . . . X .
    # X . . . . . X

    size = len(board)

    # ---- ทแยงขึ้นซ้าย (row ลด, col ลด) ----
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:            # ต้องไม่หลุดขอบบนและขอบซ้าย
        if board[r][c] == 'K':
            return True
        if is_piece(board[r][c]):
            break
        r = r - 1
        c = c - 1

    # ---- ทแยงขึ้นขวา (row ลด, col เพิ่ม) ----
    r = row - 1
    c = col + 1
    while r >= 0 and c < size:          # ต้องไม่หลุดขอบบนและขอบขวา
        if board[r][c] == 'K':
            return True
        if is_piece(board[r][c]):
            break
        r = r - 1
        c = c + 1

    # ---- ทแยงลงซ้าย (row เพิ่ม, col ลด) ----
    r = row + 1
    c = col - 1
    while r < size and c >= 0:          # ต้องไม่หลุดขอบล่างและขอบซ้าย
        if board[r][c] == 'K':
            return True
        if is_piece(board[r][c]):
            break
        r = r + 1
        c = c - 1

    # ---- ทแยงลงขวา (row เพิ่ม, col เพิ่ม) ----
    r = row + 1
    c = col + 1
    while r < size and c < size:        # ต้องไม่หลุดขอบล่างและขอบขวา
        if board[r][c] == 'K':
            return True
        if is_piece(board[r][c]):
            break
        r = r + 1
        c = c + 1

    # เดินครบ 4 ทิศแล้วไม่เจอ K
    return False

def check_rook(board, row, col):

    # Rook (R):
    # . . . X . . .
    # . . . X . . .
    # . . . X . . .
    # X X X R X X X
    # . . . X . . .
    # . . . X . . .
    # . . . X . . .

    size = len(board)   # ขนาดกระดาน (กว้าง = สูง เพราะเป็นสี่เหลี่ยมจัตุรัส)

    # ---- ทิศขึ้น (row ลดลง, col คงเดิม) ----
    r = row - 1
    while r >= 0:                       # ยังไม่หลุดขอบบน
        if board[r][col] == 'K':        # เจอ K = รุก
            return True
        if is_piece(board[r][col]):     # เจอหมากอื่นขวาง = หยุดทิศนี้
            break
        r = r - 1                       # ช่องว่าง เดินต่อขึ้นไปอีกช่อง

    # ---- ทิศลง (row เพิ่มขึ้น, col คงเดิม) ----
    r = row + 1
    while r < size:                     # ยังไม่หลุดขอบล่าง
        if board[r][col] == 'K':
            return True
        if is_piece(board[r][col]):
            break
        r = r + 1

    # ---- ทิศซ้าย (col ลดลง, row คงเดิม) ----
    c = col - 1
    while c >= 0:                       # ยังไม่หลุดขอบซ้าย
        if board[row][c] == 'K':
            return True
        if is_piece(board[row][c]):
            break
        c = c - 1

    # ---- ทิศขวา (col เพิ่มขึ้น, row คงเดิม) ----
    c = col + 1
    while c < size:                     # ยังไม่หลุดขอบขวา
        if board[row][c] == 'K':
            return True
        if is_piece(board[row][c]):
            break
        c = c + 1

    # เดินครบ 4 ทิศแล้วไม่เจอ K
    return False

def check_queen(board, row, col):

    # Queen (Q)
    # X . . X . . X
    # . X . X . X .
    # . . X X X . .
    # X X X Q X X X
    # . . X X X . .
    # . X . X . X .
    # X . . X . . X

    if check_bishop(board, row, col):
        return True
    if check_rook(board, row, col):
        return True
    return False

def is_valid(rows):
    # ตรวจว่าบอร์ดถูกต้องก่อนเริ่มเช็ก (rows คือ list ของแถว)

    # 1) บอร์ดว่างเปล่า
    if len(rows) == 0:
        return False

    # 2) ต้องเป็นสี่เหลี่ยมจัตุรัส
    for row in rows:
        if len(row) != len(rows):
            return False

    # 3) ต้องมี K ตัวเดียวเท่านั้น
    count = 0
    for row in rows:
        for char in row:
            if char == 'K':
                count = count + 1
    if count != 1:
        return False

    # ผ่านทุกเงื่อนไข
    return True

def checkmate(board):

    # อินพุตต้องเป็นข้อความ ถ้าไม่ใช่ (เช่น None, ตัวเลข) พิมพ์ Error
    if not isinstance(board, str):
        print("Error")
        return

    # แยกข้อความเป็น list ของแถว เช่น "R.\n.K" -> ["R.", ".K"]
    rows = board.splitlines()

    # ตรวจบอร์ดก่อน ถ้าผิดพิมพ์ Error แล้วจบเลย
    if not is_valid(rows):
        print("Error")
        return

    # วนดูทุกช่องในกระดาน ทีละแถว ทีละคอลัมน์
    for row in range(len(rows)):
        for col in range(len(rows)):
            piece = rows[row][col]

            if piece == 'P':
                if check_pawn(rows, row, col):
                    print("Success")
                    return
            elif piece == 'R':
                if check_rook(rows, row, col):
                    print("Success")
                    return
            elif piece == 'B':
                if check_bishop(rows, row, col):
                    print("Success")
                    return
            elif piece == 'Q':
                if check_queen(rows, row, col):
                    print("Success")
                    return

    # วนครบทุกช่องแล้วไม่มีหมากตัวไหนกิน K ได้
    print("Fail")