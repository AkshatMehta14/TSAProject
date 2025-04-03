import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def load_image_from_url(url, width=None):
    """
    Load an image from a URL and resize it if width is specified.
    Returns the image as a PIL Image object.
    """
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        
        if width:
            # Calculate height to maintain aspect ratio
            aspect_ratio = image.height / image.width
            height = int(width * aspect_ratio)
            image = image.resize((width, height))
            
        return image
    except Exception as e:
        st.error(f"Error loading image from {url}: {str(e)}")
        return None

def display_image_with_caption(url, caption=None, width=None, use_column=False):
    """
    Display an image from URL with optional caption in a streamlit app.
    If use_column is True, it will be wrapped in a column.
    """
    image = load_image_from_url(url, width)
    
    if image:
        if use_column:
            with st.container():
                st.image(image, caption=caption, use_container_width=True)
        else:
            st.image(image, caption=caption, width=width)
        return True
    return False

def create_image_grid(image_urls, captions=None, columns=3):
    """
    Create a grid of images with optional captions.
    
    Args:
        image_urls: List of image URLs
        captions: List of captions (same length as image_urls)
        columns: Number of columns in the grid
    """
    if captions and len(image_urls) != len(captions):
        st.warning("Number of captions doesn't match number of images")
        captions = None
    
    # Create rows of columns
    for i in range(0, len(image_urls), columns):
        cols = st.columns(columns)
        
        # Fill each column with an image
        for j in range(columns):
            idx = i + j
            if idx < len(image_urls):
                with cols[j]:
                    caption = captions[idx] if captions else None
                    display_image_with_caption(image_urls[idx], caption, use_column=True)

def image_with_text_overlay(image_url, title, text, overlay_opacity=0.6):
    """
    Display an image with a semi-transparent text overlay
    """
    st.markdown(
        f"""
        <style>
        .image-container {{
            position: relative;
            text-align: center;
            color: white;
            margin-bottom: 20px;
        }}
        .image-container img {{
            width: 100%;
            border-radius: 10px;
        }}
        .overlay {{
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: rgba(0, 0, 0, {overlay_opacity});
            overflow: hidden;
            width: 100%;
            padding: 20px;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 10px;
        }}
        .overlay-title {{
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .overlay-text {{
            font-size: 1rem;
        }}
        </style>
        
        <div class="image-container">
            <img src="{image_url}" alt="{title}">
            <div class="overlay">
                <div class="overlay-title">{title}</div>
                <div class="overlay-text">{text}</div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

def dish_card(dish, image_url=None):
    """
    Display a dish as a card with image and details, including spice level
    """
    # Determine spice level color and label based on spiciness value
    spiciness = dish.get('spiciness', 0.5)  # Default to medium if not specified
    
    # Convert spiciness to percentage for display
    spice_percent = int(spiciness * 100)
    
    # Determine color based on spice level
    if spiciness < 0.3:
        spice_color = "#4CAF50"  # Green for mild
        spice_label = "Mild"
    elif spiciness < 0.6:
        spice_color = "#FFC107"  # Amber for medium
        spice_label = "Medium"
    else:
        spice_color = "#F44336"  # Red for spicy
        spice_label = "Spicy"
    
    # Create spice level indicator with fixed CSS animations
    spice_indicator = f"""
    <div class="spice-level-container" style="margin: 10px 0; animation: fadeIn 0.5s ease-in;">
        <div style="display: flex; justify-content: space-between; margin-bottom: 3px;">
            <span style="font-size: 0.85rem;">Spice Level:</span>
            <span style="font-size: 0.85rem; color: {spice_color}; font-weight: bold;">{spice_label} ({spice_percent}%)</span>
        </div>
        <div style="height: 6px; width: 100%; background-color: #f0f0f0; border-radius: 3px; overflow: hidden;">
            <div style="height: 100%; width: {spice_percent}%; background-color: {spice_color}; 
                      transition: width 1s ease-in-out; animation: expandWidth 1.5s ease-out;"></div>
        </div>
    </div>
    <style>
    @keyframes expandWidth {{
        from {{ width: 0%; }}
        to {{ width: {spice_percent}%; }}
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    </style>
    """
    
    # Build the card HTML with spice indicator
    # Make sure to escape HTML in the description to prevent code from showing
    import html
    escaped_description = html.escape(dish['description'])
    
    card_html = f"""
    <div class="dish-card" style="transition: transform 0.3s ease; animation: cardEnter 0.5s ease-out;">
        <div class="dish-content">
            <h3 class="dish-name">{dish['name']} <span class="dish-price">${dish['price']:.2f}</span></h3>
            <div class="dish-origin">Origin: {dish['origin']}</div>
            {spice_indicator}
            <p class="dish-description">{escaped_description}</p>
        </div>
    """
    
    if image_url:
        # Make sure to escape the dish name as it will be used in the alt attribute
        escaped_dish_name = html.escape(dish['name'])
        
        # Format the image HTML properly
        card_html += f"""
        <div class="dish-image-container">
            <img src="{image_url}" alt="{escaped_dish_name}" class="dish-image" style="transition: all 0.5s ease;">
        </div>
        """
    
    card_html += """
    </div>
    <style>
    @keyframes cardEnter {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .dish-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }
    .dish-card:hover .dish-image {
        transform: scale(1.05);
    }
    </style>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)
