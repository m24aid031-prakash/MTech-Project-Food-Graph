# Ingredient definitions with calorie values
class Ingredient:
    def __init__(self, name, calories, category):
        self.name = name
        self.calories = calories
        self.category = category
    
    def __repr__(self):
        return f"{self.name} ({self.calories} cal)"

# Define all burger ingredients with their calorie values
INGREDIENTS = {
    # Buns
    "white_bun": Ingredient("White Bun", 150, "bun"),
    "whole_wheat_bun": Ingredient("Whole Wheat Bun", 120, "bun"),
    "brioche_bun": Ingredient("Brioche Bun", 180, "bun"),
    "lettuce_wrap": Ingredient("Lettuce Wrap", 10, "bun"),
    
    # Proteins
    "beef_patty": Ingredient("Beef Patty", 250, "protein"),
    "chicken_patty": Ingredient("Chicken Patty", 180, "protein"),
    "veggie_patty": Ingredient("Veggie Patty", 120, "protein"),
    "turkey_patty": Ingredient("Turkey Patty", 170, "protein"),
    "double_beef": Ingredient("Double Beef Patty", 500, "protein"),
    
    # Cheese
    "cheddar_cheese": Ingredient("Cheddar Cheese", 110, "cheese"),
    "swiss_cheese": Ingredient("Swiss Cheese", 100, "cheese"),
    "american_cheese": Ingredient("American Cheese", 95, "cheese"),
    "no_cheese": Ingredient("No Cheese", 0, "cheese"),
    
    # Vegetables
    "lettuce": Ingredient("Lettuce", 5, "vegetable"),
    "tomato": Ingredient("Tomato", 10, "vegetable"),
    "onion": Ingredient("Onion", 15, "vegetable"),
    "pickles": Ingredient("Pickles", 5, "vegetable"),
    "jalapenos": Ingredient("Jalapeños", 5, "vegetable"),
    "avocado": Ingredient("Avocado", 80, "vegetable"),
    
    # Sauces
    "ketchup": Ingredient("Ketchup", 20, "sauce"),
    "mustard": Ingredient("Mustard", 10, "sauce"),
    "mayo": Ingredient("Mayonnaise", 90, "sauce"),
    "bbq_sauce": Ingredient("BBQ Sauce", 30, "sauce"),
    "special_sauce": Ingredient("Special Sauce", 50, "sauce"),
    
    # Extras
    "bacon": Ingredient("Bacon", 80, "extra"),
    "fried_egg": Ingredient("Fried Egg", 90, "extra"),
    "mushrooms": Ingredient("Sautéed Mushrooms", 30, "extra"),
}
