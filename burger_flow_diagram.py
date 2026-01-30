import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import networkx as nx
from burger_graph import BurgerGraph
from burger_types import BURGER_TYPES
import os

# Create output directories for images
os.makedirs("burger_images/flow_diagrams", exist_ok=True)
os.makedirs("burger_images/hierarchical_flows", exist_ok=True)

class BurgerFlowDiagram:
    """Create calorie flow diagrams for individual burgers"""
    
    def __init__(self):
        self.graph = BurgerGraph()
    
    def draw_calorie_flow_diagram(self, burger_key, filename=None):
        """
        Draw a detailed flow diagram showing how calories flow from 
        individual ingredients to the total burger calorie count
        """
        burger = BURGER_TYPES[burger_key]
        total_calories = burger.calculate_calories()
        
        fig, ax = plt.subplots(figsize=(14, 10))
        ax.set_xlim(0, 14)
        ax.set_ylim(0, 12)
        ax.axis('off')
        
        # Title
        ax.text(7, 11, f"{burger.name} - Calorie Flow Diagram", 
                fontsize=22, fontweight='bold', ha='center')
        ax.text(7, 10.4, f"Total Calories: {total_calories}", 
                fontsize=18, ha='center', color='darkred', fontweight='bold')
        
        # Draw central burger node
        burger_circle = plt.Circle((7, 5.5), 1.2, color='orange', 
                                   ec='black', linewidth=3, zorder=3)
        ax.add_patch(burger_circle)
        ax.text(7, 5.5, f"{burger.name}\n{total_calories} cal", 
                fontsize=11, ha='center', va='center', 
                fontweight='bold', zorder=4)
        
        # Get ingredients by category
        categories = burger.get_ingredients_by_category()
        
        # Define positions for ingredient categories (arranged in a circle)
        category_positions = {
            'bun': (2, 9),
            'protein': (12, 9),
            'cheese': (12, 5.5),
            'vegetable': (12, 2),
            'sauce': (7, 1),
            'extra': (2, 2)
        }
        
        category_colors = {
            'bun': '#F4A460',
            'protein': '#8B4513',
            'cheese': '#FFD700',
            'vegetable': '#90EE90',
            'sauce': '#FF4500',
            'extra': '#FF6347'
        }
        
        # Track which categories are used
        used_categories = set(categories.keys())
        
        # Draw ingredients and arrows
        for category, ingredients in categories.items():
            if category not in category_positions:
                continue
            
            cat_x, cat_y = category_positions[category]
            color = category_colors.get(category, '#CCCCCC')
            
            # Calculate total calories for this category
            cat_total = sum(ing.calories for ing in ingredients)
            
            # Draw category box
            box_width = 2.5
            box_height = 0.4 + (len(ingredients) * 0.35)
            
            category_box = FancyBboxPatch(
                (cat_x - box_width/2, cat_y - box_height/2),
                box_width, box_height,
                boxstyle="round,pad=0.1",
                facecolor=color, edgecolor='black', 
                linewidth=2, alpha=0.8, zorder=2
            )
            ax.add_patch(category_box)
            
            # Category label
            ax.text(cat_x, cat_y + box_height/2 - 0.25, 
                   f"{category.upper()}", 
                   fontsize=10, ha='center', va='top', 
                   fontweight='bold', style='italic')
            
            # Draw individual ingredients
            y_offset = cat_y + box_height/2 - 0.55
            for ing in ingredients:
                if ing.calories > 0:  # Skip zero-calorie items
                    ax.text(cat_x, y_offset, 
                           f"• {ing.name}: {ing.calories} cal", 
                           fontsize=8, ha='center', va='top')
                    y_offset -= 0.35
            
            # Draw arrow from category to burger with calorie label
            if cat_total > 0:
                arrow = FancyArrowPatch(
                    (cat_x, cat_y - box_height/2 - 0.1) if cat_y > 5.5 else (cat_x, cat_y + box_height/2 + 0.1),
                    (7, 6.5) if cat_y > 5.5 else (7, 4.5),
                    arrowstyle='->,head_width=0.4,head_length=0.3',
                    color='gray', linewidth=2.5, alpha=0.7,
                    connectionstyle="arc3,rad=.2", zorder=1
                )
                ax.add_patch(arrow)
                
                # Add calorie label on arrow
                mid_x = (cat_x + 7) / 2
                mid_y = (cat_y + 5.5) / 2
                ax.text(mid_x, mid_y, f"{cat_total} cal", 
                       fontsize=9, ha='center', va='center',
                       bbox=dict(boxstyle='round,pad=0.3', 
                                facecolor='white', edgecolor='gray', alpha=0.9),
                       fontweight='bold', color='darkred')
        
        # Add legend
        legend_y = 0.3
        ax.text(7, legend_y, "Arrows show calorie contribution from each category to the total burger", 
               fontsize=9, ha='center', style='italic', color='gray')
        
        plt.tight_layout()
        
        if filename:
            plt.savefig(f"burger_images/flow_diagrams/{filename}", dpi=300, bbox_inches='tight')
            print(f"✓ Saved calorie flow diagram: burger_images/flow_diagrams/{filename}")
        else:
            plt.savefig(f"burger_images/flow_diagrams/{burger_key}_calorie_flow.png", 
                       dpi=300, bbox_inches='tight')
            print(f"✓ Saved calorie flow diagram: burger_images/flow_diagrams/{burger_key}_calorie_flow.png")
        
        plt.close()
    
    def draw_hierarchical_flow(self, burger_key, filename=None):
        """
        Draw a hierarchical tree-style flow diagram showing calorie flow
        from top (burger) to bottom (ingredients)
        """
        burger = BURGER_TYPES[burger_key]
        total_calories = burger.calculate_calories()
        
        fig, ax = plt.subplots(figsize=(16, 12))
        ax.set_xlim(0, 16)
        ax.set_ylim(0, 12)
        ax.axis('off')
        
        # Title
        ax.text(8, 11.5, f"{burger.name} - Hierarchical Calorie Breakdown", 
                fontsize=20, fontweight='bold', ha='center')
        
        # Draw main burger node at top
        main_box = FancyBboxPatch((6, 10), 4, 0.8,
                                 boxstyle="round,pad=0.1",
                                 facecolor='orange', edgecolor='black',
                                 linewidth=3, zorder=3)
        ax.add_patch(main_box)
        ax.text(8, 10.4, f"{burger.name}\nTotal: {total_calories} calories",
               fontsize=12, ha='center', va='center', fontweight='bold')
        
        # Get ingredients by category
        categories = burger.get_ingredients_by_category()
        
        # Calculate layout for categories
        num_categories = len(categories)
        category_y = 8
        
        category_colors = {
            'bun': '#F4A460',
            'protein': '#8B4513',
            'cheese': '#FFD700',
            'vegetable': '#90EE90',
            'sauce': '#FF4500',
            'extra': '#FF6347'
        }
        
        # Calculate spacing
        total_width = 14
        spacing = total_width / (num_categories + 1)
        
        x_positions = []
        for idx in range(num_categories):
            x_positions.append(1 + spacing * (idx + 1))
        
        # Draw categories and their ingredients
        for idx, (category, ingredients) in enumerate(sorted(categories.items())):
            cat_x = x_positions[idx]
            color = category_colors.get(category, '#CCCCCC')
            
            # Calculate total calories for category
            cat_total = sum(ing.calories for ing in ingredients)
            
            # Draw category box
            cat_box = FancyBboxPatch(
                (cat_x - 0.8, category_y - 0.3), 1.6, 0.6,
                boxstyle="round,pad=0.05",
                facecolor=color, edgecolor='black',
                linewidth=2, alpha=0.85, zorder=2
            )
            ax.add_patch(cat_box)
            ax.text(cat_x, category_y, f"{category.title()}\n{cat_total} cal",
                   fontsize=9, ha='center', va='center', fontweight='bold')
            
            # Draw arrow from burger to category
            arrow1 = FancyArrowPatch(
                (8, 10), (cat_x, category_y + 0.3),
                arrowstyle='->,head_width=0.3,head_length=0.2',
                color='gray', linewidth=2, alpha=0.6, zorder=1
            )
            ax.add_patch(arrow1)
            
            # Draw individual ingredients below category
            ing_y_start = 6.5
            ing_spacing = 0.7
            
            for ing_idx, ing in enumerate(ingredients):
                if ing.calories > 0:
                    ing_y = ing_y_start - (ing_idx * ing_spacing)
                    
                    # Draw ingredient box
                    ing_box = FancyBboxPatch(
                        (cat_x - 0.75, ing_y - 0.25), 1.5, 0.5,
                        boxstyle="round,pad=0.05",
                        facecolor='lightblue', edgecolor='black',
                        linewidth=1.5, alpha=0.7, zorder=2
                    )
                    ax.add_patch(ing_box)
                    
                    # Ingredient text
                    ax.text(cat_x, ing_y, f"{ing.name}\n{ing.calories} cal",
                           fontsize=7, ha='center', va='center')
                    
                    # Arrow from category to ingredient
                    arrow2 = FancyArrowPatch(
                        (cat_x, category_y - 0.3), (cat_x, ing_y + 0.25),
                        arrowstyle='->,head_width=0.2,head_length=0.15',
                        color='darkgray', linewidth=1.5, alpha=0.5, zorder=1
                    )
                    ax.add_patch(arrow2)
        
        # Add description
        ax.text(8, 0.5, burger.description, 
               fontsize=10, ha='center', style='italic', color='gray')
        
        plt.tight_layout()
        
        if filename:
            plt.savefig(f"burger_images/hierarchical_flows/{filename}", dpi=300, bbox_inches='tight')
            print(f"✓ Saved hierarchical flow diagram: burger_images/hierarchical_flows/{filename}")
        else:
            plt.savefig(f"burger_images/hierarchical_flows/{burger_key}_hierarchical_flow.png",
                       dpi=300, bbox_inches='tight')
            print(f"✓ Saved hierarchical flow diagram: burger_images/hierarchical_flows/{burger_key}_hierarchical_flow.png")
        
        plt.close()

def generate_flow_diagrams(burger_key=None):
    """Generate calorie flow diagrams for specific burger or all burgers"""
    visualizer = BurgerFlowDiagram()
    
    print("=" * 80)
    print("GENERATING BURGER CALORIE FLOW DIAGRAMS")
    print("=" * 80)
    
    if burger_key:
        # Generate for specific burger
        if burger_key in BURGER_TYPES:
            print(f"\nGenerating flow diagrams for {BURGER_TYPES[burger_key].name}...")
            visualizer.draw_calorie_flow_diagram(burger_key)
            visualizer.draw_hierarchical_flow(burger_key)
        else:
            print(f"Error: Burger '{burger_key}' not found!")
            print(f"Available burgers: {', '.join(BURGER_TYPES.keys())}")
    else:
        # Generate for all burgers (calorie flow only to avoid too many images)
        print("\nGenerating calorie flow diagrams for all burgers...")
        for key in BURGER_TYPES.keys():
            visualizer.draw_calorie_flow_diagram(key)
        
        # Generate hierarchical for just a few featured burgers
        print("\nGenerating hierarchical flow diagrams for featured burgers...")
        featured_burgers = ['classic', 'double_deluxe', 'veggie_delight']
        for key in featured_burgers:
            visualizer.draw_hierarchical_flow(key)
    
    print("\n" + "=" * 80)
    print("Flow diagrams generated successfully!")
    print("Check the 'burger_images' folder for the generated diagrams.")
    print("=" * 80)

def interactive_menu():
    """Interactive menu to select burger for flow diagram"""
    print("\n" + "=" * 80)
    print("BURGER CALORIE FLOW DIAGRAM GENERATOR")
    print("=" * 80)
    
    print("\nAvailable Burgers:")
    for idx, (key, burger) in enumerate(BURGER_TYPES.items(), 1):
        print(f"{idx}. {burger.name} ({burger.calculate_calories()} cal)")
    
    print(f"\n{len(BURGER_TYPES) + 1}. Generate for ALL burgers")
    print("0. Exit")
    
    try:
        choice = input("\nSelect a burger (enter number): ").strip()
        choice_num = int(choice)
        
        if choice_num == 0:
            print("Exiting...")
            return
        elif choice_num == len(BURGER_TYPES) + 1:
            generate_flow_diagrams()
        elif 1 <= choice_num <= len(BURGER_TYPES):
            burger_key = list(BURGER_TYPES.keys())[choice_num - 1]
            generate_flow_diagrams(burger_key)
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except KeyboardInterrupt:
        print("\n\nExiting...")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Command line argument provided
        burger_key = sys.argv[1]
        generate_flow_diagrams(burger_key)
    else:
        # Interactive menu
        interactive_menu()
