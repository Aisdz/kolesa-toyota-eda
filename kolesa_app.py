import streamlit as st
import pickle
import json
import numpy as np

# page config
st.set_page_config(
    page_title="Toyota Price Predictor",
    page_icon="🚗",
    layout="centered"
)

#  load artifacts 
@st.cache_resource
def load_artifacts():
    with open('xgboost_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('le_model.pkl', 'rb') as f:
        le_model = pickle.load(f)
    with open('le_location.pkl', 'rb') as f:
        le_location = pickle.load(f)
    with open('models_list.json', encoding='utf-8') as f:
        models_list = json.load(f)
    with open('locations_list.json', encoding='utf-8') as f:
        locations_list = json.load(f)
    return model, le_model, le_location, models_list, locations_list

model, le_model, le_location, models_list, locations_list = load_artifacts()

#  ui -----
st.title("🚗 Toyota Price Predictor")
st.markdown("Предсказание цены Toyota по данным с **Kolesa.kz**")
st.divider()

col1, col2 = st.columns(2)

with col1:
    car_model = st.selectbox("Модель", models_list)
    year = st.slider("Год выпуска", min_value=1983, max_value=2025, value=2015)

with col2:
    location = st.selectbox("Город", locations_list)
    engine = st.selectbox("Объём двигателя (л)", sorted([1.0, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2,
                                                          2.4, 2.5, 2.7, 3.0, 3.5, 4.0, 4.6, 5.7]))

st.divider()

if st.button("Предсказать цену", use_container_width=True, type="primary"):
    car_age = 2025 - year

    try:
        model_enc = le_model.transform([car_model])[0]
        location_enc = le_location.transform([location])[0]
    except ValueError as e:
        st.error(f"Ошибка кодирования: {e}")
        st.stop()

    X_input = np.array([[model_enc, location_enc, year, engine, car_age]])
    price = model.predict(X_input)[0]

    st.success(f"### 💰 Predicted Price: {price:,.0f} KZT")
    st.caption(f"≈ ${price / 480:,.0f} USD  •  {car_model} {year}  •  {engine}L  •  {location}")