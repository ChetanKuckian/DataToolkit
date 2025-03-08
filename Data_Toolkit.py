import streamlit as st
from converter import json_csv_xml_converter
from sql_formatter import sql_formatter_validator
from data_sampler import data_sampling_tool
from regex_tester import regex_tester
from json_formatter import json_formatter

# Initialize session state
if "tool" not in st.session_state:
    st.session_state.tool = None

# Home screen layout
def home_screen():
    st.title("📊 Data Engineer Toolkit")
    st.markdown("""
        Welcome to the **Data Engineer Toolkit**! This app provides a collection of utilities to help data engineers with common tasks.
    """)
    
    # Custom CSS for boxes, buttons, and the back button
    st.markdown("""
        <style>
        .box {
            border: 2px solid #4CAF50;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
            margin: 10px;
            background-color: #f0f0f0; /* Light gray background */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add shadow */
            transition: transform 0.2s, box-shadow 0.2s; /* Smooth hover effect */
        }
        .box:hover {
            transform: translateY(-5px); /* Lift the box on hover */
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Enhance shadow on hover */
        }
        .box h3 {
            margin-top: 0;
            color: #333; /* Dark text color */
        }
        .stButton>button {
            width: 80%; /* Slightly smaller width */
            margin: 10px auto; /* Center the button */
            display: block;
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s; /* Smooth hover effect */
        }
        .stButton>button:hover {
            background-color: #45a049; /* Darker green on hover */
        }
        .back-button {
        background: linear-gradient(45deg, #FF4B4B, #e04343); /* Gradient background */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        width: 100%;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Add shadow */
    }
    .back-button:hover {
        transform: translateY(-2px); /* Lift the button on hover */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* Enhance shadow on hover */
        background: linear-gradient(45deg, #e04343, #FF4B4B); /* Reverse gradient on hover */
    }
    
    /* Download Button */
    .download-button {
        background: linear-gradient(45deg, #4CAF50, #45a049); /* Gradient background */
        color: white;
        border: none;
        border-radius: 8px;
        padding: 12px 24px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        width: 100%;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Add shadow */
    }
    .download-button:hover {
        transform: translateY(-2px); /* Lift the button on hover */
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2); /* Enhance shadow on hover */
        background: linear-gradient(45deg, #45a049, #4CAF50); /* Reverse gradient on hover */
    }
        </style>
    """, unsafe_allow_html=True)
    
    # Row 1: Converter and Formatter
    row1_col1, row1_col2 = st.columns(2)
    
    # Box 1: JSON/CSV/XML Converter
    with row1_col1:
        st.markdown("""
            <div class="box">
                <h3>📂 JSON/CSV/XML Converter</h3>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Converter", key="converter"):
            st.session_state.tool = "JSON/CSV/XML Converter"
            st.rerun()
    
    # Box 2: SQL Formatter and Validator
    with row1_col2:
        st.markdown("""
            <div class="box">
                <h3>🔍 SQL Formatter and Validator</h3>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to SQL Formatter", key="sql_formatter"):
            st.session_state.tool = "SQL Formatter and Validator"
            st.rerun()
    
    # Row 2: JSON Formatter (centered)
    row2_col1, row2_col2, row2_col3 = st.columns([1, 2, 1])  # Center column is wider
    
    # Box 3: JSON Formatter (centered)
    with row2_col2:
        st.markdown("""
            <div class="box">
                <h3>📝 JSON Formatter</h3>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to JSON Formatter", key="json_formatter"):
            st.session_state.tool = "JSON Formatter"
            st.rerun()
    
    # Row 3: Data Sampling and Regex Tester
    row3_col1, row3_col2 = st.columns(2)
    
    # Box 4: Data Sampling Tool
    with row3_col1:
        st.markdown("""
            <div class="box">
                <h3>🎲 Data Sampler</h3>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Data Sampler", key="data_sampler"):
            st.session_state.tool = "Data Sampling Tool"
            st.rerun()
    
    # Box 5: Regex Tester
    with row3_col2:
        st.markdown("""
            <div class="box">
                <h3>🔎 Regex Tester</h3>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Go to Regex Tester", key="regex_tester"):
            st.session_state.tool = "Regex Tester"
            st.rerun()

# Main app logic
if st.session_state.tool is None:
    home_screen()
else:
    if st.session_state.tool == "JSON/CSV/XML Converter":
        json_csv_xml_converter()
    elif st.session_state.tool == "SQL Formatter and Validator":
        sql_formatter_validator()
    elif st.session_state.tool == "Data Sampling Tool":
        data_sampling_tool()
    elif st.session_state.tool == "Regex Tester":
        regex_tester()
    elif st.session_state.tool == "JSON Formatter":
        json_formatter()
    
    # Add a "Back to Home" button with custom styling
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)
    if st.button("Back to Home", key="back_to_home"):
        st.session_state.tool = None
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
    **Data Engineer Toolkit**  
    Built with ❤️ by Chetan Kuckian  
    [GitHub Repo](https://github.com/ChetanKuckian) | [LinkedIn](https://www.linkedin.com/in/chetankuckian/)
""")