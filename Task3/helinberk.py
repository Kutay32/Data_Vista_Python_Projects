
def sudoku_to_solve(row,col):
    matrix=[]
    print("Please enter the Sudoku you want to solve.")
    print("Only 9x9 Sudoku should be entered.")
    print("use -1 for empty row and col")
    for i in range(9):
        row =input(f"{i+1}. enter the row").split()
        matrix.append([int(x) for x in row])

    return matrix


def find_next_empty(matrix):
    for row in range(9):
        for col in range(9):
            if matrix[row][col]== -1:
                return row,col
    return None,None


def is_valid(matrix,guess,row,col):
    if guess in matrix[row]:
        return False

    if guess in [matrix[row][col] for row in range(9)]:
        return False

    first_row,first_col = 3 * (row//3) , 3 * (col//3)
    for row in range (first_row , first_row+3):
        for col in range (first_col, first_col+3):
             if matrix[row][col]== guess:
                 return False
    return True


def solve_sudoku(matrix):
    row , col= find_next_empty(matrix)
    if row is None:
        return True

    for guess in range(1,10):
        if is_valid(matrix,guess,row,col):
            matrix[row][col] =guess
            if solve_sudoku(matrix):
                return True
            matrix [row][col] = -1

    return False



if __name__ == '__main__':
    matrix =[
        [-1,7,2,-1,-1,4,9,-1,-1],
        [3,-1,4,-1,8,9,1,-1,-1],
        [8,1,9,-1,-1,6,2,5,4],
        [7,-1,1,-1,-1,-1,-1,9,5],
        [ 9,-1,-1,-1,-1,2,-1,7,-1],
        [-1,-1,-1,8,-1,7,-1,1,2],
        [4,-1,5,-1,-1,1,6,2,-1],
        [2,3,7,-1,-1,-1,5,-1,1],
        [-1,-1,-1,-1,2,5,7,-1,-1]
        ]
    print(solve_sudoku(matrix))
    print(matrix)















