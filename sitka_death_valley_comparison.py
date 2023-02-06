import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename1 = 'data/death_valley_2018_simple.csv'
filename2 = 'data/sitka_weather_2018_simple.csv'
with open(filename1) as f1, open(filename2) as f2:
    reader1 = csv.reader(f1)
    header_row1 = next(reader1)

    reader2 = csv.reader(f2)
    header_row2 = next(reader2)

    for index, column_header in enumerate(header_row1):
        print(index, column_header)
    for index, column_header in enumerate(header_row2):
        print(index, column_header)

    # Get dates, and high and low temperatures from Death Valley file.
    dates_valley, highs_valley, lows_valley = [], [], []
    station_sit_name = ''
    for row in reader1:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_valley.append(current_date)
            highs_valley.append(high)
            lows_valley.append(low)
            station_sit_name = row[1]

    # Get dates, and high and low temperatures from Death Valley file.
    dates_sitka, highs_sitka, lows_sitka = [], [], []
    station_val_name = ''
    for row in reader2:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates_sitka.append(current_date)
            highs_sitka.append(high)
            lows_sitka.append(low)
            station_val_name = row[1]

    # Plot the high and low temperature.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates_valley, highs_valley, c='red', alpha=0.5)
    ax.plot(dates_valley, lows_valley, c='blue', alpha=0.5)
    plt.fill_between(dates_valley, highs_valley, lows_valley, facecolor='blue', alpha=0.1)
    ax.plot(dates_sitka, highs_sitka, c='red', alpha=0.5)
    ax.plot(dates_sitka, lows_sitka, c='blue', alpha=0.5)
    plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title(f"Daily high and low temperatures comparison - 2018, \n{station_val_name}, CA and {station_sit_name}", fontsize=20)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
