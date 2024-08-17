from controller.exceptions.exception import TransactionNotFoundError
from model.da.da import DataAccess
from model.entity.transaction import Transaction

class TransactionService:

    @staticmethod
    def save(transaction):
        transaction_da = DataAccess(Transaction)
        transaction_da.save(transaction)
        return transaction



    @staticmethod
    def edit(transaction):
        transaction_da = DataAccess(Transaction)
        if transaction_da.find_by_id(transaction.id):
            transaction_da.edit(transaction)
            return transaction
        else:
            raise TransactionNotFoundError

    @staticmethod
    def remove(id):
        transaction_da = DataAccess(Transaction)
        if transaction_da.find_by_id(id):
            return transaction_da.remove(id)
        else:
            raise TransactionNotFoundError

    @staticmethod
    def date_range(start_date, end_date):
        transaction_da = DataAccess(Transaction)
        return transaction_da.find_by_date_range(start_date, end_date)

    @staticmethod
    def find_by_id(id):
        transaction_da = DataAccess(Transaction)
        return transaction_da.find_by_id(id)



    @staticmethod
    def type(transaction):
        transaction_da = DataAccess(Transaction)
        transaction_da.save(transaction)
        return transaction

    @staticmethod
    def find_all():
        Transaction_da = DataAccess(Transaction)
        return Transaction_da.find_all()












