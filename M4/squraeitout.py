import turtle

def draw_expanding_squares():
    # Setup screen and drawing speed
    window = turtle.Screen()
    window.bgcolor("black")
    
    painter = turtle.Turtle()
    painter.color("cyan")
    painter.speed(8)
    
    size = 20
    
    print("Drawing squares... Look at your popup window!")
    
    # Draw 15 expanding squares
    for _ in range(15):
        # Draw a single square
        for _ in range(4):
            painter.forward(size)
            painter.left(90)
            
        # Move back and down to position the next larger square
        painter.penup()
        painter.goto(painter.xcor() - 10, painter.ycor() - 10)
        painter.pendown()
        
        # Increase the size for the next square
        size += 20
        
    window.exitonclick()

if __name__ == "__main__":
    draw_expanding_squares()
