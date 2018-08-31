from database_package import database_accessor
from mysql import connector


class DanhMuc:
    def __init__(self):
        # self.database_accessor = database_accessor.DatabaseAccessor.get_database_accessor()
        self.database_accessor = connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="yii",
            buffered=True
        )

    def insert(self, danh_muc):
        sql_query = """
                        INSERT INTO `danh_muc`( `tenDanhMuc`, `danhMucChaID`) 
                        VALUES (%s,%s) 
                    """
        value = (danh_muc.get('tenDanhMuc'), danh_muc.get('danhMucChaID'))

        self.database_accessor.cursor().execute(sql_query, value)
        self.database_accessor.commit()

    def get_id(self, ten_danh_muc):
        sql_query = """ SELECT `danhMucID` 
                        FROM danh_muc
                        WHERE danh_muc.tenDanhMuc = %s"""
        value = (ten_danh_muc,)

        cursor = self.database_accessor.cursor()
        cursor.execute(sql_query, value)
        result = cursor.fetchone()

        if result is None:
            return None
        return result[0]

    def is_exist(self, ten_danh_muc, danh_muc_cha_id):
        sql_query = """ SELECT `danhMucID`
                        FROM danh_muc
                        WHERE danh_muc.tenDanhMuc = %s AND danh_muc.danhMucChaID = %s"""
        value = (ten_danh_muc, danh_muc_cha_id)

        cursor = self.database_accessor.cursor()
        cursor.execute(sql_query, value)
        result = cursor.fetchone()

        if result is None:
            return None
        return result[0]


if __name__ == '__main__':
    dm = DanhMuc()
    print(dm.is_exist('asdfsf', 315))
