import matplotlib.pyplot as plt
import pandas as pd


def graph():
    '''reads data from csv file to plot graph'''

    df = pd.read_csv('wildfires.csv', delimiter=',')

    plt.plot(df['Year'], df['Low'], color='limegreen')
    plt.plot(df['Year'], df['Moderate'], color='green')
    plt.plot(df['Year'], df['High'], color='orange')
    plt.plot(df['Year'], df['Unburned'], color='yellow')
    plt.plot(df['Year'], df['Increased greenness'], color='red')

    plt.fill_between(df['Year'], df['Low'], facecolor='limegreen')
    plt.fill_between(df['Year'], df['Moderate'], facecolor='green')
    plt.fill_between(df['Year'], df['High'], facecolor='orange')
    plt.fill_between(df['Year'], df['Unburned'], facecolor='yellow')
    plt.fill_between(df['Year'], df['Increased greenness'], facecolor='red')

    plt.title(
        'Data showing areas of forested land burned over the years', loc='center')
    plt.ylabel('Areas burned (million acres)')
    plt.xlabel('Year')
    plt.show()
    plt.close()


# running to plot my environmental dataset
if __name__ == "__main__":
    graph()
