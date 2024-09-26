import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
# Load the data
def load_data():
    df = pd.read_csv("epa-sea-level.csv")
    return df

# Create the scatter plot and fit lines
def create_plot():
    # Load the data
    df = load_data()

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')

    # Fit a line to the entire dataset
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # Years from 1880 to 2050
    sea_level_pred_extended = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_pred_extended, color='red', label='Best Fit Line (All Data)')

    # Fit a line to data from 2000 onward
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    sea_level_pred_recent = slope_recent * years_extended + intercept_recent
    plt.plot(years_extended, sea_level_pred_recent, color='green', label='Best Fit Line (2000+)')

    # Customize the plot
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.legend()
    plt.grid()
    plt.xlim(1880, 2050)
    plt.tight_layout()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()