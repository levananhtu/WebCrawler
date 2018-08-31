from mysql import connector


class DatabaseAccessor:
    __instance = None

    @staticmethod
    def get_database_accessor():
        """ Static access method. """
        if DatabaseAccessor.__instance is None:
            DatabaseAccessor()
        return DatabaseAccessor.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if DatabaseAccessor.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self.__instance = connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="yii4"
            )

