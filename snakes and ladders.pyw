
#import winsound
from graphics import *
from random import*
statusup = [1]
p2 = [0]
q2 = [0]
wins = []
p = [0,0]
q= [0,0]
win = GraphWin("Report Preparation Program", 1050,700)
win.setCoords(0,0,40,30)
win.setBackground("white")
Rectangle(Point(0.5,0.5), Point(29.5,29.5)).draw(win)
Image(Point(15.5,15), "imgs.gif").draw(win)
status = Text(Point(35,26), "Click dice to roll").draw(win)
status1 = Text(Point(35,28), "")
status1.draw(win)
Rectangle(Point(33, 23), Point(38, 18)).draw(win)

Text(Point(33,15), "Player 1: ").draw(win)
Text(Point(33,12), "Player 2: ").draw(win)
play1 = Text(Point(35,15), "")
play1.draw(win)
play2 = Text(Point(35,12), "")
play2.draw(win)


c0 = Point(0,0)

def gameover():
     t = Text(Point(20,20), "Game Over!")
     t.setFace("courier")
     t.setFill("white")
     t.setStyle("bold")
     t.setSize(30)
     t.draw(win)
   
     if wins[-1]=="p1":
          m = Text(Point(20,12), "Player One wins")
          m.setFace("courier")
          m.setFill("white")
          m.setStyle("bold")
          m.setSize(30)
          m.draw(win)
     else:
          m = Text(Point(20,12), "Player Two wins")
          m.setFace("courier")
          m.setFill("white")
          m.setStyle("bold")
          m.setSize(30)
          m.draw(win)

     win.getMouse()
     win.close()
          

c1 = Circle(Point(2.4, 3), 1.5)
c2 = Circle(Point(7,3),1.5)
c3 = Circle(Point(13,3),1.5)
c4 = Circle(Point(18,3),1.5)
c5 = Circle(Point(23,3),1.5)
c6 = Circle(Point(29,3),1.5)
c7 = Circle(Point(29,9),1.5)
c8 = Circle(Point(23,9),1.5)
c9 = Circle(Point(18,9),1.5)
c10 = Circle(Point(12,9),1.5)
c11 = Circle(Point(7,9),1.5)
c12 = Circle(Point(2,9),1.5)
c13 = Circle(Point(2,15),1.5)
c14 = Circle(Point(7,15),1.5)
c15 = Circle(Point(12,15),1.5)
c16 = Circle(Point(18,15),1.5)
c17 = Circle(Point(23,15),1.5)
c18 = Circle(Point(29,15),1.5)
c19 = Circle(Point(29,21),1.5)
c20 = Circle(Point(23,21),1.5)
c21 = Circle(Point(18,21),1.5)
c22 = Circle(Point(12,21),1.5)
c23 = Circle(Point(7,21),1.5)
c24 = Circle(Point(2,21),1.5)
c25 = Circle(Point(2,27),1.5)
c26 = Circle(Point(7,27),1.5)
c27 = Circle(Point(12,27),1.5)
c28 = Circle(Point(18,27),1.5)
c29 = Circle(Point(23,27),1.5)
c30 = Circle(Point(29,27),1.5)
p1 = [c0,c1, c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30]

c00 = Point(0,0)
c01 = Circle(Point(2.4, 3), 1.5)
c02 = Circle(Point(7,3),1.5)
c03 = Circle(Point(13,3),1.5)
c04 = Circle(Point(18,3),1.5)
c05 = Circle(Point(23,3),1.5)
c06 = Circle(Point(29,3),1.5)
c07 = Circle(Point(29,9),1.5)
c08 = Circle(Point(23,9),1.5)
c09 = Circle(Point(18,9),1.5)
c010 = Circle(Point(12,9),1.5)
c011 = Circle(Point(7,9),1.5)
c012 = Circle(Point(2,9),1.5)
c013 = Circle(Point(2,15),1.5)
c014 = Circle(Point(7,15),1.5)
c015 = Circle(Point(12,15),1.5)
c016 = Circle(Point(18,15),1.5)
c017 = Circle(Point(23,15),1.5)
c018 = Circle(Point(29,15),1.5)
c019 = Circle(Point(29,21),1.5)
c020 = Circle(Point(23,21),1.5)
c021 = Circle(Point(18,21),1.5)
c022 = Circle(Point(12,21),1.5)
c023 = Circle(Point(7,21),1.5)
c024 = Circle(Point(2,21),1.5)
c025 = Circle(Point(2,27),1.5)
c026 = Circle(Point(7,27),1.5)
c027 = Circle(Point(12,27),1.5)
c028 = Circle(Point(18,27),1.5)
c029 = Circle(Point(23,27),1.5)
c030 = Circle(Point(29,27),1.5)
q1 = [c00, c01, c02,c03,c04,c05,c06,c07,c08,c09,c010,c011,c012,c013,c014,c015,c016,c017,c018,c019,c020,c021,c022,c023,c024,c025,c026,c027,c028,c029,c030]

def one():
     c2 = Circle(Point(35.5,20.5),0.5)
     c2.setFill("black")
     c2.draw(win)

def two():
     c3 = Circle(Point(34.5,20.5),0.5)
     c3.setFill("black")
     c3.draw(win)
     c90 = Circle(Point(36.5,20.5),0.5)
     c90.setFill("black")
     c90.draw(win)

def three():
    c4 = Circle(Point(34.5,19.5),0.5)
    c4.setFill("black")
    c4.draw(win)
    c5 = Circle(Point(36.5,19.5),0.5)
    c5.setFill("black")
    c5.draw(win)
    c6 = Circle(Point(35.5,21.5),0.5)
    c6.setFill("black")
    c6.draw(win)

def four():
    c7 = Circle(Point(34.5,19.5),0.5)
    c7.setFill("black")
    c7.draw(win)
    c8 = Circle(Point(36.5,19.5),0.5)
    c8.setFill("black")
    c8.draw(win)
    c9 = Circle(Point(34.5,21.5),0.5)
    c9.setFill("black")
    c9.draw(win)
    c10 = Circle(Point(36.5,21.5),0.5)
    c10.setFill("black")
    c10.draw(win)

def five():
    c11 = Circle(Point(35.5,20.5),0.5)
    c11.setFill("black")
    c11.draw(win)
    c12 = Circle(Point(34.25,19),0.5)
    c12.setFill("black")
    c12.draw(win)
    c13 = Circle(Point(36.75,19),0.5)
    c13.setFill("black")
    c13.draw(win)
    c14 = Circle(Point(34.25,22),0.5)
    c14.setFill("black")
    c14.draw(win)
    c15 = Circle(Point(36.75,22),0.5)
    c15.setFill("black")
    c15.draw(win)

def six():
    c11 = Circle(Point(34.25,20.5),0.5)
    c11.setFill("black")
    c11.draw(win)
    c12 = Circle(Point(34.25,19),0.5)
    c12.setFill("black")
    c12.draw(win)
    c13 = Circle(Point(36.75,19),0.5)
    c13.setFill("black")
    c13.draw(win)
    c14 = Circle(Point(34.25,22),0.5)
    c14.setFill("black")
    c14.draw(win)
    c15 = Circle(Point(36.75,22),0.5)
    c15.setFill("black")
    c15.draw(win)
    c16 = Circle(Point(36.75,20.5),0.5)
    c16.setFill("black")
    c16.draw(win)

           
           
          

     
def rect():
     r = Rectangle(Point(33, 23), Point(38, 18))
     r.setFill("white")
     r.draw(win)

def click():
     if statusup[-1] == 1:
          status1.setText("Player one's turn")
     else:
          status1.setText("Player two's turn")
     n = win.getMouse()
     if 33<=n.x<=38 and 18<=n.y<=23:
          a = randrange(1,7)
          if a==1:
               rect()
               one()
          elif a==2:
               rect()
               two()
          elif a==3:
               rect()
               three()
          elif a==4:
               rect()
               four()
          elif a==5:
               rect()
               five()
          else:
               rect()
               six()
          return a
     else:
          click()


def main():
     c0.draw(win)
     c00.draw(win)
     def start():
          
          while statusup[-1]==1:
               a = click()
               b = p[-1] + a
               
               if b>30:
                    b= p[-1]
                    print(b)
                    statusup.append(2)
               elif b==30:
                         wins.append("p1")
                         p.append(b)
                         p2.append(b)
                         play1.setText(p[-1])
                         p1[b].setFill("red")
                         p1[b].draw(win)
                         p1[(p2[-2])].undraw()
                         gameover()
               
                   
               else:
                    n = p[-1]
                    if b == 3:
                         b = 22
                    elif b==5:
                         b = 8
                    elif b==11:
                         b=26
                    elif b==20:
                         b = 29
                    elif b == 17:
                         b=4
                    elif b == 19:
                         b=7
                    elif b==21:
                         b=9
                    elif b== 27:
                         b = 1
                    p.append(b)
                    p2.append(b)
                    play1.setText(p[-1])
                    p1[b].setFill("red")
                    p1[b].draw(win)
                    p1[(p2[-2])].undraw()
                    
                   
                    if a==6:
                         statusup.append(1)
                    
                    else:
                         statusup.append(2)
          else:
               a = click()
               b = q[-1]+ a
               if b>30:
                    b= q[-1]
                    print(b)
                    statusup.append(1)
               elif b==30:
                         wins.append("p2")
                         q.append(b)
                         q2.append(b)
                         play2.setText(q[-1])
                         q1[b].setFill("blue")
                         q1[b].draw(win)
                         q1[(q2[-2])].undraw()
                         gameover()
               else:
               
                    n = q[-1]
                    if b == 3:
                         b = 22
                    elif b==5:
                         b = 8
                    elif b==11:
                         b=26
                    elif b==20:
                         b = 29
                    elif b == 17:
                         b=4
                    elif b == 19:
                         b=7
                    elif b==21:
                         b=9
                    elif b== 27:
                         b = 1
                    q.append(b)
                    q2.append(b)
                    play2.setText(q[-1])
                    q1[b].setFill("blue")
                    q1[b].draw(win)
                    q1[(q2[-2])].undraw()
                    if a==6:
                         statusup.append(2)
                    
                    else:
                         statusup.append(1)
               start()
     start()
     
main()


#def starting():
     

     

          

     
