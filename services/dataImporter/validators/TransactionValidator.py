from ast import Raise
from click import option
from sqlalchemy import false, true
from Validator import Validator

class TransactionValidator(Validator):
    source = None

    def validate(self, transaction):
        self.source = transaction[-1]

        isValid = self.isValidTransactionLength(transaction)
        if not isValid:
            raise Exception("Transaction Is Not A Valid Length")

        isValid = self.transactionHasRequiredFields(transaction)
        if not isValid:
            raise Exception("Transaction does not have valid fields.")
        
        return true

    def isValideTransactionLength(self, transaction):
        optionsLength = {
            "bmoCreditcard2319": 6,
            "bmoCreditcard8420": 6,
            "bmoChequings": 6,
            "default": 6
        }

        expectedLength = optionsLength[self.source]
        if expectedLength is None:
            expectedLength = optionsLength["default"]

        return len(transaction) == expectedLength

    def transactionHasRequiredFields(self, transaction):
        numOfEmptyFields = 0
        minNumOfEmptyFields = 3

        for col in transaction:
            print("COL: " + col)
            if len(col) == 0:
                print("Is None: " + col)
                numOfEmptyFields += 1

        if numOfEmptyFields >= minNumOfEmptyFields:
            return false
        else:
            return true
        