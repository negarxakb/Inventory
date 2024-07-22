from model.entity.product import Product
from model.service.product_service import ProductService
from model.tools.decorators import exception_handling
from model.tools.logger import Loggerfr

class ProductController:

    @classmethod
    @exception_handling
    def save(cls, name,brand,price,description):
        product = Product(name,brand,price,description)
        ProductService.save(product)
        return True, product

    @classmethod
    @exception_handling
    def edit(cls, id,name,brand,price,description):
        product = Product(id,name,brand,price,description)
        ProductService.edit(product)
        return True, product

    @classmethod
    @exception_handling
    def remove(cls, id):
        product = ProductService.remove(id)
        Logger.info(f"Product Removed- {product}")
        return True, product

    @classmethod
    @exception_handling
    def find_all(cls, ):
        product_list = ProductService.find_all()
        Logger.info(f"Product Find  BY  Id({id})")
        return True, product_list

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        product = ProductService.find_by_id(id)
        Logger.info(f"Product Find  BY  Id({id})")
        return True, product


    @classmethod
    @exception_handling
    def find_by_name(cls, name):
        product_list = ProductService.find_by_name(name)
        Logger.info(f"Product Find  BY  Name({name})")
        return True, product_list



    @classmethod
    @exception_handling
    def find_by_brand(cls, brand):
        product_list = ProductService.find_by_brand(brand)
        Logger.info(f"Product Find  BY  Brand({brand})")
        return True, product_list







