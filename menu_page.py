import streamlit as st
from info import sample_dishes
from utils.image_utils import dish_card

def get_dish_image(dish_name):
    """Return a relevant image URL based on dish name or cuisine type"""
    # Map of dish names to image URLs
    dish_images = {
        "Paneer Tikka Masala": "https://images.unsplash.com/photo-1743525699873-b0f0911e3211",
        "Vegetarian Pad Thai": "https://images.unsplash.com/photo-1464454709131-ffd692591ee5",
        "Ratatouille": "https://images.unsplash.com/photo-1485963631004-f2f00b1d6606",
        "Falafel Bowl": "https://images.unsplash.com/photo-1498837167922-ddd27525d352",
        "Caprese Salad": "https://images.unsplash.com/photo-1498837167922-ddd27525d352",
        "Vegetarian Bibimbap": "https://images.unsplash.com/photo-1743525700011-afac212694d7",
        "Greek Spanakopita": "https://images.unsplash.com/photo-1454944338482-a69bb95894af",
    }
    
    # Default images by cuisine
    cuisine_images = {
        "Indian": "https://images.unsplash.com/photo-1743525699873-b0f0911e3211",
        "Thai": "https://images.unsplash.com/photo-1464454709131-ffd692591ee5",
        "French": "https://images.unsplash.com/photo-1485963631004-f2f00b1d6606",
        "Mediterranean": "https://images.unsplash.com/photo-1454944338482-a69bb95894af",
        "Middle Eastern": "https://images.unsplash.com/photo-1498837167922-ddd27525d352",
        "Italian": "https://images.unsplash.com/photo-1498837167922-ddd27525d352",
        "Korean": "https://images.unsplash.com/photo-1743525700011-afac212694d7",
        "North African": "https://images.unsplash.com/photo-1743525699873-b0f0911e3211",
        "Japanese": "https://images.unsplash.com/photo-1498837167922-ddd27525d352",
        "Asian": "https://images.unsplash.com/photo-1464454709131-ffd692591ee5",
        "Spanish": "https://images.unsplash.com/photo-1485963631004-f2f00b1d6606",
    }
    
    # Return specific dish image if available, otherwise return image based on cuisine
    if dish_name in dish_images:
        return dish_images[dish_name]
    
    # Find the dish's cuisine from sample_dishes
    for dish in sample_dishes:
        if dish["name"] == dish_name and dish["origin"] in cuisine_images:
            return cuisine_images[dish["origin"]]
    
    # Default fallback image
    return "https://images.unsplash.com/photo-1498837167922-ddd27525d352"

def menu_page():
    # Styled header for menu page
    st.markdown("""
    <div style="text-align: center; padding: 20px 0 40px;">
        <h1 style="color: #2E8B57; font-size: 3rem; font-family: 'Georgia', serif;">Our Menu</h1>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto; color: #666;">
            Explore our carefully crafted dishes featuring fresh, seasonal ingredients from local farms.
            Each creation tells a story of sustainability, flavor, and global culinary traditions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filter options
    st.markdown("### Filter By Cuisine")
    
    # Get unique cuisines from sample dishes
    cuisines = sorted(list(set(dish["origin"] for dish in sample_dishes)))
    cuisines.insert(0, "All Cuisines")  # Add "All" option at the beginning
    
    selected_cuisine = st.selectbox("", cuisines)
    
    # Filter dishes based on selection
    if selected_cuisine == "All Cuisines":
        filtered_dishes = sample_dishes
    else:
        filtered_dishes = [dish for dish in sample_dishes if dish["origin"] == selected_cuisine]
    
    # Group dishes by cuisine
    cuisine_groups = {}
    for dish in filtered_dishes:
        if dish["origin"] not in cuisine_groups:
            cuisine_groups[dish["origin"]] = []
        cuisine_groups[dish["origin"]].append(dish)
    
    # Display dishes grouped by cuisine
    for cuisine, dishes in cuisine_groups.items():
        st.markdown(f"""
        <div style="margin-top: 30px; margin-bottom: 15px;">
            <h2 style="color: #2E8B57; border-bottom: 2px solid #E8F5E9; padding-bottom: 10px;">
                {cuisine} Cuisine
            </h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Display dishes in this cuisine group
        for dish in dishes:
            dish_image = get_dish_image(dish["name"])
            dish_card(dish, dish_image)
    
    # If no dishes match the filter
    if not filtered_dishes:
        st.markdown("""
        <div style="text-align: center; padding: 50px 0; color: #777;">
            <i class="fas fa-search" style="font-size: 3rem; margin-bottom: 20px;"></i>
            <h3>No dishes found</h3>
            <p>Try a different cuisine filter</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Special dietary information
    st.markdown("""
    <div style="margin-top: 50px; padding: 25px; background-color: #f9f9f9; border-radius: 10px;">
        <h3 style="color: #2E8B57; margin-bottom: 15px;">Dietary Information</h3>
        <p>All dishes on our menu are vegetarian. Many can be made vegan upon request.</p>
        <p>We're happy to accommodate allergies and dietary restrictions. Please inform your server of any special needs.</p>
        <div style="display: flex; flex-wrap: wrap; margin-top: 15px;">
            <div style="margin-right: 15px; margin-bottom: 10px; background-color: #E8F5E9; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Vegetarian</div>
            <div style="margin-right: 15px; margin-bottom: 10px; background-color: #E8F5E9; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Vegan Options</div>
            <div style="margin-right: 15px; margin-bottom: 10px; background-color: #E8F5E9; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Gluten-Free Options</div>
            <div style="margin-right: 15px; margin-bottom: 10px; background-color: #E8F5E9; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem;">Nut-Free Options</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
