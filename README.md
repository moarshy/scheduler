# Scheduler Service Setup

## Poetry Setup
First, clone the repository and set up the Python environment using Poetry.

```bash
pip install poetry
git clone https://github.com/moarshy/scheduler.git
cd scheduler
poetry config virtualenvs.in-project true
poetry install
poetry env info
```
- After running poetry env info, note the Python executable path, e.g., /Users/arshath/play/insource/scheduler/.venv/bin/python.

## Systemd Service File Setup
Modify the insourcesch.service file according to your system and project configuration.

## Deploying the Systemd Service
`cp /Users/arshath/play/insource/scheduler/ops/systemd/insource_sch.service /etc/systemd/system/`

## Starting the Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now insource_sch.service
sudo systemctl status insource_sch.service

```

## Monitoring the Service with Journalctl

```
journalctl -u insource_sch.service # Logs from specific service
journalctl -f # Real-time logs
journalctl --since "YYYY-MM-DD HH:MM" # Logs since a specific time
journalctl --since "YYYY-MM-DD HH:MM" --until "YYYY-MM-DD HH:MM" # Logs between times
journalctl -n 100 # Last 100 lines of logs
journalctl -u insource_sch.service -f # Follow logs of a specific service

```
Replace insource_sch.service with your actual service name in the journalctl commands.