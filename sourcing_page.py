import streamlit as st
from utils.image_utils import display_image_with_caption, image_with_text_overlay

def sourcing_page():
    # Hero image with overlay
    image_with_text_overlay(
        "https://images.unsplash.com/photo-1471193945509-9ad0617afabf",
        "From Farm to Table 🌾",
        "Our commitment to sustainable, ethical food sourcing"
    )
    
    # Introduction
    st.markdown("""
    <div style="margin: 40px 0 30px;">
        <p style="font-size: 1.2rem; line-height: 1.8; max-width: 800px; margin: 0 auto; text-align: center; color: #444;">
            At Verdura, we believe that the best flavors come from responsibly sourced ingredients. 
            We partner with local farmers and suppliers who share our commitment to sustainable, 
            ethical practices. Follow the journey of our ingredients from seed to plate.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Journey Steps
    journey_steps = [
        {
            "emoji": "🌱",
            "title": "Sustainable Farming Practices",
            "content": """
                Our journey begins with local farmers who practice sustainable agriculture.
                They use organic methods, crop rotation, and water conservation techniques
                to minimize environmental impact while maximizing flavor and nutrition.
                We regularly visit our partner farms to ensure they maintain our high standards.
            """,
            "image_url": "https://images.unsplash.com/photo-1625246333195-78d9c38ad449"
        },
        {
            "emoji": "🚜",
            "title": "Ethical Harvesting",
            "content": """
                All produce is hand-harvested at peak ripeness to ensure maximum flavor and nutritional value.
                Farm workers are paid fair wages and provided with safe working conditions - a non-negotiable
                requirement for our farm partners. We believe food tastes better when it's grown and harvested
                with respect for both land and people.
            """,
            "image_url": "https://images.unsplash.com/photo-1539902743451-20dfa0a92ffd"
        },
        {
            "emoji": "📦",
            "title": "Minimal Transportation",
            "content": """
                The average food item travels 1,500 miles before reaching your plate. Our ingredients 
                travel an average of just 100 miles. We work with a network of local farms and arrange 
                efficient delivery routes to minimize our carbon footprint. Seasonal ingredients that 
                can't be sourced locally are carefully selected from ethical producers.
            """,
            "image_url": "https://images.unsplash.com/photo-1694892671389-642241672449"
        },
        {
            "emoji": "👨‍🍳",
            "title": "Kitchen Preparation",
            "content": """
                Our chefs work directly with farmers to plan seasonal menus, ensuring we use ingredients
                at their peak. In our kitchen, we practice nose-to-tail (or rather, root-to-stem) cooking,
                utilizing every part of the vegetable. Scraps become stocks, broths, or compost that returns
                to our partner farms, completing the cycle.
            """,
            "image_url": "https://images.unsplash.com/photo-1694892670435-c2596b34b19b"
        },
        {
            "emoji": "🍽️",
            "title": "Zero-Waste Philosophy",
            "content": """
                We're committed to eliminating waste throughout our operation. Food scraps are
                composted, packaging is minimal and biodegradable, and portions are carefully calculated
                to reduce leftovers. Even our cooking oil is recycled into biofuel. We're proud that
                over 95% of our potential waste is diverted from landfills.
            """,
            "image_url": "https://images.unsplash.com/photo-1595708711101-3f145af6adb8"
        }
    ]
    
    # Display each step of the journey
    for step in journey_steps:
        st.markdown(f"""
        <div class="journey-step">
            <div class="journey-step-title">
                <span>{step["emoji"]}</span> {step["title"]}
            </div>
            <div class="journey-step-content">
                {step["content"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Display step image
        display_image_with_caption(step["image_url"], width=800)
    
    # Meet Our Farmers Section
    st.markdown("""
    <div style="margin-top: 60px;">
        <h2 style="color: #2E8B57; text-align: center; font-size: 2.2rem; margin-bottom: 30px; font-family: 'Georgia', serif;">
            Meet Our Farm Partners
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Farm partners - using SVG icons since we can't use actual images
    farm_partners = [
        {
            "name": "Green Valley Organics",
            "description": "Family-owned farm specializing in heirloom vegetables and rare herb varieties. Located just 15 miles from our restaurant.",
            "specialty": "Heirloom tomatoes, peppers, and herbs"
        },
        {
            "name": "Sun Root Collective",
            "description": "Worker-owned cooperative practicing regenerative agriculture. Their innovative techniques have restored formerly depleted soil.",
            "specialty": "Root vegetables and leafy greens"
        },
        {
            "name": "Mountain Meadow Mushrooms",
            "description": "Specialists in organic mushroom cultivation using sustainable indoor growing techniques with minimal environmental impact.",
            "specialty": "Specialty mushrooms and fungi"
        }
    ]
    
    # Display farm partners in columns
    cols = st.columns(3)
    for i, partner in enumerate(farm_partners):
        with cols[i]:
            st.markdown(f"""
            <div style="background-color: white; padding: 25px; border-radius: 10px; height: 100%; box-shadow: 0 2px 5px rgba(0,0,0,0.05);">
                <div style="background-color: #E8F5E9; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 6V12M12 12V18M12 12H18M12 12H6" stroke="#2E8B57" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <h3 style="text-align: center; color: #2E8B57; margin-bottom: 10px;">{partner["name"]}</h3>
                <p style="text-align: center; color: #666; font-style: italic; margin-bottom: 15px;">Specialty: {partner["specialty"]}</p>
                <p style="color: #444; text-align: center;">{partner["description"]}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Sourcing Map
    st.markdown("""
    <div style="margin-top: 60px;">
        <h2 style="color: #2E8B57; text-align: center; font-size: 2.2rem; margin-bottom: 20px; font-family: 'Georgia', serif;">
            Our Local Sourcing Network
        </h2>
        <p style="text-align: center; max-width: 700px; margin: 0 auto 30px; color: #666;">
            We source over 80% of our ingredients from within a 100-mile radius, supporting local
            economies and reducing our carbon footprint.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Styled SVG map representation
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 40px;">
        <svg width="700" height="400" viewBox="0 0 700 400" style="max-width: 100%;">
            <defs>
                <linearGradient id="mapGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#E8F5E9" />
                    <stop offset="100%" stop-color="#C8E6C9" />
                </linearGradient>
            </defs>
            <rect x="50" y="50" width="600" height="300" rx="10" fill="url(#mapGradient)" />
            
            <!-- Restaurant Location -->
            <circle cx="350" cy="200" r="20" fill="#2E8B57" />
            <text x="350" y="200" font-family="Arial" font-size="12" fill="white" text-anchor="middle" dominant-baseline="middle">Verdura</text>
            
            <!-- Farm Locations -->
            <circle cx="150" cy="120" r="15" fill="#4CAF50" />
            <text x="150" cy="120" font-family="Arial" font-size="10" fill="white" text-anchor="middle" dominant-baseline="middle">Farm 1</text>
            
            <circle cx="250" cy="300" r="15" fill="#4CAF50" />
            <text x="250" cy="300" font-family="Arial" font-size="10" fill="white" text-anchor="middle" dominant-baseline="middle">Farm 2</text>
            
            <circle cx="500" cy="100" r="15" fill="#4CAF50" />
            <text x="500" cy="100" font-family="Arial" font-size="10" fill="white" text-anchor="middle" dominant-baseline="middle">Farm 3</text>
            
            <circle cx="550" cy="250" r="15" fill="#4CAF50" />
            <text x="550" cy="250" font-family="Arial" font-size="10" fill="white" text-anchor="middle" dominant-baseline="middle">Farm 4</text>
            
            <!-- Connecting Lines -->
            <line x1="350" y1="200" x2="150" y2="120" stroke="#2E8B57" stroke-width="2" stroke-dasharray="5,5" />
            <line x1="350" y1="200" x2="250" y2="300" stroke="#2E8B57" stroke-width="2" stroke-dasharray="5,5" />
            <line x1="350" y1="200" x2="500" y2="100" stroke="#2E8B57" stroke-width="2" stroke-dasharray="5,5" />
            <line x1="350" y1="200" x2="550" y2="250" stroke="#2E8B57" stroke-width="2" stroke-dasharray="5,5" />
            
            <!-- Distance Circles -->
            <circle cx="350" cy="200" r="100" fill="none" stroke="#2E8B57" stroke-width="1" stroke-dasharray="5,5" />
            <text x="450" y="200" font-family="Arial" font-size="12" fill="#2E8B57" text-anchor="start">25 miles</text>
            
            <circle cx="350" cy="200" r="200" fill="none" stroke="#2E8B57" stroke-width="1" stroke-dasharray="5,5" />
            <text x="550" y="200" font-family="Arial" font-size="12" fill="#2E8B57" text-anchor="start">50 miles</text>
        </svg>
    </div>
    """, unsafe_allow_html=True)
    
    # Sustainability Metrics
    st.markdown("""
    <div style="margin-top: 40px;">
        <h2 style="color: #2E8B57; text-align: center; font-size: 2rem; margin-bottom: 30px; font-family: 'Georgia', serif;">
            Our Sustainability Impact
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Metrics in 3 columns
    metric_cols = st.columns(3)
    
    with metric_cols[0]:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #E8F5E9; border-radius: 10px; height: 100%;">
            <div style="font-size: 3rem; color: #2E8B57; margin-bottom: 10px;">80%</div>
            <h3 style="margin-bottom: 10px; color: #2E8B57;">Locally Sourced</h3>
            <p>Of our ingredients come from within a 100-mile radius, supporting local farmers and reducing transportation emissions.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with metric_cols[1]:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #E8F5E9; border-radius: 10px; height: 100%;">
            <div style="font-size: 3rem; color: #2E8B57; margin-bottom: 10px;">95%</div>
            <h3 style="margin-bottom: 10px; color: #2E8B57;">Waste Diverted</h3>
            <p>Through composting, recycling, and careful portioning, nearly all of our potential waste avoids landfills.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with metric_cols[2]:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background-color: #E8F5E9; border-radius: 10px; height: 100%;">
            <div style="font-size: 3rem; color: #2E8B57; margin-bottom: 10px;">30+</div>
            <h3 style="margin-bottom: 10px; color: #2E8B57;">Local Partnerships</h3>
            <p>We work with over 30 local farmers, artisans, and suppliers to create our menu and sustain our local food economy.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Call to action
    st.markdown("""
    <div style="margin-top: 60px; text-align: center; padding: 40px; background: #2E8B57; color: white; border-radius: 10px;">
        <h2 style="margin-bottom: 20px; color: white;">Experience Our Farm-to-Table Philosophy</h2>
        <p style="margin-bottom: 30px; font-size: 1.1rem; max-width: 700px; margin-left: auto; margin-right: auto;">
            Join us for a meal that's not just delicious, but also helps support sustainable farming practices
            and reduces environmental impact. Every bite makes a difference.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Adding a Streamlit button that actually works
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🍽️ Make a Reservation", use_container_width=True, key="reserve_table_sourcing"):
            st.markdown("[Redirecting to reservation page...](https://www.opentable.com)")
            # You could also use st.experimental_set_query_params() or st.experimental_rerun() in more complex scenarios
