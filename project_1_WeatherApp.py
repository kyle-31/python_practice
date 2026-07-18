import requests

def GetWeather(latitude, longitude):



    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&current=temperature_2m,wind_speed_10m,relative_humidity_2m"
    )

    try:
        response = requests.get(url, timeout=10)

        #如果API回傳404和500等錯誤 主動產生例外
        response.raise_for_status()

        data = response.json()

        return data["current"]

    except requests.exceptions.Timeout:
        print("連線逾時 請稍後再試")

    except requests.exceptions.ConnectionError:
        print("無法連線 請檢查網路")

    except requests.exceptions.HTTPError:
        print("API 回傳錯誤:", response.status_code)

    except KeyError:
        print("API 資料格式不符合預期")

    return None

    response = requests.get(url)
    data = response.json()
    current = data["current"]

    return current


def DisplayWeather(city, current):
    print("\n城市:",city)
    print("溫度",current["temperature_2m"],"°C")
    print("濕度",current["relative_humidity_2m"],"%")
    print("風速",current["wind_speed_10m"],"km/h")

while True:
    print("""
1. 高雄
2. 台北
3. 台中
4. 自訂經緯度
5. 離開
""")
    choice = input("輸入選擇:")

    if choice == "1":
        current = GetWeather(22.6237,120.3014)
        
        if current is not None:
            DisplayWeather("高雄", current)
    elif choice == "2":
        current = GetWeather(25.0330,121.5654)

        if current is not None:
            DisplayWeather("台北", current)
    elif choice == "3":
        current = GetWeather(24.1477,120.6736)
        
        if current is not None:
            DisplayWeather("台中", current)
    elif choice == "4":
        try:
            latitude = float(input("輸入緯度:"))
            longitude = float(input("輸入經度:"))

        except ValueError:
            print("經緯度必須是數字")
            continue
        
        current = GetWeather(latitude,longitude)

        if current is not None:
            DisplayWeather("自訂位置", current)
        
    elif choice == "5":
        print("謝謝使用")
        break
    else:
        print("輸入錯誤")

