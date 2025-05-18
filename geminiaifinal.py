from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai
load_dotenv()
# from PIL import image

# Set page config
st.set_page_config(page_title="AI Healthadda", page_icon="🤖", layout="centered")

# Initialize Gemini Pro with your API key
GOOGLE_API_KEY = "AIzaSyAhw8axGxHhNkbF66aYr74U5_KLYWaXjUk"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize model
model = genai.GenerativeModel('gemini-2.0-flash')

# App title
st.title("🤖 AI HEALTHADDA FOR COMMON MAN")

# User input form
with st.form("user_data"):
    age = st.number_input("Age", min_value=1, max_value=100, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Trans"])
    weight = st.number_input("Weight (kg)", min_value=3.0, max_value=200.0)
    height = st.number_input("Height (cm)", min_value=20.0, max_value=225.0)
    blood_pressure = st.text_input("Blood Pressure (e.g. 120/80)")
    glucose = st.text_input("Glucose Level (mg/dL)")
    preferred_cuisine = st.text_input("Preferred Cuisine (e.g. Indian, Mediterranean)")
    is_diabetic = st.selectbox("Diabetic?", ["Yes", "No"])
    health_goal = st.selectbox("Health Goal", ["Lose Weight", "Gain Muscle", "Maintain Weight", "Control Diabetes"])
    fitness_routine = st.selectbox("Fitness Routine", ["None", "Light", "Moderate", "Intense"])
    submit = st.form_submit_button("Generate Meal Plan")

# On form submission
if submit:
    prompt = f"""
    Based on the following user information, suggest a healthy 1300 calories per day with FAT/FIBER/CARBS/PROTEIN RATIO for  Pre Breakfast, breakfast, Mid Morning Snack, Lunch, Early Afternoon Snack,  Evening Snack, and dinner with acheiving 1300 calories:

    Age: {age}
    Gender: {gender}
    Weight: {weight} kg
    Height: {height} cm
    Blood Pressure: {blood_pressure}
    Glucose Level: {glucose}
    Preferred Cuisine: {preferred_cuisine}
    Diabetic: {is_diabetic}
    Health Goal: {health_goal}
    Fitness Routine: {fitness_routine}

    Give meals with appropriate calories, balanced macronutrients, and avoid foods that may worsen medical conditions. Format the output clearly.
    """

    try:
        with st.spinner("Generating User Calorie Meal..."):
            response = model.generate_content(prompt)
            st.success("✅🍎 Calorie Generated!")
            st.markdown(response.text)
    except Exception as e:
        st.error(f"❌ Failed to generate meal plan: {e}")
