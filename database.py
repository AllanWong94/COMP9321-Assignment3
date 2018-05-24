from pymongo import MongoClient
import re


# accept the collection name and a list of data as input parameters
def db_save(collection, data):
    db = db_connect()
    posts = db[collection]
    insert_result = posts.insert_many(data)
    inserted_ids = insert_result.inserted_ids
    if len(data) != len(inserted_ids):
        return 1    # error
    return 0        # no error


# return a list of query result
def db_query(collection, query_info):
    db = db_connect()
    # query_info = db_query_parser(query_info)
    posts = db[collection]
    result_list = posts.find(query_info)
    result_list = list(result_list)

    return result_list


def db_get(collection):
    db = db_connect()
    posts = db[collection]
    result_list = posts.find()
    result_list = list(result_list)
    return result_list


def db_delete(collection, query_info):
    pass


def db_update(collection, query_info):
    pass


def db_connect():
    client = MongoClient()
    db = client.COMP9321
    return db


def db_check(collection):
    print("Checking database status...")
    db = db_connect()
    posts = db[collection]
    print(posts.count())
    r = posts.find({"Rank": "20"})
    for i in r:
        print(i)

# TODO finish the db_query_parser
# format of input query:
# x == a "||" | "&&" y != b
# query must be in string format
# def db_query_parser(query):
#     query = re.sub(r" *(\|\||\&\&|==|!=) *", r" \1 ", query)
#     para_list = query.split(" ")
#     op_list = ["==", "!=", "||", "&&"]
#     stack = []
#     # TODO no error detection on query string.
#     token = para_list.pop(0)
#     while para_list:
#         para = []
#         while token not in op_list:
#             para.append(token)
#         para_str = " ".join
#
#     token = para_list.pop(0)
#     while para_list:
#         if token in op_list:
#             try:
#                 ident = stack.pop()
#             except IndexError:
#                 print("Error query string: empty identifier in operation: ", a)
#             para = []
#             token = para_list.pop(0)
#             while token not in op_list:
#                 para.append(token)
#             para_str = " ".join(para)
#             stack.append([ident, token, para_str])
#         else:
#             ident = stack.pop()
#             ident += a
#             stack.append(ident)
#
#     return query

