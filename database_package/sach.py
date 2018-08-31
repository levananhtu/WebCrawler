from database_package import database_accessor
from mysql import connector


class Sach:
    def __init__(self):
        # self.database_accessor = database_accessor.DatabaseAccessor.get_database_accessor()
        self.database_accessor = connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="yii",
            buffered=True
        )

    def insert(self, sach):
        sql_query = """
                        INSERT INTO `sach`( `tenSach`, `giaGoc`, `soLuong`, 
                                            `soTrang`, `lanTaiBan`, `kichThuoc`, 
                                            `trongLuong`, `ngayPhatHanh`, `nhaPhatHanhID`, 
                                            `nhaXuatBanID`,`tacGiaID`,`danhMucID`,
                                            `anh`, `mieuTa`) 
                        VALUES (%s,%s,%s,
                                %s,%s,%s,
                                %s,%s,%s,
                                %s,%s,%s,
                                %s,%s) 
                        
                    """
        value = (sach.get('tenSach'), sach.get('giaGoc'), '100',
                 sach.get('soTrang'), '2', sach.get('kichThuoc'),
                 sach.get('trongLuong'), sach.get('ngayPhatHanh'), sach.get('nhaPhatHanhID'),
                 sach.get('nhaXuatBanID'), sach.get('tacGiaID'), sach.get('danhMucID'),
                 sach.get('anh'), sach.get('mieuTa'))

        cursor = self.database_accessor.cursor()
        cursor.execute(sql_query, value)
        self.database_accessor.commit()

        # ngayBatDauGiamGia`,`ngayKetThucGiamGia`,`giamGia`,
        # % s, % s, % s,
        # sach['ngayBatDauGiamGia'], sach['ngayKetThucGiamGia'], sach['giamGia'],


if __name__ == '__main__':
    sach = Sach()
    sach_data = dict(tenSach='7 deathly sins', giaGoc=None, soLuong='700',
                     soTrang='70', lanTaiBan='7', kichThuoc='70x70',
                     trongLuong='700', ngayPhatHanh='2017-07-07', nhaPhatHanhID='7',
                     nhaXuatBanID='7', tacGiaID='7', danhMucID='7',
                     anh='777', mieuTa='7777')
    sach.insert(sach_data)
