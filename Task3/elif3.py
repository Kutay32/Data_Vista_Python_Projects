
from pprint import pprint
def bir_sonraki_bos_hucreyi_bul(puzzle):
    for satir in range(9):
        for sütun in range(9):
            if puzzle[satir][sütun] == -1:
                return satir, sütun
    return None, None
def gecerli_mi(puzzle, tahmin, satir,sütun):
    if tahmin in puzzle[satir]:
        return False
    sütun_dizisi = [puzzle[i][sütun] for i in range(9)]
    if tahmin in sütun_dizisi:
        return False
    kutu_satir = (satir // 3)*3
    kutu_sütun = (sütun // 3)*3
    for i in range(kutu_satir,kutu_satir+3 ):
        for j in range(kutu_sütun,kutu_sütun+3):
            if puzzle[i][j] == tahmin:
                return False
    return True
def sudoku_coz(puzzle):
    satir, sütun = bir_sonraki_bos_hucreyi_bul(puzzle)
    if satir is None:
        return True
    for tahmin in range(1, 10):
        if gecerli_mi(puzzle, tahmin, satir, sütun):
            puzzle[satir][sütun]=tahmin
            if sudoku_coz(puzzle):
                return True
        puzzle[satir][sütun] = -1
    return False
def kullanicidan_sudoku_al():
    puzzle = []
    print("Lütfen 9x9'luk Sudoku bulmacasını girin. Boş hücreler için -1 kullanın:")

    for i in range(9):
        satir = input(f"Satır {i + 1}: ").split()
        puzzle.append([int(x) for x in satir])

    return puzzle


if __name__ == '__main__':
    example_board = [
            [3, 9, -1, -1, 5, -1, -1, -1, -1],
            [-1, -1, -1, 2, -1, -1, -1, -1, 5],
            [-1, -1, -1, 7, 1, 9, -1, 8, -1],

            [-1, 5, -1, -1, 6, 8, -1, -1, -1],
            [2, -1, 6, -1, -1, 3, -1, -1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, 4],

            [5, -1, -1, -1, -1, -1, -1, -1, -1],
            [6, 7, -1, 1, -1, 5, -1, 4, -1],
            [1, -1, 9, -1, -1, -1, 2, -1, -1]
        ]
    print(sudoku_coz(example_board))
    pprint(example_board)

