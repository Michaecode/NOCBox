import time
import os

from config import load_config
from monitor.ping import ping_host
from ui.screen import tui
from utils.logger import log_event

def main():
    os.system("clear")
    previous_status = {}
    while True:
        print("\033[H", end="")
        config = load_config()
        hosts_status = []
        online =0
        for name, host in config["hosts"].items():
            status = ping_host(host["ip"])
            host_info = {
                "name": name,
                "ip": host["ip"],
                "online": status
            }
            if status:
                online += 1
            hosts_status.append(host_info)
            if name in previous_status:
                old_status = previous_status[name]
                if old_status != status:
                    if old_status == True:
                        message = (f"Host {name} changed state ONLINE --> OFFLINE")
                    if old_status == False:
                        message = (f"Host {name} changed state OFFLINE --> ONLINE")
                    log_event(message)
            previous_status[name] = status
        devices = len(hosts_status)
        offline = devices - online
        time_in_seconds = time.time()
        time_in_seconds = time.ctime(time_in_seconds)
        tui(hosts_status, time_in_seconds, devices, online, offline)
        time.sleep(15)

if __name__ == "__main__":
    main()
