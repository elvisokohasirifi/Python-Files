from math import*
from graphics import*
win = GraphWin("PowerCalc", 350, 500)
win.setBackground("white")
win.setCoords(0,0,19,35)

def default():
          rec = Rectangle(Point(0.5, 0.5),Point(18.5,32.5))
          rec.setFill("white")
          rec.draw(win)
          t = Text(Point(2,34),"←")
          t.setSize(20)
          t.draw(win)
          Rectangle(Point(0.5,34.8),Point(3.5,32.8)).draw(win)


def calculator():
     default()
     w =Rectangle(Point(1, 22.5),Point(18,31.5))
     w.setOutline("red")
     w.draw(win)
     q = Rectangle(Point(1,1),Point(18,21.5))
     q.setOutline("red")
     q.draw(win)

     status = ["on"]

     def drew(x1,y1,x2,y2,text):
          r = Rectangle(Point(x1,y1), Point(x2,y2))
          r.draw(win)
          t = Text(Point(0.5*(x1+x2), 0.5*(y1+y2)), text)
          t.draw(win)

     drew(1,1,4,4,"±")
     drew(4.5,1,7.5,4,"0")
     drew(8,1,11,4,".")
     drew(11.5,1,14.5,4,"mod")
     drew(15,1,18,4,"=")

     drew(1,4.5,4,7.5,"√")
     drew(4.5,4.5,7.5,7.5,"1")
     drew(8,4.5,11,7.5,"2")
     drew(11.5,4.5,14.5,7.5,"3")
     drew(15,4.5,18,7.5,"+")

     drew(1,8,4,11,"tan")
     drew(4.5,8,7.5,11,"4")
     drew(8,8,11,11,"5")
     drew(11.5,8,14.5,11,"6")
     drew(15,8,18,11,"-")

     drew(1,11.5,4,14.5,"cos")
     drew(4.5,11.5,7.5,14.5,"7")
     drew(8,11.5,11,14.5,"8")
     drew(11.5,11.5,14.5,14.5,"9")
     drew(15,11.5,18,14.5,"x")

     drew(1,15,4,18,"sin")
     drew(4.5,15,7.5,18,"(")
     drew(8,15,11,18,")")
     drew(11.5,15,14.5,18,"←")
     drew(15,15,18,18,"÷")

     drew(1,18.5,4,21.5,"C")
     drew(4.5,18.5,7.5,21.5,"log")
     drew(8,18.5,11,21.5,"ln")
     drew(11.5,18.5,14.5,21.5,"π")
     drew(15,18.5,18,21.5,"e")

     r = Rectangle(Point(1,18.5),Point(4,21.5))
     r.setFill("red")
     r.draw(win)
     t = Text(Point(2.5,20),"C")
     t.setFill("white")
     t.draw(win)

     r = Rectangle(Point(15,1),Point(18,4))
     r.setFill("red")
     r.draw(win)
     t = Text(Point(16.5,2.5),"=")
     t.setFill("white")
     t.draw(win)

     main1 = Text(Point(9.5,25),"0")
     main1.draw(win)
     main2 = Text(Point(9.5,28),"")
     main2.draw(win)

     tx = [""]


     try:
          def clicks():
               te = tx[-1]
               n = win.getMouse()
               if 1<=n.x<=4 and 1<=n.y<=4:
                    te = -1*eval(te)
                    te = str(te)
               elif 4.5<=n.x<=7.5 and 1<=n.y<=4:
                    te = te+str(0)
               elif 8<=n.x<=11 and 1<=n.y<=4:
                    te = te+"."
               elif 15<=n.x<=18 and 1<=n.y<=4:
                    te = eval(te)
                    te = str(te)
               elif 11.5<=n.x<=14.5 and 1<=n.y<=4:
                    te = te+"%"
                    
               elif 1<=n.x<=4 and 4.5<=n.y<=7.5:
                    te = te + "sqrt("
               elif 4.5<=n.x<=7.5 and 4.5<=n.y<=7.5:
                    te = te+str(1)
               elif 8<=n.x<=11 and 4.5<=n.y<=7.5:
                    te = te+str(2)
               elif 15<=n.x<=18 and 4.5<=n.y<=7.5:
                    te = te+"+"
               elif 11.5<=n.x<=14.5 and 4.5<=n.y<=7.5:
                    te = te+str(3)
                    
               elif 1<=n.x<=4 and 8<=n.y<=11:
                    te = te+"tan("
               elif 4.5<=n.x<=7.5 and 8<=n.y<=11:
                    te = te+str(4)
               elif 8<=n.x<=11 and 8<=n.y<=11:
                    te = te+str(5)
               elif 11.5<=n.x<=14.5 and 8<=n.y<=11:
                    te = te+str(6)
               elif 15<=n.x<=18 and 8<=n.y<=11:
                    te = te+"-"
                    
               elif 1<=n.x<=4 and 11.5<=n.y<=14.5:
                    te = te+"cos("
               elif 4.5<=n.x<=7.5 and 11.5<=n.y<=14.5:
                    te = te+str(7)
               elif 8<=n.x<=11 and 11.5<=n.y<=14.5:
                    te = te+str(8)
               elif 11.5<=n.x<=14.5 and 11.5<=n.y<=14.5:
                    te = te+str(9)
               elif 15<=n.x<=18 and 11.5<=n.y<=14.5:
                    te = te+"*"

               elif 1<=n.x<=4 and 15<=n.y<=18:
                    te = te+"sin("
               elif 4.5<=n.x<=7.5 and 15<=n.y<=18:
                    te = te+"("
               elif 8<=n.x<=11 and 15<=n.y<=18:
                    te = te+")"
               elif 11.5<=n.x<=14.5 and 15<=n.y<=18:
                    te = te[:-1]
               elif 15<=n.x<=18 and 15<=n.y<=18:
                    te = te+"/"

               elif 1<=n.x<=4 and 18.5<=n.y<=21.5:
                    te = ""
               elif 4.5<=n.x<=7.5 and 18.5<=n.y<=21.5:
                    te = te+"log10("
               elif 8<=n.x<=11 and 18.5<=n.y<=21.5:
                    te = te+"log("
               elif 11.5<=n.x<=14.5 and 18.5<=n.y<=21.5:
                    te = te+"pi"
               elif 15<=n.x<=18 and 18.5<=n.y<=21.5:
                    te = te+"e"
               elif 0.5<=n.x<=3.5 and 32.8<=n.y<=34.8:
                     r = Rectangle(Point(-1,-1),Point(20,35))
                     r.setFill("white")
                     r.draw(win)
                     killer()

               
               else:
                    clicks()
               tx.append(te)
               main1.setText(te)
               clicks()
          clicks()
     except SyntaxError:
          main1.setText("Error")
          clicks()
     except TypeError:
          main1.setText("Error")
          clicks()
     except ValueError:
          main1.setText("Error")
          clicks()
     except NameError:
          main1.setText("Error")
          clicks()
     except ZeroDivisionError:
          main1.setText("Math Domain Error")
          clicks()



def mm2m():
     default()
     Text(Point(6, 25), "millimeters(mm):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "meters(m):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def m2mm():
     default()
     Text(Point(6, 25), "meters(m):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "millimeters(mm):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def cm2m():
     default()
     Text(Point(6, 25), "Centimeters(cm):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "meters(m):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/100)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def m2cm():
     default()
     Text(Point(6, 25), "meters(m):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "centimeters(cm):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*100)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()
def m2km():
     default()
     Text(Point(6, 25), "meters(m):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "kilometers(km):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()
def km2m():
     default()
     Text(Point(6, 25), "kilometers(km):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "meters(m):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()          

def dollar2cedi():
     default()
     Text(Point(6, 25), "Dollars($):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Cedis(₵):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*4)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()          
def cedi2dollar():
     default()
     Text(Point(6, 25), "Cedis(₵):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Dollars($):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/4)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def cedi2euro():
     default()
     Text(Point(6, 25), "Cedis(₵):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Euro(€):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/4.37)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def euro2cedi():
     default()
     Text(Point(6, 25), "Euro(€):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Cedis(₵):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*4.37)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def pound2cedi():
     default()
     Text(Point(6, 25), "Pounds(£):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Cedis(₵):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*5.58)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def cedi2pound():
     default()
     Text(Point(6, 25), "Cedis(₵):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Pounds(£):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/5.58)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def mg2g():
     default()
     Text(Point(6, 25), "milligrams(mg):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "grams(g):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()          
def g2mg():
     default()
     Text(Point(6, 25), "grams(g):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "milligram(mg):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def g2kg():
     default()
     Text(Point(6, 25), "grams(g):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "kilogram(kg):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def kg2g():
     default()
     Text(Point(6, 25), "kilogram(kg):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "gram(g):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def m2w():
     default()
     Text(Point(6, 25), "Mass(kg):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Weight(N):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*10)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def w2m():
     default()
     Text(Point(6, 25), "Weight(N):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Mass(kg):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/10)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()




def l2ml():
     default()
     Text(Point(6, 25), "litres(l):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "millilitres(ml):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()          
def ml2l():
     default()
     Text(Point(6, 25), "millilitres(ml):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "litres(l):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/1000)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def l2g():
     default()
     Text(Point(6, 25), "Litres(l):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "gallons:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/4.546)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def g2l():
     default()
     Text(Point(6, 25), "gallons:").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "litres:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*4.546)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def o2g():
     default()
     Text(Point(6, 25), "Fluid Ounces(Fl.oz):").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Gallons:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a/160)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def g2o():
     default()
     Text(Point(6, 25), "gallons:").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Fluid ounces(Fl.oz):").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a*160)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()





def c2k():
     default()
     Text(Point(6, 25), "Degree Celsius:").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Kelvin:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a+273)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()          
def k2c():
     default()
     Text(Point(6, 25), "Kelvin").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Degree Celsius:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(a-273)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def f2c():
     default()
     Text(Point(6, 25), "Fahrenheit").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Degree Celsius:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText((a- 32) * 5/9)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def c2f():
     default()
     Text(Point(6, 25), "Degree Celsius:").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Fahrenheit:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText((a* 9/5) + 32)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()

def k2f():
     default()
     Text(Point(6, 25), "Kelvin:").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Fahrenheit:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(1.8*(a-273)+32)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()              

def f2k():
     default()
     Text(Point(6, 25), "Fahrenheit:").draw(win)
     e = Entry(Point(13, 25),10)
     e.setFill("white")
     e.draw(win)
     Text(Point(6, 8), "Kelvin:").draw(win)
     effc = Text(Point(12, 8)," ")
     effc.draw(win)
     Text(Point(9.5,16.5),"Convert").draw(win)
     Rectangle(Point(6,15),Point(13,18)).draw(win)
     def clic():
          q = win.getMouse()
          if 6<=q.x<=13 and 15<=q.y<=18:
               a = eval(e.getText())
               effc.setText(5/9 * (a - 32) + 273)
               clic()
          elif 0.5<=q.x<=3.5 and 32.8<=q.y<=34.8:
               e.undraw()
               time.sleep(1)
               screen()
          else:
               clic()
     clic()
     
def length():
     default()
     Text(Point(5, 6), "mm  ⇒  m").draw(win)
     Text(Point(14, 6), "m  ⇒  mm").draw(win)
     Text(Point(5, 16), "cm  ⇒  m").draw(win)
     Text(Point(14, 16), "m  ⇒  cm").draw(win)
     Text(Point(5, 26), "m  ⇒  km").draw(win)
     Text(Point(14, 26), "km  ⇒  m").draw(win)
     Rectangle(Point(2,4.5),Point(8,7.5)).draw(win)
     Rectangle(Point(11,4.5),Point(17,7.5)).draw(win)
     Rectangle(Point(2,14.5),Point(8,17.5)).draw(win)
     Rectangle(Point(11,14.5),Point(17,17.5)).draw(win)
     Rectangle(Point(2,24.5),Point(8,27.5)).draw(win)
     Rectangle(Point(11,24.5),Point(17,27.5)).draw(win)
     def pick():
          w = win.getMouse()
          if 2<=w.x<=8 and 4.5<=w.y<=7.5:
               mm2m()
          elif 11<=w.x<=17 and 4.5<=w.y<=7.5:
               m2mm()
          elif 2<=w.x<=8 and 14.5<=w.y<=17.5:
               cm2m()
          elif 11<=w.x<=17 and 14.5<=w.y<=17.5:
               m2cm()
          elif 2<=w.x<=8 and 24.5<=w.y<=27.5:
               m2km()
          elif 11<=w.x<=17 and 24.5<=w.y<=27.5:
               km2m()
          elif 0.5<=w.x<=3.5 and 32.8<=w.y<=34.8:
               screen()
          else:
               pick()
     pick()

def currency():
     default()
     Text(Point(5, 6), "$  ⇒  ₵").draw(win)
     Text(Point(14, 6), "₵  ⇒  $").draw(win)
     Text(Point(5, 16), "€  ⇒  ₵").draw(win)
     Text(Point(14, 16), "₵  ⇒  €").draw(win)
     Text(Point(5, 26), "£  ⇒  ₵").draw(win)
     Text(Point(14, 26), "₵  ⇒  £").draw(win)
     Rectangle(Point(2,4.5),Point(8,7.5)).draw(win)
     Rectangle(Point(11,4.5),Point(17,7.5)).draw(win)
     Rectangle(Point(2,14.5),Point(8,17.5)).draw(win)
     Rectangle(Point(11,14.5),Point(17,17.5)).draw(win)
     Rectangle(Point(2,24.5),Point(8,27.5)).draw(win)
     Rectangle(Point(11,24.5),Point(17,27.5)).draw(win)
     def pick():
          w = win.getMouse()
          if 2<=w.x<=8 and 4.5<=w.y<=7.5:
               dollar2cedi()
          elif 11<=w.x<=17 and 4.5<=w.y<=7.5:
               cedi2dollar()
          elif 2<=w.x<=8 and 14.5<=w.y<=17.5:
               euro2cedi()
          elif 11<=w.x<=17 and 14.5<=w.y<=17.5:
               cedi2euro()
          elif 2<=w.x<=8 and 24.5<=w.y<=27.5:
               pound2cedi()
          elif 11<=w.x<=17 and 24.5<=w.y<=27.5:
               cedi2pound()
          elif 0.5<=w.x<=3.5 and 32.8<=w.y<=34.8:
               screen()
          else:
               pick()
     pick()
          
def mass():
     default()
     Text(Point(5, 6), "mg  ⇒  g").draw(win)
     Text(Point(14, 6), "g  ⇒  mg").draw(win)
     Text(Point(5, 16), "g  ⇒  kg").draw(win)
     Text(Point(14, 16), "kg ⇒  g").draw(win)
     Text(Point(5, 26), "mass ⇒ weight").draw(win)
     Text(Point(14, 26), "weight ⇒  mass").draw(win)
     Rectangle(Point(2,4.5),Point(8,7.5)).draw(win)
     Rectangle(Point(11,4.5),Point(17,7.5)).draw(win)
     Rectangle(Point(2,14.5),Point(8,17.5)).draw(win)
     Rectangle(Point(11,14.5),Point(17,17.5)).draw(win)
     Rectangle(Point(2,24.5),Point(8,27.5)).draw(win)
     Rectangle(Point(11,24.5),Point(17,27.5)).draw(win)
     def pick():
          w = win.getMouse()
          if 2<=w.x<=8 and 4.5<=w.y<=7.5:
               mg2g()
          elif 11<=w.x<=17 and 4.5<=w.y<=7.5:
               g2mg()
          elif 2<=w.x<=8 and 14.5<=w.y<=17.5:
               g2km()
          elif 11<=w.x<=17 and 14.5<=w.y<=17.5:
               kg2g()
          elif 2<=w.x<=8 and 24.5<=w.y<=27.5:
               m2w()
          elif 11<=w.x<=17 and 24.5<=w.y<=27.5:
               w2m()
          elif 0.5<=w.x<=3.5 and 32.8<=w.y<=34.8:
               screen()
          else:
               pick()
     pick()

def capacity():
     default()
     Text(Point(5, 6), "l  ⇒  ml").draw(win)
     Text(Point(14, 6), "ml  ⇒  l").draw(win)
     Text(Point(5, 16), "l  ⇒  gallons").draw(win)
     Text(Point(14, 16), "gallons ⇒ l").draw(win)
     Text(Point(5, 26), "Fl.oz⇒gallons").draw(win)
     Text(Point(14, 26), "gallons⇒Fl.oz").draw(win)
     Rectangle(Point(2,4.5),Point(8,7.5)).draw(win)
     Rectangle(Point(11,4.5),Point(17,7.5)).draw(win)
     Rectangle(Point(2,14.5),Point(8,17.5)).draw(win)
     Rectangle(Point(11,14.5),Point(17,17.5)).draw(win)
     Rectangle(Point(2,24.5),Point(8,27.5)).draw(win)
     Rectangle(Point(11,24.5),Point(17,27.5)).draw(win)
     def pick():
          w = win.getMouse()
          if 2<=w.x<=8 and 4.5<=w.y<=7.5:
               l2ml()
          elif 11<=w.x<=17 and 4.5<=w.y<=7.5:
               ml2l()
          elif 2<=w.x<=8 and 14.5<=w.y<=17.5:
               l2g()
          elif 11<=w.x<=17 and 14.5<=w.y<=17.5:
               g2l()
          elif 2<=w.x<=8 and 24.5<=w.y<=27.5:
               f2g()
          elif 11<=w.x<=17 and 24.5<=w.y<=27.5:
               g2f()
          elif 0.5<=w.x<=3.5 and 32.8<=w.y<=34.8:
               screen()
          else:
               pick()
     pick()
def temp():
     default()
     Text(Point(5, 6), "℃  ⇒  K").draw(win)
     Text(Point(14, 6), "K  ⇒  ℃").draw(win)
     Text(Point(5, 16), "℉  ⇒  ℃").draw(win)
     Text(Point(14, 16), "℃  ⇒  ℉").draw(win)
     Text(Point(5, 26), "K  ⇒  ℉").draw(win)
     Text(Point(14, 26), "℉  ⇒  K").draw(win)
     Rectangle(Point(2,4.5),Point(8,7.5)).draw(win)
     Rectangle(Point(11,4.5),Point(17,7.5)).draw(win)
     Rectangle(Point(2,14.5),Point(8,17.5)).draw(win)
     Rectangle(Point(11,14.5),Point(17,17.5)).draw(win)
     Rectangle(Point(2,24.5),Point(8,27.5)).draw(win)
     Rectangle(Point(11,24.5),Point(17,27.5)).draw(win)
     def pick():
          w = win.getMouse()
          if 2<=w.x<=8 and 4.5<=w.y<=7.5:
               c2k()
          elif 11<=w.x<=17 and 4.5<=w.y<=7.5:
               k2c()
          elif 2<=w.x<=8 and 14.5<=w.y<=17.5:
               f2c()
          elif 11<=w.x<=17 and 14.5<=w.y<=17.5:
               c2f()
          elif 2<=w.x<=8 and 24.5<=w.y<=27.5:
               k2f()
          elif 11<=w.x<=17 and 24.5<=w.y<=27.5:
               f2k()
          elif 0.5<=w.x<=3.5 and 32.8<=w.y<=34.8:
               screen()
          else:
               pick()
     pick()     


def screen():
     default()
     Rectangle (Point(4.5, 5),Point(14.5,8)).draw(win)
     Rectangle(Point(4.5, 10),Point(14.5,13)).draw(win)
     Rectangle (Point(4.5, 15),Point(14.5,18)).draw(win)
     Rectangle(Point(4.5, 20),Point(14.5,23)).draw(win)
     Rectangle (Point(4.5, 25),Point(14.5,28)).draw(win)

     Text(Point(9.5,6.5),"LENGTH").draw(win)
     Text(Point(9.5,11.5),"MASS").draw(win)
     Text(Point(9.5,16.5),"CAPACITY / VOLUME").draw(win)
     Text(Point(9.5,21.5),"TEMPERATURE").draw(win)
     Text(Point(9.5,26.5),"CURRENCY").draw(win)
     def choose():
          c = win.getMouse()
          if 4.5<=c.x<=14.5 and 5<=c.y<=8:
               length()
          elif 4.5<=c.x<=14.5 and 10<=c.y<=13:
               mass()
          elif 4.5<=c.x<=14.5 and 15<=c.y<=18:
               capacity()
          elif 4.5<=c.x<=14.5 and 20<=c.y<=23:
               temp()
          elif 4.5<=c.x<=14.5 and 25<=c.y<=28:
              currency()
          elif 0.5<=c.x<=3.5 and 32.8<=c.y<=34.8:
                r = Rectangle(Point(-1,-1),Point(20,35))
                r.setFill("white")
                r.draw(win)
                killer()
          else:
               choose()
     choose()





def killer():
     Text(Point(9.5,23),"Calculator").draw(win)
     Text(Point(9.5,12),"Unit Converter").draw(win)
     Rectangle(Point(4.5,21),Point(14.5, 25)).draw(win)
     Rectangle(Point(4.5,10),Point(14.5, 14)).draw(win)
     def shoot():
          er = win.getMouse()
          if 4.5<=er.x<=14.5 and 21<=er.y<=25:
               calculator()
          elif 4.5<=er.x<=14.5 and 10<=er.y<=14:
               screen()
          else:
               shoot()
     shoot()
killer()






          






          

               
          



