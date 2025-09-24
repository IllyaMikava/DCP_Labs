import py5

def setup():
    py5.size(800, 600)
    py5.rect_mode(py5.CENTER)
    
def draw():
    py5.background(0)
    
    rect_width = 350
    rect_height = 150
    center_x = py5.width / 2
    center_y = py5.height / 2
    
    # Calculation positiopn of recatngle
    left = center_x - rect_width / 2
    right = center_x + rect_width / 2
    top = center_y - rect_height / 2
    bottom = center_y + rect_height / 2
    
    # if else hover
    if (py5.mouse_x > left and py5.mouse_x < right and
        py5.mouse_y > top and py5.mouse_y < bottom):
        py5.fill(0, 255, 0)  # Green when hovering
    else:
        py5.fill(255, 0, 0)  # Red when not hovering
    
    py5.rect(center_x, center_y, rect_width, rect_height)

py5.run_sketch()