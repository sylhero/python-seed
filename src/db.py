from gino import Gino


class DBInstance():
    __instance = None

    @staticmethod
    def get_db_instance():
        if DBInstance.__instance is None:
            DBInstance.__instance = Gino()
        return DBInstance.__instance