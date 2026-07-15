import time
import os
from config import load_config
from monitor.ping import ping_host
from ui.screen import tui

def main():
    os.system("clear")
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
            if status == True:
                online += 1
            hosts_status.append(host_info)
        devices = len(hosts_status)
        offline = devices - online
        time_in_seconds = time.time()
        time_in_seconds = time.ctime(time_in_seconds)
        tui(hosts_status, time_in_seconds, devices, online, offline)
        time.sleep(10)

if __name__ == "__main__":
    main()
