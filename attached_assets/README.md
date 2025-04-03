# TSA Project

A fully vegetarian recipe web application built using Streamlit. This project features an interactive menu, a restaurant overview page, an order form for personalized recommendations (with detailed dish descriptions), and a food sourcing page that explains our sustainable practices.

## Features

- **Restaurant Page:** Overview of our vegetarian restaurant and its philosophy.
- **Menu Page:** A curated list of vegetarian dishes from various global cuisines.
- **Order Form:** Interactive form that provides personalized dish recommendations.
- **Food Sourcing:** Information on sustainable, locally sourced ingredients.
- **Modular Architecture:** Each page is split into its own file for easy maintenance.
- **Environment Configuration:** Uses a `.env` file to manage environment variables.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/vegetarian-restaurant.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd vegetarian-restaurant
   ```

3. **Install Dependencies:**

   Make sure you have Python installed. Then install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the project root with the following content (you can adjust the values as needed):

```properties
APP_NAME="Vegetarian Restaurant"
ENV=development
DEFAULT_CUISINE=Italian
DEFAULT_SPICE=Mild
IMAGE_PATH=images/
```

These variables can be loaded into your application using `python-dotenv` if required.

## Usage

Run the application with Streamlit:

```bash
streamlit run main.py
```

Use the sidebar to navigate between the **Restaurant**, **Menu**, **Order Form**, and **Food Sourcing** pages.

## Project Structure

```
vegetarian-restaurant/
├── .env
├── README.md
├── requirements.txt
├── main.py
├── info.py
├── restaurant_page.py
├── menu_page.py
├── order_form_page.py
└── sourcing_page.py
```

- **main.py:** Entrypoint of the app that handles page routing.
- **info.py:** Contains dish data and the dish description generator.
- **restaurant_page.py, menu_page.py, order_form_page.py, sourcing_page.py:** Separate files for individual pages.

## Dependencies

The project uses the following key dependencies:

- **Streamlit** (for the web app interface)
- **python-dotenv** (for loading environment variables)
- **Pillow** (for image handling, if needed)

*(See `requirements.txt` for details.)*

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

## License

This project is open source and available under the [MIT License](LICENSE).
