def uygun_mu(matrix, satir, sutun, sayi_degeri):
    for i in range(9):
        if matrix[satir][i] == sayi_degeri:
            return False

    for i in range(9):
        if matrix[i][sutun] == sayi_degeri:
            return False

    alt_kare_satir = (satir // 3) * 3
    alt_kare_sutun = (sutun // 3) * 3
    for i in range(3):
        for j in range(3):
            if matrix[alt_kare_satir + i][alt_kare_sutun + j] == sayi_degeri:
                return False
def solver(matrix, satir=0, sutun=0):
    if sutun == 9:
        satir += 1
        sutun = 0
        if satir == 9:  # Eğer satırlar biterse, Sudoku çözülmüştür
            return True

    return True


def solver(matrix, satir = 0, sutun = 0):
    if sutun == 9:
        satir += 1
        sutun = 0
        if satir == 9:
            return True

    if matrix[satir][sutun] > 0:
        return solver(matrix, satir, sutun + 1)

    for sayi_degeri in range(1,10):
        if uygun_mu(matrix, satir, sutun, sayi_degeri):
            matrix[satir][sutun] = sayi_degeri

            if solver(matrix, satir, sutun + 1):
                return True

        matrix[satir][sutun] = 0

    return False

if __name__ == "__main__":
    sudoku = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solver(sudoku):
        for i in range(9):
            for j in range(9):
                print(sudoku[i][j], end=' ')
            print("")
    else:
        print("Bu sudoku yanlıştır, çözülemez")


