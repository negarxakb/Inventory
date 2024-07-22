from datetime import datetime

from controller.transaction_controller import TransactionController

year = 2022
month = 11
day = 11
d = datetime.now()
TransactionController.save("OUT", 3, f"{d}")
