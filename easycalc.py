from math import*
def drew(x1,y1,x2,y2,text):
     r = Rectangle(Point(x1,y1), Point(x2,y2))
     r.draw(win)
     t = Text(Point(0.5*(x1+x2), 0.5*(y1+y2)), text)
     t.draw(win)
     
from graphics import*
win = GraphWin("EasyCalc", 300, 400)
win.setBackground("white")
win.setCoords(0,0,19,23)
Rectangle(Point(0.5, 0.5),Point(18.5,22.5)).draw(win)
Rectangle(Point(2, 17),Point(17,21)).draw(win)

global te
te = ""
main = Entry(Point(9.5, 19), 26)
main.setFill("white")
#main = Text(Point(9.5, 19), "0")
main.draw(win)
Rectangle(Point(2, 17),Point(17,21)).draw(win)
tx = [""]

drew(2,1.5,5,3.5,"mod")
drew(6,1.5,9,3.5,0)
drew(10,1.5,13,3.5,".")
drew(14,1.5,17,3.5,"=")
f = Rectangle(Point(14,1.5), Point(17,3.5))
f.setOutline("red")
f.draw(win)

drew(2,4.5,5,6.5,1)
drew(6,4.5,9,6.5,2)
drew(10,4.5,13,6.5,3)
drew(14,4.5,17,6.5,"+")

drew(2,7.5,5,9.5,4)
drew(6,7.5,9,9.5,5)
drew(10,7.5,13,9.5,6)
drew(14,7.5,17,9.5,"-")

drew(2,10.5,5,12.5,7)
drew(6,10.5,9,12.5,8)
drew(10,10.5,13,12.5,9)
drew(14,10.5,17,12.5,"x")

drew(2,13.5,5,15.5,"C")
drew(6,13.5,9,15.5,"←")
drew(10,13.5,13,15.5,"√")
drew(14,13.5,17,15.5,"÷")
try:
     def clicks():
          te = tx[-1]
          n = win.getMouse()
          if 2<=n.x<=5 and 1.5<=n.y<=3.5:
               te = te + "%"
               
          elif 6<=n.x<=9 and 1.5<=n.y<=3.5:
               te = te+str(0)
          elif 10<=n.x<=13 and 1.5<=n.y<=3.5:
               te = te+"."
          elif 14<=n.x<=17 and 1.5<=n.y<=3.5:
               te = eval(te)
               te = str(te)
          elif 2<=n.x<=5 and 4.5<=n.y<=6.5:
               te = te+str(1)
          elif 6<=n.x<=9 and 4.5<=n.y<=6.5:
               te = te+str(2)
          elif 10<=n.x<=13 and 4.5<=n.y<=6.5:
               te = te+str(3)
          elif 14<=n.x<=17 and 4.5<=n.y<=6.5:
               te = te+"+"
          elif 2<=n.x<=5 and 7.5<=n.y<=9.5:
               te = te+str(4)
          elif 6<=n.x<=9 and 7.5<=n.y<=9.5:
               te = te+str(5)
          elif 10<=n.x<=13 and 7.5<=n.y<=9.5:
               te = te+str(6)
          elif 14<=n.x<=17 and 7.5<=n.y<=9.5:
               te = te+"-"
          elif 2<=n.x<=5 and 10.5<=n.y<=12.5:
               te = te+str(7)
          elif 6<=n.x<=9 and 10.5<=n.y<=12.5:
               te = te+str(8)
          elif 10<=n.x<=13 and 10.5<=n.y<=12.5:
               te = te+str(9)
          elif 14<=n.x<=17 and 10.5<=n.y<=12.5:
               te = te+"*"
          elif 2<=n.x<=5 and 13.5<=n.y<=15.5:
               te ="0"
          elif 6<=n.x<=9 and 13.5<=n.y<=15.5:
               te = te[:-1]
          elif 10<=n.x<=13 and 13.5<=n.y<=15.5:
               te = sqrt(eval(te))
          elif 14<=n.x<=17 and 13.5<=n.y<=15.5:
               te = te+"/"
          else:
               clicks()
          tx.append(te)
          main.setText(te)
          clicks()
     clicks()
except SyntaxError:
     main.setText("Error")
     clicks()
except TypeError:
     main.setText("Error")
     clicks()
except ValueError:
     main.setText("Error")
     clicks()
except NameError:
     main.setText("Error")
     clicks()
except ZeroDivisionError:
     main.setText("Math Domain Error")
     clicks()
