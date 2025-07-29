class Spreadsheet:

    def __init__(self, rows: int):
        self.table = [[0] * 27 for _ in range(rows + 10)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:])
        self.table[row][col] = value
    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:])
        self.table[row][col] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        arr = formula.split('+')
        if arr[0].isdigit() and arr[1].isdigit():
            return int(arr[0]) + int(arr[1])
        elif arr[0].isdigit():
            col = ord(arr[1][0]) - 65
            row = int(arr[1][1:])
            return int(arr[0]) + self.table[row][col]
        elif arr[1].isdigit():
            col = ord(arr[0][0]) - 65
            row = int(arr[0][1:])
            return int(arr[1]) + self.table[row][col]
        else:
            col1 = ord(arr[0][0]) - 65
            row1 = int(arr[0][1:])
            col2 = ord(arr[1][0]) - 65
            row2 = int(arr[1][1:])
            return self.table[row1][col1] + self.table[row2][col2]
    
        return 0


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)