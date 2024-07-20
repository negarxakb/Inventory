import re
import datetime


def product_validator(product, message):
    if isinstance(product, str) and re.match(r"^[a-zA-Z\s]{2,30}$", product):
        return product
    else:
        raise ValueError(message)


def category_validator(category, message):
    if isinstance(category, str) and re.match(r"^[a-zA-Z\s]{2,30}$", category):
        return category
    else:
        raise ValueError(message)


def inventory_validator(intventory, message):
    if isinstance(intventory, int) and intventory >= 0:
        return intventory
    else:
        raise ValueError(message)



def boolean_validator(bool_value, message):
    if isinstance(bool_value, bool):
        return bool_value
    else:
        raise ValueError(message)




def date_time_validator(date_time_value, message):
    d = date_time_value.split("/")
    year = int(d[0])
    month = int(d[1])
    day = int(d[2])
    dd = datetime.datetime(year, month, day)
    if isinstance(dd, datetime.date):
        return dd
    else:
        raise ValueError(message)
