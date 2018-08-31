from bs4 import BeautifulSoup
from urllib import request
import mysql.connector
import vietnamese as vn
from database_package import database
import datetime
import traceback

"""
Hàm crawl4() chịu trách nhiệm về từng category
"""


def crawl4():
    url_list = ['http://nobita.vn/danh-muc/1/sach-kinh-te.html',
                'http://nobita.vn/danh-muc/2/van-hoc-nuoc-ngoai.html',
                'http://nobita.vn/danh-muc/3/van-hoc-trong-nuoc.html',
                'http://nobita.vn/danh-muc/4/sach-ki-nang-song.html',
                'http://nobita.vn/danh-muc/5/sach-tuoi-teen.html',
                'http://nobita.vn/danh-muc/6/hoc-ngoai-ngu.html',
                'http://nobita.vn/danh-muc/7/sach-thieu-nhi.html',
                'http://nobita.vn/danh-muc/8/thuong-thuc-doi-song.html',
                'http://nobita.vn/danh-muc/9/sach-chuyen-nganh.html']
    db = database.Database()

    for url in url_list:
        crawl3(url, db)
        print("\n")


"""
Hàm crawl3() chịu trách nhiệm mở từng trang to
"""


def crawl3(url, db):
    respond = request.urlopen(url=url)
    while True:
        try:
            url = crawl2(respond, db)
            respond = request.urlopen(url=url)
        except:
            break


"""
Hàm crawl2() chịu trách nhiệm giải cấu trúc trang to
"""


def crawl2(respond, db):
    soup = BeautifulSoup(respond, 'html.parser')
    body = soup.body
    next_page = body.find('ul', class_='pagenav').find('li', class_='next')
    product_contener_list = body.find_all('div', class_='product_contener')

    for product_contener in product_contener_list:
        crawl1(product_contener.div, db)

    return "http://nobita.vn" + next_page.a.get('href')


"""
Hàm crawl1() lấy dữ liệu của từng quyển sách
"""


def crawl1(product, db):
    try:
        image_tag = product.find('div', class_='image').a
        link = vn.convert(image_tag.get('href'))
        image = image_tag.img.get('src')
        book_name = product.find('div', class_='productname').a.get('title')
        try:
            authors = product.find('div', class_='fields').span.a.text
        except AttributeError:
            authors = None
        price = product.find('span', class_='rootprice')
        if price is None:
            price = product.find('div', class_='prices').text
        else:
            price = price.text

        respond = request.urlopen(url="http://nobita.vn" + link)
        soup = BeautifulSoup(respond, 'html.parser')

        description_list = soup.find('div', id="module_ProductDetail").find('div', class_='intro').find_all('p')
        description = ""
        for paragraph in description_list:
            description = description + "\n" + paragraph.text

        details = dict()
        rows = soup.find('table', class_='fields').find_all('tr')
        for row in rows:
            details[vn.convert(row.find('td', class_='title').text.replace(" ", "")).strip()] = row.find('td',
                                                                                                         class_='values').text.strip()

        details['anh'] = 'http://nobita.vn' + image
        details['tensach'] = book_name
        details['tacgia'] = authors
        details['gia'] = price[:-1].strip().replace(".", "")
        details['mieuta'] = description.strip()
        details['Muccha'] = soup.find('div', class_='pathway').ul.find_all('li')[1].a.text

        try:
            d = datetime.datetime.strptime(details.get('Ngayphathanh'), '%d/%m/%Y')
            details['Ngayphathanh'] = datetime.date.strftime(d, "%Y-%m-%d")
        except TypeError:
            details['Ngayphathanh'] = None
        # print(details)
        # print("\n\n")
        db.insert_database(details)

    except:
        traceback.print_exc()
        print(link)


# print(description + "\n")
# print("\n")
# for data1, data2 in details:
#    print(data1 + ": " + data2 + "\n")
# print(image + "\n")
# print(book_name + "\n")
# print(authors + "\n")
# print(price + "\n")


if __name__ == '__main__':
    crawl4()

"""respond = request.urlopen(url="http://nobita.vn/2631/quang-cao-sang-tao.html")
soup = BeautifulSoup(respond, 'html.parser')
rows = soup.find('table', class_='fields').find_all('tr')
for row in rows:
    print(vn.convert((row.find('td', class_='title').text).replace(" ", "")))
    print(row.find('td', class_='values').text)
    print('\n')"""
