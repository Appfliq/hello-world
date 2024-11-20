import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# File path for the dataset
file_path = r"C:\Users\mrakr\OneDrive\Official\Conestoga\Fall 2024\Week 12\crypto-23.csv"

# Check if file exists
if not os.path.exists(file_path):
    st.error(f"File not found: {file_path}. Please ensure the file is in the correct location.")
    st.stop()

# Load the dataset
crypto = pd.read_csv(file_path)

# Sidebar filters
st.sidebar.title("Crypto Dashboard Controls")
show_data = st.sidebar.checkbox("Show Raw Data")
selected_crypto = st.sidebar.multiselect(
    "Select Cryptocurrencies", options=["BTC", "ETH"], default=["BTC", "ETH"]
)
chart_type = st.sidebar.radio("Select Chart Type", ["Line Chart", "Bar Chart"])

# Slider for month range
months = crypto["Month"].tolist()
start_month, end_month = st.sidebar.slider(
    "Select Month Range", 0, len(months) - 1, (0, len(months) - 1)
)

# Display raw data if checkbox is selected
if show_data:
    st.write("### Crypto Data")
    st.dataframe(crypto)

# User input for adding a note
st.sidebar.title("Add a Note")
user_note = st.sidebar.text_input("Your note about this analysis:")
if user_note:
    st.sidebar.write(f"Your note: {user_note}")

# Form to capture user feedback
st.sidebar.title("Feedback")
with st.sidebar.form(key="feedback_form"):
    user_name = st.text_input("Your Name")
    feedback = st.text_area("Your Feedback")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.sidebar.success("Thank you for your feedback!")

# Main chart
st.title("📊 Crypto Dashboard")
st.write(f"Selected Months: {months[start_month]} to {months[end_month]}")

# Filter dataset by month range
filtered_data = crypto.iloc[start_month:end_month + 1]

# Create plot
fig, ax = plt.subplots()
if "BTC" in selected_crypto:
    if chart_type == "Line Chart":
        ax.plot(filtered_data["Month"], filtered_data["BTC"], label="BTC")
    else:
        ax.bar(filtered_data["Month"], filtered_data["BTC"], label="BTC")
if "ETH" in selected_crypto:
    if chart_type == "Line Chart":
        ax.plot(filtered_data["Month"], filtered_data["ETH"], label="ETH")
    else:
        ax.bar(filtered_data["Month"], filtered_data["ETH"], label="ETH")

ax.set_xlabel("Month")
ax.set_ylabel("Closing Value (USD)")
ax.set_title("BTC/ETH Performance")
ax.legend()

# Display plot
st.pyplot(fig)

# Add date input for future predictions (hypothetical)
st.sidebar.title("Future Prediction")
prediction_date = st.sidebar.date_input("Select a future date for prediction:")
if prediction_date:
    st.sidebar.write(f"Prediction will be made for: {prediction_date}")
