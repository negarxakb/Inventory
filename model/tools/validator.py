import re
from datetime import datetime, date


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


def date_validator(date_value, message):
    if isinstance(date_value, date):
        return date_value
    else:
        raise ValueError(message)


def date_time_validator(date_time_value, message):
    if isinstance(date_time_value, datetime):
        return date_time_value
    else:
        raise ValueError(message)