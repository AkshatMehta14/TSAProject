# Sample dishes list (fully vegetarian, ~60 items)
sample_dishes = [
    {"name": "Vegetarian Margherita Pizza", "origin": "Italian"},
    {"name": "Vegetarian Pesto Pasta", "origin": "Italian"},
    {"name": "Vegetarian Bruschetta", "origin": "Italian"},
    {"name": "Vegetarian Risotto", "origin": "Italian"},
    {"name": "Vegetarian Gnocchi", "origin": "Italian"},
    {"name": "Chickpea Curry", "origin": "Indian"},
    {"name": "Vegetarian Samosa", "origin": "Indian"},
    {"name": "Vegetarian Dal", "origin": "Indian"},
    {"name": "Vegetarian Naan", "origin": "Indian"},
    {"name": "Vegetarian Tacos", "origin": "Mexican"},
    {"name": "Vegetarian Quesadilla", "origin": "Mexican"},
    {"name": "Vegetarian Enchiladas", "origin": "Mexican"},
    {"name": "Vegetarian Guacamole", "origin": "Mexican"},
    {"name": "Asian Stir-fry Tofu", "origin": "Asian"},
    {"name": "Vegetarian Dumplings", "origin": "Asian"},
    {"name": "Vegetarian Hot and Sour Soup", "origin": "Asian"},
    {"name": "Vegetarian Sushi Rolls", "origin": "Japanese"},
    {"name": "Vegetarian Miso Soup", "origin": "Japanese"},
    {"name": "Vegetarian Teriyaki Tofu", "origin": "Japanese"},
    {"name": "Vegetarian Tempura", "origin": "Japanese"},
    {"name": "Vegetarian Bibimbap", "origin": "Korean"},
    {"name": "Vegetarian Kimchi", "origin": "Korean"},
    {"name": "Vegetarian Pad Thai", "origin": "Thai"},
    {"name": "Vegetarian Green Curry", "origin": "Thai"},
    {"name": "Vegetarian Spring Rolls", "origin": "Thai"},
    {"name": "Vegetarian Falafel Wrap", "origin": "Mediterranean"},
    {"name": "Vegetarian Hummus", "origin": "Mediterranean"},
    {"name": "Vegetarian Lentil Soup", "origin": "Mediterranean"},
    {"name": "Vegetarian Tabouleh", "origin": "Lebanese"},
    {"name": "Vegetarian Shawarma", "origin": "Lebanese"},
    {"name": "Vegetarian Paella", "origin": "Spanish"},
    {"name": "Vegetarian Gazpacho", "origin": "Spanish"},
    {"name": "Vegetarian Pretzel", "origin": "German"},
    {"name": "Vegetarian Sauerkraut", "origin": "German"},
    {"name": "Vegetarian Shepherd's Pie", "origin": "British"},
    {"name": "Vegetarian Fish and Chips", "origin": "British"},
    {"name": "Vegetarian Couscous", "origin": "North African"},
    {"name": "Vegetarian Tagine", "origin": "North African"},
    {"name": "Vegetarian Burger", "origin": "American"},
    {"name": "Vegetarian Mac and Cheese", "origin": "American"},
    {"name": "Vegetarian Burrito", "origin": "Mexican"},
    {"name": "Vegetarian Chili", "origin": "American"},
    {"name": "Vegetarian Feijoada", "origin": "Brazilian"},
    {"name": "Vegetarian Acarajé", "origin": "Brazilian"},
    {"name": "Vegetarian Mezze Platter", "origin": "Middle Eastern"},
    {"name": "Vegetarian Baklava", "origin": "Middle Eastern"},
    {"name": "Vegetarian Jerk Tofu", "origin": "Caribbean"},
    {"name": "Vegetarian Callaloo", "origin": "Caribbean"},
    {"name": "Vegetarian Avocado Toast", "origin": "Australian"},
    {"name": "Vegetarian BBQ Skewers", "origin": "Australian"},
    {"name": "Vegetarian Quinoa Salad", "origin": "American"},
    {"name": "Vegetarian Stuffed Peppers", "origin": "American"},
    {"name": "Vegetarian Frittata", "origin": "Italian"},
    {"name": "Vegetarian Currywurst", "origin": "German"},
    {"name": "Vegetarian Vegetable Dumplings", "origin": "Asian"},
    {"name": "Vegetarian Spring Salad", "origin": "American"},
    {"name": "Vegetarian Chocolate Cake", "origin": "American"},
    {"name": "Vegetarian Fruit Tart", "origin": "French"},
    {"name": "Vegetarian Ratatouille", "origin": "French"},
    {"name": "Vegetarian Baguette", "origin": "French"},
    {"name": "Vegetarian Crepe", "origin": "French"},
    {"name": "Vegetarian Gado-Gado", "origin": "Indonesian"},
    {"name": "Vegetarian Nasi Goreng", "origin": "Indonesian"},
    {"name": "Vegetarian Satay", "origin": "Indonesian"}
]

def generate_dish_description(dish_name, cuisine, spice):
    """
    Generates a detailed description for a dish based on its cuisine and the desired spice level.
    The description is designed to be lengthy and informative.
    """
    spice_level = spice.lower()
    if cuisine.lower() == "italian":
        return (f"{dish_name} is a classic Italian dish that masterfully blends the rich aroma of fresh tomatoes, "
                f"basil, and a touch of {spice_level} seasoning. Every bite embodies generations of culinary tradition, "
                "complemented by artisanal cheeses and a perfectly crisp crust, evoking the rustic charm of Italy.")
    elif cuisine.lower() == "indian":
        return (f"{dish_name} showcases the complexity of Indian spices through an expertly layered flavor profile. "
                f"The {spice_level} heat, balanced by cooling yogurt and fragrant herbs, creates a symphony of taste that "
                "celebrates the depth and history of Indian cuisine.")
    elif cuisine.lower() == "mexican":
        return (f"{dish_name} captures the vibrant spirit of Mexican cuisine with a burst of colors and flavors. "
                f"Infused with a {spice_level} kick derived from authentic chiles and a blend of tangy citrus, smoky spices, "
                "and garden-fresh vegetables, each forkful is a fiesta of taste.")
    elif cuisine.lower() == "asian":
        return (f"{dish_name} is an Asian-inspired creation that balances savory umami with a subtle {spice_level} warmth. "
                "Stir-fried vegetables and tofu shine through in a dish drizzled with a rich, savory sauce for an unforgettable experience.")
    elif cuisine.lower() == "japanese":
        return (f"{dish_name} reflects the elegant simplicity of Japanese cuisine. Lightly seasoned and meticulously arranged, "
                f"it combines a {spice_level} nuance with traditional ingredients like miso and seaweed to offer a refined sensory journey.")
    elif cuisine.lower() == "korean":
        return (f"{dish_name} is a Korean specialty characterized by bold, robust flavors and a lively {spice_level} twist. "
                "It features fermented vegetables, spicy sauces, and crisp tofu, capturing the dynamic culinary traditions of Korea.")
    elif cuisine.lower() == "thai":
        return (f"{dish_name} brings the intricate flavors of Thai cooking to life. The {spice_level} spice perfectly accentuates "
                "a harmonious blend of lemongrass, coconut milk, and fresh herbs, creating a dish that is both exotic and comforting.")
    elif cuisine.lower() == "mediterranean":
        return (f"{dish_name} is inspired by the sun-kissed traditions of Mediterranean cuisine. With a {spice_level} edge that enlivens "
                "a hearty mix of olive oil, fresh vegetables, and aromatic herbs, it is a wholesome tribute to regional culinary artistry.")
    elif cuisine.lower() == "lebanese":
        return (f"{dish_name} offers the warm, robust flavors of Lebanese cooking. The {spice_level} spice enhances a blend of chickpeas, "
                "tahini, and zesty lemon, resulting in a dish that is both hearty and refreshing with a distinct Middle Eastern flair.")
    elif cuisine.lower() == "spanish":
        return (f"{dish_name} is a vibrant Spanish dish where every ingredient sings. A {spice_level} note weaves through layers of ripe tomatoes, "
                "roasted peppers, and a pinch of saffron, transporting you straight to the lively streets of Spain.")
    elif cuisine.lower() == "german":
        return (f"{dish_name} reinvents German comfort food with a creative modern twist. With a subtle infusion of {spice_level} spice, "
                "this dish combines hearty ingredients in an innovative way that reimagines traditional flavors.")
    elif cuisine.lower() == "british":
        return (f"{dish_name} takes beloved British culinary classics and reinvents them with creative flair. A hint of {spice_level} grace is imparted "
                "through seasonal vegetables and rustic roots, offering a comforting yet sophisticated dining experience.")
    elif cuisine.lower() == "north african":
        return (f"{dish_name} is a North African delight, expertly fusing sweet and savory elements with a {spice_level} twist. A medley of couscous, dried fruits, "
                "and zesty seasonings comes together in an exotic taste sensation.")
    elif cuisine.lower() == "american":
        return (f"{dish_name} represents American comfort food reimagined. The {spice_level} heat complements a rich mix of grains, vegetables, and tangy sauces, "
                "ensuring a meal that is both hearty and innovative.")
    elif cuisine.lower() == "brazilian":
        return (f"{dish_name} celebrates the exuberant traditions of Brazilian cuisine. Infused with a {spice_level} spice, it elevates a vibrant combination of beans, rice, "
                "and tropical ingredients into a festive and colorful dish.")
    elif cuisine.lower() == "middle eastern":
        return (f"{dish_name} is a Middle Eastern treasure, steeped in history and bursting with flavor. A gentle {spice_level} accent highlights the fusion of grilled vegetables, "
                "aromatic spices, and tangy yogurt, delivering a dish that is both exotic and satisfying.")
    elif cuisine.lower() == "caribbean":
        return (f"{dish_name} transports you to the Caribbean with its tropical ingredients and a daring {spice_level} flair. Fresh fruits, peppers, and island herbs combine for a refreshing escape.")
    elif cuisine.lower() == "australian":
        return (f"{dish_name} offers a modern interpretation of Australian favorites. With a {spice_level} undertone, the dish showcases fresh local produce with a creative twist on classic recipes.")
    elif cuisine.lower() == "french":
        return (f"{dish_name} is a masterpiece inspired by French culinary art. The {spice_level} accent elevates its delicate flavors, combining fine ingredients and meticulous presentation "
                "to create a dish that is as elegant as it is delicious, capturing the essence of French sophistication.")
    elif cuisine.lower() == "indonesian":
        return (f"{dish_name} is a celebration of Indonesian diversity. A {spice_level} balance enhances a rich array of spices, fresh vegetables, and traditional herbs, culminating in a memorable feast.")
    else:
        return f"{dish_name} is an extraordinary vegetarian dish with a unique blend of international flavors and a subtle note of {spice_level} spice."