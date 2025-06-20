#!/bin/bash

# Name of the screen session
SESSION_NAME="unifi_gaurdian"

# Command to run inside the screen
COMMAND="python3 apget.py"  # Replace with your desired command

# Start a detached screen session and run the command
screen -dmS "$SESSION_NAME" bash -c "$COMMAND"
