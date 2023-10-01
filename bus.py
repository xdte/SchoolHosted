import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import pytz
import time

def calctimediff(time1, time2):
    time1 = datetime.fromisoformat(time1)
    time2 = datetime.fromisoformat(time2)
    diff = time1-time2
    return abs(int(diff.total_seconds()))

stops = [[{"id": "942E95B4336BDFA7", "name": "上行"},
         {"id": "9A16E73DC0B9AF6C", "name": "上行"},
         {"id": "29740CCBBD82FC33", "name": "上行"}],
         [{"id": "3BA9C90738A8600D", "name": "下行"},
         {"id": "58611212645F0AB1", "name": "下行"}],
         [{"id": "6D1FFB57C26F1108", "name": "彩雲"},
         {"id": "09680C5849BFA077", "name": "彩雲"},
         {"id": "177A516A81E9DEA5", "name": "彩雲"}]]
url = "https://data.etabus.gov.hk/v1/transport/kmb/stop-eta/"
placeholder = st.empty()
container = st.container()

while True:
    for direction in stops:
        formatted = {}
        for stop in direction:
            response = requests.get(url+stop['id']) 
            if response.status_code == 200:
                data = response.json()['data']
                for i in data:
                    if i['eta'] != None and i["dest_en"] != "CHOI WAN":
                        try:
                            tmp = formatted[str(i['route'])]
                            del tmp
                        except KeyError:
                            formatted[str(i['route'])] = {}
                            formatted[str(i['route'])]["Destination"] = i["dest_en"]
                            formatted[str(i["route"])]["ETA"] = []
                        formatted[str(i['route'])]["ETA"].append(i["eta"])         
            else:
                print("Request failed with status code:", response.status_code)
        print(formatted)
        for i in formatted:
            formatted[i]['ETA'].sort()
            s = []
            for j in formatted[i]["ETA"]:
                print(j)
                diff = calctimediff(j, datetime.now(pytz.timezone("Hongkong")).isoformat())
                mins = diff//60
                secs = diff%60
                s.append(f"{mins} m {secs} s")
            formatted[i]['ETA'] = ' | '.join(s)
            del s

        df = pd.DataFrame(formatted).transpose()
        with placeholder.container():
            st.write(f"{direction[0]['name']}")
            st.table(df)
            st.write(f"Last Updated: {str(datetime.now())[:-7]}")
        time.sleep(8)
