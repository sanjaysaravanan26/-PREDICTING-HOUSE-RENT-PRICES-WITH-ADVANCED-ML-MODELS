import streamlit as st
import joblib
import numpy as np
import pickle
import pandas as pd

# Load model
model = joblib.load("model.pkl")

# Define city mapping
city_mapping = {
    "chennai": 1,
    "delhi": 2,
    "bangalore": 3,
    "mumbai": 4,
    "hyderabad": 5
}

# App Title and Description
st.title("Predicting House Rent Prices with Advanced ML Models")
st.divider()
st.write("House Price Prediction App, utilizes machine learning to estimate property prices based on various input features such as location, number of bedrooms, and bathrooms. Built with Streamlit, it provides an interactive interface for users to input property details and receive instant price predictions")
st.divider()

# Input Fields
bedroom = st.number_input("Number of bedrooms🛏", min_value=0, value=0)
bathrooms = st.number_input("Number of bathrooms🛁", min_value=0, value=0)
livingarea = st.number_input("Enter the square ft🏬", min_value=0, value=2000)
condition = st.number_input("Condition(1 to 5)📭", min_value=0, value=3)
number_of_hospital = st.number_input("Number of hospital nearby🏫", min_value=0, value=0)
area_of_the_house = st.selectbox("Select area of the house", list(city_mapping.keys()))

st.divider()

# Prepare input data for prediction
x = [[bedroom, bathrooms, livingarea, condition, number_of_hospital, city_mapping[area_of_the_house]]]

area_encoded=city_mapping[area_of_the_house]

x_array = np.array([[
    bedroom,
    bathrooms,
    livingarea,
    condition,
  number_of_hospital
    ]])

# Prediction Button
predictbutton = st.button("PREDICT!")

if predictbutton:
    st.balloons()
    x_array = np.array(x)
    prediction = model.predict(x_array)[0]
    
    # Show prediction result
    import inflect
    p=inflect.engine()
    price_in_world=p.number_to_words(int(prediction)).upper()
    

    st.markdown(f"""
    <div style="background-color: #D6EAF8; padding: 15px; border-radius: 10px;">
    <h1>Predicted House Price</h1>
        <h2 style="color: #154360;">{ prediction}</h2>
        <p style="font-size: 18px; font-weight: bold;">({price_in_world} RUPEES ONLY😊)</p>
    </div>
""", unsafe_allow_html=True)
#Define default house condition values
    swimming_pool = "Yes"
    garden = "No"
    car_parking = "Yes"
    water_supply = "24-Hours"
# Display House Condition Details
    st.write("### 🏠 House Condition Details")
    st.write(f"✅ Swimming Pool: *{swimming_pool}*")
    st.write(f"✅ Garden: *{garden}*")
    st.write(f"✅ Car Parking: *{car_parking}*")
    st.write(f"✅ Water Supply: *{water_supply}*")

st.divider()

import streamlit as st

# City mapping with Latitudes and Longitudes
city_mapping = {
    "chennai": {"id": 1, "lat": 13.0827, "lon": 80.2707},
    "delhi": {"id": 2, "lat": 28.6139, "lon": 77.2090},
    "bangalore": {"id": 3, "lat": 12.9716, "lon": 77.5946},
    "mumbai": {"id": 4, "lat": 19.0760, "lon": 72.8777},
    "hyderabad": {"id": 5, "lat": 17.3850, "lon": 78.4867}
}

# Display map after prediction
if area_of_the_house in city_mapping:
    lat, lon = city_mapping[area_of_the_house]["lat"], city_mapping[area_of_the_house]["lon"]

    # Generate Google Maps iframe
    map_html = f"""
    <iframe width="700" height="450"
    src="https://www.google.com/maps?q={lat},{lon}&hl=es;z=14&output=embed"></iframe>
    """

    # Display Google Maps iframe
    st.components.v1.html(map_html, height=500)

st.divider()

# Bar chart for price comparison
st.write("🔹 This comparison helps you understand price variations across cities.")

 
import matplotlib.pyplot as plt
st.subheader("📊 Price Comparison")
data = {
    "City": ["Delhi", "Bangalore", "Mumbai", "Hyderabad"],
    "Price": [850000, 750000, 950000, 650000]  # Dummy data, replace with actual predictions
}
data = pd.DataFrame(data)

fig, ax = plt.subplots()
ax.bar(data["City"], data["Price"], color=["blue", "green", "red", "purple"])
ax.set_ylabel("Price in INR")
ax.set_xlabel("City")
ax.set_title("House Price Comparison")

st.pyplot(fig)

# Add multiple images
st.subheader("🏡 House Visualization")
images = ["new home image.jpeg", "home_image.jpeg.jpeg","bathroom.jpeg","bedroom.jpeg","kitchen.jpeg"]  
selected_image = st.selectbox("Choose House Image", images)

st.image(selected_image, caption="Sample House",width=500)
page=("About","Contact")
if page == "About":
    st.switch_page("pages/About.py")  
elif page == "Contact":
    st.switch_page("pages/Contact.py") 
  
st.title("📖 About This Project")
st.write("""
    his project is a *House Rent Prediction System* using *Machine Learning*.
It helps users estimate rent based on factors like *location, house condition, and facilities*.
""")

st.subheader("Project Features")
st.markdown("""
- 📊 *Data Analysis* to understand key rent factors  
- 🏡 *Predicts House Rent* using ML models  
- 🗺️ *Google Maps Integration* to show selected city  
""")

st.write("More details on the next pages...")


                                                       



