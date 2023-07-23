#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 14:48
# @Author : way
# @Site : 
# @Describe:

import json
import csv

class SourceDataDemo:

    def __init__(self):
        self.title = '大数据可视化展板通用模板'
        self.counter = {'name': '2018年总收入情况', 'value': 12581189}
        self.counter2 = {'name': '2018年总支出情况', 'value': 3912410}
        self.echart1_data = {
            'title': '行业分布',
            'data': [
                {"name": "商超门店", "value": 47},
                {"name": "教育培训", "value": 52},
                {"name": "房地产", "value": 90},
                {"name": "生活服务", "value": 84},
                {"name": "汽车销售", "value": 99},
                {"name": "旅游酒店", "value": 37},
                {"name": "五金建材", "value": 2},
            ]
        }
        self.echart2_data = {
            'title': '省份分布',
            'data': [
                {"name": "浙江", "value": 47},
                {"name": "上海", "value": 52},
                {"name": "江苏", "value": 90},
                {"name": "广东", "value": 84},
                {"name": "北京", "value": 99},
                {"name": "深圳", "value": 37},
                {"name": "安徽", "value": 150},
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "0岁以下", "value": 47},
                {"name": "20-29岁", "value": 52},
                {"name": "30-39岁", "value": 90},
                {"name": "40-49岁", "value": 84},
                {"name": "50岁以上", "value": 99},
            ]
        }
        self.echarts3_2_data = {
            'title': '职业分布',
            'data': [
                {"name": "电子商务", "value": 10},
                {"name": "教育", "value": 20},
                {"name": "IT/互联网", "value": 20},
                {"name": "金融", "value": 30},
                {"name": "学生", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '兴趣分布',
            'data': [
                {"name": "汽车价格", "value": 4},
                {"name": "汽车", "value": 5},
                {"name": "财经", "value": 9},
                {"name": "教育", "value": 8},
                {"name": "软件", "value": 9},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart4_data = {
            'title': '时间趋势',
            'data': [
                {"name": "安卓", "value": [3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 2, 4, 3, 4, 3, 4, 3, 4, 3, 6, 2, 4, 4]},
                {"name": "IOS", "value": [5, 3, 5, 6, 1, 5, 3, 5, 6, 4, 6, 4, 8, 3, 5, 6, 1, 5, 3, 7, 2, 5, 8]},
            ],
            'xAxis': ['01', '02', '03', '04', '05', '06', '07', '08', '09', '11', '12', '13', '14', '15', '16', '17',
                      '18', '19', '20', '21', '22', '23', '24'],
        }
        self.echart5_data = {
            'title': '省份TOP',
            'data': [
                {"name": "浙江", "value": 2},
                {"name": "上海", "value": 3},
                {"name": "江苏", "value": 3},
                {"name": "广东", "value": 9},
                {"name": "北京", "value": 15},
                {"name": "深圳", "value": 18},
                {"name": "安徽", "value": 20},
                {"name": "四川", "value": 13},
            ]
        }
        self.echart6_data = {
            'title': '4月份一线城市销售情况',
            'data': [
                {"name": "上海", "value": 5.8, "color": "01", "radius": ['59%']},
                {"name": "北京", "value": 5.5, "color": "02", "radius": ['49%']},
                {"name": "成都", "value": 5.0, "color": "03", "radius": ['39%']},
                {"name": "广州", "value": 4.2, "color": "04", "radius": ['29%']},
                {"name": "郑州", "value": 3.8, "color": "05", "radius": ['20%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '海门', 'value': 239},
                {'name': '鄂尔多斯', 'value': 231},
                {'name': '招远', 'value': 203},
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):

        self.title = '近期上市新车可视化'
        self.counter = {'name': '2023年总销售情况', 'value': 7607013}
        self.counter2 = {'name': '2023年六月份总销售情况', 'value': 1600000}
        self.echart1_data = {
            'title': '品牌销量排行',
            'data': [
                {"name": "比亚迪", "value": 877309},
                {"name": "大众", "value": 790220},
                {"name": "丰田", "value": 640454},
                {"name": "本田", "value": 414617},
                {"name": "长安", "value": 387351},
                {"name": "吉利", "value": 329045},
                {"name": "五菱汽车", "value": 290377},
                {"name": "奔驰", "value": 252339},
                {"name": "日产", "value": 240108},
                {"name": "奥迪", "value": 229493},
                {"name": "特斯拉", "value": 219893},
                {"name": "宝马", "value": 217630},
                {"name": "别克", "value": 196507},
                {"name": "广汽埃安", "value": 166323},
                {"name": "哈弗", "value": 164661},
                {"name": "奇瑞", "value": 144183},
                {"name": "广汽传祺", "value": 132614},
                {"name": "红旗", "value": 124160},
                {"name": "理想", "value": 103840},
                {"name": "现代", "value": 103242},
                {"name": "长安欧尚", "value": 78925},
                {"name": "凯迪拉克", "value": 71535},
                {"name": "雪佛兰", "value": 65264},
                {"name": "福特", "value": 64078},
                {"name": "捷达", "value": 63535},
                {"name": "荣威", "value": 62656},
                {"name": "领克", "value": 61392},
                {"name": "捷途", "value": 54948},
                {"name": "沃尔沃", "value": 53414},
                {"name": "腾势", "value": 45534},
                {"name": "蔚来", "value": 43744},
                {"name": "哪吒汽车", "value": 42505},
                {"name": "东风风神", "value": 42339},
                {"name": "坦克", "value": 41971},
                {"name": "名爵", "value": 37626},
                {"name": "思皓", "value": 37033},
                {"name": "起亚", "value": 33394},
                {"name": "小鹏汽车", "value": 32815},
                {"name": "极氪", "value": 32013},
                {"name": "深蓝汽车", "value": 31872},
                {"name": "零跑汽车", "value": 31293},
                {"name": "欧拉", "value": 28859},
                {"name": "启辰", "value": 27946},
                {"name": "吉利几何", "value": 25695},
                {"name": "北京汽车", "value": 24915},
                {"name": "马自达", "value": 24686},
                {"name": "奔腾", "value": 24518},
                {"name": "林肯", "value": 24151},
                {"name": "东风风行", "value": 21602},
                {"name": "smart", "value": 19711},
                {"name": "凯翼", "value": 19100},
                {"name": "AITO", "value": 18135},
                {"name": "雪铁龙", "value": 15456},
                {"name": "标致", "value": 15363},
                {"name": "SWM斯威汽车", "value": 14873},
                {"name": "北京", "value": 14119},
                {"name": "星途", "value": 13416},
                {"name": "路虎", "value": 13008},
                {"name": "岚图汽车", "value": 12024},
                {"name": "东风风光", "value": 11715},
                {"name": "三菱", "value": 11652},
                {"name": "魏牌", "value": 11160},
                {"name": "斯柯达", "value": 10509},
                {"name": "东风EV新能源", "value": 10507},
                {"name": "上汽大通MAXUS", "value": 10214},
                {"name": "合创", "value": 9068},
                {"name": "阿维塔", "value": 9002},
                {"name": "捷豹", "value": 8272},
                {"name": "智己", "value": 7783},
                {"name": "海马", "value": 7280},
                {"name": "ARCFOX极狐", "value": 6557},
                {"name": "大运汽车", "value": 6552},
                {"name": "瑞风汽车", "value": 6476},
                {"name": "睿蓝汽车", "value": 6440},
                {"name": "凌宝汽车", "value": 6236},
                {"name": "SRM鑫源", "value": 6081},
                {"name": "创维汽车", "value": 5456},
                {"name": "长安凯程", "value": 5365},
                {"name": "国金汽车", "value": 5350},
                {"name": "飞凡汽车", "value": 4900},
                {"name": "金杯新能源", "value": 3730},
                {"name": "宝骏", "value": 3224},
                {"name": "英菲尼迪", "value": 3188},
                {"name": "曹操汽车", "value": 3078},
                {"name": "北汽制造", "value": 2674},
                {"name": "SERES赛力斯", "value": 2121},
                {"name": "江铃集团新能源", "value": 1833},
                {"name": "中国重汽", "value": 1755},
                {"name": "江淮", "value": 1490},
                {"name": "思铭", "value": 1483},
                {"name": "电动屋", "value": 1113},
                {"name": "蓝电", "value": 1109},
                {"name": "新宝骏", "value": 548},
                {"name": "东南", "value": 512},
                {"name": "东风富康", "value": 486},
                {"name": "小虎", "value": 475},
                {"name": "广汽集团", "value": 367},
                {"name": "天际汽车", "value": 359},
                {"name": "江淮钇为", "value": 348},
                {"name": "DS", "value": 301},
                {"name": "爱驰", "value": 111},
                {"name": "讴歌", "value": 109},
                {"name": "理念", "value": 81},
                {"name": "开瑞", "value": 76},
                {"name": "观致", "value": 23},
                {"name": "福汽启腾", "value": 14},
                {"name": "雷丁", "value": 1},
            ]
        }

        self.echart2_data = {
        'title': '国家销售额',
        'data': [
                {"name": "中国", "value": 3804884},
                {"name": "德国", "value": 1572928},
                {"name": "日本", "value": 1334814},
                {"name": "美国", "value": 641428},
                {"name": "韩国", "value": 136636},
                {"name": "瑞典", "value": 53414},
                {"name": "法国", "value": 31120},
                {"name": "捷克", "value": 10509}
            ]
        }
        self.echarts3_1_data = {
            'title': '年龄分布',
            'data': [
                {"name": "0岁以下", "value": 0},
                {"name": "20-29岁", "value": 52},
                {"name": "30-39岁", "value": 90},
                {"name": "40-49岁", "value": 84},
                {"name": "50岁以上", "value": 10},
            ]
        }
        self.echarts3_2_data = {
            'title': '职业分布',
            'data': [
                {"name": "电子商务", "value": 10},
                {"name": "教育", "value": 20},
                {"name": "IT/互联网", "value": 20},
                {"name": "金融", "value": 30},
                {"name": "服务人员", "value": 40},
                {"name": "其他", "value": 50},
            ]
        }
        self.echarts3_3_data = {
            'title': '兴趣分布',
            'data': [
                {"name": "汽车价格", "value": 4},
                {"name": "汽车配置", "value": 5},
                {"name": "汽车销量", "value": 9},
                {"name": "汽车评价", "value": 8},
                {"name": "汽车车型", "value": 9},
                {"name": "其他", "value": 9},
            ]
        }
        self.echart4_data = {
            'title': '上市新车价格（万）',
            'data': [
                {"name": "最低价格", "value": [13.39, 8.48, 42.68, 28.93, 39.68, 27.88, 63.28, 2.88, 7.98, 154.7, 99.43, 146.8, 39.57, 43.65, 2.98, 5.28, 7.99, 9.4, 16.88, 8.69, 4.97, 13.38, 9.78, 15.78, 12.68]},
                {"name": "最高价格", "value": [17.49, 13.48, 49.99, 36.53, 48.88, 32.97, 80.48, 4.38, 16.38, 156.6, 146.88, 682.8, 56.78,56.25, 4.18, 9.31, 7.99, 15.19, 25.88, 11.69, 4.97, 16.28, 11.28, 17.68, 13.88]},
            ],
            'xAxis': ['瑞虎8 PRO', '江淮T6', '奥迪Q5L Sportback', '奥迪Q3 Sportback', '奥迪Q5L', '奥迪Q3', '奥迪Q7',
                      '大力牛魔王01', '威狮1986', '奔驰EQS AMG', 'GLE级AMG', '迈巴赫S级', 'A级AMG(进口)', '宝马5系',
                      '凌宝Uni', '鲸卡T7', '奔奔E-Star', '朗逸', 'SEM DELICA', 'SWM斯威G05', '纳米BOX', '江豚',
                      '本田LIFE', '海豚EV'],
        }

        self.echart5_data = {
            'title': '六月份销量省份TOP10',
            'data': [
                {"name": "广东", "value": 17.6},
                {"name": "江苏", "value": 13.4},
                {"name": "山东", "value": 12.0},
                {"name": "浙江", "value": 11.9},
                {"name": "河南", "value": 9.4},
                {"name": "四川", "value": 8.5},
                {"name": "河北", "value": 7.9},
                {"name": "上海", "value": 5.8},
            ]
        }
        self.echart6_data = {
            'title': '4月份一线城市销售情况',
            'data': [
                {"name": "太原", "value": 80, "value2": 20, "color": "01", "radius": ['59%', '70%']},
                {"name": "上海", "value": 70, "value2": 30, "color": "02", "radius": ['49%', '60%']},
                {"name": "广州", "value": 65, "value2": 35, "color": "03", "radius": ['39%', '50%']},
                {"name": "北京", "value": 60, "value2": 40, "color": "04", "radius": ['29%', '40%']},
                {"name": "深圳", "value": 50, "value2": 50, "color": "05", "radius": ['20%', '30%']},
            ]
        }
        self.map_1_data = {
            'symbolSize': 100,
            'data': [
                {'name': '北京', 'value': 555},
                {'name': '上海', 'value': 740},
                {'name': '广州', 'value': 531},
                {'name': '杭州', 'value': 509},
                {'name': '深圳', 'value': 478},
                {'name': '苏州', 'value': 414},
                {'name': '重庆', 'value': 397},
                {'name': '武汉', 'value': 383},
                {'name': '郑州', 'value': 379},
                {'name': '东莞', 'value': 362},
                {'name': '天津', 'value': 345},
                {'name': '西安', 'value': 325},
            ]
        }


class CorpData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('corp.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')

class JobData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        with open('job.json', 'r', encoding='utf-8') as f:
            data = json.loads(f.read())
        self.title = data.get('title')
        self.counter = data.get('counter')
        self.counter2 = data.get('counter2')
        self.echart1_data = data.get('echart1_data')
        self.echart2_data = data.get('echart2_data')
        self.echarts3_1_data = data.get('echarts3_1_data')
        self.echarts3_2_data = data.get('echarts3_2_data')
        self.echarts3_3_data = data.get('echarts3_3_data')
        self.echart4_data = data.get('echart4_data')
        self.echart5_data = data.get('echart5_data')
        self.echart6_data = data.get('echart6_data')
        self.map_1_data = data.get('map_1_data')

