# from datetime import datetime
#
# from controller.transaction_controller import TransactionController
#
# year = 2022
# month = 11
# day = 11
# d = datetime.now()
# TransactionController.save("OUT", 3, f"{d}")
from datetime import datetime

from sqlalchemy import create_engine, and_, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, database_exists
from model.entity.base import Base
from model.entity.transaction import Transaction

connection_string = "mysql+pymysql://root:root123@localhost:3306/mft"
if not database_exists(connection_string):
    create_database(connection_string)

engine = create_engine(connection_string)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

transaction =Transaction("income",3,datetime.now())
session.add(transaction)
session.commit()