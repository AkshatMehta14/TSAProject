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
    The function uses Streamlit native components instead of raw HTML
    """
    # Create a container for the dish card
    with st.container():
        # Apply custom CSS for card styling 
        st.markdown("""
        <style>
        .dish-card-container {
            border: 1px solid #e6e6e6;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            background-color: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .dish-card-container:hover {
            box-shadow: 0 8px 16px rgba(0,0,0,0.15);
            transform: translateY(-5px);
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Create a card container
        st.markdown('<div class="dish-card-container">', unsafe_allow_html=True)
        
        # Dish information using pure Streamlit
        col1, col2 = st.columns([3, 2])
        
        with col1:
            # Dish name and price
            st.markdown(f"### {dish['name']} ${dish['price']:.2f}")
            
            # Origin
            st.markdown(f"**Origin:** {dish['origin']}")
            
            # Spice level
            spiciness = dish.get('spiciness', 0.5)  # Default to medium if not specified
            spice_percent = int(spiciness * 100)
            
            # Determine color and label based on spice level
            if spiciness < 0.3:
                spice_color = "#4CAF50"  # Green for mild
                spice_label = "Mild"
            elif spiciness < 0.6:
                spice_color = "#FFC107"  # Amber for medium
                spice_label = "Medium"
            else:
                spice_color = "#F44336"  # Red for spicy
                spice_label = "Spicy"
            
            st.markdown(f"**Spice Level:** {spice_label} ({spice_percent}%)")
            
            # Simple progress bar for spice level
            st.progress(spiciness)
            
            # Description - using plain text with st.write to avoid HTML rendering issues
            st.write(f"**Description:** {dish['description']}")
        
        # Image in the second column if available
        with col2:
            if image_url:
                st.image(image_url, width=200)
        
        # Close the card container
        st.markdown('</div>', unsafe_allow_html=True)
