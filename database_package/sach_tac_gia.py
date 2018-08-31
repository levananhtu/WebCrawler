from database_package import database_accessor
from mysql import connector


class SachTacGia:
    def __init__(self):
        # self.database_accessor = database_accessor.DatabaseAccessor.get_database_accessor()
        self.database_accessor = connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="yii",
            buffered=True
        )

    def insert(self, sach_tac_gia):
        sql_query = """
                        INSERT INTO `sach_tac_gia`( `tacGiaID`, `sachID`) 
                        VALUES (%s,%s) 
                    """
        value = (sach_tac_gia.get('tacGiaID'), sach_tac_gia.get('sachID'))

        self.database_accessor.cursor().execute(sql_query, value)
        self.database_accessor.commit()

        pass
