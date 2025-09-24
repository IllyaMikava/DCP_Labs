import py5

# Mode definitions
MODE_SMILEY = 0
MODE_RED_CIRCLE = 1
MODE_BLUE_SQUARE = 2
MODE_MUSHROOM = 3

mode = MODE_SMILEY
last_pressed = False
prev_mouse_x = 0 
prev_mouse_y = 0 

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)
    py5.ellipse_mode(py5.CENTER)

def draw():
    global mode, last_pressed, prev_mouse_x, prev_mouse_y
    
    py5.background(0)
    
    # Draw based on current mode
    if mode == MODE_SMILEY:
        draw_smiley()
    elif mode == MODE_RED_CIRCLE:
        draw_red_circle()
    elif mode == MODE_BLUE_SQUARE:
        draw_blue_square()
    elif mode == MODE_MUSHROOM:
        draw_mushroom()
    
    # Handle mode switching with keyboard
    if py5.is_key_pressed:
        if not last_pressed:
            mode = (mode + 1) % 4
        last_pressed = True
    else:
        last_pressed = False
        
    prev_mouse_x = py5.mouse_x
    prev_mouse_y = py5.mouse_y

def mouse_pressed():
    global mode
    mode = (mode + 1) % 4  # toggle modes on click

def draw_smiley():
    x, y = py5.mouse_x, py5.mouse_y
    
    # Face
    py5.fill(255, 255, 0)
    py5.ellipse(x, y, 100, 100)
    
    # Eyes
    py5.fill(0)
    py5.ellipse(x - 20, y - 10, 15, 20)
    py5.ellipse(x + 20, y - 10, 15, 20)
    
    # Mouth
    py5.no_fill()
    py5.stroke(0)
    py5.arc(x, y + 10, 40, 30, 0, py5.PI)
    py5.no_stroke()

def draw_red_circle():
    cx, cy = py5.width // 2, py5.height // 2
    dx = py5.mouse_x - cx
    dy = py5.mouse_y - cy
    dist_from_center = (dx * dx + dy * dy) ** 0.5  # diameter with pythagoras
    py5.no_stroke()
    py5.fill(220, 40, 40)
    py5.circle(cx, cy, dist_from_center)

def draw_blue_square():
    # Draw a square in the middle of the screen
    center_x = py5.width // 2
    center_y = py5.height // 2
    size = 100
    
    py5.fill(0, 100, 255)  # Blue color
    py5.no_stroke()
    py5.rect(center_x, center_y, size, size)

def draw_mushroom():
    x, y = py5.mouse_x, py5.mouse_y
    
    # Stem
    py5.fill(255)
    py5.rect(x, y + 30, 20, 60)
    
    # Cap
    py5.fill(255, 0, 0)
    py5.ellipse(x, y, 80, 40)
    
    # White spots
    py5.fill(255)
    py5.no_stroke()
    py5.ellipse(x - 15, y - 5, 15, 15)
    py5.ellipse(x + 15, y - 5, 15, 15)
    py5.ellipse(x, y + 5, 15, 15)

py5.run_sketch()