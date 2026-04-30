import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
def load_model():
    # Fixed filename to match your exact file: 30aprilmodel.pkl
    with open('30aprilmodel.pkl', 'rb') as file:
        return pickle.load(file)

# Initialize the model
model = load_model()

st.set_page_config(page_title="Taxi Fare Predictor", page_icon="🚖")
st.title("🚖 Trip Fare Predictor")
st.write("Enter the trip details below to estimate the fare.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    trip_distance = st.number_input("Trip Distance (km)", min_value=0.0, value=5.0)
    time_of_day = st.selectbox("Time of Day (0-23)", options=list(range(24)))
    day_of_week = st.selectbox("Day of Week (0=Mon, 6=Sun)", options=list(range(7)))
    passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)
    traffic = st.slider("Traffic Conditions (1=Low, 3=High)", 1, 3, 2)

with col2:
    weather = st.slider("Weather (1=Clear, 3=Stormy)", 1, 3, 1)
    base_fare = st.number_input("Base Fare", min_value=0.0, value=2.5)
    km_rate = st.number_input("Per Km Rate", min_value=0.0, value=1.5)
    min_rate = st.number_input("Per Minute Rate", min_value=0.0, value=0.2)
    duration = st.number_input("Trip Duration (Minutes)", min_value=1, value=15)

# Prediction Logic
if st.button("Predict Fare"):
    # Prepare the input data in the exact order the model expects
    input_data = pd.DataFrame([[
        trip_distance, time_of_day, day_of_week, passenger_count,
        traffic, weather, base_fare, km_rate, min_rate, duration
    ]], columns=[
        'Trip_Distance_km', 'Time_of_Day', 'Day_of_Week', 'Passenger_Count',
        'Traffic_Conditions', 'Weather', 'Base_Fare', 'Per_Km_Rate',
        'Per_Minute_Rate', 'Trip_Duration_Minutes'
    ])
    
    # Generate prediction
    prediction = model.predict(input_data)
    
    # FIXED: Added [0] to extract the value from the array and fixed indentation
    st.success(f"### Estimated Fare: ${prediction[0]:.2f}")
