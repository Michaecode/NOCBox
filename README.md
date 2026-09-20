# NOCBox
> ⚠️ This README is still a work in progress.

NOCBox is a Python-based Network Operation Center (NOC) designed to provide a lightweight terminal interface for monitoring network infrastructure, events and system status.

> ⚠️ This project is still a work in progress.

Feel free to use it, modify it, or suggest improvements!

It provides a simple terminal-based dashboard for monitoring hosts through ICMP ping, showing their current status and recording state changes in a log file.

The project is designed to run on a small dedicated Linux machine and continuously monitor different hosts across multiple networks.

## Features

- Continuous host monitoring through ICMP ping
- Online/offline status detection
- Automatic dashboard refresh
- Number of monitored, online and offline devices
- Last update timestamp
- Detection of host state changes
- Event logging
- Recent events displayed directly in the dashboard
- YAML-based configuration
- Simple terminal user interface (TUI)


## Installation
### Requirements

- Linux
- Python 3
- `ping` command
- PyYAML
- git


### Clone the repository
```shell
git clone https://github.com/Michaecode/NOCBox.git 
cd NOCBox
```

### Create a virtual environment
```shell
python3 -m venv .venv 
source .venv/bin/activate
```
### Install the dependencies
```shell
pip install -r requirements.txt
```
### Configuration:
Copy the example configuration:
```shell
cp config/config-example.yaml config/config.yaml
```
Edit config/config.yaml and add the hosts you want NOCBox to monitor.

### Run NOCBox
```shell
python3 src/main.py
```
The dashboard will start in the terminal and refresh automatically.

## Project structure

```text
NOCBox/
├── src/
│   ├── main.py
│   ├── config.py
│   ├── monitor/
│   │   └── ping.py
│   ├── ui/
│   │   └── screen.py
│   └── utils/
│       └── logger.py
├── config.yml
├── logs/
│   └── .gitkeep
├── .gitignore
└── README.md
```
