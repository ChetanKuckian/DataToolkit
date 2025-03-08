import streamlit as st
import json

def json_formatter():
    st.header("🔍 JSON Formatter")
    
    # Input JSON data
    st.write("**Input JSON Data**")
    json_input = st.text_area("Paste your JSON here:", height=200)
    
    # File upload for JSON
    uploaded_file = st.file_uploader("Or upload a JSON file:", type=["json"])
    
    if uploaded_file is not None:
        try:
            json_input = uploaded_file.getvalue().decode("utf-8")
            st.write("**Uploaded JSON Preview:**")
            st.code(json_input, language="json")
        except Exception as e:
            st.error(f"Error reading JSON file: {e}")
    
    if json_input:
        try:
            # Parse JSON input
            json_data = json.loads(json_input)
            
            # Format JSON with indentation
            formatted_json = json.dumps(json_data, indent=4)
            
            # Display formatted JSON
            st.write("**Formatted JSON:**")
            st.code(formatted_json, language="json")
            
            # Download formatted JSON
            st.download_button(
                label="Download Formatted JSON",
                data=formatted_json,
                file_name="formatted_json.json",
                mime="application/json",
                key="download_json"
            )
        except json.JSONDecodeError as e:
            st.error(f"Invalid JSON: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")