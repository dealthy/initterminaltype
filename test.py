import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Tess moves in space")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()

def leftTurtle():
    tess.left(90)

def rightTurtle():
    tess.right(90)

should_move = False

def movementControl():
    global should_move
    should_move = not should_move

def advance_state_machine():
    global should_move
    if should_move:       
        tess.pendown()
        tess.forward(2)
    else:     
        tess.penup()
    wn.ontimer(advance_state_machine, 25)

def exitWindow():
    wn.bye()

wn.onkey(movementControl, "space")
wn.onkey(exitWindow, "q")
wn.onkey(leftTurtle, "Left")
wn.onkey(rightTurtle, "Right")

wn.listen()                      
advance_state_machine()

wn.mainloop()
