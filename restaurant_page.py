import streamlit as st
from utils.image_utils import display_image_with_caption, create_image_grid, image_with_text_overlay

def restaurant_page():
    # Restaurant exterior image with overlay text
    image_with_text_overlay(
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4",
        "Welcome to Verdura 🌱",
        "A global vegetarian experience rooted in sustainability, culture, and flavor"
    )
    
    # Main content with three columns for features
    st.markdown("<div class='header-title'>Vegetarian Excellence</div>", unsafe_allow_html=True)
    
    # Three feature columns
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
        <div class="section animate-in">
            <h2>🌿 Artisanal</h2>
            <p>
                Every dish is crafted by chefs who understand that vegetarian cuisine is not about 
                limitation, but infinite creativity. We transform seasonal ingredients into masterpieces
                that surprise and delight.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with cols[1]:
        st.markdown("""
        <div class="section animate-in">
            <h2>🌍 Global</h2>
            <p>
                Our menu draws inspiration from culinary traditions worldwide - from 
                the aromatic spices of India to the rustic comfort of Mediterranean fare, 
                creating a passport of flavors on every plate.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with cols[2]:
        st.markdown("""
        <div class="section animate-in">
            <h2>♻️ Sustainable</h2>
            <p>
                Sustainability isn't just a buzzword at Verdura - it's our foundation. 
                We partner with local farms, minimize waste, and create a dining experience 
                that nurtures both people and planet.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Restaurant interior images
    st.markdown("<div class='header-title'>Our Space</div>", unsafe_allow_html=True)
    
    # Create a 2x2 grid of restaurant interior images
    interior_images = [
        "https://images.unsplash.com/photo-1538333581680-29dd4752ddf2",
        "https://images.unsplash.com/photo-1538334421852-687c439c92f4", 
        "https://images.unsplash.com/photo-1559339352-11d035aa65de",
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4"
    ]
    
    interior_captions = [
        "Our sustainable dining area features reclaimed wood and natural lighting",
        "Private dining nooks offer an intimate experience",
        "The garden view section connects you with nature while dining",
        "Our welcoming entry maintains our commitment to elegant simplicity"
    ]
    
    create_image_grid(interior_images, interior_captions, columns=2)
    
    # Mission Section
    st.markdown("""
    <div class='section'>
        <h2>🌱 Our Mission</h2>
        <p>
            At Verdura, we believe that plant-based food can be just as indulgent as it is intentional. 
            Our mission is to redefine what it means to eat consciously — one unforgettable dish at a time.
        </p>
        <p>
            We're not just serving meals — we're building a movement toward ecological balance, animal welfare, 
            and global culinary connection. Our commitment to authenticity, ethics, and artistry shapes everything we do.
        </p>
        
        <div class="quote">
            "The future of food is plant-based, and the future is delicious." — Chef Marina, Verdura Founder
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Featured dishes section with images
    st.markdown("<div class='header-title'>Featured Dishes</div>", unsafe_allow_html=True)
    
    # Featured dishes in 3 columns with images
    dish_cols = st.columns(3)
    
    with dish_cols[0]:
        display_image_with_caption(
            "https://images.unsplash.com/photo-1464454709131-ffd692591ee5",
            "Paneer Tikka Masala - A rich, aromatic Indian classic",
            use_column=True
        )
        
    with dish_cols[1]:
        display_image_with_caption(
            "https://images.unsplash.com/photo-1454944338482-a69bb95894af",
            "Mediterranean Bowl - Fresh, vibrant and nourishing",
            use_column=True
        )
        
    with dish_cols[2]:
        display_image_with_caption(
            "https://images.unsplash.com/photo-1498837167922-ddd27525d352",
            "Seasonal Risotto - Creamy comfort with local produce",
            use_column=True
        )
    
    # Why Vegetarian Section
    st.markdown("""
    <div class='section'>
        <h2>🥦 Why Vegetarian?</h2>
        <p>
            Choosing a vegetarian lifestyle is one of the most powerful steps you can take for the planet, your health, 
            and the lives of countless animals. Each dish at Verdura celebrates this choice through flavor and form.
        </p>
        <p>
            Studies link plant-based diets to lower risks of chronic illness. Environmentally, it reduces carbon emissions, 
            water use, and deforestation. But it's more than just stats — it's about discovering new ingredients, bold spices, 
            and untold culinary stories.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Chef Spotlight 
    st.markdown("<div class='header-title'>Meet Our Chef</div>", unsafe_allow_html=True)
    
    chef_col1, chef_col2 = st.columns([1, 2])
    
    with chef_col1:
        st.markdown("""
        <div style="background-color: #f5f9f5; border-radius: 50%; width: 220px; height: 220px; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
            <svg width="150" height="150" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 15C15.3137 15 18 12.3137 18 9C18 5.68629 15.3137 3 12 3C8.68629 3 6 5.68629 6 9C6 12.3137 8.68629 15 12 15Z" stroke="#2E8B57" stroke-width="1.5"/>
                <path d="M2.90625 20.2491C3.82834 18.6531 5.1542 17.3278 6.75064 16.4064C8.34708 15.485 10.1579 15 12.0002 15C13.8424 15 15.6532 15.4851 17.2497 16.4065C18.8461 17.3279 20.172 18.6533 21.094 20.2493" stroke="#2E8B57" stroke-width="1.5" stroke-linecap="round"/>
                <path d="M12 12C13.6569 12 15 10.6569 15 9C15 7.34315 13.6569 6 12 6C10.3431 6 9 7.34315 9 9C9 10.6569 10.3431 12 12 12Z" stroke="#2E8B57" stroke-width="1.5"/>
            </svg>
        </div>
        """, unsafe_allow_html=True)
    
    with chef_col2:
        st.markdown("""
        <div style="padding: 20px;">
            <h3 style="color: #2E8B57; margin-bottom: 10px; font-size: 1.8rem;">Chef Marina Costa</h3>
            <p style="font-style: italic; color: #666; margin-bottom: 15px;">Executive Chef & Founder</p>
            <p>
                With over 15 years of experience in vegetarian cuisine, Chef Marina brings her passion for 
                plant-based innovation to every dish at Verdura. Trained in both classical European techniques 
                and traditional Asian methods, she creates unforgettable flavor combinations that celebrate 
                vegetables in their purest form while surprising even the most dedicated meat-eaters.
            </p>
            <p>
                "My philosophy is simple: respect the ingredient, understand its essence, and let it shine. 
                Every vegetable has a story to tell if you listen carefully enough."
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Awards & Recognition
    st.markdown("""
    <div class="section">
        <h2>🏆 Awards & Recognition</h2>
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; margin-top: 20px;">
            <div style="flex: 1; min-width: 200px; padding: 15px; text-align: center;">
                <div style="font-size: 1.8rem; color: #2E8B57; margin-bottom: 10px;">🍽️</div>
                <h3 style="margin-bottom: 5px; font-size: 1.2rem;">Best Vegetarian Restaurant</h3>
                <p style="color: #666; font-style: italic;">GreenDining Awards 2023</p>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; text-align: center;">
                <div style="font-size: 1.8rem; color: #2E8B57; margin-bottom: 10px;">♻️</div>
                <h3 style="margin-bottom: 5px; font-size: 1.2rem;">Sustainability Excellence</h3>
                <p style="color: #666; font-style: italic;">EcoTable Certification 2023</p>
            </div>
            <div style="flex: 1; min-width: 200px; padding: 15px; text-align: center;">
                <div style="font-size: 1.8rem; color: #2E8B57; margin-bottom: 10px;">⭐</div>
                <h3 style="margin-bottom: 5px; font-size: 1.2rem;">Innovation in Plant-Based Cuisine</h3>
                <p style="color: #666; font-style: italic;">Culinary Institute of America</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2E8B57 0%, #3CB371 100%); padding: 40px; border-radius: 10px; text-align: center; margin-top: 40px; color: white;">
        <h2 style="font-size: 2rem; margin-bottom: 15px;">Experience Verdura Today</h2>
        <p style="font-size: 1.2rem; margin-bottom: 25px;">Join us for a meal that nourishes both body and planet. Reservations recommended but walk-ins always welcome.</p>
        <div style="background: white; display: inline-block; padding: 10px 25px; border-radius: 30px; font-weight: bold; color: #2E8B57; font-size: 1.1rem; cursor: pointer; transition: all 0.3s ease;">
            Book A Table
        </div>
    </div>
    """, unsafe_allow_html=True)
