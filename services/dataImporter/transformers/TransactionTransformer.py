from services.dataImporter.transformers.Transformer import Transformer
from services.api.models.Transaction import Transaction

class TransactionTransformer(Transformer):
    
    def transform(self, transaction):
        # transaction = self.TransactionTransformer.transform(transaction)
        # transactionColumns = Transaction.getColumnMap()
        # externalId = transaction[]
        # transactionModel = Transaction.query.filter_by(Transaction.externalId=)

        return transaction