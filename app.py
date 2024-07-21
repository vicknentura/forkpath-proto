

import streamlit as st

def join_dataframes(dataframes):
    # ... (Your function to join DataFrames on common ID)

st.title("CSV Data Joiner")
uploaded_files = st.file_uploader("Upload CSV Files", accept_multiple=True)

if uploaded_files:
    dataframes = []
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        dataframes.append(df)

    joined_df = join_dataframes(dataframes)
    st.dataframe(joined_df)
