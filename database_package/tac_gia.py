from database_package import database_accessor
from mysql import connector


class TacGia:
    def __init__(self):
        # self.database_accessor = database_accessor.DatabaseAccessor.get_database_accessor()
        self.database_accessor = connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="yii",
            buffered=True
        )

    def insert(self, tac_gia):
        sql_query = """
                        INSERT INTO `tac_gia`( `tenTacGia`) 
                        VALUES (%s) 
                    """
        value = (tac_gia.get('tenTacGia'),)

        self.database_accessor.cursor().execute(sql_query, value)
        self.database_accessor.commit()

    def get_id(self, tac_gia):
        sql_query = """ SELECT `tacGiaID` 
                        FROM tac_gia
                        WHERE tac_gia.tenTacGia = %s"""
        value = (tac_gia,)
        # self.database_accessor.cursor().execute(sql_query, value)
        # self.database_accessor.commit()
        # result = self.database_accessor.cursor().fetchone()

        cursor = self.database_accessor.cursor()
        cursor.execute(sql_query, value)
        result = cursor.fetchone()

        if result is None:
            return None
        return result[0]


if __name__ == '__main__':
    tg = TacGia()
    print(tg.insert(dict(tenTacGia='Cáo')))
    print(tg.get_id('Cáo'))
