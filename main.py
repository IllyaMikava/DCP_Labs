import py5

mode = 0
last_pressed = False
prev_mouse_x = 0 
prev_mouse_y = 0 
circle_size = 50.0
base_size = 50.0
direction_vector = [0, 0]

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)
    py5.ellipse_mode(py5.CENTER)

def draw():
    global mode, last_pressed, prev_mouse_x, prev_mouse_y, circle_size, direction_vector
    
    py5.background(0)
    
    if mode == 0:
        draw_face()
    elif mode == 1:
        draw_circle()
    elif mode == 2:
        draw_squares()
    elif mode == 3:
        draw_amanita()
    
    if py5.is_key_pressed:
        if not last_pressed:
            mode = (mode + 1) % 4
        last_pressed = True
    else:
        last_pressed = False
        
    prev_mouse_x = py5.mouse_x
    prev_mouse_y = py5.mouse_y

def draw_face():
    x, y = py5.mouse_x, py5.mouse_y
    
    py5.fill(255, 255, 0)
    py5.ellipse(x, y, 100, 100)
    
    py5.fill(0)
    py5.ellipse(x - 20, y - 10, 15, 20)
    py5.ellipse(x + 20, y - 10, 15, 20)
    
    py5.no_fill()
    py5.stroke(0)
    py5.arc(x, y + 10, 40, 30, 0, py5.PI)

def draw_circle():
    global circle_size, direction_vector
    
    x, y = py5.mouse_x, py5.mouse_y
    
    current_vector = [x - prev_mouse_x, y - prev_mouse_y]
    
    dot_product = current_vector[0] * direction_vector[0] + current_vector[1] * direction_vector[1]
    
    if abs(current_vector[0]) > 0 or abs(current_vector[1]) > 0:
        movement_distance = py5.dist(0, 0, current_vector[0], current_vector[1]) * 0.8
        
        if dot_product > 0:
            circle_size += movement_distance
        else:
            circle_size -= movement_distance
        
        direction_vector = current_vector
    
    else:
        if circle_size > base_size:
            circle_size -= 1
        elif circle_size < base_size:
            circle_size += 1
    
    circle_size = py5.constrain(circle_size, 10.0, 400.0)
    
    py5.fill(100, 150, 255, 180)
    py5.no_stroke()
    py5.ellipse(x, y, circle_size, circle_size)

def draw_squares():
    x, y = py5.mouse_x, py5.mouse_y
    
    for i in range(7):
        offset_x = py5.random_int(-70, 70)
        offset_y = py5.random_int(-70, 70)
        size = py5.random_int(15, 45)
        r = py5.random_int(50, 200)
        g = py5.random_int(50, 200)
        b = py5.random_int(50, 200)
        
        py5.fill(r, g, b, 180)
        py5.no_stroke()
        py5.rect(x + offset_x, y + offset_y, size, size)

def draw_amanita():
    x, y = py5.mouse_x, py5.mouse_y
    
    py5.fill(255)
    py5.rect(x, y + 30, 20, 60)
    
    py5.fill(255, 0, 0)
    py5.ellipse(x, y, 80, 40)
    
    py5.fill(255)
    py5.no_stroke()
    py5.ellipse(x - 15, y - 5, 15, 15)
    py5.ellipse(x + 15, y - 5, 15, 15)
    py5.ellipse(x, y + 5, 15, 15)

py5.run_sketch()