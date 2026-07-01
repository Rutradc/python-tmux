#!/bin/sh

tmux new-session -d -s app "python /app/main.py"

tail -f /dev/null