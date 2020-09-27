from pymongo import MongoClient
from decouple import config


def mongo_con(poolsize=1000):
    mongodb = MongoClient(config('MONGO_URI')).get_database(config('MONGO_DATABASE'))
    return mongodb
