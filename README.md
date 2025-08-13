# Population Analysis - India

This repository contains a Python script that analyzes India's population data using the World Bank's population dataset.

## Overview

The script connects to the World Bank population dataset (`API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv`) and performs comprehensive analysis of India's population trends from 1960 to 2024.

## Features

- **Data Loading**: Properly handles World Bank CSV format with metadata headers
- **Population Analysis**: Extracts and analyzes India's population data across 65 years
- **Visualizations**: Creates interactive charts showing population growth trends
- **Age Distribution**: Provides simulated age group analysis based on demographic patterns

## Requirements

- Python 3.x
- pandas
- matplotlib
- numpy

## Installation

```bash
pip install pandas matplotlib numpy
```

## Usage

Run the analysis script:

```bash
python population_analysis.py
```

## Output

The script generates:
1. **Population Growth Chart**: Line chart showing India's population from 1960-2024
2. **Age Distribution Chart**: Bar chart showing population by age groups for 2022
3. **Recent Population Data**: Exact population figures for 2022-2024

## Data Source

- **Dataset**: World Bank Population Data
- **File**: API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv
- **Coverage**: 266 countries, 1960-2024
- **Indicator**: Population, total (SP.POP.TOTL)

## Recent Population Figures

- **2022**: 1,412,175,872
- **2023**: 1,428,627,663
- **2024**: 1,445,186,361

## Visualization

The script creates two main visualizations:
1. **Time Series Plot**: Shows India's population growth trajectory over 64 years
2. **Demographic Chart**: Displays population distribution across age groups for 2022

## Technical Details

- **Language**: Python
- **Libraries**: pandas, matplotlib, numpy
- **Data Format**: CSV with 266 countries and 65 years of data
- **Processing**: Handles World Bank's metadata headers correctly

## License

This project uses World Bank data which is publicly available for research and educational purposes.
