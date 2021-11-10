import pyautogui
import time
delay = .001
count = 0
message = str(input("Message:"))
time.sleep(2)


try:
    while True:
        pyautogui.write(message)
        pyautogui.press("enter")
        count += 1
        print("Count:", count)
        time.sleep(delay)


except KeyboardInterrupt:
    pass
