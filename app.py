
import streamlit as st
from nvidiva_API import structured_generator

# Page Config
st.set_page_config(
    page_title="Health AI Assistant",
    page_icon="🩺",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    color: #2E8B57;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 30px;
}

.stButton>button {
    width: 100%;
    background-color: #2E8B57;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    height: 50px;
    border: none;
}

.stButton>button:hover {
    background-color: #256d46;
    color: white;
}

.response-box {
    background-color: white;
    color: black;
    padding: 20px;
    border-radius: 15px;
    border-left: 6px solid #2E8B57;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
        width=120
    )

    st.title("🩺 Health AI")

    st.markdown("""
    ### Features
    ✅ Health Advice  
    ✅ Skin Care Tips  
    ✅ Disease Information  
    ✅ Fitness Guidance  
    ✅ Nutrition Support  
    ✅ Wellness Suggestions  
    """)

    st.info(
        "⚠️ This AI is not a replacement for professional medical advice."
    )


# Main Title
st.markdown(
    "<div class='title'>🩺 Health & Skin Care AI Assistant</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Ask health, skincare, fitness, and wellness questions instantly.</div>",
    unsafe_allow_html=True
)


# User Input
user_input = st.text_area(
    "Enter your health question:",
    placeholder="Example: How to reduce acne naturally?",
    height=150
)


# Generate Button
if st.button("Generate Health Advice"):

    if user_input.strip() == "":
        st.warning("Please enter a health-related question.")

    else:

        prompt = f"""
You are an advanced AI Health and Skin Care Assistant.

Your role is to provide helpful, safe, beginner-friendly, and professional information ONLY related to:

1. General Health
2. Skin Care
3. Common Diseases
4. Healthy Lifestyle
5. Nutrition and Fitness
6. Mental Wellness
7. Preventive Care
8. Safe Home Remedies
9. Hygiene and Self Care

STRICT RULES:

- Reply ONLY to health, skincare, wellness, disease, fitness, nutrition, hygiene, and medical-related questions.

- If the user asks anything unrelated to health or skincare, politely respond with:

"Sorry, I can only answer health, skincare, fitness, wellness, and disease-related questions."

- Never provide dangerous medical advice.
- Never prescribe medicines or dosages.
- Never claim to be a real doctor.

User Question:
{user_input}
"""

        with st.spinner("Generating health advice..."):

            result = structured_generator(prompt)

        st.markdown("## 🧾 AI Response")

        st.markdown(
            f"<div class='response-box'>{result}</div>",
            unsafe_allow_html=True
        )


# Footer
st.markdown(
    "<div class='footer'>Made By ℕ𝕚𝕣𝕒𝕟𝕛𝕒𝕟✨</div>",
    unsafe_allow_html=True
)

