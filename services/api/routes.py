from flask import Flask, request

from services.api import app
from services.api.controllers.TransactionController import TransactionController
from services.api.controllers.TransactionTypeController import TransactionTypeController
from services.api.controllers.TransactionCategoryController import TransactionCategoryController
from services.api.controllers.MortgageController import MortgageController

@app.route("/")
def home():
    return "HOME PAGE BABY"


#  ----- TRANSACTIONS -----

@app.route("/api/transactions")
def getTransactions():
    transactions = TransactionController().getAll()
    return transactions

@app.route("/api/transactions/<int:transactionId>")
def getTransactionById(transactionId):
    transaction = TransactionController().getById(transactionId)
    return transaction

@app.route("/api/transactions/debits")
def getDebitTransactions():
    debitTransactions = TransactionController().getDebitTransactions()
    return debitTransactions

@app.route("/api/transactions/credits")
def getCreditTransactions():
    creditTransactions = TransactionController().getCreditTransactions()
    return creditTransactions


# ----- TRANSACTION TYPES -----

@app.route("/api/transactionTypes")
def getTransactionTypes():
    transactions = TransactionTypeController().getAll()
    return transactions

@app.route("/api/transactionTypes/<int:transactionTypeId>")
def getTransactionTypeById(transactionTypeId):
    transactions = TransactionTypeController().getById(transactionTypeId)
    return transactions



# ----- TRANSACTION CATEGORIES -----

@app.route("/api/transactionCategories")
def getTransactionCategories():
    transactions = TransactionCategoryController().getAll()
    return transactions

@app.route("/api/transactionCategories/<int:transactionCategoryId>")
def getTransactionCategoriesById(transactionCategoryId):
    transactions = TransactionCategoryController().getById(transactionCategoryId)
    return transactions