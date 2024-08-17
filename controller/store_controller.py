from controller import *

class StoreController:
    @classmethod
    @exception_handling
    def save(cls, product,inventory,product_id):
        store = Store(product,inventory,product_id)
        StoreService.save(store)
        return True, StoreService.save(store)

    @classmethod
    @exception_handling
    def edit(cls, product):
        store = Store(id,product)
        StoreService.edit(store)
        return True, store

    @classmethod
    @exception_handling
    def remove(cls, id):
        store = StoreService.remove(id)
        Logger.info(f"Store Removed- {store}")
        return True, store

    @classmethod
    @exception_handling
    def find_all(cls):
        # store_list = StoreService.find_all()
         #Logger.info(f"Store Find  BY  Id({id})")
        return True, StoreService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        store = StoreService.find_by_id(id)
        Logger.info(f"Store Find BY Id({id})")
        return True, store


    @classmethod
    @exception_handling
    def find_by_category(cls, category):
        store_list = StoreService.find_by_category(category)
        Logger.info(f"Store Find  BY  Category({category})")
        return True, store_list






