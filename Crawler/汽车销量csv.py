import requests
import parsel
import csv

#伪装
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67"
}

base_url = "https://xl.16888.com/brand-0-202301-202305-{}.html"
pages = [1, 2, 3]  # Update this list with the actual page numbers

# Open the CSV file in write mode with GBK encoding and create a CSV writer object
with open('car_sales1.csv', 'w', newline='', encoding='GBK') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['brand_rank','brand_name', 'country', 'sales'])  # Write header row

    for page in pages:
        url = base_url.format(page)
        response = requests.get(url, headers=header)
        data_html = response.text
        selector = parsel.Selector(data_html)
        rows = selector.css('.xl-table-def tr')

        for row in rows[1:]:  # Exclude the header row
            brand_rank = row.css('.xl-td-t1::text').get()
            brand_name = row.css('.xl-td-t2 a::text').get()
            country = row.css('.xl-td-t3:nth-child(4)::text').get()
            sales = row.css('.xl-td-t3:nth-child(5)::text').get()

            writer.writerow([brand_rank, brand_name, country, sales])  # Write data row

print("Data exported to car_sales.csv with GBK encoding")
