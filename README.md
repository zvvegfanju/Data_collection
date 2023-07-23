# Data_collection
数据采集可视化大屏
#我的题目是近期上市新车数据采集、分析及可视化，我将会进行数据采集和预处理，进行统计和分析，然后进行可视化。最后要达到的指标是应该爬取几个关于汽车的网站，进行处理后做出来它的可视化图表。
    涉及的内容与原理，主要是爬虫与echart的应用。确定合适的数据来源，选择一个或多个国内外大型汽车评论网站作为数据采集的来源，以确保数据的广泛性和可靠性。这些网站应该涵盖各种汽车品牌、车型和地区的信息。明确定义需要采集的数据字段，以满足后续的统计分析和可视化展示需求。本人爬取了车型、品牌、上市日期、销量、评价等信息。并且将爬取到的csv文件进行处理，产生出几个具有确定目标与含义的csv文件，然后存储在数据库中。
通过爬取到的数据，我进行了可视化处理，先对好几个csv文件读取然后制作出图表，最后集合在一个大的可视化大屏当中。

#对于上市新车的数据，我上网找到几个网站进行了爬取，分别为https://price.pcauto.com.cn/cars/6/2023/，爬取了六个月上市新车的品牌，价格，车型。https://xl.16888.com/brand-0-202301-202305-{}.html，爬取了今年我国新车对各国的销量等。爬取后进行数据清洗，检查数据结构和缺失值，处理缺失值，删除重复数据。并且由于爬取到的价格为最低到最高价格，所以对两种价格进行分离。