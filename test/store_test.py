from controller.store_controller import StoreController
from model.entity import Product

product = Product("name","brand",1000, "description")

print(StoreController.save(product, 1))





