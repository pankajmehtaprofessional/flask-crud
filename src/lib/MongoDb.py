from pymongo import MongoClient
import os

class MongoDb:

    mongo = "";
    
    def __init__(self):
        self.database = os.getenv("MONGO_DB")

    @staticmethod
    def connect():
        try:
            client = MongoClient(os.getenv("MONGO_URI"))

            print("Mongo Connection Successfull ...")

            MongoDb.mongo = client[os.getenv("MONGO_DB")];

            return MongoDb.mongo
        except:
            # handle the error
            print("Mongo connection error")
            raise
        else:
            # no error
            print("Mongo Connection Successfull ...")
        finally:
            # regardless of the result of the try- and except blocks
            print("Mongo connection executed!")

    def get_conn(self):
        return MongoDb.mongo;