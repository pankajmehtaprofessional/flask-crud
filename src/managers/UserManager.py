from src import BaseDao

class UserManager(BaseDao):

    def __init__(self):
        BaseDao.__init__(self, "users")

    def details(self, query=None):

        if query is None:
            query = {}

        return self.find(query)
