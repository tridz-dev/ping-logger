# Network Ping Monitor - Setup Guide

A Python-based network monitoring tool that continuously pings multiple IP addresses and logs the results with automatic log rotation.

## Features

- Monitor up to 6 IP addresses simultaneously (DNS, Gateway, and 4 custom IPs)
- Automatic log rotation (keeps 7 days of hourly logs)
- Configurable via environment variables
- Runs as a systemd service for continuous monitoring
- Detailed logging with timestamps and response times

## Requirements

### System Requirements
- Linux operating system (Ubuntu/Debian recommended)
- Python 3.10 or higher
- Root/sudo access (required for ICMP ping operations)

### Python Dependencies
- `ping3` - For sending ICMP ping requests
- `python-dotenv` - For loading environment variables from .env file

## Installation

### 1. Install System Dependencies

```bash
# Update package list
sudo apt update

# Install Python 3 and venv support
sudo apt install python3 python3-venv python3-pip -y
```

### 2. Setup Project Directory

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install Python dependencies
pip install ping3 python-dotenv

# Deactivate virtual environment
deactivate
```

### 3. Clone this repo master branch 

Clone this repo under `/home/YOUR_USERNAME/ping/` with the monitoring script.

### 4. update Environment Configuration

open file named `ping.env` in the same directory:

```env
DNS=1.1.1.1
GATEWAY=192.168.10.1
EXTRA=8.8.8.8
EXTRA2=192.168.1.10
EXTRA3=192.168.1.20
EXTRA4=192.168.1.30
```

**Configuration Options:**
- `DNS` - Primary DNS server to monitor (default: 1.1.1.1)
- `GATEWAY` - Your network gateway/router (default: 192.168.10.1)
- `EXTRA` - Optional additional IP address
- `EXTRA2` - Optional additional IP address
- `EXTRA3` - Optional additional IP address
- `EXTRA4` - Optional additional IP address

### 5. Test the Script

```bash
# Navigate to project directory
cd ~/ping

# Run the script manually (requires sudo for ICMP)
sudo ./venv/bin/python ping.py
```

Press `Ctrl+C` to stop. Check that `ping.log` is created in the same directory.

## Running as a System Service

### 1. Create Systemd Service File

```bash
sudo nano /etc/systemd/system/ping-monitor.service
```

Add the following content (replace `YOUR_USERNAME` with your actual username):

```ini
[Unit]
Description=Network Ping Monitor
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/home/YOUR_USERNAME/ping
ExecStart=/home/YOUR_USERNAME/ping/venv/bin/python /home/YOUR_USERNAME/ping/ping.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 2. Enable and Start the Service

```bash
# Reload systemd to recognize the new service
sudo systemctl daemon-reload

# Enable service to start on boot
sudo systemctl enable ping-monitor

# Start the service
sudo systemctl start ping-monitor

# Check service status
sudo systemctl status ping-monitor
```

## Managing the Service

### Service Control Commands

```bash
# Start the service
sudo systemctl start ping-monitor

# Stop the service
sudo systemctl stop ping-monitor

# Restart the service
sudo systemctl restart ping-monitor

# Check service status
sudo systemctl status ping-monitor

# Enable auto-start on boot
sudo systemctl enable ping-monitor

# Disable auto-start on boot
sudo systemctl disable ping-monitor
```

### Viewing Logs

```bash
# View systemd service logs (live)
sudo journalctl -u ping-monitor -f

# View last 50 lines of service logs
sudo journalctl -u ping-monitor -n 50

# View the actual ping log file
tail -f /home/YOUR_USERNAME/ping/ping.log

# View ping log with less
less /home/YOUR_USERNAME/ping/ping.log
```

## Log Files

### Log Location
- Main log file: `/home/YOUR_USERNAME/ping/ping.log`
- Rotated logs: `ping.log.YYYY-MM-DD_HH-MM-SS` (automatically created)

### Log Rotation
- Logs rotate every hour
- Keeps 168 hours (7 days) of history
- Old logs are automatically deleted

### Log Format
```
YYYY-MM-DD HH:MM:SS - LEVEL - Message
```

Example log entries:
```
2026-02-02 11:15:30 - INFO - Ping to 1.1.1.1 successful. Response time: 12.45 ms
2026-02-02 11:15:31 - WARNING - Ping to 192.168.10.1 failed.
2026-02-02 11:15:32 - ERROR - Error pinging 8.8.8.8: timeout
```

## Troubleshooting

### Service Won't Start

1. Check service status:
```bash
sudo systemctl status ping-monitor
```

2. View detailed logs:
```bash
sudo journalctl -u ping-monitor -n 100
```

3. Verify Python path in service file matches your installation:
```bash
ls -l /home/YOUR_USERNAME/ping/venv/bin/python
```

### Module Not Found Errors

Ensure packages are installed in the virtual environment:
```bash
cd ~/ping
source venv/bin/activate
pip list | grep -E "ping3|python-dotenv"
deactivate
```

If missing:
```bash
source venv/bin/activate
pip install ping3 python-dotenv
deactivate
sudo systemctl restart ping-monitor
```
### No Logs Being Created

1. Check working directory permissions:
```bash
ls -ld ~/ping
```

2. Manually create log file:
```bash
sudo touch ~/ping/ping.log
sudo chown root:root ~/ping/ping.log
```

3. Run script manually to see errors:
```bash
cd ~/ping
sudo ./venv/bin/python ping.py
```
## Uninstalling

```bash
# Stop and disable the service
sudo systemctl stop ping-monitor
sudo systemctl disable ping-monitor

# Remove service file
sudo rm /etc/systemd/system/ping-monitor.service

# Reload systemd
sudo systemctl daemon-reload

# Remove project directory
rm -rf ~/ping
```

## Project Structure

```
~/ping/
├── ping.py              # Main Python script
├── ping.env             # Environment configuration
├── ping.log             # Current log file
├── ping.log.2026-02-01_* # Rotated log files
└── venv/                # Virtual environment
    ├── bin/
    │   └── python       # Python interpreter
    └── lib/
        └── python3.*/
            └── site-packages/  # Installed packages
```

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review systemd logs: `sudo journalctl -u ping-monitor -n 100`
3. Test the script manually: `sudo ~/ping/venv/bin/python ~/ping/ping.py`

## License


This script is provided as-is for network monitoring purposes.
