import pyautogui
import time
import calendar
import keyboard

while True:
    if keyboard.is_pressed("left alt"):
        print(pyautogui.position())
        time.sleep(0.1)
    if keyboard.is_pressed("esc"):
        break

year = 2016
month = 8
i = 1
kto = 15 #numer ID instalacji fotowoltaiczej

while year < 2018:
    while month <= 12:
        monthRange = calendar.monthrange(year, month)
        if month < 10:
            month2 = f'0{month}'
        else:
            month2 = month
        day = monthRange[1]
        while i <= day:
            if keyboard.is_pressed("left alt"):
                break
            url = f'https://pvmonitor.pl//i_user.php?idinst={kto}&od={year}-{month2}-{i}&do={year}-{month2}-{i}#/pv3'
            pyautogui.click(346, 51)
            pyautogui.typewrite(url)
            pyautogui.press('enter')
            time.sleep(6)
            if keyboard.is_pressed("left alt"):
                break
            pyautogui.click(1346, 477)
            time.sleep(1)
            if keyboard.is_pressed("left alt"):
                break
            pyautogui.click(1286, 666)
            time.sleep(2)
            if keyboard.is_pressed("left alt"):
                break
            i = i + 1
        month = month + 1
        i = 1
    year = year + 1
    month = 1