import pandas as pd

# Load dataset
file_path  = "../data/P_Data_Extract_From_World_Development_Indicators.xlsx"
df = pd.read_excel(file_path)

# Convert wide format to long format
df_long = df.melt(
    id_vars=["Country Name", "Country Code", "Series Name", "Series Code"],
    var_name="Year",
    value_name="Value"
)

# Extract year number
df_long["Year"] = df_long["Year"].str.extract(r'(\d+)').astype(int)

# Replace missing values
df_long["Value"] = df_long["Value"].replace("..", pd.NA)

# Convert to numeric
df_long["Value"] = pd.to_numeric(df_long["Value"], errors="coerce")

# Drop missing values
df_long = df_long.dropna(subset=["Value"])

# Save cleaned data
df_long.to_csv("../data/cleaned_data.csv", index=False)

print("Data cleaning complete. File saved as cleaned_data.csv")