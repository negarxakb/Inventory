
class ProductNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Product Not Found !!!")


class StoreNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Store Not Found !!!")


class TransactionNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Transaction Not Found !!!")


class PersonNotFoundError(Exception):
    def __init__(self, *args):
        super().__init__("Person Not Found !!!")


