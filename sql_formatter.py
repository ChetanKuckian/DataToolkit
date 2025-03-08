import streamlit as st
from sqlparse import format
import sqlglot
from sqlglot import ParseError

def validate_sql_syntax(sql_query):
    """
    Validate SQL syntax using sqlglot.
    """
    try:
        # Parse the SQL query
        sqlglot.parse_one(sql_query)
        return True, None
    except ParseError as e:
        return False, str(e)

def sql_formatter_validator():
    st.header("SQL Formatter and Validator")
    
    # Input SQL query
    sql_query = st.text_area("Enter your SQL query:")
    
    if sql_query:
        # Format SQL using sqlparse
        formatted_sql = format(sql_query, reindent=True, keyword_case="upper")
        st.write("Formatted SQL:")
        st.code(formatted_sql, language="sql")
        
        # Validate SQL syntax using sqlglot
        is_valid, error_message = validate_sql_syntax(sql_query)
        
        if is_valid:
            st.success("SQL query is valid!")
        else:
            st.error(f"Invalid SQL syntax: {error_message}")