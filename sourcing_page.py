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
    st.write("""
        At Verdura, we believe that the best flavors come from responsibly sourced ingredients. 
        We partner with local farmers and suppliers who share our commitment to sustainable, 
        ethical practices. Follow the journey of our ingredients from seed to plate.
    """)
    
    # Journey Steps
    journey_steps = [
        {
            "emoji": "🌱",
            "title": "Sustainable Farming Practices",
            "content": """Our journey begins with local farmers who practice sustainable agriculture.
                They use organic methods, crop rotation, and water conservation techniques
                to minimize environmental impact while maximizing flavor and nutrition.
                We regularly visit our partner farms to ensure they maintain our high standards.""",
            "image_url": "https://images.unsplash.com/photo-1625246333195-78d9c38ad449"
        },
        {
            "emoji": "🚜",
            "title": "Ethical Harvesting",
            "content": """All produce is hand-harvested at peak ripeness to ensure maximum flavor and nutritional value.
                Farm workers are paid fair wages and provided with safe working conditions - a non-negotiable
                requirement for our farm partners. We believe food tastes better when it's grown and harvested
                with respect for both land and people.""",
            "image_url": "https://images.unsplash.com/photo-1539902743451-20dfa0a92ffd"
        },
        {
            "emoji": "📦",
            "title": "Minimal Transportation",
            "content": """The average food item travels 1,500 miles before reaching your plate. Our ingredients 
                travel an average of just 100 miles. We work with a network of local farms and arrange 
                efficient delivery routes to minimize our carbon footprint. Seasonal ingredients that 
                can't be sourced locally are carefully selected from ethical producers.""",
            "image_url": "https://images.unsplash.com/photo-1694892671389-642241672449"
        },
        {
            "emoji": "👨‍🍳",
            "title": "Kitchen Preparation",
            "content": """Our chefs work directly with farmers to plan seasonal menus, ensuring we use ingredients
                at their peak. In our kitchen, we practice nose-to-tail (or rather, root-to-stem) cooking,
                utilizing every part of the vegetable. Scraps become stocks, broths, or compost that returns
                to our partner farms, completing the cycle.""",
            "image_url": "https://images.unsplash.com/photo-1694892670435-c2596b34b19b"
        },
        {
            "emoji": "🍽️",
            "title": "Zero-Waste Philosophy",
            "content": """We're committed to eliminating waste throughout our operation. Food scraps are
                composted, packaging is minimal and biodegradable, and portions are carefully calculated
                to reduce leftovers. Even our cooking oil is recycled into biofuel. We're proud that
                over 95% of our potential waste is diverted from landfills.""",
            "image_url": "https://images.unsplash.com/photo-1595708711101-3f145af6adb8"
        }
    ]
    
    # Display each step of the journey
    for step in journey_steps:
        st.subheader(f"{step['emoji']} {step['title']}")
        st.write(step['content'])
        display_image_with_caption(step["image_url"], width=800)
    
    # Meet Our Farmers Section
    st.header("Meet Our Farm Partners")
    
    # Farm partners
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
            st.subheader(partner["name"])
            st.caption(f"Specialty: {partner['specialty']}")
            st.write(partner["description"])
    
    # Sustainability Metrics
    st.header("Our Sustainability Impact")
    
    # Metrics in 3 columns
    metric_cols = st.columns(3)
    
    with metric_cols[0]:
        st.metric("Locally Sourced", "80%", "of ingredients within 100 miles")
    
    with metric_cols[1]:
        st.metric("Waste Diverted", "95%", "from landfills")
    
    with metric_cols[2]:
        st.metric("Local Partnerships", "30+", "farmers and suppliers")
    
    # Call to action
    st.markdown("---")
    st.header("Experience Our Farm-to-Table Philosophy")
    st.write(
        "Join us for a meal that's not just delicious, but also helps support sustainable "
        "farming practices and reduces environmental impact. Every bite makes a difference."
    )
    
    # Reservation button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🍽️ Make a Reservation", use_container_width=True, key="sourcing_reserve"):
            st.link_button("Book Your Table", "https://www.opentable.com")
