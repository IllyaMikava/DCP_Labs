# Star Map Visualization
# Name: Illya Mikava

import py5
import pandas as pd
import numpy as np

# Global variables
df = None
selected_star1 = None
selected_star2 = None

def load_data():
    """Load the star data from CSV file"""
    try:
        # Try different encodings
        df = pd.read_csv('HabHYG15ly.csv', encoding='utf-8')
        print(f"Successfully loaded {len(df)} stars")
        return df
    except UnicodeDecodeError:
        try:
            df = pd.read_csv('HabHYG15ly.csv', encoding='latin-1')
            print(f"Successfully loaded {len(df)} stars")
            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None
    except FileNotFoundError:
        print("Error: HabHYG15ly.csv file not found!")
        return None

def print_stars():
    """Print useful information about the stars"""
    if df is None:
        print("No data loaded")
        return
    
    print("\n=== STAR MAP DATA ===")
    print(f"Total number of stars: {len(df)}")
    print("\nFirst 5 stars:")
    print("-" * 80)
    
    for idx in range(min(5, len(df))):
        row = df.iloc[idx]
        print(f"Star: {row['Display Name']}")
        print(f"  Distance: {row['Distance']:.2f} parsecs")
        print(f"  Coordinates: X={row['Xg']:.2f}, Y={row['Yg']:.2f}, Z={row['Zg']:.2f}")
        print(f"  Magnitude: {row['AbsMag']:.2f}")
        if 'Hab?' in df.columns:
            print(f"  Habitable: {row['Hab?']}")
        print()
    
    # Statistics
    print("\n=== STATISTICS ===")
    print(f"Average distance: {df['Distance'].mean():.2f} parsecs")
    print(f"Closest star: {df.loc[df['Distance'].idxmin(), 'Display Name']} at {df['Distance'].min():.2f} parsecs")
    print(f"Farthest star: {df.loc[df['Distance'].idxmax(), 'Display Name']} at {df['Distance'].max():.2f} parsecs")
    
    if 'Hab?' in df.columns:
        habitable = df[df['Hab?'] == 1]
        print(f"Stars with habitable planets: {len(habitable)}")
    
    print("=" * 80 + "\n")

def parsecs_to_pixels(parsecs):
    """Convert parsecs to pixel coordinates"""
    return py5.remap(parsecs, -5, 5, 50, 750)

def pixels_to_parsecs(pixels):
    """Convert pixel coordinates to parsecs"""
    return py5.remap(pixels, 50, 750, -5, 5)

def calculate_distance(star1, star2):
    """Calculate 3D distance between two stars"""
    dx = star1['Xg'] - star2['Xg']
    dy = star1['Yg'] - star2['Yg']
    dz = star1['Zg'] - star2['Zg']
    return np.sqrt(dx**2 + dy**2 + dz**2)

def find_star_at_position(x, y):
    """Find if there's a star at the given pixel position"""
    if df is None:
        return None
    
    # Convert pixel position to parsecs
    x_parsec = pixels_to_parsecs(x)
    y_parsec = pixels_to_parsecs(y)
    
    # Check each star
    for idx, row in df.iterrows():
        star_x = parsecs_to_pixels(row['Xg'])
        star_y = parsecs_to_pixels(row['Yg'])
        
        # Calculate circle radius based on magnitude
        radius = max(5, py5.remap(row['AbsMag'], -2, 20, 20, 5))
        
        # Check if click is within star's radius
        dist = np.sqrt((x - star_x)**2 + (y - star_y)**2)
        if dist < radius + 5:  # Add some tolerance
            return row
    
    return None

def setup():
    global df
    py5.size(800, 800)
    
    # Load the data
    df = load_data()
    
    # Print star information
    if df is not None:
        print_stars()

def draw():
    global selected_star1, selected_star2
    
    py5.background(0)  # Black background
    
    # Draw grid
    draw_grid()
    
    # Draw stars
    if df is not None:
        draw_stars()
    
    # Draw selection lines
    if selected_star1 is not None:
        draw_selection_line()
    
    # Draw distance text
    if selected_star1 is not None and selected_star2 is not None:
        draw_distance_text()

def draw_grid():
    """Draw the coordinate grid"""
    py5.stroke(200, 100, 255)  # Bright purple
    py5.stroke_weight(1)
    
    border = 50
    grid_size = 700
    cell_size = grid_size / 10
    
    # Vertical lines
    for i in range(11):
        x = border + i * cell_size
        py5.line(x, border, x, border + grid_size)
    
    # Horizontal lines
    for i in range(11):
        y = border + i * cell_size
        py5.line(border, y, border + grid_size, y)
    
    # Labels
    py5.fill(200, 100, 255)
    py5.text_size(12)
    py5.text_align(py5.CENTER, py5.CENTER)
    
    labels = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
    for i in range(11):
        x = border + i * cell_size
        y = border + i * cell_size
        
        # X-axis labels (TOP)
        py5.text(str(labels[i]), x, border - 20)
        
        # Y-axis labels (left)
        py5.text(str(labels[i]), border - 20, y)

def draw_stars():
    """Draw all stars on the map"""
    for idx, row in df.iterrows():
        # Convert coordinates
        x = parsecs_to_pixels(row['Xg'])
        y = parsecs_to_pixels(row['Yg'])
        
        # Draw yellow cross
        py5.stroke(255, 255, 0)  # Yellow
        py5.stroke_weight(2)
        cross_size = 5
        py5.line(x - cross_size, y, x + cross_size, y)
        py5.line(x, y - cross_size, x, y + cross_size)
        
        # Draw red circle based on magnitude
        py5.stroke(255, 0, 0)  # Red
        py5.stroke_weight(2)
        py5.no_fill()
        
        # Map magnitude to circle size (smaller magnitude = brighter = bigger circle)
        diameter = py5.remap(row['AbsMag'], -2, 20, 40, 10)
        diameter = max(10, diameter)  # Minimum size
        
        py5.circle(x, y, diameter)
        
        # Draw star name
        py5.fill(255, 255, 255)  # White text
        py5.text_size(10)
        py5.text_align(py5.LEFT, py5.CENTER)
        py5.text(row['Display Name'], x + diameter/2 + 5, y)

def draw_selection_line():
    """Draw line from selected star to mouse or second star"""
    global selected_star1, selected_star2
    
    if selected_star1 is None:
        return
    
    x1 = parsecs_to_pixels(selected_star1['Xg'])
    y1 = parsecs_to_pixels(selected_star1['Yg'])
    
    py5.stroke(255, 255, 0)  # Yellow
    py5.stroke_weight(2)
    
    if selected_star2 is None:
        # Draw to mouse
        py5.line(x1, y1, py5.mouse_x, py5.mouse_y)
    else:
        # Draw to second star
        x2 = parsecs_to_pixels(selected_star2['Xg'])
        y2 = parsecs_to_pixels(selected_star2['Yg'])
        py5.line(x1, y1, x2, y2)

def draw_distance_text():
    """Draw the distance between two selected stars"""
    global selected_star1, selected_star2
    
    if selected_star1 is None or selected_star2 is None:
        return
    
    distance = calculate_distance(selected_star1, selected_star2)
    
    text = f"Distance from {selected_star1['Display Name']} to {selected_star2['Display Name']} is {distance:.2f} parsecs"
    
    # Draw text box at bottom
    py5.fill(0, 0, 0, 200)  # Semi-transparent black
    py5.no_stroke()
    py5.rect(0, 760, 800, 40)
    
    py5.fill(255, 255, 0)  # Yellow text
    py5.text_size(14)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text(text, 400, 780)

def mouse_pressed():
    """Handle mouse clicks for star selection"""
    global selected_star1, selected_star2
    
    # Find star at click position
    clicked_star = find_star_at_position(py5.mouse_x, py5.mouse_y)
    
    if clicked_star is not None:
        if selected_star1 is None:
            # First selection
            selected_star1 = clicked_star
            print(f"Selected first star: {clicked_star['Display Name']}")
        elif selected_star2 is None:
            # Second selection
            selected_star2 = clicked_star
            distance = calculate_distance(selected_star1, selected_star2)
            print(f"Selected second star: {clicked_star['Display Name']}")
            print(f"Distance: {distance:.2f} parsecs")
        else:
            # Reset and start over
            selected_star1 = clicked_star
            selected_star2 = None
            print(f"Reset - Selected first star: {clicked_star['Display Name']}")

py5.run_sketch()