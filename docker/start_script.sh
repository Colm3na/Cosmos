#!/bin/bash
# Start the first process
tmux new-session -s "gaiad" -d -n "main"
tmux send-keys -t "gaiad:main" C-z 'gaiad start' Enter
tmux split-window -v
tmux select-pane -t 1
tmux send-keys "cd /usr/src/app/lunie && npm run serve" C-m
