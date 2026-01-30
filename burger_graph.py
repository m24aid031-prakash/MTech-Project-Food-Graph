import networkx as nx
from ingredients import INGREDIENTS
from burger_types import BURGER_TYPES

class BurgerGraph:
    """
    Graph-based representation of burgers and their ingredients.
    Uses NetworkX to create a directed graph where:
    - Burger nodes connect to ingredient nodes
    - Each edge has a 'calories' attribute
    """
    
    def __init__(self):
        self.graph = nx.DiGraph()
        self._build_graph()
    
    def _build_graph(self):
        """Build the complete burger-ingredient graph"""
        
        # Add ingredient nodes
        for ing_key, ingredient in INGREDIENTS.items():
            self.graph.add_node(
                f"ingredient_{ing_key}",
                type="ingredient",
                name=ingredient.name,
                calories=ingredient.calories,
                category=ingredient.category
            )
        
        # Add burger nodes and connect to ingredients
        for burger_key, burger in BURGER_TYPES.items():
            burger_node = f"burger_{burger_key}"
            self.graph.add_node(
                burger_node,
                type="burger",
                name=burger.name,
                description=burger.description,
                total_calories=burger.calculate_calories()
            )
            
            # Connect burger to its ingredients
            for ingredient in burger.ingredients:
                # Find the ingredient key
                ing_key = None
                for key, ing in INGREDIENTS.items():
                    if ing.name == ingredient.name:
                        ing_key = key
                        break
                
                if ing_key:
                    self.graph.add_edge(
                        burger_node,
                        f"ingredient_{ing_key}",
                        calories=ingredient.calories
                    )
    
    def get_burger_calories(self, burger_key):
        """Calculate total calories for a burger by traversing the graph"""
        burger_node = f"burger_{burger_key}"
        
        if burger_node not in self.graph:
            return None
        
        total_calories = 0
        # Get all ingredients connected to this burger
        for neighbor in self.graph.neighbors(burger_node):
            edge_data = self.graph.get_edge_data(burger_node, neighbor)
            total_calories += edge_data['calories']
        
        return total_calories
    
    def get_burger_ingredients(self, burger_key):
        """Get all ingredients for a specific burger"""
        burger_node = f"burger_{burger_key}"
        
        if burger_node not in self.graph:
            return []
        
        ingredients = []
        for neighbor in self.graph.neighbors(burger_node):
            node_data = self.graph.nodes[neighbor]
            ingredients.append({
                'name': node_data['name'],
                'calories': node_data['calories'],
                'category': node_data['category']
            })
        
        return ingredients
    
    def get_burgers_with_ingredient(self, ingredient_key):
        """Find all burgers that contain a specific ingredient"""
        ingredient_node = f"ingredient_{ingredient_key}"
        
        if ingredient_node not in self.graph:
            return []
        
        burgers = []
        # Get all predecessors (burgers that have this ingredient)
        for burger_node in self.graph.predecessors(ingredient_node):
            node_data = self.graph.nodes[burger_node]
            burgers.append({
                'name': node_data['name'],
                'total_calories': node_data['total_calories']
            })
        
        return burgers
    
    def get_burgers_by_calorie_range(self, min_cal, max_cal):
        """Find burgers within a specific calorie range"""
        matching_burgers = []
        
        for node, data in self.graph.nodes(data=True):
            if data['type'] == 'burger':
                total_cal = data['total_calories']
                if min_cal <= total_cal <= max_cal:
                    matching_burgers.append({
                        'name': data['name'],
                        'calories': total_cal,
                        'description': data['description']
                    })
        
        return sorted(matching_burgers, key=lambda x: x['calories'])
    
    def get_graph_stats(self):
        """Get statistics about the graph"""
        burger_nodes = [n for n, d in self.graph.nodes(data=True) if d['type'] == 'burger']
        ingredient_nodes = [n for n, d in self.graph.nodes(data=True) if d['type'] == 'ingredient']
        
        return {
            'total_nodes': self.graph.number_of_nodes(),
            'total_edges': self.graph.number_of_edges(),
            'burger_count': len(burger_nodes),
            'ingredient_count': len(ingredient_nodes),
            'avg_ingredients_per_burger': self.graph.number_of_edges() / len(burger_nodes) if burger_nodes else 0
        }
    
    def compare_burgers(self, burger_key1, burger_key2):
        """Compare two burgers by calories and ingredients"""
        burger1_cal = self.get_burger_calories(burger_key1)
        burger2_cal = self.get_burger_calories(burger_key2)
        
        burger1_ing = set(ing['name'] for ing in self.get_burger_ingredients(burger_key1))
        burger2_ing = set(ing['name'] for ing in self.get_burger_ingredients(burger_key2))
        
        common_ingredients = burger1_ing & burger2_ing
        unique_to_1 = burger1_ing - burger2_ing
        unique_to_2 = burger2_ing - burger1_ing
        
        return {
            'burger1_calories': burger1_cal,
            'burger2_calories': burger2_cal,
            'calorie_difference': abs(burger1_cal - burger2_cal),
            'common_ingredients': list(common_ingredients),
            'unique_to_burger1': list(unique_to_1),
            'unique_to_burger2': list(unique_to_2)
        }
