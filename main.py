from PyQt5.QtWidgets import QApplication
from main_ui import Ui_Funy
import requests
import sys
import os

class Fun(Ui_Funy):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
        self.listWidget.itemClicked.connect(self.switch_pages)
        self.chp()
        self.btn_next_chp.clicked.connect(self.chp)
        self.btn_xz_search.clicked.connect(self.xz)
        self.btn_weather_search.clicked.connect(self.weather)

    def switch_pages(self):
        left_idx = self.listWidget.currentRow()
        self.stackedWidget.setCurrentIndex(left_idx)

    # 彩虹屁
    def chp(self):
        pi = requests.get("https://api.shadiao.pro/chp").json()["data"]["text"]
        self.textBrowser_chp.setText(pi)
        pass

    # 星座运势查询
    def xz(self):
        xz = self.input_xz.text()
        try:
            res = requests.get(
                f"http://api.tianapi.com/star/index?key={os.getenv('API_KEY')}&astro={xz}").json()
            count = 1
            str_tmp = ""
            for kv in res["newslist"]:
                if count % 2 == 0:
                    str_tmp += f"{kv['type']}: {kv['content']}\n\n"
                else:
                    str_tmp += f"{kv['type']}: {kv['content']}        "
                count += 1
            self.textBrowser_xz.setText(str_tmp)
        except:
            pass
            
    # 天气查询
    def weather(self):
        city = self.input_city.text()
        try:
            url = f"https://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city={city}&needMoreData=true&pageNo=1&pageSize=1"
            res = requests.get(url).json()
            if res["code"] == 105 or res["code"] == 1017:
                self.textBrowser_weather.setText(res["msg"])
            else:
                weather_data = res['data']['list'][0]
                weather_str = f"数据来源: {res['data']['sourceName']}\n\n城市: {weather_data['city']}        天气: {weather_data['weather']}\n\n当前温度: {weather_data['temp']}℃        湿度: {weather_data['humidity']}\n\n最低温度: {weather_data['low']}℃        最高温度: {weather_data['high']}℃\n\n风: {weather_data['wind']}        空气质量:{weather_data['airQuality']}\n\npm2.5: {weather_data['pm25']}        pm10: {weather_data['pm10']}"
                self.textBrowser_weather.setText(weather_str)
        except:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fun = Fun()
    sys.exit(app.exec_())
