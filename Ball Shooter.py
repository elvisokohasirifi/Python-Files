from graphics import*

win = GraphWin("Bubble Shooter", 600,550)
win.setCoords(0,0,100,100)
win.setBackground("white")

def gameOver():
    if len(deletions) == 0:
        return True
    return False

variables = []
deletions = []
default = "a"
y = 96
x = 3
n = 0
for i in range(57):
    if i == 19 or i == 38:
        n = 0
    if  i >= 38:
        y = 84
    elif i >= 19:
        y = 90   
    else:
        y = 96
    variables.append(default + str(i))
    deletions.append(i)
    variables[i] = Image(Point(n * 5 + 5, y) ,"apple.png")
    variables[i].draw(win)
    n += 1
y = 90

bow = Image(Point(50,5),"bow.png")
bow.draw(win)

def shoot(x, y):
    l = Image(Point(x,y+11),"arrow.png")
    l.draw(win)
    while y <= 108:
        l.move(0, 2)
        time.sleep(0.02)
        y = l.getAnchor().getY()
    try:
        variables[int(x//5) - 1].undraw()
        variables[(int(x//5) - 1 )+ 19].undraw()
        variables[(int(x//5) - 1) + 38].undraw()
        deletions.remove(int(x//5) - 1)
        deletions.remove((int(x//5) - 1 )+ 19)
        deletions.remove((int(x//5) - 1) + 38)
        
    except(ValueError):
        z = None
def get():
    try:
        key = win.getKey()
        if key == "Left":
            if bow.getAnchor().getX() <= 5:
                z = None
            else:
                bow.move(-5, 0)
        elif key == "Right":
            if bow.getAnchor().getX() >= 95:
                z = None
            else:
                bow.move(5, 0)
        elif key == "space":
            shoot(bow.getAnchor().getX(), bow.getAnchor().getY())
        else:
            z = None
    except(GraphicsError):
        win.close()

while not gameOver():
    get()

t = Text(Point(50,80),"GAME OVER! ")
t.setSize(36)
t.setFace("courier")
t.setFill("red")
t.draw(win)
Image(Point(50,50),"trophy.png").draw(win)
win.getMouse()
win.close()
