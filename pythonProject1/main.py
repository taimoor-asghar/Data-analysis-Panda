import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('Formula Sleep.csv')

print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Formula Sleep 1.html")