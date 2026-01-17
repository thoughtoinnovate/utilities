#!/bin/bash

# Run Python keep_awake script
echo "Starting mouse mover to prevent sleep..."
python3 keep_awake.py &

# Wait for user to stop the script (Ctrl+C)
wait $!

echo "Mouse mover stopped."
