from Loader import Loader
from services.api import db

class TransactionLoader(Loader):
    
    def load(self, transaction):
        db.session.add(transaction)
        db.session.commit()
        self.log("Loaded")