# common.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.gridspec as gridspec
import math
from influxdb_client import InfluxDBClient

# 1. 폰트 설정
font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
fontprop = fm.FontProperties(fname=font_path)
font_name = fontprop.get_name()
mpl.rcParams['font.family'] = font_name
mpl.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
plt.rcParams['font.family'] = font_name

# 2. InfluxDB 연결 함수
def get_influx_client():
    INFLUX_URL   = "https://influx.aiot2.live"
    INFLUX_TOKEN = "RmaabELI9VpYPRu4nt_xBZX5l3Gv5lx8XnR4mVZnqep4Ya3eYrfpLUk4Y4dYE4J0mlcFHFPLUCKh8a4jq_lMNw=="
    INFLUX_ORG   = "aiot2-team2-coffee"
    INFLUX_BUCKET= "coffee-mqtt"
    client = InfluxDBClient(
        url=INFLUX_URL,
        token=INFLUX_TOKEN,
        org=INFLUX_ORG
    )
    return client, INFLUX_BUCKET

# 3. 센서 타입 정의 및 한글 매핑
sensor_types = [
    "co2", "distance", "humidity", "illumination", "infrared", "pressure",
    "temperature", "infrared_and_visible", "occupancy", "battery_level",
    "activity", "battery"
]
sensor_type_mapping = {
    'temperature': '실내 온도(°C)',
    'humidity': '상대습도(%)',
    'co2': '이산화탄소 농도(ppm)',
    'tvoc': '총휘발성유기화합물(ppb)',
    'pressure': '대기압(hPa)',
    'occupancy': '재실 여부',
    'activity': '활동 수준',
    'distance': '거리(cm)',
    'illumination': '조도(lux)',
    'infrared': '적외선',
    'infrared_and_visible': '적외선 및 가시광선',
    'battery': '배터리 상태',
    'battery_level': '배터리 잔량(%)'
}