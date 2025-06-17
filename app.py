import streamlit as st
import pandas as pd

# Load the dictionary CSV
@st.cache_data
def load_dictionary():
    return pd.read_csv("C:/Users/prema/OneDrive/Documents/Mundari Translator/data/mundari_dictionary (1).csv")

dictionary_df = load_dictionary()

# Search function
def get_all_translations(input_text, input_script):
    row = dictionary_df[dictionary_df[input_script].str.lower() == input_text.lower()]
    if row.empty:
        return None
    else:
        return row.iloc[0]

# Streamlit UI
st.set_page_config(page_title="Mundari Text Translator", page_icon="🗣️")
st.title("🗣️ Mundari Text Translator")
st.write("Translate Mundari words between Latin, Devanagari, Ol Chiki, and English.")

input_text = st.text_input("Enter Mundari word:")
input_script = st.selectbox("Select input script:", ["Latin", "Devanagari", "Ol Chiki"])

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter a word.")
    else:
        result = get_all_translations(input_text, input_script)
        if result is not None:
            st.success("Translations:")
            st.write(f"**Latin:** {result['Latin']}")
            st.write(f"**Devanagari:** {result['Devanagari']}")
            st.write(f"**Ol Chiki:** {result['Ol Chiki']}")
            st.write(f"**English Meaning:** {result['English Meaning']}")
        else:
            st.error("Translation not found.")


