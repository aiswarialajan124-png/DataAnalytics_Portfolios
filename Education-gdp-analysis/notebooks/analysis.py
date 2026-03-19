import pandas as pd

file_path = "../data/P_Data_Extract_From_World_Development_Indicators (1).xlsx"

df = pd.read_excel(file_path)
print(df.head())

print(df["Series Name"].unique())