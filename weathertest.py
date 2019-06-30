import requests
import json
city = input('请输入要查询的城市名称：')

url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'%city
# 使用requests发起请求，接受返回的结果
rs = requests.get(url)
# 使用loads函数，将json字符串转换为python的字典或列表
rs_dict = json.loads(rs.text)
# 取出error
error_code = rs_dict['error']
# 如果取出的error为0，表示数据正常，否则没有查询到结果
if error_code == 0:
 # 从字典中取出数据
    results = rs_dict['results']
# 根据索引取出天气信息字典
    info_dict = results[0]
  # 根据字典的key，取出城市名称
    city_name = info_dict['currentCity']
# 取出pm值
    pm25 = info_dict['pm25']
    print('当前城市：%s  pm值：%s'%(city_name,pm25))
# 取出天气信息列表
    weather_data = info_dict['weather_data']
# for循环取出每一天天气的小字典
    for weather_dict in weather_data:
 # 取出日期，天气，风级，温度
        date = weather_dict['date']
        weather = weather_dict['weather']
        wind = weather_dict['wind']
        temperature = weather_dict['temperature']

print("%s,%s"%(weather,date))