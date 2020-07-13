import turtle
import time
counter=0
flag=False
class PenPath(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.color("grey","red")
    self.penup()
    self.speed(-1)
    self.hideturtle()
class PenFinalPath(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.color("grey","yellow")
    self.penup()
    self.speed(-1)
    self.hideturtle()
arx = []
arxF=[]
aryF=[]
ary = []
t = turtle.Turtle()
t.width(5)
tt = turtle.Turtle()
u = turtle.Turtle()
tt.color("blue")
u.speed(-1)
u.hideturtle()
start_t=turtle.Turtle()
start_t.hideturtle()
maze=[]

def boxPath(x,y,obj):
    if (x >= 300):
        x = 280
    if (x <= -300):
        x = -300
    if (y >= 300):
        y = 280
    if (y <= -300):
        y = -300
    obj.goto(x, y)
    obj.pendown()
    obj.begin_fill()
    for i in range(4):
        obj.forward(20)
        obj.left(90)
    obj.end_fill()
    obj.penup()


def box(x, y):
    if(x>=300):
        x=280
    if(x<=-300):
        x=-300
    if(y>=300):
        y=280
    if(y<=-300):
        y=-300

    arxF.append(x)
    aryF.append(y)
    u.goto(x, y)
    u.pendown()
    u.color("grey", "black")
    u.begin_fill()
    for i in range(4):
        u.forward(20)
        u.left(90)
    u.end_fill()
    u.penup()


def nearX(x):
    xl = 0
    while (True):
        if (x % 20 == 0):
            xl = x
            break
        else:
            x = x - 1
    return xl
def nearY(y):
    yl = 0
    while (True):
        if (y % 20 == 0):
            yl = y
            break
        else:
            y = y - 1
    return yl
def recreate(x, y):
    global counter
    u.goto(x, y)
    xl=nearX(x)
    yl=nearY(y)

    box(xl,yl)
    dummyline=0
    if(counter!=len(arx)-1):
        for i in range(counter+1,len(arx)):
            sx=nearX(arx[i])
            sy=nearY(ary[i])
            if(xl==sx and yl==sy):
                arxF.append(x)
                aryF.append(y)
                dummyline=1

            else:
                if(dummyline==1):
                    dummyline=0
                    counter=i
                    recreate(arx[i + 1], ary[i + 1])
                    break
                else:
                    counter=i
                    recreate(arx[i + 1], ary[i + 1])
                    break






def slate():
    t.speed(-1)
    t.penup()
    t.goto(-300, 300)
    t.pendown()
    t.width(8)
    t.color("grey")
    for i in range(4):
        t.forward(600)
        t.right(90)
    t.width(3)
    for i in range(15):
        t.forward(20)
        t.right(90)
        t.forward(600)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(600)
        t.right(90)
    for i in range(15):
        t.right(90)
        t.forward(20)
        t.right(90)
        t.forward(600)
        t.left(90)
        t.forward(20)
        t.left(90)
        t.forward(600)
    t.penup()
    t.goto(0,300)
    t.pendown()
    t.color("red")
    t.right(90)
    t.forward(600)

    t.penup()
    t.goto(-300,0)
    t.pendown()
    t.left(90)
    t.forward(600)
    t.penup()


def dragging(x, y):
    if (x >= 300):
        x = 300
    if (x <= -300):
        x = -300
    if (y >= 300):
        y = 300
    if (y <= -300):
        y = -300
    tt.ondrag(None)
    tt.setheading(t.towards(x, y))
    arx.append(x)
    ary.append(y)
    tt.goto(x, y)
    tt.ondrag(dragging)

def righclick(x, y):
    start_t.clear()
    u.clear()
    tt.clear()
    tt.penup()
    tt.goto(0, 0)
    tt.pendown()
    arxF.clear()
    aryF.clear()
    penPathFinal.clear()
    penPath.clear()


def midclick(x, y):
    recreate(arx[0],ary[0])
    print("arxf :")
    print(arxF)
    print("aryf :")
    print(aryF)
def spaceclick():
    start_t.speed(-1)
    start_t.color("grey","yellow")
    start_t.penup()
    start_t.goto(-300,280)
    start_t.pendown()
    start_t.begin_fill()
    for i in range(4):
        start_t.forward(20)
        start_t.left(90)
    start_t.end_fill()
    start_t.penup()

    start_t.goto(20,-20)
    start_t.pendown()
    start_t.begin_fill()
    for i in range(4):
        start_t.forward(20)
        start_t.left(90)
    start_t.end_fill()

    dataini()
    solveMaze(maze,1,1)
def dataini():
    maze.append(['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])
    for i in range(1,29):
        ar=["X"]
        for j in range(1,29):
            if(i==15 and j==16):
                ar.append("E")
            else:
                x = -300 + (j * 20)
                y = 280 - (i * 20)
                done = 0
                if (x <= -300 or x >= 280):
                    ar.append("X")
                if (y >= 280 or y <= -300):
                    ar.append("X")
                else:
                    for k in range(len(arxF)):
                        if (x == arxF[k] and y == aryF[k]):
                            ar.append("X")
                            done = 1
                            break
                    if (done == 1):
                        done = 0
                        continue
                    ar.append(" ")
        ar.append("X")
        maze.append(ar)
    maze.append(['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'])

    for i in range(30):
        ss=""
        for j in range(30):
            ss=ss+maze[i][j]
        print(ss)



def main():
    slate()
    tt.width(3)
    tt.speed(-1)

    turtle.listen()

    tt.ondrag(dragging)
    turtle.onscreenclick(righclick, 3)
    turtle.onscreenclick(midclick, 2)
    turtle.onkey(spaceclick , "space")
    turtle.mainloop()
    print(arx)
    print(len(arx))
    print(ary)
    print(len(ary))
def checkAllSides(maze,x,y):
    if(checkL(maze,x,y)!=True and checkR(maze,x,y)!=True and checkU(maze,x,y)!=True and checkD(maze,x,y)!=True ):
        return True
    else:
        return False
def checkL(maze, x, y):
    if (maze[x][y - 1] == "X" or maze[x][y - 1] == "-"):
        return False
    else:
        return True


def checkR(maze, x, y):
    if (maze[x][y + 1] == "X" or maze[x][y + 1] == "-"):
        return False
    else:
        return True


def checkU(maze, x, y):
    if (maze[x - 1][y] == "X" or maze[x - 1][y] == "-"):
        return False
    else:
        return True


def checkD(maze, x, y):
    if (maze[x + 1][y] == "X" or maze[x + 1][y] == "-"):
        return False
    else:
        return True

def solveMaze(maze, x, y):
    global flag

    if(checkAllSides(maze,x,y)):
        screen_x = -300 + (y * 20)
        screen_y = 280 - (x * 20)
        boxPath(screen_x,screen_y,penPath)


    if (0 <= x + 1 <= len(maze) and 0 <= y <= len(maze[0]) and checkD(maze, x, y) and flag == False):
        if (maze[x + 1][y] == "E"):
            maze[x][y] = "."
            screen_x = -300 + (y * 20)
            screen_y = 280 - (x * 20)
            boxPath(screen_x, screen_y,penPathFinal)
            flag = True
        else:
            maze[x][y] = "-"
            screen_x = -300 + (y * 20)
            screen_y = 280 - (x * 20)
            boxPath(screen_x, screen_y,penPath)
            solveMaze(maze, x + 1, y)
            if (flag):
                maze[x][y] = "."
                screen_x = -300 + (y * 20)
                screen_y = 280 - (x * 20)
                boxPath(screen_x, screen_y,penPathFinal)

    if (0 <= x - 1 <= len(maze) and 0 <= y <= len(maze[0]) and checkU(maze, x, y) and flag == False):
        if (maze[x - 1][y] == "E"):
            maze[x][y] = "."
            screen_x = -300 + (y * 20)
            screen_y = 280 - (x * 20)
            boxPath(screen_x, screen_y,penPathFinal)
            flag = True
        else:
            maze[x][y] = "-"
            screen_x = -300 + (y * 20)
            screen_y = 280 - (x * 20)
            boxPath(screen_x, screen_y,penPath)
            solveMaze(maze, x - 1, y)
            if (flag):
                maze[x][y] = "."
                screen_x = -300 + (y * 20)
                screen_y = 280 - (x * 20)
                boxPath(screen_x, screen_y,penPathFinal)

    if (0 <= x <= len(maze) and 0 <= y + 1 <= len(maze[0]) and checkR(maze, x, y) and flag == False):
        if (maze[x][y + 1] == "E"):
            maze[x][y] = "."
            screen_x = -300 + (y * 20)
            screen_y = 280 - (x * 20)
            boxPath(screen_x, screen_y,penPathFinal)
            flag = True
        else:
            maze[x][y] = "-"
            screen_x = -300 + (y * 20)
            screen_y = 280 - (x * 20)
            boxPath(screen_x, screen_y,penPath)
            solveMaze(maze, x, y + 1)
            if (flag):
                maze[x][y] = "."
                screen_x = -300 + (y * 20)
                screen_y = 280 - (x * 20)
                boxPath(screen_x, screen_y,penPathFinal)

    if (0 <= x <= len(maze) and 0 <= y - 1 <= len(maze[0]) and checkL(maze, x, y) and flag == False):
        if (maze[x][y - 1] == "E"):
            maze[x][y] = "."
            screen_x = -300 + (y * 20)
            screen_y = 280 - (x * 20)
            boxPath(screen_x, screen_y,penPathFinal)
            flag = True
        else:
            maze[x][y] = "-"
            screen_x = -300 + (y * 20)
            screen_y = 280- (x * 20)
            boxPath(screen_x, screen_y,penPath)
            solveMaze(maze, x, y - 1)
            if (flag):
                maze[x][y] = "."
                screen_x = -300 + (y * 20)
                screen_y = 280 - (x * 20)
                boxPath(screen_x, screen_y,penPathFinal)

penPath=PenPath()
penPathFinal=PenFinalPath()
main()

