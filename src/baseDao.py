from bson.objectid import ObjectId
from src.lib.MongoDb import MongoDb

class BaseDao:

    def __init__(self, collection):
        self.db = MongoDb.mongo[collection];
    
    def insert_one(self, data):
        return self.db.insert_one(data);

    def find_one(self, query):

        if(query and query["_id"]):
            query["_id"] = ObjectId(query["_id"]);

        return self.db.find_one(query);

    def insert_many(self, data):
        return self.db.insert_many(data);

    def count(self, query = None):

        if query is None:
            query = {}

        return self.db.count_documents(query);

    def find(self, query = None, sort = "updatedAt", order = -1, skip = 0, limit = 10):

        if query is None:
            query = {}
        
        return list(self.db.find(query, {'password': 0}).sort(sort, order).skip(skip).limit(limit));
    
    def delete(self, _id):
        return self.db.delete_one({ "_id": ObjectId(_id) })
