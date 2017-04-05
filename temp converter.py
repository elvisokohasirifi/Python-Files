from graphics import *
def main():
     
     win = GraphWin("Celsius Converter", 400, 400)
     win.setCoords(0.0, 0.0, 3.0, 4.0)
     Text(Point(1,3), "Celsius Temperature: ").draw(win)
     Text(Point(1,1), "Fahrenheit Temperature: ").draw(win)
     inputs = Entry(Point(2,3), 5)
     inputs.setText("0.0")
     inputs.draw(win)
     output = Text(Point(2,1), " ")
     output.draw(win)
     button = Text(Point(1.5, 2.0), "Convert it")
     button.draw(win)
     Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)
     

     def calculate():
          n = win.getMouse()
          X = n.getX()
          Y = n.getY()
          if 1<=X<=2 and 1.5<=Y<=2.5:
               celsius = eval(inputs.getText())
               fahrenheit = 9.0/5.0 * celsius + 32
               output.setText(fahrenheit)
               button.setText("Quit")
          else:
               button.setText("Click here to convert")
               calculate()
               
     calculate()       
     def quits():
          t = win.getMouse()
          W = t.getX()
          E = t.getY()
          if 1<=W<=2 and 1.5<=E<=2.5:
               win.close()
          else:
               button.setText("Click here to quit")
               quits()
     quits()
               

main()

     
     
