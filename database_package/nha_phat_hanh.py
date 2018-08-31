from database_package import database_accessor
from mysql import connector


class NhaPhatHanh:
    def __init__(self):
        # self.database_accessor = database_accessor.DatabaseAccessor.get_database_accessor()
        self.database_accessor = connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="yii",
            buffered=True
        )

    def insert(self, nha_phat_hanh):
        sql_query = """
                        INSERT INTO `nha_phat_hanh`( `tenNhaPhatHanh`) 
                        VALUES (%s) 
                    """
        value = (nha_phat_hanh.get('tenNhaPhatHanh'),)
        self.database_accessor.cursor().execute(sql_query, value)
        self.database_accessor.commit()

    def get_id(self, ten_nha_phat_hanh):
        sql_query = """ SELECT `nhaPhatHanhID` 
                        FROM nha_phat_hanh
                        WHERE nha_phat_hanh.tenNhaPhatHanh = %s"""
        value = (ten_nha_phat_hanh,)
        cursor = self.database_accessor.cursor()
        cursor.execute(sql_query, value)
        result = cursor.fetchone()

        if result is None:
            return None
        return result[0]


if __name__ == '__main__':
    nph = NhaPhatHanh()
    print(nph.insert(dict(tenNhaPhatHanh='asdfsf')))
    print(nph.get_id('asdfsf'))
