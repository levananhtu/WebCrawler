from database_package import table_factory
import re


class Database:
    def __init__(self):
        self.table_danh_muc = table_factory.TableFactory().get_table(table='danh_muc')
        self.table_nha_phat_hanh = table_factory.TableFactory().get_table(table='nha_phat_hanh')
        self.table_nha_xuat_ban = table_factory.TableFactory().get_table(table='nha_xuat_ban')
        self.table_sach = table_factory.TableFactory().get_table(table='sach')
        self.table_tac_gia = table_factory.TableFactory().get_table(table='tac_gia')
        print(type(self.table_sach))
        print(type(self.table_danh_muc))
        print(type(self.table_nha_phat_hanh))
        print(type(self.table_nha_xuat_ban))
        print(type(self.table_tac_gia))

    def insert_database(self, data):
        tac_gia_id = self.table_tac_gia.get_id(data.get('tacgia'))
        # print('done1')

        nha_xuat_ban_id = self.table_nha_xuat_ban.get_id(data.get('NXB'))
        # print('done2')

        nha_phat_hanh_id = self.table_nha_phat_hanh.get_id(data.get('Phathanh'))
        # print('done3')

        danh_muc_cha_id = self.table_danh_muc.get_id(data.get('Muccha'))
        # print('done4')

        danh_muc_id = self.table_danh_muc.is_exist(data.get('Danhmuc'), danh_muc_cha_id)
        # print('done5')

        sach_data = dict()

        if (tac_gia_id is None) and (data.get('tacgia') is not None):
            self.table_tac_gia.insert(dict(tenTacGia=data.get('tacgia')))
            tac_gia_id = self.table_tac_gia.get_id(data.get('tacgia'))
        # print('done6')

        if (nha_xuat_ban_id is None) and (data.get('NXB') is not None):
            self.table_nha_xuat_ban.insert(dict(tenNhaXuatBan=data.get('NXB')))
            nha_xuat_ban_id = self.table_nha_xuat_ban.get_id(data.get('NXB'))
        # print('done7')

        if (nha_phat_hanh_id is None) and (data.get('Phathanh') is not None):
            self.table_nha_phat_hanh.insert(dict(tenNhaPhatHanh=data.get('Phathanh')))
            nha_phat_hanh_id = self.table_nha_phat_hanh.get_id(data.get('Phathanh'))
        # print('done8')
        # print(danh_muc_cha_id)

        if danh_muc_cha_id is None:
            self.table_danh_muc.insert(dict(tenDanhMuc=data.get('Muccha'), danhMucChaID=0))
            danh_muc_cha_id = self.table_danh_muc.get_id(data.get('Muccha'))
        # print('done9')

        # print('done9.1')
        if danh_muc_id is None:
            self.table_danh_muc.insert(dict(tenDanhMuc=data.get('Danhmuc'), danhMucChaID=danh_muc_cha_id))
            danh_muc_id = self.table_danh_muc.is_exist(data.get('Danhmuc'), danh_muc_cha_id)
        # print('done10')

        sach_data['tenSach'] = data.get('tensach')
        sach_data['giaGoc'] = data.get('gia')
        sach_data['soTrang'] = data.get('Sotrang')
        sach_data['kichThuoc'] = data.get('Kichthuoc')
        sach_data['trongLuong'] = data.get('Trongluong')
        sach_data['ngayPhatHanh'] = data.get('Ngayphathanh')
        sach_data['nhaPhatHanhID'] = nha_phat_hanh_id
        sach_data['nhaXuatBanID'] = nha_xuat_ban_id
        sach_data['tacGiaID'] = tac_gia_id
        sach_data['danhMucID'] = danh_muc_id
        sach_data['anh'] = data.get('anh')
        sach_data['mieuTa'] = data.get('mieuta')
        # print('done11')

        self.table_sach.insert(sach=sach_data)
        # print('done12')
