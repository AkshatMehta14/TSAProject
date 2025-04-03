import streamlit as st
from info import sample_dishes, generate_dish_description
from utils.image_utils import display_image_with_caption

def order_form_page():
    # Styled header
    st.markdown("""
    <div style="text-align: center; padding: 20px 0 40px;">
        <h1 style="color: #2E8B57; font-size: 3rem; font-family: 'Georgia', serif;">Order & Recommendations</h1>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto; color: #666;">
            Tell us about your taste preferences, and we'll suggest vegetarian dishes tailored just for you.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create two columns - one for form, one for image
    col1, col2 = st.columns([3, 2])
    
    # Initialize spice level session state variables for order form page
    if 'order_spice_percent' not in st.session_state:
        st.session_state.order_spice_percent = 50
        
    if 'order_spice_text' not in st.session_state:
        st.session_state.order_spice_text = "Medium"
        
    if 'order_spice_color' not in st.session_state:
        st.session_state.order_spice_color = "#FF9800"  # Orange for Medium
        
    # Define a callback function to update the spice level indicators
    def update_spice_indicators():
        # Get the current value
        spice_percent = st.session_state.order_spice_percent
        
        # Update text and color based on percentage
        if spice_percent < 33:
            st.session_state.order_spice_text = "Mild"
            st.session_state.order_spice_color = "#4CAF50"  # Green
        elif spice_percent < 66:
            st.session_state.order_spice_text = "Medium"
            st.session_state.order_spice_color = "#FF9800"  # Orange
        else:
            st.session_state.order_spice_text = "Hot"
            st.session_state.order_spice_color = "#F44336"  # Red
    
    with col1:
        # Order form with enhanced styling
        with st.form(key='menu_form', clear_on_submit=True):
            st.markdown('<div class="form-header">Fill in your preferences</div>', unsafe_allow_html=True)
            
            # Preference options
            st.selectbox("Choose Your Preference", ["Vegetarian", "Vegan"])
            
            # Cuisine selection
            form_cuisine = st.selectbox("Favorite Cuisine", [
                "Italian", "Indian", "Mexican", "Asian", "Japanese", "Korean", "Thai",
                "Mediterranean", "Lebanese", "Spanish", "German", "British", "North African",
                "American", "Brazilian", "Middle Eastern", "Caribbean", "Australian", "French", "Indonesian"
            ])
            
            # Spice level selection with percentage slider
            st.slider(
                "Spice Level", 
                0, 100, 
                st.session_state.order_spice_percent, 
                5, 
                format="%d%%", 
                key="order_spice_percent",
                on_change=update_spice_indicators
            )
            
            # Show the spice level outside the form so it can be updated in real-time
            st.markdown(
                f"""
                <div style='text-align: center; margin-top: 5px; animation: pulse 1.5s infinite;'>
                    <span style='color: {st.session_state.order_spice_color}; font-weight: bold; font-size: 1.1rem;'>
                        {st.session_state.order_spice_text} ({st.session_state.order_spice_percent}%)
                    </span>
                </div>
                <style>
                    @keyframes pulse {{
                        0% {{ opacity: 0.8; }}
                        50% {{ opacity: 1; }}
                        100% {{ opacity: 0.8; }}
                    }}
                </style>
                """, 
                unsafe_allow_html=True
            )
            
            # Dietary restrictions multiselect
            dietary_restrictions = st.multiselect(
                "Dietary Restrictions (if any)",
                ["Gluten-Free", "Nut-Free", "Soy-Free", "Dairy-Free"]
            )
            
            # Form submit button with custom styling
            submitted = st.form_submit_button(
                label="Get Recommendations",
            )
    
    with col2:
        # Display an appetizing image
        display_image_with_caption(
            "https://images.unsplash.com/photo-1498837167922-ddd27525d352", 
            "Our chef will prepare recommendations based on your preferences",
            width=400
        )
    
    # Show recommendations when form is submitted
    if submitted:
        st.markdown(
            f"""
            <div style="margin-top: 30px; padding: 20px; background-color: #f0f5f0; border-radius: 10px; border-left: 4px solid #2E8B57;">
                <h3 style="color: #2E8B57; margin-bottom: 10px;">Your Preference Profile</h3>
                <p><strong>Cuisine:</strong> {form_cuisine}</p>
                <p><strong>Spice Level:</strong> <span style="color: {st.session_state.order_spice_color}; font-weight: bold;">{st.session_state.order_spice_text} ({st.session_state.order_spice_percent}%)</span></p>
                <p><strong>Dietary Needs:</strong> {', '.join(dietary_restrictions) if dietary_restrictions else 'None specified'}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        # Find recommended dishes based on cuisine
        recommended = [dish for dish in sample_dishes if dish["origin"].lower() == form_cuisine.lower()]
        if not recommended:
            recommended = sample_dishes[:3]  # Show top 3 dishes if none match cuisine
        
        st.markdown(
            """
            <h2 style="color: #2E8B57; margin-top: 40px; margin-bottom: 20px; font-family: 'Georgia', serif;">
                Our Recommendations For You
            </h2>
            """, 
            unsafe_allow_html=True
        )
        
        # Display recommendations in an attractive grid
        for i, dish in enumerate(recommended):
            with st.container():
                cols = st.columns([1, 3])
                
                with cols[0]:
                    # Get an image URL based on cuisine
                    if dish["origin"] == "Indian":
                        img_url = "https://images.unsplash.com/photo-1743525699873-b0f0911e3211"
                    elif dish["origin"] in ["Thai", "Asian"]:
                        img_url = "https://images.unsplash.com/photo-1464454709131-ffd692591ee5"
                    elif dish["origin"] in ["Mediterranean", "Middle Eastern", "Lebanese"]:
                        img_url = "https://images.unsplash.com/photo-1498837167922-ddd27525d352"
                    elif dish["origin"] in ["Italian", "French", "Spanish"]:
                        img_url = "https://images.unsplash.com/photo-1485963631004-f2f00b1d6606"
                    else:
                        img_url = "https://images.unsplash.com/photo-1454944338482-a69bb95894af"
                    
                    display_image_with_caption(img_url, use_column=True)
                
                with cols[1]:
                    st.markdown(f"""
                    <div style="padding: 10px;">
                        <h3 style="color: #2E8B57; margin-bottom: 5px;">{dish["name"]}</h3>
                        <p style="color: #666; font-style: italic; margin-bottom: 10px;">Origin: {dish["origin"]}</p>
                        <p style="margin-bottom: 15px;">{dish["description"]}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Generate personalized description
                    with st.spinner(f"Customizing {dish['name']} for your preferences..."):
                        description = generate_dish_description(dish["name"], form_cuisine, st.session_state.order_spice_text)
                    
                    st.markdown(f"""
                    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 8px; margin-top: 10px;">
                        <p style="color: #444;"><strong>Chef's Note:</strong> {description}</p>
                    </div>
                    """, unsafe_allow_html=True)
            
            # Add a divider between dishes
            if i < len(recommended) - 1:
                st.markdown("<hr style='margin: 30px 0; border-color: #e0e0e0;'>", unsafe_allow_html=True)
        
        # Call to action after recommendations
        st.markdown("""
        <div style="margin-top: 40px; text-align: center; padding: 30px; background: linear-gradient(135deg, #f0f5f0 0%, #e8f5e9 100%); border-radius: 10px;">
            <h3 style="color: #2E8B57; margin-bottom: 15px;">Ready to experience these flavors?</h3>
            <p style="margin-bottom: 25px;">Visit us today or place an online order for pickup or delivery.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Adding actual functioning buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📅 Reserve a Table", use_container_width=True, key="reserve_table_order"):
                st.markdown("[Redirecting to reservation page...](https://www.opentable.com)")
        
        with col2:
            if st.button("🥡 Order Online", use_container_width=True, key="order_online"):
                st.markdown("[Redirecting to online ordering...](https://www.doordash.com)")
        
