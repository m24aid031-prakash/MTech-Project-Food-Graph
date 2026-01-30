import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch
import networkx as nx
from burger_graph import BurgerGraph
from burger_types import BURGER_TYPES
import os

# Create output directories for images
os.makedirs("burger_images/individual_diagrams", exist_ok=True)
os.makedirs("burger_images/comparisons", exist_ok=True)
os.makedirs("burger_images/networks", exist_ok=True)
os.makedirs("burger_images/distributions", exist_ok=True)

class BurgerVisualizer:
    """Create visual representations of burgers and their calorie information"""
    
    def __init__(self):
        self.graph = BurgerGraph()
    
    def draw_burger_diagram(self, burger_key, filename=None):
        """Draw a visual representation of a burger with layers and calorie info"""
        burger = BURGER_TYPES[burger_key]
        
        fig, ax = plt.subplots(figsize=(10, 12))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 15)
        ax.axis('off')
        
        # Title
        ax.text(5, 14, burger.name, fontsize=24, fontweight='bold', ha='center')
        ax.text(5, 13.3, f"Total: {burger.calculate_calories()} calories", 
                fontsize=18, ha='center', color='red')
        
        # Group ingredients by category for proper burger layer ordering
        categories = burger.get_ingredients_by_category()
        
        # Define layer order (bottom to top)
        layer_order = ['bun', 'sauce', 'vegetable', 'cheese', 'protein', 'extra', 'bun']
        
        # Organize ingredients by layer
        layers = []
        
        # Bottom bun
        if 'bun' in categories:
            layers.append(('Bottom ' + categories['bun'][0].name, categories['bun'][0].calories, '#F4A460'))
        
        # Add protein
        if 'protein' in categories:
            for ing in categories['protein']:
                color = '#8B4513' if 'beef' in ing.name.lower() else '#DEB887'
                layers.append((ing.name, ing.calories, color))
        
        # Add cheese
        if 'cheese' in categories:
            for ing in categories['cheese']:
                if ing.calories > 0:  # Skip "no cheese"
                    layers.append((ing.name, ing.calories, '#FFD700'))
        
        # Add extras
        if 'extra' in categories:
            for ing in categories['extra']:
                layers.append((ing.name, ing.calories, '#FF6347'))
        
        # Add vegetables
        if 'vegetable' in categories:
            for ing in categories['vegetable']:
                layers.append((ing.name, ing.calories, '#90EE90'))
        
        # Add sauces
        if 'sauce' in categories:
            for ing in categories['sauce']:
                layers.append((ing.name, ing.calories, '#FF4500'))
        
        # Top bun
        if 'bun' in categories:
            layers.append(('Top ' + categories['bun'][0].name, categories['bun'][0].calories, '#F4A460'))
        
        # Draw layers
        y_position = 2
        layer_height = 0.6
        
        for layer_name, calories, color in layers:
            # Draw layer rectangle
            rect = FancyBboxPatch((1, y_position), 8, layer_height, 
                                 boxstyle="round,pad=0.05", 
                                 facecolor=color, edgecolor='black', linewidth=2)
            ax.add_patch(rect)
            
            # Add text
            ax.text(5, y_position + layer_height/2, f"{layer_name}", 
                   fontsize=11, ha='center', va='center', fontweight='bold')
            ax.text(9.5, y_position + layer_height/2, f"{calories} cal", 
                   fontsize=10, ha='left', va='center', color='darkred', fontweight='bold')
            
            y_position += layer_height + 0.1
        
        # Add description at bottom
        description_words = burger.description.split()
        description_lines = []
        current_line = []
        for word in description_words:
            current_line.append(word)
            if len(' '.join(current_line)) > 50:
                description_lines.append(' '.join(current_line))
                current_line = []
        if current_line:
            description_lines.append(' '.join(current_line))
        
        y_desc = 1.2
        for line in reversed(description_lines):
            ax.text(5, y_desc, line, fontsize=10, ha='center', style='italic')
            y_desc -= 0.3
        
        plt.tight_layout()
        
        if filename:
            plt.savefig(f"burger_images/individual_diagrams/{filename}", dpi=300, bbox_inches='tight')
            print(f"Saved burger diagram: burger_images/individual_diagrams/{filename}")
        else:
            plt.savefig(f"burger_images/individual_diagrams/{burger_key}_diagram.png", dpi=300, bbox_inches='tight')
            print(f"Saved burger diagram: burger_images/individual_diagrams/{burger_key}_diagram.png")
        
        plt.close()
    
    def draw_all_burgers_comparison(self, filename="all_burgers_comparison.png"):
        """Create a bar chart comparing all burgers by calories"""
        burgers_data = [(key, burger.name, burger.calculate_calories()) 
                       for key, burger in BURGER_TYPES.items()]
        burgers_data.sort(key=lambda x: x[2])
        
        names = [b[1] for b in burgers_data]
        calories = [b[2] for b in burgers_data]
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Create color gradient based on calorie count
        colors = plt.cm.RdYlGn_r([c/max(calories) for c in calories])
        
        bars = ax.barh(names, calories, color=colors, edgecolor='black', linewidth=1.5)
        
        # Add calorie values on bars
        for i, (bar, cal) in enumerate(zip(bars, calories)):
            ax.text(bar.get_width() + 10, bar.get_y() + bar.get_height()/2, 
                   f'{cal} cal', va='center', fontweight='bold', fontsize=10)
        
        ax.set_xlabel('Calories', fontsize=14, fontweight='bold')
        ax.set_title('Burger Types Comparison by Calories', fontsize=18, fontweight='bold', pad=20)
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        
        plt.tight_layout()
        plt.savefig(f"burger_images/comparisons/{filename}", dpi=300, bbox_inches='tight')
        print(f"Saved comparison chart: burger_images/comparisons/{filename}")
        plt.close()
    
    def draw_graph_network(self, filename="burger_graph_network.png"):
        """Visualize the burger-ingredient graph network"""
        fig, ax = plt.subplots(figsize=(20, 16))
        
        # Create layout
        pos = nx.spring_layout(self.graph.graph, k=2, iterations=50, seed=42)
        
        # Separate nodes by type
        burger_nodes = [n for n, d in self.graph.graph.nodes(data=True) if d['type'] == 'burger']
        ingredient_nodes = [n for n, d in self.graph.graph.nodes(data=True) if d['type'] == 'ingredient']
        
        # Draw ingredient nodes
        nx.draw_networkx_nodes(self.graph.graph, pos, 
                              nodelist=ingredient_nodes,
                              node_color='lightblue',
                              node_size=1500,
                              node_shape='o',
                              alpha=0.7,
                              ax=ax)
        
        # Draw burger nodes
        nx.draw_networkx_nodes(self.graph.graph, pos,
                              nodelist=burger_nodes,
                              node_color='orange',
                              node_size=3000,
                              node_shape='s',
                              alpha=0.9,
                              ax=ax)
        
        # Draw edges
        nx.draw_networkx_edges(self.graph.graph, pos,
                              edge_color='gray',
                              alpha=0.3,
                              arrows=True,
                              arrowsize=10,
                              ax=ax)
        
        # Draw labels
        labels = {}
        for node, data in self.graph.graph.nodes(data=True):
            if data['type'] == 'burger':
                labels[node] = f"{data['name']}\n{data['total_calories']} cal"
            else:
                labels[node] = f"{data['name']}\n{data['calories']} cal"
        
        nx.draw_networkx_labels(self.graph.graph, pos, labels, 
                               font_size=7, font_weight='bold', ax=ax)
        
        ax.set_title('Burger-Ingredient Graph Network\n(Orange = Burgers, Blue = Ingredients)', 
                    fontsize=20, fontweight='bold', pad=20)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(f"burger_images/networks/{filename}", dpi=300, bbox_inches='tight')
        print(f"Saved graph network: burger_images/networks/{filename}")
        plt.close()
    
    def draw_calorie_distribution(self, filename="calorie_distribution.png"):
        """Draw a pie chart showing calorie distribution across categories for each burger"""
        fig, axes = plt.subplots(2, 4, figsize=(20, 10))
        axes = axes.flatten()
        
        for idx, (key, burger) in enumerate(BURGER_TYPES.items()):
            if idx >= len(axes):
                break
            
            categories = burger.get_ingredients_by_category()
            category_calories = {}
            
            for category, ingredients in categories.items():
                total = sum(ing.calories for ing in ingredients)
                if total > 0:  # Only include categories with calories
                    category_calories[category.title()] = total
            
            # Create pie chart
            if category_calories:
                colors = ['#F4A460', '#8B4513', '#FFD700', '#90EE90', '#FF4500', '#FF6347']
                wedges, texts, autotexts = axes[idx].pie(
                    category_calories.values(),
                    labels=category_calories.keys(),
                    autopct='%1.1f%%',
                    colors=colors[:len(category_calories)],
                    startangle=90
                )
                
                for autotext in autotexts:
                    autotext.set_color('white')
                    autotext.set_fontweight('bold')
                    autotext.set_fontsize(9)
                
                axes[idx].set_title(f"{burger.name}\n{burger.calculate_calories()} cal", 
                                   fontsize=11, fontweight='bold')
        
        # Hide unused subplots
        for idx in range(len(BURGER_TYPES), len(axes)):
            axes[idx].axis('off')
        
        plt.suptitle('Calorie Distribution by Category', fontsize=18, fontweight='bold', y=0.98)
        plt.tight_layout()
        plt.savefig(f"burger_images/distributions/{filename}", dpi=300, bbox_inches='tight')
        print(f"Saved calorie distribution: burger_images/distributions/{filename}")
        plt.close()

def generate_all_visualizations():
    """Generate all visualizations"""
    print("Generating burger visualizations...")
    print("=" * 80)
    
    visualizer = BurgerVisualizer()
    
    # Generate individual burger diagrams
    print("\nGenerating individual burger diagrams...")
    for key in BURGER_TYPES.keys():
        visualizer.draw_burger_diagram(key)
    
    # Generate comparison chart
    print("\nGenerating comparison chart...")
    visualizer.draw_all_burgers_comparison()
    
    # Generate graph network
    print("\nGenerating graph network visualization...")
    visualizer.draw_graph_network()
    
    # Generate calorie distribution
    print("\nGenerating calorie distribution charts...")
    visualizer.draw_calorie_distribution()
    
    print("\n" + "=" * 80)
    print("All visualizations generated successfully!")
    print(f"Check the 'burger_images' folder for all generated images.")
    print("=" * 80)

if __name__ == "__main__":
    generate_all_visualizations()
