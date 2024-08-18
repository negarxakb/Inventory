from controller import *



class TransactionController:
    @classmethod
    @exception_handling
    def save(cls,transaction_type,count,transaction_date_time):
        transaction = Transaction(transaction_type,count,transaction_date_time)
        TransactionService.save(transaction)
        return True, transaction

    @classmethod
    @exception_handling
    def edit(cls,id,product_id,transaction_type,count):
        transaction = Transaction(id,product_id,transaction_type,count)
        TransactionService.edit(transaction)
        return True, transaction


    @classmethod
    @exception_handling
    def remove(cls,id):
        transaction = TransactionService.remove(id)
        Logger.info(f"Transaction Removed- {transaction}")
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
























