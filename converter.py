import streamlit as st
import pandas as pd
import xml.etree.ElementTree as ET
import re

def sanitize_column_name(name):
    """
    Sanitize column names to make them valid XML tag names.
    """
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if not name[0].isalpha() and name[0] != "_":
        name = "_" + name
    return name

def json_csv_xml_converter():
    st.header("📂 JSON/CSV/XML Converter")
    
    # File upload widget
    uploaded_file = st.file_uploader("Upload a file (JSON, CSV, or XML)", type=["json", "csv", "xml"])
    
    if uploaded_file is not None:
        # Display file details
        file_details = {"filename": uploaded_file.name, "filetype": uploaded_file.type, "filesize": uploaded_file.size}
        st.write("**File Details:**")
        st.write(file_details)
        
        # Read and process the file
        try:
            if uploaded_file.type == "application/json":
                df = pd.read_json(uploaded_file)
            elif uploaded_file.type == "text/csv":
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.type == "application/xml":
                tree = ET.parse(uploaded_file)
                root = tree.getroot()
                data = []
                for child in root:
                    data.append(child.attrib)
                df = pd.DataFrame(data)
            
            # Display file preview
            st.write("**File Preview:**")
            st.write(df.head())
            
            # Convert to another format
            st.write("**Convert File:**")
            output_format = st.selectbox("Select output format:", ["CSV", "JSON", "XML"])
            
            if output_format == "CSV":
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="converted_file.csv",
                    mime="text/csv",
                    key="download_csv"
                )
            
            elif output_format == "JSON":
                json = df.to_json(orient="records")
                st.download_button(
                    label="Download JSON",
                    data=json,
                    file_name="converted_file.json",
                    mime="application/json",
                    key="download_json"
                )
            
            elif output_format == "XML":
                # Sanitize column names
                df.columns = [sanitize_column_name(col) for col in df.columns]
                xml = df.to_xml(index=False)
                st.download_button(
                    label="Download XML",
                    data=xml,
                    file_name="converted_file.xml",
                    mime="application/xml",
                    key="download_xml"
                )
        
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")