# from database_package import database_accessor
from mysql import connector


class NhaXuatBan:
    def __init__(self):
        connector.connect()
        self.database_accessor = connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="yii",
            buffered=True
        )

    def insert(self, nha_xuat_ban):
        sql_query = """
                        INSERT INTO `nha_xuat_ban`( `tenNhaXuatBan`) 
                        VALUES (%s) 
                    """
        value = (nha_xuat_ban.get('tenNhaXuatBan'),)

        self.database_accessor.cursor().execute(sql_query, value)
        self.database_accessor.commit()

    def get_id(self, ten_nha_xuat_ban):
        sql_query = """ SELECT * 
                        FROM `nha_xuat_ban`
                        WHERE tenNhaXuatBan = %s"""
        value = (ten_nha_xuat_ban,)
        cursor = self.database_accessor.cursor()
        cursor.execute(sql_query, value)
        result = cursor.fetchone()

        if result is None:
            return None
        return result[0]


if __name__ == '__main__':
    nxb = NhaXuatBan()
    print(nxb.get_id('asdfsf'))
