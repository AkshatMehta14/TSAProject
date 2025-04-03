import streamlit as st
from info import sample_dishes, generate_dish_description

def order_form_page():
    st.header("Order Form & Recommendations")
    with st.form(key='menu_form', clear_on_submit=True):
        st.markdown("<div class='page-header'>Fill in your preferences</div>", unsafe_allow_html=True)
        st.selectbox("Choose Your Preference", ["Vegetarian"])
        form_cuisine = st.selectbox("Favorite Cuisine", [
            "Italian", "Indian", "Mexican", "Asian", "Japanese", "Korean", "Thai",
            "Mediterranean", "Lebanese", "Spanish", "German", "British", "North African",
            "American", "Brazilian", "Middle Eastern", "Caribbean", "Australian", "French", "Indonesian"
        ])
        form_spice = st.selectbox("Spice Level", ["Mild", "Medium", "Hot"])
        submitted = st.form_submit_button(label="Get Recommendations")
    
    if submitted:
        recommended = [dish for dish in sample_dishes if dish["origin"].lower() == form_cuisine.lower()]
        if not recommended:
            recommended = sample_dishes
        st.header("Recommended Dishes")
        for dish in recommended:
            st.subheader(dish["name"])
            st.markdown(f"**Origin:** {dish['origin']}")
            with st.spinner(f"Generating details for {dish['name']}..."):
                description = generate_dish_description(dish["name"], form_cuisine, form_spice)
            st.markdown(f"**Details:** {description}")