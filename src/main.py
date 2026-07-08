from config import load_config

def main():
    config = load_config()

    print("=== NOCBOX ==")
    print("NOCBOC Config:")
    print("")

    for name, host in config["hosts"].items():
        print(f"{name}: {host['ip']}")

if __name__ == "__main__":
    main()
