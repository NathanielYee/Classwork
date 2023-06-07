import pandas as pd
import matplotlib.pyplot as plt


CHERRY = "cherry.csv"

def main():
    # Read in
    cherry = pd.read_csv(CHERRY)

    # Parse and Edit Data using forward fill
    cherry['DOY'] = cherry['FLOWERING_DOY'].fillna(method='ffill')

    # Create new variable without missing values
    cherry = cherry.dropna()
    lst = list(cherry.FLOWERING_DOY)

    # Print Check
    print(lst)

    # Compute moving averages
    cherry['MA_10'] = cherry['DOY'].rolling(window=10, center=True, min_periods=1).mean()
    cherry['MA_100'] = cherry['DOY'].rolling(window=100, center=True, min_periods=1).mean()

    # Plotting
    plt.figure(figsize=(8,6), dpi=200)
    plt.plot(cherry.YEAR, cherry.MA_10, color='blue', label='10-year Moving Average')
    plt.plot(cherry.YEAR, cherry.MA_100, color='red', label='100-year Moving Average')
    plt.scatter(cherry.YEAR, cherry.DOY, color = '#FF66B2')
    plt.yticks([80, 90, 100, 110, 120], ['Mar 21', 'Mar 31', 'Apr 10', 'Apr 20', 'Apr 30'])
    plt.grid()
    plt.xlabel("Year")
    plt.ylabel("Day of Year")
    plt.legend(prop={'size': 5})
    plt.title("Cherry Blossom Dates In Kyoto, Japan")
    plt.show()

main()