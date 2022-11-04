from flask import Flask, request
import json

from services.api import app
from services.api.controllers.TransactionController import TransactionController
from services.api.controllers.TransactionTypeController import TransactionTypeController
from services.api.controllers.TransactionCategoryController import TransactionCategoryController
from services.api.controllers.TransactionSourceController import TransactionSourceController
from services.api.controllers.TransactionSourceMapController import TransactionSourceMapController
from services.api.controllers.LogController import LogController

@app.route("/", methods = ["GET"])
def home():
    return "Welcome To Financial Services API"

@app.route("/transactions/import", methods = ["POST"])
def importTransactions():
    transactionImporter = ""
    return "Importing Transaction Data"

@app.route("/transactions/logs", methods=["GET", "POST"])
def logs():
    if request.method == "GET":
        logs = LogController.getALL()
        return logs
    elif request.method == "POST":
        log = LogController.create(request.json)
        return log

@app.route("/transactions/sources", methods = ["GET", "POST"])
def transactionSources():
    if request.method == "GET":
        sources = TransactionSourceController().getAll()
        return sources
    elif request.method == "POST":
        source = TransactionSourceController().create(request.json)
        return source

@app.route("/transactions/sources/<transactionSourceId>", methods = ["GET", "PUT", "DELETE"])
def transactionSource(transactionSourceId):
    if request.method == "GET":
        source = TransactionSourceController().getById(transactionSourceId)
        return source
    elif request.method == "PUT":
        source = TransactionSourceController().update(transactionSourceId, request.json)
        return source
    elif request.method == "DELETE":
        source = TransactionSourceController().delete(transactionSourceId)
        return source

@app.route("/transactions/sources/<transactionSourceId>/map", methods = ["GET", "POST", "DELETE"])
def transactionSourceMap(transactionSourceId):
    if request.method == "GET":
        maps = TransactionSourceMapController(transactionSourceId).getAll()
        return maps
    elif request.method == "POST":
        map = TransactionSourceMapController(transactionSourceId).create(request.json)
        return map
    elif request.method == "DELETE":
        map = TransactionSourceMapController(transactionSourceId).delete()
        return map
    

@app.route("/transactions", methods=["GET", "POST"])
def transactions():
    if request.method == "GET":
        transactions = TransactionController().getAll()
        return transactions
    elif request.method == "POST":
        transaction = TransactionController.create(request.json)
        return transaction

@app.route("/transactions/<int:transactionId>", methods=["GET", "PUT", "DELETE"])
def transaction(transactionId):
    if request.method == "GET":
        transaction = TransactionController().getById(transactionId)
        return transaction
    elif request.method == "PUT":
        transaction = TransactionController.update(transactionId, request.json)
        return transaction
    elif request.method == "DELETE":
        transaction = TransactionController.delete(transactionId)
        return transaction

@app.route("/api/transactions/types", methods = ["GET", "POST"])
def transactionTypes():
    if request.method == 'GET':
        transactionTypes = TransactionTypeController().getAll()
        return transactionTypes
    elif request.method == "POST":
        transactionType = TransactionTypeController().create(request.json)
        return transactionType

@app.route("/api/transactions/types/<transactionTypeId>", methods = ["GET", "PUT", "DELETE"])
def transactionType(transactionTypeId):
    if request.method == "GET":
        transactionType = TransactionTypeController().getById(transactionTypeId)
        return transactionType
    elif request.method == "PUT":
        transactionType = TransactionTypeController().update(transactionTypeId, request.data)
        return transactionType
    elif request.method == "DELETE":
        transactionType = TransactionTypeController().delete(transactionTypeId)
        return transactionType

@app.route("/api/transactions/categories", methods = ["GET", "POST"])
def transactionCategories():
    if request.method == 'GET':
        transactionCategories = TransactionCategoryController().getAll()
        return transactionCategories
    elif request.method == "POST":
        transactionCategory = TransactionCategoryController().create(request.json)
        return transactionCategory

@app.route("/api/transactions/categories/<transactionCategoryId>", methods = ["GET", "PUT", "DELETE"])
def transactionCategory(transactionCategoryId):
    if request.method == "GET":
        transactionCategories = TransactionCategoryController().getById(transactionCategoryId)
        return transactionCategories
    elif request.method == "PUT":
        transactionCategory = TransactionCategoryController().update(transactionCategoryId, request.json)
        return transactionCategory
    elif request.method == "DELETE":
        transactionCategory = TransactionCategoryController().delete(transactionCategoryId)
        return transactionCategory