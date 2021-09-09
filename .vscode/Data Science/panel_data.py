#pandas
import pandas as pd
#creating dataframes with a dictionary
data = {
   'ages': [14, 18, 24, 42],
   'heights': [165, 180, 176, 184]
} 
#passing it to dataframe constructor
df = pd.DataFrame(data,index=["john","james","sudi","chief"])
print(df)
#accessing values using loc function
print(df.loc["sudi"])
print(df.heights)
print(df.ages)
print(df[["heights","ages"]])

#slicing
print(df.iloc[::-1])
#conditions
print(df[(df["ages"]>16)&(df["heights"]>150)])