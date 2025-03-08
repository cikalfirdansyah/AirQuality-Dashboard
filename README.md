<<<<<<< HEAD
# AirQuality-Dashboard
=======
# Air Quality Analysis Dashboard

This project provides an interactive Streamlit dashboard to visualize and analyze air quality data. The dashboard uses data from multiple air quality stations, allowing users to explore key air pollutants, view statistical insights, and filter the data based on specific date ranges and pollutants.

## Project Structure

The directory structure is as follows:
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt


## Overview

This project uses air quality data from two stations (Guanyuan and Wanshouxigong) to analyze key pollutants, such as PM2.5, PM10, NO2, SO2, CO, and O3. The data is processed and visualized using various techniques, including statistical analysis and interactive plots. The primary goal of the dashboard is to allow users to interact with the data by selecting different pollutants and viewing the corresponding trends.

### Key Features

- **Data Filtering**: Allows users to filter the data by date range and pollutants.
- **Visualizations**: Includes line charts and boxplots for analyzing trends in air quality and comparing pollutant levels.
- **Descriptive Statistics**: Displays summary statistics for the pollutants, including mean, median, standard deviation, and more.
- **Station Comparison**: Compares the air quality data from two stations to understand regional differences in pollution levels.

## Requirements

The project requires the following Python libraries:

- **Pandas**: For data manipulation and analysis.
- **Streamlit**: For creating the interactive dashboard.
- **Matplotlib**: For data visualization.
- **Seaborn**: For additional advanced visualizations.
- **Numpy**: For numerical operations.
- **Plotly**: For interactive plots (if used).

You can install the required dependencies using:

```bash
pip install -r requirements.txt
>>>>>>> df8caeb (First commit)
