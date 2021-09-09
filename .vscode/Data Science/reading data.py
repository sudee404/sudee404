import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")

df.drop('state', axis=1, inplace=True)

df["month"]=pd.to_datetime(df["date"],format="%d.%m.%y").dt.month_name()

df.set_index('date', inplace=True)


print(df["cases"].describe())