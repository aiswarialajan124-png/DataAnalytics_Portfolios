# GDP Inequality Analysis Portfolio

## Research Question
This projetc investigates the relationship betweeen economic growth and income inequality across many countries.The goal is to analyse how GDP growth rates are associated with increases or decreases in income inequality, measured using the Gini index.

## Dataset
The analysis uses data from the World Bank World Development Indicators dataset.

The following indicators were selected:
- GDP growth (annual %) - measures the rate of economic expansion
- GDP per capita (current US$) - used to classify countries by level of development
- Population, total - included for contextual economic scale
- Gini index - measures income inequality within a country

The dataset was cleaned and reshaped from wide format into a long format to allow easier analysis and merging indicators.

## Methodology
The analysis was conducted using Python, primarily with the pandas,matplotlib, and seaborn libraries.

The workflow followed these steps:
1. Data Cleaning
   - Reshaped the dataset from wide format to long format.
   - Extracted year values from column names.
   - Converted values to numeric format.
   - Removed missing values.

2. Data Integration
   - Individual indicators were seperated into datasets.
   - GDP growth,Gini index,GDP per capita, and population were merged using:
        - Country Name
        - Country Code
        - Year

3. Country Classification
   - Countries were classified into two groups:
        - Developed economies (GDP per capita > $20,000)
        - Developing economies (GDP per capita ≤ $20,000)

4. Correlation Analysis
   - The relationship between GDP growth and inequality was measured using the Python correlation coefficient.

5. Visualisation
   - Several charts were created to explore patterns in the data:
      - GDP growth vs inequality scatterplot
      - Correlation heatmap
      - Global inequality trend
      - Growth comparison between developed and developing economies
      - Inequality trends by development level
      - Kuznets Curve test (GDP per capita vs inequality)

## Project Structure
GDP-inequality-analysis_portfolio/
|
|-- charts/
|    |-- correlation_heatmap.png
|    |-- gdp_vs_inequality.png
|    |-- global_inequality_trend.png
|    |-- growth_comparison.png
|    |-- inequality_by_country_type.png
|    |-- kuznets_curve_test.png
|
|-- data/
|   |-- P_Data_Extract_From_World_Development_Indcators.xlsx
|   |-- cleaned_data.csv
|   |-- final_analysis_dataset.csv
|
|-- scripts/
|   |-- analysis.py
|   |-- data_cleaning.py
|
|-- README.md
|-- requirements.txt

### Folder Description
charts/
All visualizations generated during the analysis process.

data/
Contains the raw dataset downloaded from the World Bank and the processed datasets used for analysis.

scripts/
Pythin scripts used to clean the data and perform the economic analysis.

requirements.txt
List of Python libraries required to run the project.

README.md
Documentation describing the project, methodology, and findings.

## Key Findings
1. 