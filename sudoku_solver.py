
def display(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid(board, x, y, val):
    # Check row
    if val in board[x]:
        return False
    
    # Check column
    for row in board:
        if row[y] == val:
            return False
    
    # Check 3x3 sub-grid
    smi, smj = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[smi + i][smj + j] == val:
                return False
    
    return True

def solve_sudoku(board, i=0, j=0):
    if i == 9:
        print("Final Solution:")
        display(board)
        return True
    
    ni, nj = (i + 1, 0) if j == 8 else (i, j + 1)
    
    if board[i][j] != 0:
        return solve_sudoku(board, ni, nj)
    
    for num in range(1, 10):
        if is_valid(board, i, j, num):
            board[i][j] = num
            print(f"Placing {num} at ({i}, {j}):")
            display(board)
            if solve_sudoku(board, ni, nj):
                return True
            print(f"Backtracking at ({i}, {j})")
            board[i][j] = 0
            display(board)
    
    return False

def main():
    board = []
    print("Enter the Sudoku puzzle row by row, use 0 for empty cells:")
    for _ in range(9):
        board.append(list(map(int, input().split())))
    
    print("Initial Board:")
    display(board)
    
    if not solve_sudoku(board):
        print("No solution exists.")

if __name__ == "__main__":
    main()
