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

ids = ["942E95B4336BDFA7","3BA9C90738A8600D","9A16E73DC0B9AF6C","58611212645F0AB1","29740CCBBD82FC33","6D1FFB57C26F1108","09680C5849BFA077","177A516A81E9DEA5"]
url = "https://data.etabus.gov.hk/v1/transport/kmb/stop-eta/"
placeholder = st.empty()
container = st.container()

while True:
    for idd in ids:
        response = requests.get(url+idd)
        formatted = {}
        if response.status_code == 200:
            data = response.json()['data']
            print(*data,end='\n\n',sep="\n")
            for i in data:
                if i['eta'] != None:
                    try:
                        tmp = formatted[str(i['route'])]
                    except KeyError:
                        formatted[str(i['route'])] = {}
                        formatted[str(i['route'])]["Destination"] = i["dest_en"]
                        formatted[str(i["route"])]["ETA"] = []
                    formatted[str(i['route'])]["ETA"].append(i["eta"])
                    
            for i in formatted:
                formatted[i]['ETA'].sort()
                s = []
                for j in formatted[i]["ETA"]:
                    print(j)
                    diff = calctimediff(j, datetime.now(pytz.timezone("Hongkong")).isoformat())
                    mins = diff//60
                    secs = diff%60
                    s.append(f"{mins}m{secs}s")
                formatted[i]['ETA'] = '\n'.join(s)
                del s
                    
        else:
            print("Request failed with status code:", response.status_code)
        print(formatted)

        df = pd.DataFrame(formatted).transpose()
        with placeholder.container():
            st.write(df)
        time.sleep(5)