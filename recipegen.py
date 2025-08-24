# recipegen.py (Streamlit Web App)

import streamlit as st
import google.generativeai as genai
import os

# ======================
# 🔑 Setup API key
# ======================
if "GEMINI_API_KEY" not in os.environ:
    raise ValueError("❌ No Gemini API key found! Please set it in Colab first.")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# === Collect user input via Streamlit ===
st.title("🥗 Personalized Recipe Generator (Gemini Flash)")

ingredients = st.text_input("Enter your ingredients (e.g., chicken, broccoli, pasta)")
restrictions = st.text_input("Any dietary restrictions? (e.g., vegetarian, gluten-free)")
cuisine = st.text_input("Choose a cuisine (optional)")

if st.button("Generate Recipe"):
    if not ingredients:
        st.error("⚠️ Please enter at least one ingredient!")
    else:
        prompt = f"""
        You are a master chef AI. Create a detailed, step-by-step recipe.

        Ingredients: {ingredients}
        Dietary restrictions: {restrictions if restrictions else 'None'}
        Cuisine preference: {cuisine if cuisine else 'Any'}

        Format the response as:
        - 📋 Title
        - 🛒 Ingredients list
        - 👩‍🍳 Instructions
        - 💡 Extra tips
        """

        st.info("✨ Generating recipe using gemini-1.5-flash...")
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)

        # === Output the recipe ===
        st.subheader("🍴 Here’s your personalized recipe:")
        st.write(response.text)
