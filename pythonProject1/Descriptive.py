import pandas as pd
import numpy as np

# Load your dataset from a CSV file
df = pd.read_csv("Extreme Refined Sleep.csv")

# Get summary statistics using Pandas and convert to HTML
summary_stats_html = df.describe().to_html()

# Calculate the mean, median, standard deviation, and variance for each column
mean = df.mean()
median = df.median()
std_dev = df.std()
variance = df.var()

# Convert the calculated statistics to a DataFrame
calculated_stats_df = pd.DataFrame({
    'Mean': mean,
    'Median': median,
    'Standard Deviation': std_dev,
    'Variance': variance
})

# Convert the DataFrame to HTML
calculated_stats_html = calculated_stats_df.to_html()

# Write the HTML output to a file
with open("statistics.html", "w") as file:
    file.write(summary_stats_html)
    file.write(calculated_stats_html)
