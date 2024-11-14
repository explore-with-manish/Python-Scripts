# class BankAccount:
#     def __init__(self, accNo, bankName):
#         self._accNumber = accNo
#         self._bankName = bankName

#     def getAccountNumber(self):
#         return self._accNumber

#     def getBankName(self):
#         return self._bankName

# a1 = BankAccount(1, "ICICI")
# print("Bank Name: ", a1.getBankName())
# print("Account Number: ", a1.getAccountNumber())

# a2 = BankAccount(2, "ICICI")
# print("Bank Name: ", a2.getBankName())
# print("Account Number: ", a2.getAccountNumber())

# ---------------------------------------------------------------

class BankAccount:
    _bankName = "ICICI"

    def __init__(self, accNo):
        self._accNumber = accNo

    def getAccountNumber(self):
        return self._accNumber

    def getBankName(self):
        return BankAccount._bankName

    @staticmethod
    def setBankName(value):
        BankAccount._bankName = value

BankAccount.setBankName("HDFC")

a1 = BankAccount(1)
print("Bank Name: ", a1.getBankName())
print("Account Number: ", a1.getAccountNumber())

a2 = BankAccount(2)
print("Bank Name: ", a2.getBankName())
print("Account Number: ", a2.getAccountNumber())