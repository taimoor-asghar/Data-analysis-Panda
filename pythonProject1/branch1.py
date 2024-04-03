# Import the necessary libraries
from tableone import TableOne
import pandas as pd

# Load your data into a pandas DataFrame (replace 'Formula Sleep.csv' with your actual dataset)
df = pd.read_csv('Extreme Refined Sleep.csv')

# Create the TableOne object
table = TableOne(df)

# Display the table in HTML format
html_table = table.tabulate(tablefmt='html')
print(html_table)

# Save the HTML table to a file
with open('tableone_output.html', 'w') as f:
    f.write(html_table)

# Print a success message
print("TableOne summary statistics have been generated and saved as an HTML file.")
