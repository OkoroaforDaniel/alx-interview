import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed in the given cell without attacking others
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def nqueens(board, row, N, solutions):
    # Base case: All queens are placed successfully, add the solution to the list
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            nqueens(board, row + 1, N, solutions)
            board[row] = -1

def print_solutions(N, solutions):
    for solution in solutions:
        print(solution)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    nqueens(board, 0, N, solutions)
    print_solutions(N, solutions)

if __name__ == "__main__":
    main()

