from controller.exceptions.exception import StoreNotFoundError
from model.da.da import DataAccess
from model.entity.store import Store


class StoreService:

    @staticmethod
    def save(store):
        store_da = DataAccess(Store)
        store_da.save(store)
        return store


    @staticmethod
    def edit(store):
        store_da = DataAccess(Store)
        if store_da.find_by_id(store.id):
            store_da.edit(store)
            return store
        else:
            raise StoreNotFoundError

    @staticmethod
    def remove(id):
        store_da = DataAccess(Store)
        if store_da.find_by_id(id):
            return store_da.remove(id)
        else:
            raise StoreNotFoundError

    @staticmethod
    def find_by_id(id):
        store_da = DataAccess(Store)
        return store_da.find_by_id(id)


    @staticmethod
    def find_by_product(product):
        store_da = DataAccess(Store)
        return store_da.find_by(product)

    @staticmethod
    def find_by_category(cateory):
        store_da = DataAccess(Store)
        return store_da.find_by(cateory)

    @staticmethod
    def find_all():
        Store_da = DataAccess(Store)
        return Store_da.find_all()












