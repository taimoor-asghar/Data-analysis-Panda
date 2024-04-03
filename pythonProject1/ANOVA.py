import pandas as pd
from scipy.stats import f_oneway

# Load your dataset
df = pd.read_csv("Extreme Refined Sleep.csv")  # Replace "your_dataset.csv" with the actual path to your dataset

# Perform ANOVA
f_statistic, p_value = f_oneway(
    df[df['Gender'] == 1]['Global PSQI Score'],
    df[df['Gender'] == 2]['Global PSQI Score']
)

# Format results as HTML
html_output = f"<h2>ANOVA Results:</h2>"
html_output += f"<p>F-statistic: {f_statistic}</p>"
html_output += f"<p>p-value: {p_value}</p>"

# Write HTML output to a file
with open("anova_results_Gender.html", "w") as file:
    file.write(html_output)

print("ANOVA results saved to anova_results.html")
