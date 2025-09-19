class Spreadsheet:

    def __init__(self, rows: int):
        self.dic = defaultdict(list)
        for i in range(26):
            ch = chr(65 + i)
            self.dic[ch] = [0 for _ in range(rows + 5)]

    def setCell(self, cell: str, value: int) -> None:
        col = cell[0]
        row = int(cell[1:])
        self.dic[col][row] = value



    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:])
        self.dic[col][row] = 0

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        li = formula.split('+')
        c1, c2 = li[0], li[1]
        res = 0
        if c1[0].isalpha():
            col = c1[0]
            row = int(c1[1:])
            res += self.dic[col][row]
        else:
            res += int(c1)
        
        if c2[0].isalpha():
            col = c2[0]
            row = int(c2[1:])
            res += self.dic[col][row]
        else:
            res += int(c2)

        return res




# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)