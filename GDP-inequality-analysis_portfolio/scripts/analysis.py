import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/cleaned_data.csv")
print(df["Series Name"].unique())

# Seperate economic indicators
gdp_growth = df[df["Series Name"] == "GDP growth (annual %)"]
gdp_pc = df[df["Series Name"] == "GDP per capita (current US $)"]
population = df[df["Series Name"] == "Population, total"]
gini = df[df["Series Name"] == "Gini index"]

# merge GDP Growth and Gini (inequality)
merged = pd.merge(
    gdp_growth,
    gini,
    on=["Country Name", "Country Code", "Year"],
    suffixes=("_gdp", "_gini")
)
# Add GDP per capita
gdp_pc = gdp_pc[["Country Name", "Year", "Value"]]
gdp_pc = gdp_pc.rename(columns={"Value": "gdp_pc"})

merged = merged.merge(
    gdp_pc,
    on=["Country Name", "Year"]
)
# Add population
population = population[["Country Name", "Year", "Value"]]
population = population.rename(columns={"Value": "population"})

merged = merged.merge(
    population,
    on=["Country Name", "Year"]
)
# Classify countries (developed vs developing)
merged["Country Type"] = merged["gdp_pc"].apply(
    lambda x: "Developed" if x > 20000 else "Developing"
)
# Correlation analysis
correlation = merged["Value_gdp"].corr(merged["Value_gini"])
print("Correlation between GDP growth and inequality:", correlation)


# Chart 1: GDP Growth vs Inequality
plt.figure()

sns.scatterplot(
    data=merged,
    x="Value_gdp",
    y="Value_gini",
    hue="Country Type"
)

plt.title("GDP Growth vs Income Inequality")
plt.xlabel("GDP Growth (%)")
plt.ylabel("Gini Index")

plt.savefig("../charts/gdp_vs_inequality.png")
plt.close()

# Chart 2: Correlation Heatmap
plt.figure()

sns.heatmap(
    merged[["Value_gdp", "Value_gini", "gdp_pc"]].corr(),
    annot=True
)
plt.title("Economic Indicator Correlation")

plt.savefig("../charts/correlation_heatmap.png")
plt.close()

# Chart 3: Global inequality trend
trend = merged.groupby("Year")["Value_gini"].mean()

plt.figure()

trend.plot()

plt.title("Global Income Inequality Trend")
plt.xlabel("Year")
plt.ylabel("Average Gini Index")

plt.savefig("../charts/global_inequality_trend.png")
plt.close()

# Chart 4: Developed vs Developing Growth
plt.figure()

sns.boxplot(
    data=merged,
    x="Country Type",
    y="Value_gdp"
)
plt.title("GDP Growth: Developed vs Developing Countries")

plt.savefig("../charts/growth_comparison.png")
plt.close()

# Chart 5: Developed vs Developing countries
trend = merged.groupby(["Year","Country Type"])["Value_gini"].mean().reset_index()

plt.figure()

sns.lineplot(
    data=trend,
    x="Year",
    y="Value_gini",
    hue="Country Type"
)

plt.title("Inequality Trends: Developed vs Developing Countries")
plt.xlabel("Year")
plt.ylabel("Average Gini Index")

plt.savefig("../charts/inequality_by_country_type.png")