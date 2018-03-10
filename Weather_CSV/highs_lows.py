import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs ,lows= [], [],[]
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

fig = plt.figure(dpi=240, figsize=(16, 9))

plt.plot(dates, highs, c='red',alpha = 1)
plt.plot(dates, lows, c='blue',alpha = 1)
plt.fill_between(dates,highs,lows,facecolor = 'green',alpha = 0.5)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()

plt.ylabel('Temperture(F)', fontsize=16)

plt.tick_params(axis='', which='major', labelsize=16)

plt.savefig('tem.png')
