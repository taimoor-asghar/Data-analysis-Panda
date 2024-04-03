import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('Orignal Sleep.csv')
print(df)

profile = ProfileReport(df)
profile.to_file(output_file="Questionnaire2.html")