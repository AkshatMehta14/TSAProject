import streamlit as st
from info import sample_dishes, generate_dish_description
import restaurant_page
import menu_page
import order_form_page
import sourcing_page
import os
from utils.image_utils import display_image_with_caption

# Set page config first
st.set_page_config(
    page_title="Verdura - Farm to Table Vegetarian",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load and inject custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Inject font from Google Fonts
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# Animate elements with CSS 
st.markdown(
    """
    <style>
    @keyframes slideInFromLeft {
        0% { transform: translateX(-30px); opacity: 0; }
        100% { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    
    .sidebar .element-container {
        animation: slideInFromLeft 0.5s ease-out forwards;
    }
    
    .stButton button {
        transition: all 0.3s ease;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    /* Animated sidebar highlight */
    .sidebar .element-container:not(:first-child) {
        transition: all 0.2s ease;
    }
    
    .sidebar .element-container:hover:not(:first-child) {
        background-color: rgba(46, 139, 87, 0.1);
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a logo to the sidebar
logo_html = """
<div style="display: flex; justify-content: center; margin-bottom: 20px;">
    <svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
        <circle cx="50" cy="50" r="48" fill="#2E8B57" stroke="#FFF" stroke-width="2"/>
        <text x="50" y="58" font-family="Georgia" font-size="24" font-weight="bold" text-anchor="middle" fill="#FFF">V</text>
        <path d="M30,70 Q50,30 70,70" fill="none" stroke="#FFF" stroke-width="2"/>
        <path d="M25,40 Q40,60 55,40" fill="none" stroke="#FFF" stroke-width="1.5"/>
        <path d="M45,40 Q60,60 75,40" fill="none" stroke="#FFF" stroke-width="1.5"/>
    </svg>
</div>
<h2 style="text-align: center; color: #2E8B57; margin-top: 0; font-family: 'Georgia', serif;">Verdura</h2>
"""

st.sidebar.markdown(logo_html, unsafe_allow_html=True)
st.sidebar.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)

# Sidebar navigation using custom buttons
st.sidebar.markdown("### Navigation")

# Custom CSS for glowing navigation buttons with animations
st.markdown("""
<style>
/* Glowing Button Styles */
.nav-button {
    display: block;
    width: 100%;
    padding: 12px 15px;
    margin: 8px 0;
    background: linear-gradient(135deg, #2E8B57, #3AA76D);
    color: white;
    border: none;
    border-radius: 6px;
    font-weight: 500;
    text-align: center;
    cursor: pointer;
    transition: all 0.5s ease;
    position: relative;
    overflow: hidden;
    font-size: 16px;
}

.nav-button:before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: rgba(255, 255, 255, 0.2);
    transform: rotate(45deg);
    z-index: 1;
    transition: all 0.6s ease;
    opacity: 0;
}

.nav-button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 20px rgba(46, 139, 87, 0.6);
}

.nav-button:hover:before {
    animation: glowingEffect 1.5s infinite;
}

@keyframes glowingEffect {
    0% {
        transform: rotate(45deg) translateX(-100%);
        opacity: 0;
    }
    50% {
        opacity: 0.5;
    }
    100% {
        transform: rotate(45deg) translateX(100%);
        opacity: 0;
    }
}

.nav-button.active {
    background: linear-gradient(135deg, #1A6B37, #2E8B57);
    box-shadow: 0 0 15px rgba(46, 139, 87, 0.5);
}

/* Button shake animation */
@keyframes shake {
    0% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    50% { transform: translateX(5px); }
    75% { transform: translateX(-5px); }
    100% { transform: translateX(0); }
}

.nav-button:active {
    animation: shake 0.3s ease;
}
</style>
""", unsafe_allow_html=True)

# Session state to track page
if 'page' not in st.session_state:
    st.session_state.page = "Home"

# Create custom button styling using Streamlit components
# Navigation buttons with actual click functionality
def nav_button(label, page_name):
    if st.sidebar.button(label, key=f"nav_{page_name}", 
                        use_container_width=True,
                        type="primary" if st.session_state.page == page_name else "secondary"):
        st.session_state.page = page_name
        st.rerun()  # Rerun the app to refresh the UI

# Add custom animated buttons with actual click functionality
nav_button("🏠 Home", "Home")
nav_button("🍽️ Menu", "Menu") 
nav_button("🛒 Order", "Order Form")
nav_button("🌱 Sourcing", "Food Sourcing")

# The page variable is now controlled by session state
page = st.session_state.page

# Add a subtle decoration to the sidebar
st.sidebar.markdown(
    """
    <div style="padding: 20px 0; text-align: center; color: #777; font-size: 0.85rem;">
        <div style="margin-bottom: 10px;">🌱 Farm to Table 🌱</div>
        <div style="width: 100%; height: 1px; background: linear-gradient(to right, transparent, #2E8B57, transparent);"></div>
    </div>
    """,
    unsafe_allow_html=True
)

# Add hours and location to sidebar
st.sidebar.markdown("### Hours")
st.sidebar.markdown("""
- **Monday - Friday**: 11am - 10pm
- **Saturday**: 10am - 11pm
- **Sunday**: 10am - 9pm
""")

st.sidebar.markdown("### Location")
st.sidebar.markdown("123 Green Street, Eco City")

# Contact section in sidebar
st.sidebar.markdown("### Contact")
st.sidebar.markdown("📞 (555) 123-4567")
st.sidebar.markdown("📧 hello@verdura.com")

# Add social media icons to sidebar
st.sidebar.markdown(
    """
    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 30px;">
        <a href="#" style="color: #2E8B57; font-size: 24px;">
            <i class="fab fa-facebook"></i>
        </a>
        <a href="#" style="color: #2E8B57; font-size: 24px;">
            <i class="fab fa-instagram"></i>
        </a>
        <a href="#" style="color: #2E8B57; font-size: 24px;">
            <i class="fab fa-twitter"></i>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# Import Font Awesome for icons
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """,
    unsafe_allow_html=True
)

# --- Page Routing --- #
if page == "Home":
    restaurant_page.restaurant_page()
elif page == "Menu":
    menu_page.menu_page()
elif page == "Order Form":
    order_form_page.order_form_page()
elif page == "Food Sourcing":
    sourcing_page.sourcing_page()

# Footer
st.markdown(
    """
    <footer style="margin-top: 70px; padding-top: 20px; border-top: 1px solid #e0e0e0; text-align: center; color: #777; font-size: 0.9rem;">
        <div>Verdura Farm to Table Vegetarian Restaurant © 2023</div>
        <div style="margin-top: 5px;">🌱 Nourishing People & Planet 🌱</div>
    </footer>
    """,
    unsafe_allow_html=True
)
