import datetime as dt

from services.api import db
from services.api.models.TransactionType import TransactionType
from services.api.models.TransactionCategory import TransactionCategory
from services.api.models.Transaction import Transaction 
from services.api.models.TransactionSource import TransactionSource
from services.api.models.TransactionSourceMap import TransactionSourceMap 

db.create_all()

# transactionType1 = TransactionType(name="Debit")
# transactionType2 = TransactionType(name="Credit")

# transactionCategory1 = TransactionCategory(name="Restaurants")
# TransactionCategory.save()
# transactionCategory2 = TransactionCategory(name="Grocery")
# transactionCategory3 = TransactionCategory(name="Utillities")
# transactionCategory4 = TransactionCategory(name="EmploymentIncome")

# db.session.add(transactionType1)
# db.session.add(transactionType2)

# db.session.add(transactionCategory1)
# db.session.add(transactionCategory2)
# db.session.add(transactionCategory3)
# db.session.add(transactionCategory4)

# db.session.commit()

# transactionSource1 = TransactionSource(name="BMOCreditCard")
# transactionSource1.save()
# transactionSource2 = TransactionSource(name="TDCreditCard")
# transactionSource2.save()
# transactionSource3 = TransactionSource(name="BMOChequings")
# transactionSource3.save()

# transaction1 = Transaction(id=1, transaction_type_id=1, transaction_category_id=1, date=dt.date(2022, 1, 1), source="BMOCreditCard", description="Restaurant Refund")
# transaction2 = Transaction(id=2, transaction_type_id=1, transaction_category_id=4, date=dt.date(2022, 1, 1), source="BMOCreditCard", description="Job Pay")
# transaction3 = Transaction(id=3, transaction_type_id=2, transaction_category_id=1, date=dt.date(2022, 1, 1), source="BMOCreditCard", description="KFC Baby")
# transaction4 = Transaction(id=4, transaction_type_id=2, transaction_category_id=2, date=dt.date(2022, 1, 1), source="BMOCreditCard", description="NOFrills")



# db.session.add(transaction1)
# db.session.add(transaction2)
# db.session.add(transaction3)
# db.session.add(transaction4)

# db.session.commit()

print('TRANSACTIONS')
print(Transaction.query.all())

print("TYPES")
print(TransactionType.query.all())

print('CATEGORIES')
print(TransactionCategory.query.all())