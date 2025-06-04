'''
Eliza Hardy
Project Variation #4 
Made stars and towers refactored, can be resized and moved around

'''


# loads the Turtle graphics module, which is a built-in library in Python
import turtle
import math

def setup_turtle():
    """Initialize turtle with standard settings"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    screen = turtle.Screen()
    screen.title("Turtle Graphics Assignment")
    return t, screen


def draw_rectangle(t, width, height, fill_color=None):
    """Draw a rectangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    """Draw a square with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()


def draw_triangle(t, size, fill_color=None):
    """Draw an equilateral triangle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()


def draw_circle(t, radius, fill_color=None):
    """Draw a circle with optional fill"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()


def draw_polygon(t, sides, size, fill_color=None):
    """Draw a regular polygon with given number of sides"""
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def draw_curve(t, length, curve_factor, segments=10, fill_color=None):
    """
    Draw a curved line using small line segments
    
    Parameters:
    - t: turtle object
    - length: total length of the curve
    - curve_factor: positive for upward curve, negative for downward curve
    - segments: number of segments (higher = smoother curve)
    - fill_color: optional color to fill if creating a closed shape
    """
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
        
    segment_length = length / segments
    # Save the original heading
    original_heading = t.heading()
    
    for i in range(segments):
        # Calculate the angle for this segment
        angle = curve_factor * math.sin(math.pi * i / segments)
        t.right(angle)
        t.forward(segment_length)
        t.left(angle)  # Reset the angle for the next segment
    
    # Reset to original heading
    t.setheading(original_heading)
    
    if fill_color:
        t.end_fill()
        
def jump_to(t, x, y):
    """Move turtle without drawing"""
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_star(t, x, y, b):
    """Draw six pointed star"""
    jump_to(t,x,y)
    draw_triangle(t,b,"yellow")
    jump_to(t,x+b,y+(2*b/3))
    t.right(180)
    draw_triangle(t,b,"yellow")

def draw_tower(t, x, y, b):
    """Draw tower for castle"""
    jump_to(t, x, y)
    t.setheading(0)
    draw_square(t, b, "lightgray")


def draw_scene(t):
    """Draw a colorful scene with various shapes"""
    # Set background color
    screen = t.getscreen()
    screen.bgcolor("midnightblue")

    # Moon
    jump_to(t, -220, 160)
    t.setheading(0)
    draw_circle(t, 40, "white")
    jump_to(t, -210, 170)
    t.setheading(0)
    draw_circle(t, 45, "midnightblue")

    # Castle
    jump_to(t, -150, -150)
    t.setheading(0)
    draw_rectangle(t, 300, 100, "lightgray")

    # Left tower
    draw_tower(t, -170, -100, 60)

    # Right tower 
    draw_tower(t, 110, -100, 60)

    # Star One
    draw_star(t,100,300, 30)
    
    # Star Two
    t.right(180)
    draw_star(t,-30,270, 30)

    # Star Three
    t.right(180)
    draw_star(t,220,180, 30)

    # Star Four
    t.right(180)
    draw_star(t,-100,120, 30)

    # Star Five
    t.right(180)
    draw_star(t,40,160, 30)

    


def main():
    t, screen = setup_turtle()
    draw_scene(t)
    screen.mainloop()


if __name__ == "__main__":
    main()

