import csv

data = {
    'symbolSize': 100,
    'data': [
        {"name": "临汾", "value": 17.6},
        {"name": "太原", "value": 13.4},
        {"name": "深圳", "value": 12.0},
        {"name": "中山", "value": 11.9},
        {"name": "西安", "value": 9.4},
        {"name": "深圳", "value": 8.5},
        {"name": "汕头", "value": 7.9},
        {"name": "上海", "value": 5.8},
    ]
}

filename = 'map_1_data.csv'

with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'value'])
    writer.writeheader()
    writer.writerows(data['data'])

print('Data saved successfully to', filename)
