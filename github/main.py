import pandas as pd

df = pd.read_csv("github/survey_data.csv")
df.head()
df.isna().sum()
