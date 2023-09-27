import requests
import pandas as pd
import calendar

year = 2018
month = 1
switch = False

while year <= 2022:
    while month <= 12:
        monthRange = calendar.monthrange(year, month)
        if month < 10:
            month2 = f'0{month}'
        else:
            month2 = month
        day = monthRange[1]

        url = f'https://api.weather.com/v1/location/EPGD:9:PL/observations/historical.json?apiKey=e1f10a1e78da46f5b10a1e78da96f525&units=m&startDate={year}{month2}01&endDate={year}{month2}{day}'

        payload = {}
        headers = {
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://www.wunderground.com/',
            'DNT': '1',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
            'sec-ch-ua-platform': '"Windows"'
        }

        r = requests.get(url, headers=headers)

        weatherdata = r.json()

        if switch == True:
            df = pd.concat([df, pd.json_normalize(weatherdata['observations'])], axis=0)
        else:
            df = pd.json_normalize(weatherdata['observations'])

        switch = True

        print(df)

        month = month + 1

    year = year + 1
    month = 1

df.to_csv('WeatherData.csv', index=False)
print('Data download finished')


