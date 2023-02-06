import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rains.append(rain)

    # Plot the rainfall.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, rains, c='blue')

    # Format plot.
    plt.title("Daily rainfall amounts in 2018, Sitka", fontsize=26)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Rainfall amounts (mm)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
