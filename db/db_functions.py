from db.db import *


# return all available book types from DB
def get_book_types_list():
    bookTypesRecords = BookTypes.query.with_entities(BookTypes.type).all()
    bookTypes = []
    for bookType in bookTypesRecords:
        bookTypes.append(bookType.type)
    return bookTypes


# return all book types and its charges per day from DB
def get_book_types_and_charges():
    bookTypesRecords = BookTypes.query.all()
    bookTypes = {}
    for bookType in bookTypesRecords:
        bookTypes[bookType.type] = bookType.charge
    return bookTypes
