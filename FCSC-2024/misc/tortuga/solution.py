import turtle

# The two sequences in the text files
sequence_example = [(2, 0), (-1, 2), (-1, -2),(0, 0), (3, 0),(-1, 2), (2, 0), (-1, -2),(0, 0), (1, 0)] * 6
sequence_flag = [(0,0),(1,1),(0,2),(0,-2),(1,0),(-1,0),(0,1),(1,0),(0,0),(1,1),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(2,-2),(-1,0),(0,1),(1,0),(0,1),(-1,0),(0,0),(2,0),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,0),(3,-2),(-1,0),(0,1),(-1,0),(1,0),(0,1),(1,0),(0,0),(4,-2),(-2,0),(0,0),(0,2),(2,0),(0,-2),(0,1),(-2,0),(0,0),(3,-1),(0,2),(0,0),(3,-2),(-1,0),(-1,1),(0,1),(2,0),(0,-1),(-2,0),(0,0),(3,0),(1,0),(0,-1),(-1,0),(0,2),(1,0),(0,-1),(0,0),(1,1),(1,0),(0,-2),(-1,0),(0,0),(0,1),(1,0),(0,0),(2,1),(0,-2),(-1,1),(2,0),(0,0),(1,-1),(1,0),(-1,2),(0,0),(0,-1),(1,0),(0,0),(1,-1),(1,0),(0,1),(-1,0),(0,1),(1,0),(0,0),(1,0),(1,0),(0,-1),(-1,0),(0,-1),(1,0),(0,0),(1,2),(0,-2),(1,0),(-1,0),(0,2),(1,0),(0,-1),(-1,0),(0,0),(2,1),(1,0),(-1,0),(0,-2),(1,0),(-1,2),(1,0),(0,-2),(0,0),(1,0),(0,1),(1,0),(0,-1),(0,2),(0,0),(2,-2),(1,0),(0,1),(1,0),(-1,0),(0,1),(-1,0)]

turtle.hideturtle()
turtle.screensize(600, 400)

not_writing = False
turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()

# For each move in the sequence, we move to the point from our current position
for mv in sequence_flag:
    if mv[0] == 0 and mv[1] == 0:
        # Stop writing until next move
        turtle.penup()
        not_writing = True

    else:
        # Move from current position, *20 so we draw more pixels and we can read the flag
        turtle.goto((turtle.position()[0] + mv[0] * 20, turtle.position()[1] - mv[1] * 20))

        if not_writing:
            turtle.pendown()
            not_writing = False


turtle.exitonclick()
