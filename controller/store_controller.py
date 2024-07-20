from model.entity.store import Store
from model.service.store_service import StoreService
from model.tools.decorators import exception_handling
from model.tools.logger import Logger


class StoreController:
    @classmethod
    @exception_handling
    def save(cls, product,inventory,category):
        store = Store(product,inventory,category)
        StoreService.save(store)
        return True, store

    @classmethod
    @exception_handling
    def edit(cls, product,inventory,category):
        store = Store(id,product,inventory,category)
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
    def find_all(cls, ):
        store_list = StoreService.find_all()
        Logger.info(f"Store Find  BY  Id({id})")
        return True, store_list

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        store = StoreService.find_by_id(id)
        Logger.info(f"Store Find  BY  Id({id})")
        return True, store


    @classmethod
    @exception_handling
    def find_by_category(cls, category):
        store_list = StoreService.find_by_category(category)
        Logger.info(f"Store Find  BY  Category({category})")
        return True, store_list






