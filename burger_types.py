from ingredients import INGREDIENTS

# Define different burger types with their ingredients
class Burger:
    def __init__(self, name, ingredients_list, description=""):
        self.name = name
        self.ingredients = [INGREDIENTS[ing] for ing in ingredients_list]
        self.description = description
    
    def calculate_calories(self):
        return sum(ing.calories for ing in self.ingredients)
    
    def get_ingredients_by_category(self):
        categories = {}
        for ing in self.ingredients:
            if ing.category not in categories:
                categories[ing.category] = []
            categories[ing.category].append(ing)
        return categories
    
    def __repr__(self):
        return f"{self.name} - {self.calculate_calories()} calories"

# Define various burger types
BURGER_TYPES = {
    "classic": Burger(
        name="Classic Burger",
        ingredients_list=[
            "white_bun",
            "beef_patty",
            "cheddar_cheese",
            "lettuce",
            "tomato",
            "onion",
            "pickles",
            "ketchup",
            "mustard"
        ],
        description="Traditional American burger with all the classics"
    ),
    
    "double_deluxe": Burger(
        name="Double Deluxe Burger",
        ingredients_list=[
            "brioche_bun",
            "double_beef",
            "cheddar_cheese",
            "lettuce",
            "tomato",
            "onion",
            "bacon",
            "special_sauce"
        ],
        description="Premium burger with double beef and bacon"
    ),
    
    "chicken_club": Burger(
        name="Chicken Club Burger",
        ingredients_list=[
            "whole_wheat_bun",
            "chicken_patty",
            "swiss_cheese",
            "lettuce",
            "tomato",
            "bacon",
            "mayo"
        ],
        description="Grilled chicken with bacon and Swiss cheese"
    ),
    
    "veggie_delight": Burger(
        name="Veggie Delight Burger",
        ingredients_list=[
            "whole_wheat_bun",
            "veggie_patty",
            "no_cheese",
            "lettuce",
            "tomato",
            "onion",
            "avocado",
            "mushrooms",
            "mustard"
        ],
        description="Healthy vegetarian option packed with veggies"
    ),
    
    "spicy_turkey": Burger(
        name="Spicy Turkey Burger",
        ingredients_list=[
            "whole_wheat_bun",
            "turkey_patty",
            "american_cheese",
            "lettuce",
            "tomato",
            "jalapenos",
            "onion",
            "mayo"
        ],
        description="Lean turkey burger with a spicy kick"
    ),
    
    "breakfast_burger": Burger(
        name="Breakfast Burger",
        ingredients_list=[
            "brioche_bun",
            "beef_patty",
            "cheddar_cheese",
            "fried_egg",
            "bacon",
            "ketchup"
        ],
        description="Start your day with this hearty breakfast burger"
    ),
    
    "keto_burger": Burger(
        name="Keto Burger",
        ingredients_list=[
            "lettuce_wrap",
            "beef_patty",
            "cheddar_cheese",
            "bacon",
            "avocado",
            "mayo"
        ],
        description="Low-carb burger wrapped in lettuce"
    ),
    
    "bbq_bacon": Burger(
        name="BBQ Bacon Burger",
        ingredients_list=[
            "white_bun",
            "beef_patty",
            "cheddar_cheese",
            "bacon",
            "onion",
            "bbq_sauce"
        ],
        description="Smoky BBQ flavor with crispy bacon"
    ),
}
