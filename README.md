Python code which uses which use requests and pyautogui to access data from different websites.

Requests is used to connect with website API and ask for weather data from certain date up to specified date.

Pyautogui has been used for a website where, no API connection or parsing html could have been used for easy access to data.
Instead, website had a button which allowed to download data for that specific day. Code loops the website through all of the days,
and presses the button which is always located in the same place. This is faster than pyautogui.locateOnScreen but also less safe.

For situations where button could be anywhere on the screen, pyautogui.locateOnScreen should be used.
