import requests
import parsel
import csv

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}#����αװ

base_url = "https://price.pcauto.com.cn/cars/6/2023/"
months = ["1", "2", "3", "4", "5", "6", "7"]

# ��GBK���뷽ʽ��дģʽ��CSV�ļ���������CSV writer����
with open('car_data1.csv', 'w', newline='', encoding='GBK') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Month', 'Icon Blue', 'Title', 'Price', 'link'])  # д���ͷ��

    for month in months:
        url = base_url + month + "/"
        response = requests.get(url, headers=header)  # ����HTTP GET����
        data_html = response.text  # ��ȡ��Ӧ��HTML����
        selector = parsel.Selector(data_html)  # ����Selector����
        lis = selector.css('.picList.clearfix li')  # ѡ�����е�liԪ��

        for li in lis:
            icon_blue = li.css('.icon-blue::text').get()  # ��ȡicon_blue����
            title = li.css('.tit a::text').get()  # ��ȡtitle����
            price = li.css('.price::text').get()  # ��ȡprice����
            link = li.css('.link::text').get()  # ��ȡlink����

            writer.writerow([month, icon_blue, title, price, link])  # д��������

print("��������GBK���뷽ʽ������car_data.csv�ļ���")
