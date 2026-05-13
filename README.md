# 🚗 Toyota Cars — Web scraping & EDA (Kolesa.kz)

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/Scraping-BeautifulSoup4-orange.svg)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458.svg)
![Plotly](https://img.shields.io/badge/Viz-Plotly-3F4F75.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

End-to-end pipeline: scraping Toyota car listings from [Kolesa.kz](https://kolesa.kz), cleaning the data, and exploring it through visualizations.

---

## 📌 Project Overview

Kolesa.kz is Kazakhstan's largest car marketplace. This project scrapes 500+ pages of Toyota listings, builds a structured dataset, and performs exploratory data analysis to uncover pricing trends, popular models, and regional distribution.

---

## 📦 Dataset

| Column | Description |
|---|---|
| `Car` | Full car name (brand + model + trim) |
| `Model` | Extracted model name |
| `Brand` | Always Toyota in this dataset |
| `Price` | Listing price in KZT (Tenge) |
| `Location` | City of the seller |
| `Year` | Manufacturing year |
| `Engine_Liter` | Engine displacement in liters |
| `Car_Age` | Computed: `2025 - Year` |

> Dataset is saved as `toyota_data.csv` after scraping.

---

##  Pipeline

```
Kolesa.kz (500+ pages)
        ↓
  Web Scraping
  (requests + BeautifulSoup, User-Agent headers, retry logic, sleep between pages)
        ↓
  DataFrame Construction
  (pandas, feature extraction: Model, Brand, Car_Age)
        ↓
  Data Cleaning
  (drop nulls, remove duplicates, round Engine_Liter)
        ↓
  EDA & Visualization
  (matplotlib, seaborn, plotly)
        ↓
  toyota_data.csv
```

---

## 📊 Visualizations

| Chart | Description |
|---|---|
| Price distribution | Histogram + KDE — how prices are spread |
| Price vs Car Age | Scatter — does older mean cheaper? |
| Engine Size vs Price | Scatter — bigger engine = higher price? |
| Car Age distribution | Histogram — what years dominate the market |
| Top 10 models by avg price | Bar chart — most expensive Toyota models |
| Cars by year | Bar chart — which production years are most common |
| Avg price by year | Line chart — price trend over manufacturing years |
| Year × Price × Engine (Bubble) | Bubble chart — three variables at once |
| Correlation heatmap | Seaborn heatmap — Price / Year / Engine_Liter |
| Cars by city (Interactive map) | Plotly map — geographic distribution across Kazakhstan |

---

##  How to Run

### 1. Install dependencies

```bash
pip install requests beautifulsoup4 pandas matplotlib seaborn plotly
```

### 2. Run the notebook

```bash
jupyter notebook kolesa_scraped.ipynb
```

> ⚠️ Scraping 500+ pages takes time. The notebook uses `time.sleep()` between requests to avoid getting blocked. Don't reduce the delay.

---

## 📁 Project Structure

```
├── kolesa_scraped.ipynb   # Full pipeline: scraping + cleaning + EDA
├── toyota_data.csv        # Scraped and cleaned dataset (generated)
└── README.md
```
<img width="857" height="289" alt="Screenshot 2026-05-04 at 17 17 42" src="https://github.com/user-attachments/assets/4d5cb69b-f0cc-4251-868c-dd76cc9c0b21" />
   ...
   VS code doesn't show the output of this visualization, anyway, I decided to upload it.
