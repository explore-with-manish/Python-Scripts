# Create a BankAccount Class with bankName and accName as data properties and 
# create accessor properties 
# to access the data outside using instance.

# class BankAccount:
#     def __init__(self, accNo, bName):
#         self._accNumber = accNo
#         self._bankName = bName

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

# class BankAccount:
#     def __init__(self, accNo, bName):
#         self._accNumber = accNo
#         self._bankName = bName

#     @property
#     def AccountNumber(self):
#         return self._accNumber
    
#     @property
#     def BankName(self):
#         return self._bankName
    
# a1 = BankAccount(1, "ICICI")
# print("Bank Name: ", a1.BankName)
# print("Account Number: ", a1.AccountNumber)

# a2 = BankAccount(2, "ICICI")
# print("Bank Name: ", a2.BankName)
# print("Account Number: ", a2.AccountNumber)

class BankAccount:
    _bankName = "ICICI"

    def __init__(self, accNo):
        self._accNumber = accNo

    @property
    def AccountNumber(self):
        return self._accNumber
    
    @property
    def BankName(self):
        return BankAccount._bankName
    
    @BankName.setter
    def BankName(self,value):
        BankAccount._bankName = value

    @staticmethod
    def setBankName(value):
        BankAccount._bankName = value
    
a1 = BankAccount(1)
print("Bank Name: ", a1.BankName)
print("Account Number: ", a1.AccountNumber)

a2 = BankAccount(2)
print("Bank Name: ", a2.BankName)
print("Account Number: ", a2.AccountNumber)

print("\nUpdating Bank Name using Prop")
BankAccount.BankName = "BFL"        # Property
print("Bank Name: ", a1.BankName)
print("Account Number: ", a1.AccountNumber)
print("Bank Name: ", a2.BankName)
print("Account Number: ", a2.AccountNumber)

print("\nUpdating Bank Name using Fn")
BankAccount.setBankName("HDFC")        # Function Call
print("Bank Name: ", a1.BankName)
print("Account Number: ", a1.AccountNumber)
print("Bank Name: ", a2.BankName)
print("Account Number: ", a2.AccountNumber)


