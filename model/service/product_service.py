from controller.exceptions.exception import ProductNotFoundError
from model.da.da import DataAccess
from model.entity.product import Product

class ProductService:
    @staticmethod
    def save(product):
        product_da = DataAccess(Product)
        product_da.save(product)
        return product


    @staticmethod
    def edit(product):
        product_da = DataAccess(Product)
        product_da.edit(product)
        return product

    @staticmethod
    def remove(id):
        product_da = DataAccess(Product)
        if  product_da.find_by_id(id):
            return product_da.remove(id)
        else:
            raise ProductNotFoundError

    @staticmethod
    def find_by_id(id):
        product_da = DataAccess(Product)
        return product_da.find_by_id(id)

    @staticmethod
    def find_by_name(name):
        product_da = DataAccess(Product)
        return product_da.find_by(name)

    @staticmethod
    def find_by_brand(brand):
        product_da = DataAccess(Product)
        return product_da.find_by(brand)

    @staticmethod
    def find_by_category(category):
        product_da = DataAccess(Product)
        return product_da.find_by(category)





