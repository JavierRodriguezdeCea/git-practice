# Supermarket Price Comparison

This project analyzes product prices across three Spanish supermarkets (Eroski, Dia, and Alcampo) to identify which store offers the lowest prices.

## Project Overview

Using web scraping and APIs, we gathered pricing data for various products across the three supermarkets. Our Python code allows you to search for any product, returning a dataframe with that product's prices across stores. We further analyzed a sample of 10 products to identify the supermarket with the most frequent lowest prices and created a heatmap to visualize the price distribution.

## Workflow

1. **Data Extraction**:
   - Used web scraping and APIs to collect product data, including names, prices, and package sizes, from each supermarket’s website.

2. **Data Cleaning & Transformation**:
   - Utilized `replace`, `strip`, and `str.contains` to standardize product data and remove irrelevant items.
   - Aggregated and sorted product data using `concat` and `sort_values` for each store to prepare for analysis.

3. **Analysis & Visualization**:
   - Calculated average prices per supermarket with `groupby` and `mean`.
   - Used `value_counts` to identify the store with the lowest prices most frequently.
   - Visualized the results through a bar chart and a price heatmap for a clear comparison across products and stores.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your_user/supermarket-price-comparison.git
   cd supermarket-price-comparison
   ```

2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main analysis script to retrieve prices and generate visualizations. Adjust the search parameters to analyze the price distribution of any desired product across the supermarkets.

## Technologies Used

- **Python** for data analysis and processing.
- **Pandas** for data cleaning and transformation.
- **Matplotlib & Seaborn** for data visualization.
- **Web Scraping & APIs** for data extraction from the supermarkets.
