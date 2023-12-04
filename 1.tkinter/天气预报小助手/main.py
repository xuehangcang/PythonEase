import requests
import tkinter as tk

# 基本窗口
root = tk.Tk()
root.title("天气预报小助手")

# 输入字段
city_entry = tk.Entry(root)
city_entry.pack()

# 天气信息标签
weather_label = tk.Label(root, text="请输入城市名称，查询天气", font=('Helvetica', 15))
weather_label.pack()

# 查询按钮
search_button = tk.Button(root, text="查询", width=10)
search_button.pack()


def get_weather_data(city):
    """获取天气数据"""
    # 查询区县的行政区划编码
    wd = {}
    with open("weather_district_id.csv", "r", encoding="utf-8") as f:
        weather_district = f.read().split("\n")
    for district in weather_district:
        districtcode = district.split(",")[1]
        district = district.split(",")[5]
        wd[district] = districtcode

    # 获取天气信息 https://lbsyun.baidu.com/faq/api?title=webapi/weather/base API文档

    url = "https://api.map.baidu.com/weather/v1/"  # API地址
    ak = "你的AK"  # 你的AK
    params = {
        "district_id": wd.get(city),
        "data_type": "all",
        "ak": ak,
    }
    response = requests.get(url=url, params=params)
    result = response.json()["result"]
    if response.status_code == 200:  # 状态码200表示成功接收到信息
        return result
    else:
        return None


def update_weather_label(weather_data):
    """更新天气信息标签"""
    if weather_data:
        print(weather_data)
        city_name = weather_data["location"]["name"]
        temp = weather_data["now"]["temp"]
        description = weather_data["now"]["text"]
        weather_label['text'] = f"{city_name}的温度：{temp}°C\n天气状况：{description}"
    else:
        weather_label['text'] = "未能获取数据，请检查城市名称是否正确。"


def search_weather():
    """查询天气"""
    city = city_entry.get()  # 获取输入的城市名称
    weather_data = get_weather_data(city)  # 获取天气数据
    update_weather_label(weather_data)  # 更新天气信息标签


search_button['command'] = search_weather
root.mainloop()
