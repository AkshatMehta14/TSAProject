import streamlit as st
from info import sample_dishes, generate_dish_description

# Inject custom CSS for enhanced UI and simple animations
st.markdown(
    """
    <style>
    .stForm {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .header-title {
        color: #2E8B57;
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .page-header {
        color: #2E8B57;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation using radio buttons
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Restaurant", "Menu", "Order Form", "Food Sourcing"])

# --- Page Functions --- #
def restaurant_page():
    st.markdown("<div class='header-title'>Vegetarian Restaurant</div>", unsafe_allow_html=True)
    st.write("""
        Welcome to our Vegetarian Restaurant – where passion for plant-based cuisine meets culinary artistry.
        Enjoy a warm and inviting atmosphere, complete with locally sourced organic ingredients and a menu that celebrates the diversity of vegetarian fare.
        Sit back, relax, and let our carefully crafted dishes delight your palate.
    """)

def menu_page():
    st.header("Our Full Menu")
    for dish in sample_dishes:
        st.subheader(dish["name"])
        st.markdown(f"<em>Origin:</em> {dish['origin']}", unsafe_allow_html=True)
        st.markdown("---")

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

def sourcing_page():
    st.header("From Farm to Table")
    st.write("""
        Our commitment to quality begins with sustainable, locally sourced ingredients.
        We partner with local farmers and organic suppliers who share our passion for ethical, eco-friendly practices.
        Every ingredient is carefully selected to ensure freshness, flavor, and health benefits.
        From the farm where the produce is grown to the meticulous preparation in our kitchen,
        our process guarantees that you receive a meal that is both nourishing and full of character.
        Enjoy the journey from farm to table – a celebration of nature's bounty and culinary innovation.
    """)

# --- Page Routing --- #
if page == "Restaurant":
    restaurant_page()
elif page == "Menu":
    menu_page()
elif page == "Order Form":
    order_form_page()
elif page == "Food Sourcing":
    sourcing_page()