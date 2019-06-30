# _*_ coding: utf-8 _*_
import requests
from wxpy import *
import json
city = input('请输入要查询的城市名称：')

#url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'%city
#pXtbAAE9nOGYBBT7aflPwraLfuHY7GQM
url = 'https://restapi.amap.com/v3/weather/weatherInfo'
params = {'key': 'e825c1532a5afd46730123a6c41e4bb9',     # 你的密钥
          'city': city,         # 以南京市浦口区为例
          'extensions': 'all'}
# 使用requests发起请求，接受返回的结果
rs = requests.get(url,params)
# 使用loads函数，将json字符串转换为python的字典或列表
rs_dict = json.loads(rs.text)
# 取出error
error_code = rs_dict['status']
# 如果取出的error为0，表示数据正常，否则没有查询到结果
if error_code == '1':
 # 从字典中取出数据
    results = rs_dict['forecasts']
# 根据索引取出天气信息字典
    info_dict = results[0]
  # 根据字典的key，取出城市名称
    city_name = info_dict['city']
# 取出pm值
    province = info_dict['province']
    print('%s%s' %(province,city_name))
# 取出天气信息列表
    weather_data = info_dict['casts']
# for循环取出每一天天气的小字典
    for weather_dict in weather_data:
 # 取出日期，天气，风级，温度
        date = weather_dict['date']
        weather = weather_dict['dayweather']
        wind = weather_dict['daywind']
        temperature = weather_dict['daytemp']

print("%s,%s"%(weather,date))