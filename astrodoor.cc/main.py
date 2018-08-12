import requests
from bs4 import BeautifulSoup
import shutil
# Disable SSL warning
import urllib3
urllib3.disable_warnings()

def getData(data, img_data):
  form_url = "https://astrodoor.cc/horoscope.jsp"
  url = "https://astrodoor.cc/horoscope_result_phone.jsp"
  # cImg_url = "https://astrodoor.cc/createImage.jsp"
  img_url = "https://astrodoor.cc"

  header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:62.0) Gecko/20100101 Firefox/62.0"}
  
  s = requests.Session()
  s.headers = header
  s.verify = False

  s.get(form_url)

  cookieVal = s.cookies._cookies["astrodoor.cc"]["/"]["JSESSIONID"].value
  header["Cookie"] = "JSESSIONID=" + cookieVal
  header["Referer"] = "https://astrodoor.cc/horoscope.jsp"
  
  text = s.post(url, data= data)
  
  # imgNo = s.post(cImg_url, data= img_data)
  # imgNo = BeautifulSoup(imgNo.text, "html.parser").find("input").get("value")
  # img = s.get(img_url + imgNo + ".png")

  text = BeautifulSoup(text.text, "html.parser")

  header["Referer"] = "https://astrodoor.cc/horoscope_result_phone.jsp"
  img_url += text.find(id="imgout").get("src")
  img = s.get(img_url, stream=True)

  file = open("text.html","w")
  file.write(text.prettify())
  file.close()

  with open("img.png", "wb") as f:
    img.raw.decode_content = True
    shutil.copyfileobj(img.raw, f)

if __name__ == "__main__":
  data = {
  # 出生年月日及時間：
    "year": "2018",
    "month": "7",
    "day": "21",
    "hour": "21",
    "minute": "11",


  # 出生地點：
  # 地區 (area)，不可不送，但可亂填！
  # 臺灣(0, 預設), 馬來西亞(1), 新加坡(2)
    "area": "0",
  # 省份 (province)，不可不送，但可亂填！
  # 預設地區
  # 臺灣(0, 預設), 香港(1), 澳门(2), 北京(3), 上海(4), 天津(5), 重庆(6),
  # 河北(7), 山西(8), 内蒙古(9), 辽宁(10), 吉林(11), 黑龙江(12), 江苏(13),
  # 浙江(14), 安徽(15), 福建(16), 江西(17), 山东(18), 河南(19), 湖北(20),
  # 湖南(21), 广东(22), 广西(23), 海南(24), 四川(25), 贵州(26), 云南(27), 
  # 西藏(28), 陕西(29), 甘肃(30), 青海(31), 宁夏(32), 新疆(33)
  # 馬來西亞
  # Johor(34), Kuala Lumpur(35), Kedah(36), Kelantan(37), Labuan(38),
  # Melaka(39), Negeri Sembilan(40), Pahang(41), Perak(42), Perlis(43),
  # Pulau Pinang(44), Putrajaya(45), Sabah(46), Sarawak(47), Selangor(48),
  # Terengganu(49).....(不想寫了)
    "province": "0",
  # 城鎮經緯度 (city)
    "city": "121E30 25N03",
  # 拆解經緯度
    "latitude": "N",
    "latitudeDegree": "3",
    "latitudeMinute": "25",
    "longitude": "E",
    "longitudeDegree": "121",
    "longitudeMinute": "30",
  # 時區
  # GMT+11:30(-690), GMT+11:00(-660), GMT+10:30(-630), GMT+10:00(-600),
  # GMT+09:30(-570), GMT+09:00(-540), GMT+08:30(-510), GMT+08:00(-480),
  # GMT+07:30(-450), GMT+07:00(-420), GMT+06:30(-390), GMT+06:00(-360),
  # GMT+05:30(-330), GMT+05:00(-300), GMT+04:30(-270), GMT+04:00(-240),
  # GMT+03:30(-210), GMT+03:00(-180), GMT+02:30(-150), GMT+02:00(-120),
  # GMT+01:30(-90), GMT+01:00(-60), GMT+00:30(-30), GMT 00:00(0),
  # GMT-01:00(60), GMT-00:30(30), GMT-01:30(90), GMT-02:00(120),
  # GMT-02:30(150), GMT-03:00(180), GMT-03:30(210), GMT-04:00(240),
  # GMT-04:30(270), GMT-05:00(300), GMT-05:30(330), GMT-06:00(360),
  # GMT-06:30(390), GMT-07:00(420), GMT-07:30(450), GMT-08:00(480),
  # GMT-08:30(510), GMT-09:00(540), GMT-09:30(570), GMT-10:00(600),
  # GMT-10:30(630), GMT-11:00(660), GMT-12:00(720), GMT-11:30(690)
    "timezone": "-480",


  # 宮位系統 (houseSystem)：
  #  Placidus(P, 預設), Koch(K), Campanus(C), Regiomontanus(R), Equal(E),
  #  Vehlow(V), Meridian(X), Porphyry(O), Alcabitius(B), Krusinski(U),
  #  Azimuth(H), Morinus(M), Polich-Page(T)
    "houseSystem": "P",


  # 選填欄位「預設不傳送」，若要啟用功能，請加送這些資訊：
  # 顯示小行星（凱龍星、婚神星、智神星、灶神星與榖神星）
    # "showAsteroids": "Y",
  # 顯示次要相位（30°、45°、135°、150°）
    # "minorAspect": "yes",
  # 星盤圖形左上角不打印出生資訊
    # "showBirthInfo":	"no",
  # 我輸入的出生時間為日光節約（夏令時)
    # "daylight": "yes",


  # 相位容許度：
  # 合相(0°), 六分相(60°), 四分相(90°), 三分相(120°), 二分相(180°), 次要相位
  # 太陽
    "sun0": "8",
    "sun60": "4",
    "sun90": "6",
    "sun120": "6",
    "sun180": "8",
    "sunminor": "1.5",
  # 月亮
    "moon0": "7",
    "moon60":	"4",
    "moon90": "6",
    "moon120": "6",
    "moon180": "7",
    "moonminor": "1.5",
  # 行星
    "planet0": "6",
    "planet60": "4",
    "planet90": "6",
    "planet120": "6",
    "planet180": "6",
    "planetminor": "1.5"
  }

  img_data= {
    "isIE6": "NO",
    "showAsteroids": "N",
    "showBirthInfo": "yes"
  }

  getData(data, img_data)