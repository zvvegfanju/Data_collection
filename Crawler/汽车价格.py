import requests
import parsel
import csv

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}#进行伪装

base_url = "https://price.pcauto.com.cn/cars/6/2023/"
months = ["1", "2", "3", "4", "5", "6", "7"]

# 以GBK编码方式以写模式打开CSV文件，并创建CSV writer对象
with open('car_data1.csv', 'w', newline='', encoding='GBK') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Month', 'Icon Blue', 'Title', 'Price', 'link'])  # 写入表头行

    for month in months:
        url = base_url + month + "/"
        response = requests.get(url, headers=header)  # 发送HTTP GET请求
        data_html = response.text  # 获取响应的HTML内容
        selector = parsel.Selector(data_html)  # 创建Selector对象
        lis = selector.css('.picList.clearfix li')  # 选择所有的li元素

        for li in lis:
            icon_blue = li.css('.icon-blue::text').get()  # 提取icon_blue数据
            title = li.css('.tit a::text').get()  # 提取title数据
            price = li.css('.price::text').get()  # 提取price数据
            link = li.css('.link::text').get()  # 提取link数据

            writer.writerow([month, icon_blue, title, price, link])  # 写入数据行

print("数据已以GBK编码方式导出到car_data.csv文件中")
