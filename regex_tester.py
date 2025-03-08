import streamlit as st
import re

def regex_tester():
    # Regex Tester
    st.header("🔎 Regex Tester")

    # Input text
    text = st.text_area("Enter text to test:", height=150)

    # Input regex pattern
    regex_pattern = st.text_input("Enter regex pattern:")

    # Advanced options
    with st.expander("Advanced Options"):
        case_insensitive = st.checkbox("Case-insensitive matching")
        multiline = st.checkbox("Multiline matching")

    # Validate and highlight matches
    if text and regex_pattern:
        flags = 0
        if case_insensitive:
            flags |= re.IGNORECASE
        if multiline:
            flags |= re.MULTILINE
        
        try:
            matches = list(re.finditer(regex_pattern, text, flags))
            
            if matches:
                st.success(f"Found {len(matches)} match(es)!")
                
                # Highlight matches
                highlighted_text = text
                for match in reversed(matches):
                    start, end = match.span()
                    highlighted_text = (
                        highlighted_text[:start]
                        + f"<span style='background-color: yellow;'>{highlighted_text[start:end]}</span>"
                        + highlighted_text[end:]
                    )
                
                st.markdown(f"<pre>{highlighted_text}</pre>", unsafe_allow_html=True)
                
                # Display match details
                st.write("Match details:")
                for i, match in enumerate(matches, start=1):
                    st.write(f"Match {i}: `{match.group()}` (position {match.start()} to {match.end()})")
            else:
                st.warning("No matches found.")
        except re.error as e:
            st.error(f"Invalid regex pattern: {e}")