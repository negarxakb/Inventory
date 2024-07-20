from model.entity.transaction import Transaction
from model.service.transaction_service import  TransactionService
from model.tools.decorators import exception_handling
from model.tools.logger import Logger


class TransactionController:
    @classmethod
    @exception_handling
    def save(cls,product_id,type,count,date_time):
        transaction = Transaction(product_id,type,count,date_time)
        TransactionService.save(transaction)
        return True, transaction

    @classmethod
    @exception_handling
    def edit(cls,id,product_id,type,count,date_time):
        transaction = Transaction(id,product_id,type,count,date_time)
        TransactionService.edit(transaction)
        return True, transaction


    @classmethod
    @exception_handling
    def remove(cls,id,product_id,type,count,date_time):
        transaction = Transaction(id,product_id,type,count,date_time)
        TransactionService.remove(transaction)
        return True, transaction


    @classmethod
    @exception_handling
    def find_all(cls,):
        transaction_list = TransactionService.find_all()
        Logger.info(f"Transaction Find  BY  Id({id})")
        return True,transaction_list


    @classmethod
    @exception_handling
    def find_by_id(cls,id):
        transaction = TransactionService.find_by_id(id)
        Logger.info(f"Transaction Find  BY  Id({id})")
        return True,transaction


    @classmethod
    @exception_handling
    def find_by_product_id(cls,product_id):
        transaction=TransactionService.find_by_product_id(product_id)
        Logger.info(f"Transaction Find  BY  Product({product_id})")
        return True,transaction


    @classmethod
    @exception_handling
    def find_by_count(cls,count):
        transaction = TransactionService.find_by_count(count)
        Logger.info(f"Transaction Find  BY  Count({count})")
        return True,transaction

















