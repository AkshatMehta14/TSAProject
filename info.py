sample_dishes = [
    {
        "name": "Paneer Tikka Masala",
        "origin": "Indian",
        "description": "Grilled paneer cubes marinated in yogurt and spices, roasted in a tandoor, then simmered in a creamy tomato-based sauce.",
        "price": 12.99,
        "spiciness": 0.7  # Spicier dish (0-1 scale)
    },
    {
        "name": "Vegetarian Pad Thai",
        "origin": "Thai",
        "description": "Rice noodles stir-fried with tofu, eggs, scallions, bean sprouts, and peanuts in a tangy tamarind sauce.",
        "price": 11.49,
        "spiciness": 0.6  # Medium-high spice
    },
    {
        "name": "Ratatouille",
        "origin": "French",
        "description": "A rustic vegetable stew made with eggplant, zucchini, bell peppers, and tomatoes, slow-cooked with Provencal herbs.",
        "price": 13.75,
        "spiciness": 0.2  # Mild dish
    },
    {
        "name": "Falafel Bowl",
        "origin": "Middle Eastern",
        "description": "Golden-brown falafel balls served over couscous with hummus, pickled vegetables, cucumber salad, and tahini drizzle.",
        "price": 10.95,
        "spiciness": 0.4  # Medium spice
    },
    {
        "name": "Caprese Salad",
        "origin": "Italian",
        "description": "Layers of fresh mozzarella, tomatoes, and basil, finished with sea salt, olive oil, and balsamic glaze.",
        "price": 8.50,
        "spiciness": 0.1  # Very mild
    },
    {
        "name": "Vegetarian Bibimbap",
        "origin": "Korean",
        "description": "A sizzling rice bowl topped with sautéed vegetables, marinated tofu, pickled radish, and a spicy gochujang sauce.",
        "price": 12.25,
        "spiciness": 0.8  # Very spicy
    },
    {
        "name": "Chickpea Tagine",
        "origin": "North African",
        "description": "Slow-cooked chickpeas, sweet potatoes, and apricots in a spiced tomato broth with cinnamon and cumin.",
        "price": 11.95,
        "spiciness": 0.5  # Medium spice
    },
    {
        "name": "Greek Spanakopita",
        "origin": "Mediterranean",
        "description": "Flaky phyllo pastry stuffed with spinach, feta cheese, onions, and herbs, baked until golden and crispy.",
        "price": 9.75,
        "spiciness": 0.2  # Mild dish
    },
    {
        "name": "Vegetarian Biryani",
        "origin": "Indian",
        "description": "Aromatic basmati rice cooked with mixed vegetables, saffron, and fragrant spices, served with cooling raita.",
        "price": 13.25,
        "spiciness": 0.75  # Quite spicy
    },
    {
        "name": "Vegetable Gyoza",
        "origin": "Japanese",
        "description": "Pan-fried dumplings filled with cabbage, carrots, and shiitake mushrooms, served with a soy dipping sauce.",
        "price": 7.95,
        "spiciness": 0.3  # Mild to medium
    },
    {
        "name": "Tofu Stir Fry",
        "origin": "Asian",
        "description": "Crispy tofu cubes tossed in garlic-ginger sauce with seasonal vegetables over steamed jasmine rice.",
        "price": 10.99,
        "spiciness": 0.5  # Medium spice
    },
    {
        "name": "Vegetarian Paella",
        "origin": "Spanish",
        "description": "A saffron-infused rice dish with roasted vegetables, chickpeas, and artichoke hearts cooked in vegetable stock.",
        "price": 14.50,
        "spiciness": 0.4  # Medium spice
    }
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