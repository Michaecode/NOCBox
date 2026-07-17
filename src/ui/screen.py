
def tui(hosts_status, time_in_seconds, devices, online, offline):
    print("==========================================")
    print("                 NOCBOX")
    print("==========================================")
    print("Last Update: ", time_in_seconds)
    print("")
    print("Devices:", devices, "|", "Online:", online, "|", "Offline:", offline)
    print("")
    for host in hosts_status:
        if host["online"]:
            status = "[ONLINE]"
        else:
            status = "[OFFLINE]"
        print(f"{host['name']:<30}{host['ip']:<18}{status}")
    print("")
    print("")
    print("==========================================")
    print("Recents Events ")
    print("==========================================")
    with open('logs/nocbox.log', "r") as log_file:
        for line in log_file:
            print(line.strip())