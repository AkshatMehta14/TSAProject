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
    st.markdown("""
        <style>
        .hero {
            background: linear-gradient(to right, #e8f5e9, #ffffff);
            padding: 50px 30px;
            border-radius: 20px;
            text-align: center;
        }
        .hero h1 {
            font-size: 3rem;
            font-weight: 800;
            color: #2E7D32;
            margin-bottom: 0.5em;
        }
        .hero p {
            font-size: 1.2rem;
            max-width: 700px;
            margin: 0 auto;
            color: #555;
        }
        .section {
            padding: 40px 10px;
        }
        .section h2 {
            color: #388E3C;
            font-size: 2rem;
            margin-bottom: 10px;
        }
        .section p {
            font-size: 1.05rem;
            color: #444;
            max-width: 800px;
        }
        .quote {
            font-style: italic;
            color: #777;
            margin-top: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class='hero'>
        <h1>Welcome to Verdura 🍃</h1>
        <p>A global vegetarian experience rooted in sustainability, culture, and flavor. More than a restaurant — it's a movement.</p>
    </div>
    """, unsafe_allow_html=True)

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
    </div>
    """, unsafe_allow_html=True)

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
            water use, and deforestation. But it’s more than just stats — it’s about discovering new ingredients, bold spices, 
            and untold culinary stories.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Story Section
    st.markdown("""
    <div class='section'>
        <h2>📖 Our Story</h2>
        <p>
            Verdura began as a vision shared by three dreamers:
            Nina, a regenerative farmer; Raj, a spice alchemist from Mumbai; and Elena, a Mediterranean food critic on a quest for soul food.
        </p>
        <p>
            They came together not just to start a restaurant, but to create a sanctuary. 
            A space where purpose meets plate, and every meal tells a story — about people, place, and planet.
        </p>
        <p class='quote'>
            "Vegetarianism is not a restriction — it's a rediscovery."
        </p>
    </div>
    """, unsafe_allow_html=True)


def menu_page():
    st.header("Our Full Menu")
    for dish in sample_dishes:
        st.subheader(f"{dish['name']} — ${dish['price']:.2f}")
        st.markdown(f"*Origin:* **{dish['origin']}**")
        st.markdown(f"{dish['description']}")
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

import streamlit.components.v1 as components

def sourcing_page():
    st.markdown("<div class='header-title'>From Farm to Table 🌾</div>", unsafe_allow_html=True)

    stages = [
        {
            "title": "🌱 Sowing & Growing",
            "text": """
                It all begins on lush, organic farmland where the soil is nourished using compost and natural fertilizers.
                Seeds are chosen for their biodiversity, and crops are rotated to restore the earth — not deplete it.
            """,
            "vanta": "waves",
            "color": "#88cc88"
        },
        {
            "title": "🐓 Ethical Animal Enclosures",
            "text": """
                Our vegetarian philosophy extends to protecting all life. Birds and animals are not caged — they roam free in open-air sanctuaries,
                contributing to natural compost cycles and pest control. The presence of birds symbolizes balance, not exploitation.
            """,
            "vanta": "birds",
            "color": "#cce5ff"
        },
        {
            "title": "☁️ Aerial Delivery Routes",
            "text": """
                When ingredients travel, they fly efficiently. Some rare spices and heirloom grains are delivered via air cargo along curated green routes —
                flights that offset carbon emissions and optimize fuel efficiency. It's not just fast — it's thoughtful.
            """,
            "vanta": "clouds",
            "color": "#ddeeff"
        },
        {
            "title": "🔥 Cooking in a Tandoor",
            "text": """
                Back in the kitchen, ingredients meet fire. We slow-roast vegetables in traditional clay tandoors at 900°F to caramelize flavor while preserving nutrients.
                Foggy heat rises, spices sizzle — and your dish begins its transformation into magic.
            """,
            "vanta": "fog",
            "color": "#ffcc99"
        },
        {
            "title": "🌍 Served to You with Purpose",
            "text": """
                Finally, the dish arrives at your table — hot, ethical, and fully traceable. 
                Our farm-to-table system reduces emissions, eliminates waste, and supports a regional food economy. 
                Every plate you enjoy is a vote for sustainability.
            """,
            "vanta": "globe",
            "color": "#222222"  # Dark background for globe effect
        },
    ]

    for stage in stages:
        st.subheader(stage["title"])
        st.write(stage["text"])
        components.html(f"""
            <div id="vanta-{stage["vanta"]}" style="width: 100%; height: 300px; background-color: {stage["color"]};"></div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r121/three.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.{stage["vanta"]}.min.js"></script>
            <script>
              VANTA.{stage["vanta"].upper()}({{
                el: "#vanta-{stage["vanta"]}",
                mouseControls: true,
                touchControls: true,
                minHeight: 300.00,
                minWidth: 200.00,
                scale: 1.0,
                scaleMobile: 1.0
              }});
            </script>
        """, height=300)
        st.markdown("---")


# --- Page Routing --- #
if page == "Restaurant":
    restaurant_page()
elif page == "Menu":
    menu_page()
elif page == "Order Form":
    order_form_page()
elif page == "Food Sourcing":
    sourcing_page()