# 🍔 Food-Graph: Burger Calorie Calculator

A graph-based burger nutrition analysis system that calculates total calories for different burger types based on their ingredients using graph data structures.

## 📊 Project Overview

This project demonstrates how to use graph data structures to model relationships between burgers and their ingredients, enabling efficient calorie calculations and nutritional analysis.

### Features

- **8 Different Burger Types** with unique ingredient combinations
- **30+ Ingredients** categorized by type (buns, proteins, cheese, vegetables, sauces, extras)
- **Graph-Based Architecture** using NetworkX for relationship modeling
- **Calorie Calculation Engine** that traverses the graph to compute total calories
- **Visual Representations** including burger diagrams, comparison charts, and network graphs
- **Advanced Queries** to find burgers by calorie range, common ingredients, and more

## 🍔 Available Burger Types

| Burger Name | Calories | Description |
|-------------|----------|-------------|
| Keto Burger | 555 cal | Low-carb burger wrapped in lettuce |
| Veggie Delight Burger | 580 cal | Healthy vegetarian option packed with veggies |
| Spicy Turkey Burger | 585 cal | Lean turkey burger with a spicy kick |
| Classic Burger | 665 cal | Traditional American burger with all the classics |
| Chicken Club Burger | 675 cal | Grilled chicken with bacon and Swiss cheese |
| BBQ Bacon Burger | 705 cal | Smoky BBQ flavor with crispy bacon |
| Breakfast Burger | 770 cal | Start your day with this hearty breakfast burger |
| Double Deluxe Burger | 1055 cal | Premium burger with double beef and bacon |

## 🏗️ Project Structure

```
Food-Graph/
│
├── ingredients.py           # Ingredient definitions with calorie values
├── burger_types.py          # Burger type definitions with ingredient lists
├── burger_graph.py          # Graph data structure implementation
├── calorie_calculator.py    # Main calculator and analysis engine
├── visualize_burgers.py     # Visualization generation
├── burger_flow_diagram.py   # Calorie flow diagram generator
├── requirements.txt         # Python dependencies
├── README.md               # This file
│
└── burger_images/          # Generated visualizations (created when running scripts)
    ├── individual_diagrams/   # Layer-by-layer burger diagrams
    │   ├── classic_diagram.png
    │   ├── double_deluxe_diagram.png
    │   └── ...
    ├── comparisons/           # Comparison charts
    │   └── all_burgers_comparison.png
    ├── networks/              # Graph network visualizations
    │   └── burger_graph_network.png
    ├── distributions/         # Calorie distribution pie charts
    │   └── calorie_distribution.png
    ├── flow_diagrams/         # Radial calorie flow diagrams
    │   ├── classic_calorie_flow.png
    │   └── ...
    └── hierarchical_flows/    # Hierarchical flow diagrams
        ├── classic_hierarchical_flow.png
        └── ...
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone or navigate to the project directory:
```bash
cd c:\Projects\Learning\Food-Graph
```

2. Install required dependencies:
```bash
pip install networkx matplotlib
```

### Usage

#### 1. Run the Calorie Calculator

Display all burgers, their ingredients, and calorie breakdowns:

```bash
python calorie_calculator.py
```

This will show:
- Complete list of all burger types with ingredient breakdowns
- Calorie rankings from lowest to highest
- Graph-based calorie calculations
- Burger comparisons

#### 2. Generate Visualizations

Create visual diagrams and charts:

```bash
python visualize_burgers.py
```

This generates:
- Individual burger layer diagrams for each burger type
- Comparison bar chart of all burgers
- Graph network showing burger-ingredient relationships
- Pie charts showing calorie distribution by category

All images are organized in categorized subfolders within `burger_images/`:
- `individual_diagrams/` - Layer-by-layer burger diagrams
- `comparisons/` - Burger comparison charts
- `networks/` - Graph network visualizations
- `distributions/` - Calorie distribution pie charts

#### 3. Generate Calorie Flow Diagrams

Create detailed flow diagrams showing how calories flow from ingredients to the burger:

```bash
python burger_flow_diagram.py
```

This opens an interactive menu where you can:
- Select a specific burger to visualize
- Generate flow diagrams for all burgers
- View both radial and hierarchical flow layouts

Or generate for a specific burger directly:

```bash
python burger_flow_diagram.py classic
```

Flow diagrams show:
- Radial layout with ingredients grouped by category
- Arrows showing calorie contribution from each category
- Hierarchical tree structure from burger → categories → ingredients

Images are saved in:
- `burger_images/flow_diagrams/` - Radial calorie flow diagrams
- `burger_images/hierarchical_flows/` - Hierarchical tree diagrams

## 📊 Graph Structure

The project uses a **directed graph** where:

- **Nodes** represent either burgers or ingredients
- **Edges** connect burgers to their ingredients
- **Edge weights** represent the calorie contribution of each ingredient

### Graph Operations

```python
from burger_graph import BurgerGraph

graph = BurgerGraph()

# Get calories for a specific burger
calories = graph.get_burger_calories("classic")

# Find all burgers with bacon
bacon_burgers = graph.get_burgers_with_ingredient("bacon")

# Get burgers in a calorie range
medium_cal_burgers = graph.get_burgers_by_calorie_range(400, 600)

# Compare two burgers
comparison = graph.compare_burgers("classic", "keto_burger")
```

## 🧪 Example Code

### Calculate Calories for a Burger

```python
from burger_types import BURGER_TYPES

# Get a specific burger
classic = BURGER_TYPES["classic"]

# Calculate total calories
total_calories = classic.calculate_calories()
print(f"{classic.name}: {total_calories} calories")

# Get ingredients by category
categories = classic.get_ingredients_by_category()
for category, ingredients in categories.items():
    print(f"{category}:")
    for ing in ingredients:
        print(f"  - {ing.name}: {ing.calories} cal")
```

### Custom Burger Creation

```python
from burger_types import Burger

# Create a custom burger
my_burger = Burger(
    name="My Custom Burger",
    ingredients_list=[
        "brioche_bun",
        "beef_patty",
        "swiss_cheese",
        "avocado",
        "bacon",
        "special_sauce"
    ],
    description="My perfect burger creation"
)

print(f"Total Calories: {my_burger.calculate_calories()}")
```

## 📈 Ingredient Categories

- **Buns**: White, Whole Wheat, Brioche, Lettuce Wrap
- **Proteins**: Beef, Chicken, Veggie, Turkey, Double Beef
- **Cheese**: Cheddar, Swiss, American, or No Cheese
- **Vegetables**: Lettuce, Tomato, Onion, Pickles, Jalapeños, Avocado
- **Sauces**: Ketchup, Mustard, Mayo, BBQ, Special Sauce
- **Extras**: Bacon, Fried Egg, Sautéed Mushrooms

## 🎯 Key Concepts Demonstrated

1. **Graph Data Structures**: Using NetworkX to model complex relationships
2. **Object-Oriented Design**: Clean class hierarchies for Ingredients and Burgers
3. **Data Aggregation**: Calculating totals by traversing graph edges
4. **Data Visualization**: Creating meaningful charts and diagrams with Matplotlib
5. **Nutritional Analysis**: Comparing food items by calorie content

## 🔍 Advanced Features

- **Calorie Range Queries**: Find burgers within specific calorie limits
- **Ingredient Search**: Identify all burgers containing a specific ingredient
- **Burger Comparison**: Analyze differences between two burger types
- **Graph Statistics**: Get insights about the entire burger-ingredient network
- **Visual Layer Diagrams**: See burger construction with calorie-coded layers

## 📝 Adding New Burgers

To add a new burger type:

1. Open `burger_types.py`
2. Add a new entry to the `BURGER_TYPES` dictionary:

```python
"my_new_burger": Burger(
    name="My New Burger",
    ingredients_list=[
        "whole_wheat_bun",
        "chicken_patty",
        "cheddar_cheese",
        "lettuce",
        "tomato",
        "mayo"
    ],
    description="A delicious new burger creation"
)
```

3. Run the scripts to see your new burger in the analysis and visualizations!

## 🤝 Contributing

Feel free to extend this project by:
- Adding more ingredients
- Creating new burger types
- Implementing additional graph algorithms
- Adding nutritional information beyond calories (protein, fat, carbs)
- Creating interactive web visualizations

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Built with NetworkX for graph operations
- Visualizations created with Matplotlib
- Calorie data is approximate for demonstration purposes

---

**Enjoy exploring the delicious world of graph-based burger analysis! 🍔📊**
