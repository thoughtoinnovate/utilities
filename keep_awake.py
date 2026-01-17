#!/usr/bin/env python3

import pyautogui
import time

# Disable failsafe to allow mouse movement
pyautogui.FAILSAFE = False

def main():
    last_pos = pyautogui.position()
    pause_until = 0
    
    print("Keep awake script running...")
    
    try:
        while True:
            current_pos = pyautogui.position()
            current_time = time.time()
            
            # Check if mouse moved manually
            if current_pos != last_pos:
                pause_until = current_time + 30  # Pause for 30 seconds
                print(f"Mouse movement detected. Pausing auto-movement for 30 seconds...")
                last_pos = current_pos
            
            # Only move mouse if not in pause period
            if current_time > pause_until:
                pyautogui.move(50, 0)
                time.sleep(0.2)
                pyautogui.move(-50, 0)
                print("Mouse moved to keep system awake")
                last_pos = pyautogui.position()
            
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nScript stopped by user")

if __name__ == "__main__":
    main()
