import pandas as pd
import re

# 读取CSV文件
df = pd.read_csv('C:/Users/Zhang Hengrui/PycharmProjects/pythonProject1/car_data.csv', encoding='GBK', header=0, sep='\t')

# 检查数据结构和缺失值
print(df.info())

# 处理缺失值
data = df.dropna()  # 删除包含缺失值的行
# 或者使用其他方法来处理缺失值，如填充均值、中位数或众数等

# 删除重复数据
data = data.drop_duplicates()

# 修复格式错误
# 根据具体情况，可以使用字符串处理方法来修复格式错误，如去除多余的空格、修复日期格式等

# 保存清洗后的数据到新的CSV文件
data.to_csv('cleaned_file.csv', index=False)

# 对CSV文件中的Price列进行分列，分为最小和最大值

# 提取最小值和最大值
min_values = []
max_values = []

for price in df['Price']:
    match = re.match(r'([\d.]+)-([\d.]+)万', price)
    if match:
        min_value = float(match.group(1))
        max_value = float(match.group(2))
        min_values.append(min_value)
        max_values.append(max_value)

# 创建最小值和最大值列
df['minprice'] = df['Price'].str.split(" ").str[0]
df['maxprice'] = df['Price'].str.split(" ").str[1]

# 将结果存入CSV文件
df.to_csv("C:/Users/Zhang Hengrui/PycharmProjects/pythonProject1/car_data_modified.csv", index=False)

# 打印结果
print(df)
