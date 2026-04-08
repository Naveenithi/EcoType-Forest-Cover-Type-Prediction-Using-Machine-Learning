import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load files
model = joblib.load('forest_cover_model.pkl')
encoder = joblib.load('target_encoder.pkl')
features = joblib.load('model_features.pkl')

st.title("🌲 EcoType: Forest Cover Type Prediction")

st.write("Enter the environmental parameters below:")

# Input fields
Elevation = st.number_input("Elevation", value=2500)
Aspect = st.number_input("Aspect", value=100)
Slope = st.number_input("Slope", value=10)

Horizontal_Distance_To_Hydrology = st.number_input("Horizontal Distance to Hydrology", value=100)
Vertical_Distance_To_Hydrology = st.number_input("Vertical Distance to Hydrology", value=10)

Horizontal_Distance_To_Roadways = st.number_input("Distance to Roadways", value=500)

Hillshade_9am = st.number_input("Hillshade 9am", value=200)
Hillshade_Noon = st.number_input("Hillshade Noon", value=220)
Hillshade_3pm = st.number_input("Hillshade 3pm", value=150)

Horizontal_Distance_To_Fire_Points = st.number_input("Distance to Fire Points", value=1000)

Wilderness_Area = st.number_input("Wilderness Area (numeric)", value=0)
Soil_Type = st.number_input("Soil Type (numeric)", value=10)

# Feature Engineering (same as training)
Hydrology_Ratio = Horizontal_Distance_To_Hydrology / (abs(Vertical_Distance_To_Hydrology) + 1)
Road_Fire_Ratio = Horizontal_Distance_To_Roadways / (Horizontal_Distance_To_Fire_Points + 1)
Hillshade_Diff_1 = Hillshade_9am - Hillshade_Noon
Hillshade_Diff_2 = Hillshade_Noon - Hillshade_3pm
Elevation_Slope = Elevation * Slope

# Create input dataframe
input_data = pd.DataFrame([{
    'Elevation': Elevation,
    'Aspect': Aspect,
    'Slope': Slope,
    'Horizontal_Distance_To_Hydrology': Horizontal_Distance_To_Hydrology,
    'Vertical_Distance_To_Hydrology': Vertical_Distance_To_Hydrology,
    'Horizontal_Distance_To_Roadways': Horizontal_Distance_To_Roadways,
    'Hillshade_9am': Hillshade_9am,
    'Hillshade_Noon': Hillshade_Noon,
    'Hillshade_3pm': Hillshade_3pm,
    'Horizontal_Distance_To_Fire_Points': Horizontal_Distance_To_Fire_Points,
    'Wilderness_Area': Wilderness_Area,
    'Soil_Type': Soil_Type,
    'Hydrology_Ratio': Hydrology_Ratio,
    'Road_Fire_Ratio': Road_Fire_Ratio,
    'Hillshade_Diff_1': Hillshade_Diff_1,
    'Hillshade_Diff_2': Hillshade_Diff_2,
    'Elevation_Slope': Elevation_Slope
}])

# Align columns
input_data = input_data.reindex(columns=features, fill_value=0)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    result = encoder.inverse_transform(prediction)

    st.success(f"🌳 Predicted Forest Cover Type: {result[0]}")