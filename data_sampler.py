import streamlit as st
import pandas as pd

def data_sampling_tool():
    st.header("Data Sampling Tool")
    
    # File upload
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview:")
        st.write(df.head())
        
        # Sampling options
        sample_size = st.slider("Select sample size (number of rows):", 1, len(df), 100)
        sample = df.sample(n=sample_size)
        
        st.write("Sampled Data:")
        st.write(sample)
        
        # Download sampled data
        csv = sample.to_csv(index=False)
        st.download_button("Download Sampled Data", data=csv, file_name="sampled_data.csv", mime="text/csv")