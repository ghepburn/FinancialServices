from flask import Flask, request

from services.api import app
from services.api.controllers.TransactionController import TransactionController
from services.api.controllers.TransactionTypeController import TransactionTypeController
from services.api.controllers.TransactionCategoryController import TransactionCategoryController
from services.api.controllers.TransactionSourceController import TransactionSourceController

@app.route("/", methods = ["GET"])
def home():
    return "HOME PAGE BABY"

@app.route("/transactions/import", methods = ["POST"])
def importTransactions():
    transactionImporter = ""
    return "Importing Transaction Data"

@app.route("/transactions/import/logs", methods=["GET", "POST"])
def getTransactionImportLogs():
    if request.method == "GET":
        return "Getting transaction import logs"
    else:
        return "Creating transaction import logs: " + request.data

@app.route("/transactions/sources", methods = ["GET", "POST"])
def transactionSources():
    if request.method == "GET":
        maps = TransactionSourceController().getAll()
        return maps
    elif request.method == "POST":
        map = TransactionSourceController().create(request.data)
        return map

@app.route("/transactions/sources/<transactionSourceId>", methods = ["GET", "PUT", "DELETE"])
def getTransactionImportMaps(transactionSourceId):
    if request.method == "GET":
        maps = TransactionSourceController().getById(transactionSourceId)
        return maps
    elif request.method == "POST":
        map = TransactionSourceController().create(transactionSourceId, request.data)
        return map
    elif request.method == "DELETE":
        map = TransactionSourceController().delete(transactionSourceId, request.data)

@app.route("/transactions/sources/<transactionSourceId>/map", methods = ["GET", "POST", "DELETE"])
def getTransactionImportMaps(transactionSourceId):
    if request.method == "GET":
        map = TransactionSourceMapController(transactionSourceId).getAll()
        return map
    elif request.method == "POST":
        map = TransactionSourceMapController(transactionSourceId).create(request.data)
        return map
    elif request.method == "DELETE":
        map = TransactionSourceMapController(transactionSourceId).delete()
        return map
    


@app.route("/transactions")
def transactions():
    transactions = TransactionController().getAll()
    return transactions

@app.route("/transactions/<int:transactionId>")
def transactionById(transactionId):
    transaction = TransactionController().getById(transactionId)
    return transaction

@app.route("/api/transactions/types", methods = ["GET", "POST"])
def transactionTypes():
    if request.method == 'GET':
        transactionTypes = TransactionTypeController().getTransactionTypes()
        return transactionTypes
    elif request.method == "POST":
        transactionType = TransactionTypeController().createTransactionType(request.data)
        return transactionType

@app.route("/api/transactions/types/<transactionTypeId>", methods = ["GET", "PUT", "DELETE"])
def transactionType(transactionTypeId):
    if request.method == "GET":
        transactionType = TransactionTypeController().getTransactionType(transactionTypeId)
        return transactionType
    elif request.method == "PUT":
        transactionType = TransactionTypeController().updateTransactionType(transactionTypeId, request.data)
        return transactionType
    elif request.method == "DELETE":
        transactionType = TransactionTypeController().deleteTransactionType(transactionTypeId)
        return transactionType

@app.route("/api/transactions/categories", methods = ["GET", "POST"])
def transactionCategories():
    if request.method == 'GET':
        transactionCategories = TransactionCategoryController().getTransactionCategories()
        return transactionCategories
    elif request.method == "POST":
        transactionCategory = TransactionCategoryController().createTransactionCategory(request.data)
        return transactionCategory

@app.route("/api/transactions/categories/<transactionCategoryId>", methods = ["GET", "PUT", "DELETE"])
def transactionCategory(transactionCategoryId):
    if request.method == "GET":
        transactionCategories = TransactionCategoryController().getTransactionCategory(transactionCategoryId)
        return transactionCategories
    elif request.method == "PUT":
        transactionCategory = TransactionCategoryController().updateTransactionCategory(transactionCategoryId, request.data)
        return transactionCategory
    elif request.method == "DELETE":
        transactionCategory = TransactionCategoryController().deleteTransactionCategory(transactionCategoryId)
        return transactionCategory