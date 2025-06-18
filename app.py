import streamlit as st
import pandas as pd

# Load the dictionary CSV and clean it
@st.cache_data
def load_dictionary():
    df = pd.read_csv("mundari_dictionary.csv")
    # Clean all columns: remove spaces and convert to string
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()
    return df

dictionary_df = load_dictionary()

# Search function
def get_all_translations(input_text, input_script):
    # Clean input text
    input_text = input_text.strip().lower()

    # Make a copy and clean the selected script column
    cleaned_df = dictionary_df.copy()
    cleaned_df[input_script] = cleaned_df[input_script].astype(str).str.strip().str.lower()

    # Search
    row = cleaned_df[cleaned_df[input_script] == input_text]

    if row.empty:
        return None
    else:
        return row.iloc[0]

# Streamlit UI setup
st.set_page_config(page_title="Mundari Text Translator", page_icon="🗣️")
st.title("🗣️ Mundari Text Translator")
st.write("Translate Mundari words between Latin, Devanagari, Ol Chiki, and English.")

# User input section
input_text = st.text_input("Enter Mundari word:")
input_script = st.selectbox("Select input script:", ["Latin", "Devanagari", "Ol Chiki"])

# Translate button
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
