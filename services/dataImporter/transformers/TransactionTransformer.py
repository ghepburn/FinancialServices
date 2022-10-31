from services.dataImporter.transformers.Transformer import Transformer
from services.api.models.Transaction import Transaction

class TransactionTransformer(Transformer):
    
    def transform(self, transaction):
        source = transaction[-1]
        dataMap = self.getMap(source)
        dataMap = dataMap(transaction)

        transactionType = dataMap.getTransactionType()
        transactionTypeId = dataMap.getTransactionTypeId(transactionType)
        transactionCategoryId = dataMap.getTransactionCategoryId()
        transactionDate = dataMap.getTransactionDate()
        transactionAmount = dataMap.getTransactionAmount()
        transactionSource = dataMap.getTransactionSource()
        transactionDescription = dataMap.getTransactionDescription()

        newTransaction = Transaction(transaction_type_id=transactionTypeId, transaction_category_id=transactionCategoryId, date=transactionDate, amount=transactionAmount, source=transactionSource, description=transactionDescription)

        return newTransaction