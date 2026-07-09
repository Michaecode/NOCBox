from config import load_config
from monitor.ping import ping_host

def main():
    config = load_config()

    print("=== NOCBOX ==")
    print("NOCBOC Config:")
    print("")

    for name, host in config["hosts"].items():
        status = ping_host(host["ip"])
        if status:
            status_text = "ONLINE"
        else:
            status_text = "OFFLINE"
        print(f"{name}: {host['ip']}", status_text)
        print("")

if __name__ == "__main__":
    main()
