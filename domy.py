import streamlit as st
from nvidiva_API import structured_generator

def main():
    st.title("Health")
    st.write("...")


    user_input = st.text_input("Enter the topic","...")


    if st.button("Generate"):
        prompt= f"{user_input}"

        result = structured_generator(prompt)

if __name__ == "__main__":
    main()
