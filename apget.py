import warnings
import requests
import os
import time
from subprocess import call
warnings.filterwarnings("ignore")
from datetime import datetime


# CONFIGURE THESE
CONTROLLER = ""  # UniFi Controller URL
USERNAME = ""  # UniFi Controller username
PASSWORD = ""  # UniFi Controller password
SITE = "default"  


session = requests.Session()
session.verify = False  # Ignore SSL cert
while True:
    # Get time
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    
    # Login to UniFi Controller
    login_url = f"{CONTROLLER}/api/login"
    login_data = {"username": USERNAME, "password": PASSWORD}
    resp = session.post(login_url, json=login_data)
    resp.raise_for_status()

    # Get AP data
    aps_url = f"{CONTROLLER}/api/s/{SITE}/stat/device"
    aps_resp = session.get(aps_url)
    aps_resp.raise_for_status()
    aps = aps_resp.json().get("data", [])


    state_map = {
        0: "Disconnected",
        1: "Connected",
        2: "Pending Adoption",
        3: "Upgrading",
        4: "Provisioning",
        5: "Heartbeat Missed"
    }


    for ap in aps:
        state = ap.get('state')
        state_str = state_map.get(state, f"Unknown ({state})")
        print("----------------------Log Time:", current_time, "----------------------")
        print("Access Point Details:")
        print(f"Name: {ap.get('name')}, MAC: {ap.get('mac')}, Model: {ap.get('model')}")
        print(f"State: {state_str}")

    if state != 1: # If not connected, reboot the AP
        print("Access Point is not connected, Running readoption script...")
        call(["python3", "reboot.py"])
        call(["python3", "restart_bar.py"])
        call(["python3", "wait.py"])
        #could add line here to run set-inform on the AP if needed
        print("------------------------------------------------------------------------\n\n")

    else:
        print ('No Issues Detected') 
        call(["python3", "normal.py"])
        call(["python3", "wait.py"])
        print("------------------------------------------------------------------------\n\n")
