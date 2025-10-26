class Bank:

    def __init__(self, balance: List[int]):
        self.bl = balance
        self.n = len(self.bl)

    def transfer(self, ac1: int, ac2: int, money: int) -> bool:
        n = self.n
        bl = self.bl
        if ac1 <= n and ac2 <= n and money <= bl[ac1 - 1]:
            bl[ac1 - 1] -= money
            bl[ac2 - 1] += money
            return True
        return False

    def deposit(self, ac: int, money: int) -> bool:
        n = self.n
        bl = self.bl
        if ac <= n:
            bl[ac - 1] += money
            return True
        return False

    def withdraw(self, ac: int, money: int) -> bool:
        n = self.n
        bl = self.bl
        if ac <= n and money <= bl[ac - 1]:
            bl[ac - 1] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
