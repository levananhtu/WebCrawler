from database_package import danh_muc
from database_package import sach
from database_package import nha_xuat_ban
from database_package import tac_gia
from database_package import nha_phat_hanh


class TableFactory:
    def __init__(self):
        pass

    def get_table(self, table):
        if str(table) == 'sach':
            return sach.Sach()
        if str(table) == 'nha_phat_hanh':
            return nha_phat_hanh.NhaPhatHanh()
        if str(table) == 'danh_muc':
            return danh_muc.DanhMuc()
        if str(table) == 'tac_gia':
            return tac_gia.TacGia()
        if str(table) == 'nha_xuat_ban':
            return nha_xuat_ban.NhaXuatBan()

        return None


if __name__ == '__main__':
    print(type(TableFactory().get_table('sach')))
    print(type(TableFactory().get_table('nha_phat_hanh')))
    print(type(TableFactory().get_table('danh_muc')))
    print(type(TableFactory().get_table('tac_gia')))
    print(type(TableFactory().get_table('nha_xuat_ban')))
    print(type(TableFactory().get_table('adsf')))
