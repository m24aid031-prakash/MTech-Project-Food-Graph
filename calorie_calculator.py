from burger_graph import BurgerGraph
from burger_types import BURGER_TYPES
from ingredients import INGREDIENTS

def print_separator(char="=", length=80):
    """Print a separator line"""
    print(char * length)

def display_all_burgers():
    """Display all burger types with their calorie information"""
    print_separator()
    print("ALL BURGER TYPES AND THEIR CALORIE COUNTS")
    print_separator()
    
    for key, burger in BURGER_TYPES.items():
        print(f"\n{burger.name}")
        print(f"Description: {burger.description}")
        print(f"Total Calories: {burger.calculate_calories()}")
        print("\nIngredients:")
        
        categories = burger.get_ingredients_by_category()
        for category, ingredients in sorted(categories.items()):
            print(f"  {category.title()}:")
            for ing in ingredients:
                print(f"    - {ing.name}: {ing.calories} cal")
        print("-" * 80)

def display_calorie_analysis():
    """Display calorie analysis and comparisons"""
    print_separator()
    print("CALORIE ANALYSIS")
    print_separator()
    
    # Find highest and lowest calorie burgers
    burgers_with_calories = [(key, burger.name, burger.calculate_calories()) 
                             for key, burger in BURGER_TYPES.items()]
    burgers_with_calories.sort(key=lambda x: x[2])
    
    lowest = burgers_with_calories[0]
    highest = burgers_with_calories[-1]
    
    print(f"\nLowest Calorie Burger: {lowest[1]} - {lowest[2]} calories")
    print(f"Highest Calorie Burger: {highest[1]} - {highest[2]} calories")
    print(f"Calorie Difference: {highest[2] - lowest[2]} calories")
    
    print("\n\nAll Burgers Ranked by Calories:")
    for key, name, calories in burgers_with_calories:
        bar = "█" * (calories // 20)
        print(f"{name:30s} {calories:4d} cal {bar}")

def display_graph_operations():
    """Display graph-based operations and queries"""
    print_separator()
    print("GRAPH-BASED CALORIE CALCULATIONS")
    print_separator()
    
    graph = BurgerGraph()
    
    # Display graph statistics
    stats = graph.get_graph_stats()
    print("\nGraph Statistics:")
    print(f"  Total Nodes: {stats['total_nodes']}")
    print(f"  Total Edges: {stats['total_edges']}")
    print(f"  Burger Types: {stats['burger_count']}")
    print(f"  Unique Ingredients: {stats['ingredient_count']}")
    print(f"  Avg Ingredients per Burger: {stats['avg_ingredients_per_burger']:.1f}")
    
    # Show burgers by calorie range
    print("\n\nBurgers by Calorie Range:")
    
    ranges = [
        (0, 400, "Low Calorie (< 400)"),
        (400, 600, "Medium Calorie (400-600)"),
        (600, 1000, "High Calorie (> 600)")
    ]
    
    for min_cal, max_cal, label in ranges:
        burgers = graph.get_burgers_by_calorie_range(min_cal, max_cal)
        print(f"\n{label}:")
        if burgers:
            for burger in burgers:
                print(f"  - {burger['name']}: {burger['calories']} cal")
        else:
            print("  None")
    
    # Find burgers with specific ingredients
    print("\n\nBurgers containing Bacon:")
    bacon_burgers = graph.get_burgers_with_ingredient("bacon")
    for burger in bacon_burgers:
        print(f"  - {burger['name']}: {burger['total_calories']} cal")
    
    print("\n\nBurgers containing Avocado:")
    avocado_burgers = graph.get_burgers_with_ingredient("avocado")
    for burger in avocado_burgers:
        print(f"  - {burger['name']}: {burger['total_calories']} cal")

def compare_two_burgers(burger1_key, burger2_key):
    """Compare two specific burgers"""
    graph = BurgerGraph()
    comparison = graph.compare_burgers(burger1_key, burger2_key)
    
    burger1_name = BURGER_TYPES[burger1_key].name
    burger2_name = BURGER_TYPES[burger2_key].name
    
    print_separator()
    print(f"COMPARING: {burger1_name} vs {burger2_name}")
    print_separator()
    
    print(f"\n{burger1_name}: {comparison['burger1_calories']} calories")
    print(f"{burger2_name}: {comparison['burger2_calories']} calories")
    print(f"Difference: {comparison['calorie_difference']} calories")
    
    print(f"\nCommon Ingredients ({len(comparison['common_ingredients'])}):")
    for ing in sorted(comparison['common_ingredients']):
        print(f"  - {ing}")
    
    print(f"\nUnique to {burger1_name} ({len(comparison['unique_to_burger1'])}):")
    for ing in sorted(comparison['unique_to_burger1']):
        print(f"  - {ing}")
    
    print(f"\nUnique to {burger2_name} ({len(comparison['unique_to_burger2'])}):")
    for ing in sorted(comparison['unique_to_burger2']):
        print(f"  - {ing}")

def main():
    """Main function to run all calorie calculations"""
    print("\n" + "=" * 80)
    print(" " * 20 + "BURGER CALORIE CALCULATOR")
    print(" " * 15 + "Graph-Based Nutrition Analysis")
    print("=" * 80)
    
    # Display all burgers
    display_all_burgers()
    
    # Display calorie analysis
    display_calorie_analysis()
    
    # Display graph operations
    display_graph_operations()
    
    # Compare specific burgers
    print("\n")
    compare_two_burgers("classic", "double_deluxe")
    
    print("\n")
    compare_two_burgers("veggie_delight", "keto_burger")
    
    print("\n" + "=" * 80)
    print("Analysis Complete!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
