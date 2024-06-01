from src.lib.MongoDb import MongoDb as MONGODB
from src.routes.user_routes import user_bp

class Bootstrap:

    """ Static Method """
    @staticmethod
    def init(app):

        # ------------------------------------------
        # SETUP MONGO DB
        # ------------------------------------------
        MONGODB.connect();

        # ------------------------------------------
        # SETUP ROUTE
        # ------------------------------------------
        Bootstrap.init_route(app);

    """ Static Method """
    @staticmethod
    def init_route(app):
        app.register_blueprint(user_bp, url_prefix = "/user")
