# Titanic Exploratory Data Analysis (EDA)

This repository contains a comprehensive exploratory data analysis of the Titanic disaster dataset, focusing on survival patterns, passenger demographics, and key factors affecting survival rates.

## Overview

The script `titanic_eda_fixed.py` performs detailed analysis of the Titanic passenger dataset to uncover insights about survival patterns, passenger characteristics, and the factors that influenced survival during the disaster.

## Features

- **Data Cleaning**: Handles missing values and data inconsistencies
- **Survival Analysis**: Comprehensive analysis of survival rates across different demographics
- **Passenger Demographics**: Age, gender, class, and family relationships analysis
- **Feature Engineering**: Creates new features for deeper insights
- **Visualizations**: Multiple charts and graphs for data exploration
- **Statistical Analysis**: Correlation analysis and statistical significance testing

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- scipy

## Installation

```bash
pip install pandas numpy matplotlib seaborn scipy
```

## Usage

Run the analysis script:

```bash
python titanic_eda_fixed.py
```

## Analysis Components

### 1. Data Overview
- Dataset shape and structure
- Missing value analysis
- Data type verification
- Basic statistics summary

### 2. Passenger Demographics
- **Age Distribution**: Analysis across age groups
- **Gender Distribution**: Male vs female passenger ratios
- **Class Distribution**: First, second, and third class passenger analysis
- **Embarkation Points**: Southampton, Cherbourg, and Queenstown analysis

### 3. Survival Analysis
- **Overall Survival Rate**: Total survival statistics
- **Gender-based Survival**: Survival rates by gender
- **Class-based Survival**: Survival rates by passenger class
- **Age-based Survival**: Survival patterns across age groups
- **Family-based Survival**: Impact of family size on survival

### 4. Feature Engineering
- **Family Size**: Combined siblings/spouses and parents/children
- **Is Alone**: Binary feature indicating solo travelers
- **Title Extraction**: Extracted titles from names
- **Age Groups**: Categorized age ranges
- **Fare Groups**: Categorized fare ranges

### 5. Visualizations
- **Survival Count Plots**: Overall survival visualization
- **Gender-based Survival**: Male vs female survival rates
- **Class-based Survival**: Survival by passenger class
- **Age Distribution**: Age histograms with survival overlay
- **Correlation Heatmap**: Feature correlation analysis
- **Family Size Impact**: Survival rates by family size

## Key Findings

### Survival Rates by Demographics:
- **Gender**: Females had significantly higher survival rates (74%) compared to males (19%)
- **Class**: First-class passengers had highest survival rates (63%), followed by second-class (47%), and third-class (24%)
- **Age**: Children had better survival rates, while elderly passengers had lower survival rates
- **Family Size**: Passengers with 1-3 family members had better survival rates than solo travelers or large families

### Statistical Insights:
- **Gender** was the strongest predictor of survival
- **Passenger class** showed clear correlation with survival
- **Age** showed moderate correlation with survival
- **Fare** showed positive correlation with survival (higher fare = better survival)

## Data Sources

- **Primary Dataset**: Titanic passenger dataset (commonly available as train.csv)
- **Format**: CSV with 891 passenger records
- **Features**: 12 columns including passenger demographics, ticket information, and survival status

## Technical Details

- **Language**: Python 3.x
- **Libraries**: pandas, numpy, matplotlib, seaborn, scipy
- **Analysis Type**: Exploratory Data Analysis (EDA)
- **Visualization**: Matplotlib and Seaborn
- **Statistical Testing**: Chi-square tests and correlation analysis

## File Structure

```
titanic_eda_fixed.py    # Main analysis script
README_TITANIC_EDA.md   # This documentation
```

## Output

The script generates:
1. **Console Output**: Statistical summaries and key findings
2. **Visualizations**: Multiple plots saved as PNG files
3. **Data Insights**: Detailed analysis results printed to console
4. **Cleaned Dataset**: Processed dataset ready for machine learning

## Usage Example

```python
# Run the complete analysis
python titanic_eda_fixed.py

# The script will:
# 1. Load and clean the data
# 2. Generate comprehensive visualizations
# 3. Print statistical summaries
# 4. Display key insights and findings
```

## License

This analysis uses the Titanic dataset which is publicly available for educational and research purposes. The dataset is commonly used for machine learning competitions and educational purposes.
