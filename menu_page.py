import streamlit as st
from info import sample_dishes

def menu_page():
    st.header("Our Full Menu")
    for dish in sample_dishes:
        st.subheader(dish["name"])
        st.markdown(f"<em>Origin:</em> {dish['origin']}", unsafe_allow_html=True)
        st.markdown("---")