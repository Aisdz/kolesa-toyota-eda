# 🚗 Toyota price predictor — Kolesa.kz

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![BeautifulSoup](https://img.shields.io/badge/Scraping-BeautifulSoup4-orange.svg)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-red.svg)
![Streamlit](https://img.shields.io/badge/App-Streamlit-FF4B4B.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

End-to-end pipeline: scraping Toyota listings from [Kolesa.kz](https://kolesa.kz) → EDA → ML price prediction → Streamlit web app.

---

## 📊 Results

| Model | MAE (KZT) | R² |
|---|---|---|
| Linear Regression | 3,840,263 | 0.6373 |
| Random Forest | 1,451,027 | 0.9412 |
| **XGBoost** | **1,337,178** | **0.9498** |

> Best model: **XGBoost** - mean prediction error ~1.3M KZT ($2,700) on a 20% validation set.

### Feature importance (XGBoost)
<img width="731" height="453" alt="Screenshot 2026-05-14 at 14 56 42" src="https://github.com/user-attachments/assets/48b7b637-6b4b-4c53-a1a2-ba3152aea2bd" />

| Rank | Feature | Note |
|---|---|---|
| 1 | Year | Newer = more expensive |
| 2 | Engine_Liter | Bigger engine = higher price |
| 3 | Model | Land Cruiser vs Corolla matters |
| 4 | Location | Minor effect - prices similar across KZ |

---

## Project overview

Kolesa.kz is Kazakhstan's largest car marketplace. This project scrapes 13,300+ Toyota listings, cleans and explores the data, trains a price prediction model, and serves it through a Streamlit app.

---

## Pipeline

```
Kolesa.kz (500+ pages)
        ↓
  Web scraping
  (requests + BeautifulSoup, retry logic, sleep between pages)
        ↓
  Data cleaning
  (drop duplicates, remove placeholder prices < 100,000 KZT)
        ↓
  EDA
  (price distribution, price vs age/engine, top models, city distribution)
        ↓
  Feature engineering
  (LabelEncoding for Model + Location, Car_Age)
        ↓
  Model training
  (LinearRegression, RandomForest, XGBoost — 80/20 val split)
        ↓
  Streamlit app
  (select model, year, engine, city → predicted price)
```

---

## ⚠️ Limitations

The model is missing several features that likely affect price in the real market:

- **Mileage** - not available on listing pages during scraping; probably the strongest missing predictor
- **Color** - minor effect but present
- **Steering side** - right-hand drive affects price in KZ
- **Condition / accident history** - not structured on Kolesa

As a result, predictions are a reasonable estimate but not a precise valuation tool.

---

## Dataset

| Column | Description |
|---|---|
| `Model` | Toyota model name |
| `Price` | Listing price in KZT |
| `Location` | City of the seller |
| `Year` | Manufacturing year |
| `Engine_Liter` | Engine displacement in liters |
| `Car_Age` | Computed: `2025 - Year` |

> 13,300 listings scraped. After cleaning: 13,292 rows.

---

## How to Run

### 1. Clone the repo

```bash
git clone https://github.com/Aisdz/kolesa-toyota-price-prediction
cd kolesa-toyota-price-prediction
```

### 2. Install dependencies

```bash
pip install requests beautifulsoup4 pandas numpy matplotlib seaborn xgboost scikit-learn streamlit
```

### 3. Scrape the data / Use ready dataset

Run `kolesa_scraped.ipynb` — generates `toyota_data.csv`.

> ⚠️ Scraping 500+ pages takes time. Dataset is already uploaded in repository (toyota_data.csv)

### 4. Train the model

Run `kolesa_ml.ipynb` - generates `xgboost_model.pkl`, `le_model.pkl`, `le_location.pkl`, `models_list.json`, `locations_list.json`.

### 5. Launch the app

```bash
streamlit run kolesa_app.py
```

Opens at `http://localhost:8501`

---

## 📁 Project Structure

```
├── kolesa_scraping.ipynb   # Scraping + cleaning + EDA
├── kolesa_ml.ipynb        # Feature engineering + model training
├── kolesa_app.py          # Streamlit web app
├── toyota_data.csv        # Scraped dataset(13,292 rows)
└── README.md
```

> `*.pkl`, `*.json` are not tracked by git - generated locally by running the notebooks.
