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

## Requirements

- Linux
- Python 3
- `ping` command
- PyYAML

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
└── README.md```
