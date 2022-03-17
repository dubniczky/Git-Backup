#!/bin/bash

SCRIPT_PATH="/etc/gitbackup/main.py"


# Install cron job
sudo cat >> /etc/crontab << EOF!

# Git auto backup script (runs every friday midnigt)
0 0 * * 5 root $SCRIPT_PATH
EOF!

chmod +x "$SCRIPT_PATH"