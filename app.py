import streamlit as st
from nlp.text_extractor import extract_text_from_file
from nlp.clause_extractor import extract_clauses
from nlp.risk_scoring import risk_score

st.title("AI Legal Contract Risk Analyzer")

uploaded_file = st.file_uploader(
    "Upload Contract File", type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:
    text = extract_text_from_file(uploaded_file)
    clauses = extract_clauses(text)

    st.subheader("Clause-wise Risk Analysis")

    for i, clause in enumerate(clauses, start=1):
        st.write(f"Clause {i}: {clause}")
        st.write("Risk:", risk_score(clause))
        st.markdown("---")

