#import winsound
from graphics import *
win = GraphWin("EasyRep!", 650, 650)
win.setCoords(0,0,30,30)
def error_occured():
     win2 = GraphWin("Error", 300,200)
     win2.setCoords(0.0,0.0, 5.0, 5.0)
     but6 = Text(Point(2.5,2.5), "Input Error!").draw(win2)
     winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
     time.sleep(0.05)
     win2.close()
     
class Thanks:
     def thanks(self):
          win2 = GraphWin("The Report Preparation Program", 650, 650)
          win2.setCoords(0,0,30,30)
          win2.setBackground("white")
          Image(Point(15,17), "thank.gif").draw(win2)
          ta = Text(Point(15, 3),"Thanks for using The Report Preparation Program.")
          tb = Text(Point(15,28),"Open the recordss.txt file to see results")
          tb.setFace("courier")
          tb.draw(win2)
          ta.setFace("courier")
          ta.draw(win2)
          time.sleep(5)
          win2.close()

t0 = Image(Point(15,15), "than.gif")
t0.draw(win)
for i in range(15):
     
     t1 = Text(Point(i,  24), "Bonne Arrivé!")
     t1.setFace("courier")
     t1.setStyle("italic")
     t1.setSize(36)
     t1.setTextColor("red3")
     t1.draw(win)
     time.sleep(0.1)
     t1.undraw()

t1 = Text(Point(i,  24), "Bonne Arrivé!")
t1.setFace("courier")
t1.setStyle("italic")
t1.setSize(36)
t1.setTextColor("red3")
t1.draw(win)
time.sleep(0.5)

for i in range(15):
     t2 = Text(Point(i,  21), "Welcome to The Report Preparation Program")
     t2.setFace("courier")
     t2.setStyle("italic")
     t2.setSize(15)
     t2.setTextColor("green")
     t2.draw(win)
     time.sleep(0.1)
     t2.undraw()
     
t2 = Text(Point(i,  21), "Welcome to The Report Preparation Program")
t2.setFace("courier")
t2.setStyle("italic")
t2.setSize(15)
t2.setTextColor("green")
t2.draw(win)

t3 = Text(Point(15,  2), "Powered By Okoh-Asirifi Elvis. ©2016. All Rights Reserved.")
t3.setFace("courier")
t3.setStyle("italic")
t3.setSize(11)
t3.setTextColor("blue")
t3.draw(win)
time.sleep(1)
t6 = Rectangle(Point(13,9), Point(17, 11))
t6.setFill("orange red")
t6.draw(win)
t5 = Text(Point(15, 10), "Next >")
t5.setStyle("bold")
t5.setFill("white")
t5.draw(win)

time.sleep(0.5)
t4 = Text(Point(15, 13), "Click Next to continue...")
t4.setFace("courier")
t4.draw(win)


def clicks():
     e = win.getMouse()
     if 13<=e.x<=17 and 9<=e.y<=11:
          t1.undraw()
          t2.undraw()
          t3.undraw()
          t4.undraw()
          t5.undraw()
          t6.undraw()
          t0.undraw()
          time.sleep(1)

     else:
          clicks()
     def main():
          t0 = Image(Point(11,15), "thans.gif")
          t0.draw(win)
          names = ["hi"]
          mathScore = []
          engScore = []
          sciScore = []
          ictScore = []
          frenScore=[]
          twiScore = []
          rmeScore = []
          socScore = []
          bdtScore = []
          
          mathScorex = []
          engScorex = []
          sciScorex = []
          ictScorex = []
          frenScorex=[]
          twiScorex = []
          rmeScorex = []
          socScorex = []
          bdtScorex = []
          
          mathScores = []
          engScores = []
          sciScores = []
          ictScores = []
          frenScores=[]
          twiScores = []
          rmeScores = []
          socScores = []
          bdtScores = []
          totalss = []
          records = open("recordss.txt", "w")
          certificate = open("certificate.txt", "w")
          positions = []
          totali = []
          bdtt = []
          rmee = []
          schoolname = []
          teachername = []
          mastername = []
          Rectangle(Point(1,1), Point(29,29)).draw(win)
          welcome = Text(Point(15, 27), "Report Preparation Program")
          welcome.setStyle("bold")
          welcome.setSize(16)
          welcome.setTextColor('red')
          welcome.draw(win)
          helps =  Text(Point(25, 27), "Help")
          helps.setStyle("bold")
          helps.draw(win)
          Rectangle(Point(23.5,26.5),Point(26.5,27.5)).draw(win)
          info = Text(Point(15, 26), " ")
          info.draw(win)

          def enter():
               schools = Text(Point(5, 20), "Name of School: ")
               schools.setStyle("bold")
               schools.setTextColor('green')
               schools.draw(win)
               teachers = Text(Point(5, 15), "Name of Teacher: ")
               teachers.setStyle("bold")
               teachers.setTextColor('orange')
               teachers.draw(win)
               masters = Text(Point(5, 10), "Name of Headmaster: ")
               masters.setStyle("bold")
               masters.setTextColor('blue2')
               masters.draw(win)
               school = Entry(Point(17.4,20), 40)
               school.setFill("white")
               school.draw(win)
               teacher = Entry(Point(17.4,15), 40)
               teacher.setFill("white")
               teacher.draw(win)
               master = Entry(Point(17.4,10), 40)
               master.setFill("white")
               master.draw(win)
               tt = Text(Point(25,5), "Continue")
               tt.draw(win)
               re = Rectangle(Point(22,4),Point(28,6))
               re.draw(win)
               def sax():
                    wg = win.getMouse()
                    wgx = wg.getX()
                    wgy = wg.getY()
                    if 22<=wgx<=28 and 4 <=wgy <=6:
                         schoolname.append(school.getText())
                         teachername.append(teacher.getText())
                         mastername.append(master.getText())
                         schools.undraw()
                         school.undraw()
                         teachers.undraw()
                         teacher.undraw()
                         masters.undraw()
                         master.undraw()
                         re.undraw()
                         tt.undraw()
                         welcome.undraw()
                         time.sleep(2)
                    elif 23.5<=wgx<=26.5 and 26.5<=wgy<=27.5:
                         win2 = GraphWin("Help", 500,200)
                         win2.setCoords(0.0,0.0, 150, 10.0)
                         but6 = Text(Point(75,9), "The Report Preparation Program helps you create")
                         but8 = Text(Point(75,8), "a report of your students' performance. Fill the spaces provided with").draw(win2)
                         but9 = Text(Point(75,7), "the necessary information. Click Add to add the information").draw(win2)
                         but6.draw(win2)
                         but10 = Text(Point(75,6), "about the student you entered. After you are done with entering").draw(win2)
                         but11 = Text(Point(75,5), "the scores for all the students, click on Done to compute ").draw(win2)
                         Text(Point(75,4), "everything. The report is saved in a file named recordss in").draw(win2)
                         Text(Point(75,3), "the folder in which you stored this program's module. Click").draw(win2)
                         Text(Point(75,2), "Quit if you do not want to use the program again. Click Continue.").draw(win2)
                        
                         but7 = Text(Point(75,1), "Got it!").draw(win2)
                         rect6 = Rectangle(Point(65.5,0.5),Point(85.5,1.5)).draw(win2)
                         def helps():
                              n = win2.getMouse()
                              X = n.getX()
                              Y = n.getY()
                              if 65.5<=X<=85.5 and 0.5<=Y<=1.5:
                                   win2.close()
                                   enter()
                              else:
                                   helps()
                         helps()
                         
                    else:
                         sax()
                    def draw():
                         name =  Text(Point(5, 27), "Name of Student")
                         name.setStyle("bold")
                         name.draw(win)
                         nameInput = Entry(Point(17.4,27), 40)
                         ex = Text(Point(15, 25),"Examination")
                         ex.setStyle("bold")
                         ex.draw(win)
                         cl = Text(Point(25, 25),"Class work")
                         cl.setStyle("bold")
                         cl.draw(win)
                         nameInput.setFill("white")
                         nameInput.draw(win)
                         maths =  Text(Point(4.5, 23), "Mathematics")
                         maths.setStyle("bold")
                         maths.draw(win)
                         english =  Text(Point(3.5, 21), "English")
                         english.setStyle("bold")
                         english.draw(win)
                         science =  Text(Point(3.5, 19), "Science")
                         science.setStyle("bold")
                         science.draw(win)
                         social =  Text(Point(3.4, 17), "Social")
                         social.setStyle("bold")
                         social.draw(win)
                         ict =  Text(Point(3, 15), "ICT")
                         ict.setStyle("bold")
                         ict.draw(win)
                         rme =  Text(Point(3.1, 13), "RME")
                         rme.setStyle("bold")
                         rme.draw(win)
                         twi =  Text(Point(3, 11), "Twi")
                         twi.setStyle("bold")
                         twi.draw(win)
                         bdt =  Text(Point(3.1, 9), "BDT")
                         bdt.setStyle("bold")
                         bdt.draw(win)
                         french =  Text(Point(3.5, 7), "French")
                         french.setStyle("bold")
                         french.draw(win)
                         mathsInput = Entry(Point(15,23), 5)
                         mathsInput.setFill("white")
                         mathsInput.draw(win)
                         englishInput = Entry(Point(15,21), 5)
                         englishInput.setFill("white")
                         englishInput.draw(win)
                         scienceInput = Entry(Point(15,19), 5)
                         scienceInput.setFill("white")
                         scienceInput.draw(win)
                         socialInput = Entry(Point(15,17), 5)
                         socialInput.setFill("white")
                         socialInput.draw(win)
                         ictInput = Entry(Point(15,15), 5)
                         ictInput.setFill("white")
                         ictInput.draw(win)
                         rmeInput = Entry(Point(15,13), 5)
                         rmeInput.setFill("white")
                         rmeInput.draw(win)
                         twiInput = Entry(Point(15,11), 5)
                         twiInput.setFill("white")
                         twiInput.draw(win)
                         bdtInput = Entry(Point(15,9), 5)
                         bdtInput.setFill("white")
                         bdtInput.draw(win)
                         frenchInput = Entry(Point(15,7), 5)
                         frenchInput.setFill("white")
                         frenchInput.draw(win)


                         mathsex = Entry(Point(25,23), 5)
                         mathsex.setFill("white")
                         mathsex.draw(win)
                         englishex = Entry(Point(25,21), 5)
                         englishex.setFill("white")
                         englishex.draw(win)
                         scienceex = Entry(Point(25,19), 5)
                         scienceex.setFill("white")
                         scienceex.draw(win)
                         socialex = Entry(Point(25,17), 5)
                         socialex.setFill("white")
                         socialex.draw(win)
                         ictex = Entry(Point(25,15), 5)
                         ictex.setFill("white")
                         ictex.draw(win)
                         rmeex = Entry(Point(25,13), 5)
                         rmeex.setFill("white")
                         rmeex.draw(win)
                         twiex = Entry(Point(25,11), 5)
                         twiex.setFill("white")
                         twiex.draw(win)
                         bdtex = Entry(Point(25,9), 5)
                         bdtex.setFill("white")
                         bdtex.draw(win)
                         frenchex = Entry(Point(25,7), 5)
                         frenchex.setFill("white")
                         frenchex.draw(win)

                         
                         quits =  Text(Point(5, 4), "Quit")
                         quits.setStyle("bold")
                         quits.setTextColor('red')
                         quits.draw(win)
                         Rectangle(Point(3.2,3),Point(6.7,5)).draw(win)
                         done =  Text(Point(15, 4), "Done")
                         done.draw(win)
                         Rectangle(Point(13.2,3),Point(16.7,5)).draw(win)
                         add =  Text(Point(25, 4), "Add")
                         add.draw(win)
                         Rectangle(Point(23.2,3),Point(26.7,5)).draw(win)

                         def add():
                              welcome.undraw()
                              try:
                                   a = win.getMouse()
                                   ax = a.getX()
                                   ay = a.getY()
                                   if 23.2<=ax<=26.7 and 3<=ay<=5:
                                        
                                        try:
                                             maths = eval(mathsInput.getText())
                                             mathe = eval(mathsex.getText())
                                             if 0<=maths<=100 and 0<=mathe<=50: 
                                                  mathScore.append(maths)
                                                  mathScores.append(maths)
                                                  mathScorex.append(mathe) 
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()
                                                  
                                             
                                        try:
                                             english = eval(englishInput.getText())
                                             englishe = eval(englishex.getText())
                                             if 0<=english<=100 and 0<=englishe<=50: 
                                                  engScore.append(english)
                                                  engScores.append(english)
                                                  engScorex.append(englishe)
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()       
                                             
                                        try:
                                             science = eval(scienceInput.getText())
                                             sciencee = eval(scienceex.getText())
                                             if 0<=science<=100 and 0<=sciencee<=50: 
                                                  sciScore.append(science)
                                                  sciScores.append(science)
                                                  sciScorex.append(sciencee)
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()
                                                  
                                           
                                        try:
                                             social = eval(socialInput.getText())
                                             sociale = eval(socialex.getText())
                                             if 0<=social<=100 and 0<=sociale<=50: 
                                                  socScore.append(social)
                                                  socScores.append(social)
                                                  socScorex.append(sociale)
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()
                                                  
                                            
                                        try:
                                             ict = eval(ictInput.getText())
                                             icte = eval(ictex.getText())
                                             if 0<=ict<=100 and 0<=icte<=50: 
                                                  ictScore.append(ict)
                                                  ictScores.append(ict)
                                                  ictScorex.append(icte)
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()
                                                  
                                            
                                        try:
                                             rme = eval(rmeInput.getText())
                                             rmees = eval(rmeex.getText())
                                             if 0<=rme<=100 and 0<=rmees<=50: 
                                                  rmeScore.append(rme)
                                                  rmeScores.append(rme)
                                                  rmeScorex.append(rmees)
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()
                                                  
                                             
                                        try:
                                             twi = eval(twiInput.getText())
                                             twie = eval(twiex.getText())
                                             if 0<=twi<=100 and 0<=twie<=50:  
                                                  twiScore.append(twi)
                                                  twiScores.append(twi)
                                                  twiScorex.append(twie)
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()
                                           
                                        try:
                                             bdt = eval(bdtInput.getText())
                                             bdte = eval(bdtex.getText())
                                             if 0<=bdt<=100 and 0<=bdte<=50: 
                                                  bdtScore.append(bdt)
                                                  bdtScores.append(bdt)
                                                  bdtScorex.append(bdte)
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()
                                                  
                                            
                                        try:
                                             french = eval(frenchInput.getText())
                                             frenche= eval(frenchex.getText())
                                             if 0<=french<=100 and 0<=frenche<=50: 
                                                  frenScore.append(french)
                                                  frenScores.append(french)
                                                  frenScorex.append(frenche)
                                             else:
                                                  error_occured()
                                                  add()
                                        except SyntaxError:
                                             error_occured()
                                             add()
                                        except NameError:
                                             error_occured()
                                             add()
                                        name = nameInput.getText()
                                        names.append(name)
                                        info.setText("saved")
                                        time.sleep(1)
                                        info.setText(" ")
                                        
                                        draw()
                                        add()

                                   elif 23.5<=ax<=26.5 and 26.5<=ay<=27.5:
                                        win2 = GraphWin("Help", 500,200)
                                        win2.setCoords(0.0,0.0, 150, 10.0)
                                        but6 = Text(Point(75,9), "The Report Preparation Program helps you create")
                                        but8 = Text(Point(75,8), "a report of your students' performance. Fill the spaces provided with").draw(win2)
                                        but9 = Text(Point(75,7), "the necessary information. Click Add to add the information").draw(win2)
                                        but6.draw(win2)
                                        but10 = Text(Point(75,6), "about the student you entered. After you are done with entering").draw(win2)
                                        but11 = Text(Point(75,5), "the scores for all the students, click on Done to compute ").draw(win2)
                                        Text(Point(75,4), "everything. The report is saved in a file named recordss in").draw(win2)
                                        Text(Point(75,3), "the folder in which you stored this program's module. Click").draw(win2)
                                        Text(Point(75,2), "Quit if you do not want to use the program again. Enjoy yourself.").draw(win2)
                                       
                                        but7 = Text(Point(75,1), "Got it!").draw(win2)
                                        rect6 = Rectangle(Point(65.5,0.5),Point(85.5,1.5)).draw(win2)
                                        def helps():
                                             n = win2.getMouse()
                                             X = n.getX()
                                             Y = n.getY()
                                             if 65.5<=X<=85.5 and 0.5<=Y<=1.5:
                                                  win2.close()
                                                  add()
                                             else:
                                                  helps()
                                        helps()
                                                  
                                             
                                        
                                   elif 13.2<=ax<=16.7 and 3<=ay<=5:
                                        win3 = GraphWin("Done", 300,200)
                                        win3.setCoords(0.0,0.0, 6.0, 6.0)
                                        but6 = Text(Point(3,5), "Are you sure you are done?")
                                        but6.draw(win3)
                                        but7 = Text(Point(2,3), "Yes").draw(win3)
                                        but8 = Text(Point(3.5,3), "No").draw(win3)
                                        rect6 = Rectangle(Point(1.5,2.5),Point(2.5,3.5)).draw(win3)
                                        rect7 = Rectangle(Point(3,2.5),Point(4,3.5)).draw(win3)
                                        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

                                        def done():
                                             try:
                                                  d = win3.getMouse()
                                                  X = d.getX()
                                                  Y = d.getY()
                                                  if 1.5<=X<=2.5 and 2.5<=Y<=3.5:

                                                       win3.close()
                                                       m,e,sc,ict,f,t,r,so,b = 0,0,0,0,0,0,0,0,0
                                                       a = 0
                                                       print("MATHEMATICS", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                       
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*mathScore[i] + mathScorex[i]
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"

                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, mathScore[i], mathScorex[i], mark, grade), file = records)
                                                            m = m + mark
                                                       print("\n", file = records)
                                                       print ("The average score for Maths is", m/len(mathScore), file = records)
                                                       a = 0
                                                       print("\n", file = records)
                                                       
                                                       print("ENGLISH", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*engScore[i] + engScorex[i]
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"
                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, engScore[i], engScorex[i], mark, grade), file = records)
                                                            e = e + mark
                                                       print("\n", file = records)
                                                       print ("The average score for English is", e/len(mathScore), file = records)
                                                       print("\n", file = records)
                                                       a = 0
                                                       print("SCIENCE", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*sciScore[i] + sciScorex[i]
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"
                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, sciScore[i], sciScorex[i], mark, grade), file = records)
                                                            sc = sc + mark
                                                       print("\n", file = records)
                                                       print ("The average score for Science is", sc/len(mathScore), file = records)
                                                       print("\n", file = records)
                                                       a = 0
                                                       print("ICT", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*ictScore[i] + ictScorex[i]
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"
                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, ictScore[i], ictScorex[i], mark, grade), file = records)
                                                            ict = ict + mark
                                                       print("\n", file = records)
                                                       print ("The average score for ICT is", ict/len(mathScore), file = records)
                                                       a = 0
                                                       print("\n", file = records)
                                                       print("FRENCH", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                      
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*frenScore[i] + frenScorex[i]
                                                  
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"
                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, frenScore[i], frenScorex[i], mark, grade), file = records)
                                                            f = f + mark
                                                       print("\n", file = records)
                                                       print ("The average score for French is", f/len(mathScore), file = records)
                                                       a = 0
                                                       print("\n", file = records)
                                                       print("TWI", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*twiScore[i] + twiScorex[i]
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"
                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, twiScore[i], twiScorex[i], mark, grade), file = records)
                                                            t = t + mark
                                                       print("\n", file = records)
                                                       print ("The average score for Twi is", t/len(mathScore), file = records)
                                                       print("\n", file = records)
                                                       a = 0
                                                       print("RME", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*rmeScore[i] + rmeScorex[i]
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"
                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, rmeScore[i], rmeScorex[i], mark, grade), file = records)
                                                            r = r + mark
                                                       rmee.append(r)
                                                       print("\n", file = records)
                                                       print ("The average score for RME is", r/len(mathScore), file = records)
                                                       a = 0
                                                       print("\n", file = records)
                                                       print("SOCIAL", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*socScore[i] + socScorex[i]
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"
                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, socScore[i], socScorex[i], mark, grade), file = records)
                                                            so = so + mark
                                                       print("\n", file = records)
                                                       print ("The average score for Social is", so/len(mathScore), file = records)
                                                       a = 0
                                                       print("\n", file = records)
                                                       print("BDT", file=records)
                                                       print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format("Name", "Exam", "Class work", "Total", "Grade"), file = records)
                                                       for i in range(len(mathScore)):
                                                            mark = 0.5*bdtScore[i] + bdtScorex[i]
                                                            a = a + 1
                                                            mn = names[a]
                                                            if mark>=80:
                                                                 grade = "1"
                                                            elif 75<=mark<80:
                                                                 grade= "2"
                                                            elif 70<=mark<75:
                                                                 grade= "3"
                                                            elif 65<=mark<70:
                                                                 grade= "4"
                                                            elif 60<=mark<65:
                                                                 grade= "5"
                                                            elif 55<=mark<60:
                                                                 grade= "6"
                                                            elif 50<=mark<55:
                                                                 grade= "7"
                                                            elif 40<=mark<50:
                                                                 grade= "8"
                                                            elif mark<=39:
                                                                 grade= "9"
                                                            print("{0:25} {1:^15}{2:^15} {3:^15} {4:^15}".format(mn, bdtScore[i], bdtScorex[i], mark, grade), file = records)
                                                            b = b + mark
                                                       bdtt.append(b)

                                                       print("\n", file = records)
                                                       print()
                                                       print ("The average score for BDT is", b/len(mathScore), file = records)
                                                       print("\n", file = records)
                                                       print("\n", file = records)
                                                       print("\n", file = records)
                                                       print("\n", file = records)
                                                       print("\n", file = records)
                                                       z = 0
                                                       for q in range(len(mathScore)):
                                                            
                                                            totals = mathScore[z]+engScore[z]+sciScore[z]+ictScore[z]+frenScore[z]+twiScore[z]+rmeScore[z]+socScore[z]+bdtScore[z]
                                                            totalss.append(totals)
                                                            totali.append(totals)
                                                            z = z + 1

                                                       totalss.sort(reverse = True)
                                                       for i in totali:
                                                            if i in totalss:
                                                                 b = totalss.index(i)
                                                                 positions.append(b+1)
                                                       z = 0
                                                       print("{0:20} {1:^5} {2:^5} {3:^5} {4:^5} {5:^5} {6:^5} {7:^5} {8:^5} {9:^5} {10:^5} {11:^3}".format("Name", "Maths", "Eng", "Sci", "ICT", "Fren", "Twi", "RME", "Soc", "BDT", "Total", "Pos"), file = records)
                                                       for r in range(len(mathScore)):
                                                            totals = mathScore[z]+engScore[z]+sciScore[z]+ictScore[z]+frenScore[z]+twiScore[z]+rmeScore[z]+socScore[z]+bdtScore[z]
                                                            print("{0:20} {1:^5} {2:^5} {3:^5} {4:^5} {5:^5} {6:^5} {7:^5} {8:^5} {9:^5} {10:^5} {11:^3}".format(names[z+1], mathScore[z], engScore[z],
                                                                                                                                                               sciScore[z], ictScore[z], frenScore[z], twiScore[z], rmeScore[z], socScore[z], bdtScore[z],totals, positions[z]), file=records)
                                                           
                                                            z = z + 1
                                                            print()
                                                            print("\n", file = records)


                                                            
                                                       totalss.sort(reverse = True)
                                                       if totalss[0] in totali:
                                                               b = totali.index(totalss[0])
                                                               print(schoolname[0] .center(60), file=certificate)
                                                               print(" \n", file=certificate)
                                                               print(" \n", file=certificate)
                                                               print(" \n", file=certificate)
                                                               print("CERTIFICATE OF EXCELLENCE".center(60), file=certificate)
                                                               print(" \n", file=certificate)
                                                               print(" \n", file=certificate)
                                                               print(" \n", file=certificate)
                                                               print("This certificate is presented to", names[b+1] .center(40), file=certificate )
                                                               print(" \n", file=certificate)
                                                               print(" \n", file=certificate)
                                                               print(" \n", file=certificate)
                                                               print("for being the OVERALL BEST STUDENT in the end of term exams".center(60), file=certificate)
                                                               print("for the 2015/2016 academic year.".center(60), file=certificate)
                                                               print(" \n", file=certificate)
                                                               print(" \n", file=certificate)
                                                               print(" \n", file=certificate)
                                                               print("    Teacher                                   Headmaster".center(60), file=certificate)
                                                               print(" \n", file=certificate)
                                                               print("   __________                                _____________".center(60), file=certificate)
                                                               print("",teachername[0], "   ", mastername[0]  .center(60), file=certificate)
                                                               print("   (CLASS TEACHER)                            (HEADMASTER)".center(20), file=certificate)                              

                                                       print("\n", file=records)
                                                       print("\n", file = records)
                                                       print("\n", file = records)
                                                       print("\n", file = records)
                                                       print("\n", file = records)
                                                       print("BEST IN SUBJECTS", file = records)
                                                       mathScore.sort(reverse = True)
                                                       if mathScore[0] in mathScores:
                                                               b = mathScores.index(mathScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("Mathematics", names[b+1], mathScore[0]), file = records)
                                             
                                                               print("\n", file=records)
                                                       engScore.sort(reverse = True)
                                                       if engScore[0] in engScores:
                                                               b = engScores.index(engScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("English", names[b+1], engScore[0]), file = records)
                                                               
                                                               print("\n", file=records)
                                                       sciScore.sort(reverse = True)
                                                       if sciScore[0] in sciScores:
                                                               b = sciScores.index(sciScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("Science", names[b+1], sciScore[0]), file = records)
                                                               
                                                               print("\n", file=records)
                                                       ictScore.sort(reverse = True)
                                                       if ictScore[0] in ictScores:
                                                               b = ictScores.index(ictScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("ICT", names[b+1], ictScore[0]), file = records)
                                                               
                                                               print("\n", file=records)
                                                       frenScore.sort(reverse = True)
                                                       if frenScore[0] in frenScores:
                                                               b = frenScores.index(frenScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("French", names[b+1], frenScore[0]), file = records)
                                                               
                                                               print("\n", file=records)
                                                       twiScore.sort(reverse = True)
                                                       if twiScore[0] in twiScores:
                                                               b = twiScores.index(twiScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("Twi", names[b+1], twiScore[0]), file = records)
                                                               
                                                               print("\n", file=records)
                                                       rmeScore.sort(reverse = True)
                                                       if rmeScore[0] in rmeScores:
                                                               b = rmeScores.index(rmeScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("RME", names[b+1], rmeScore[0]), file = records)
                                                               
                                                               print("\n", file=records)
                                                       socScore.sort(reverse = True)
                                                       if socScore[0] in socScores:
                                                               b = socScores.index(socScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("Social", names[b+1], socScore[0]), file = records)
                                                               
                                                               print("\n", file=records)
                                                       bdtScore.sort(reverse = True)
                                                       if bdtScore[0] in bdtScores:
                                                               b = bdtScores.index(bdtScore[0])
                                                               print("{0:25} {1:^25} {2:^15}".format("BDT", names[b+1], bdtScore[0]), file = records)
                                                               
                                                               print("\n", file=records)
                                                       records.close()
                                                       certificate.close()
                                                       thankss = Thanks()
                                                       thankss.thanks()
                                                       print("Done. Open recordss.txt and certificate.txt for results...")
                                                       win = GraphWin("Bar Graph", 1000,600)
                                                       win.setCoords (0.0,0.0,12.0,14.0)
                                                       line1 = Line(Point(1,1), Point(1,12)).draw(win)
                                                       line2 = Line(Point(1,1), Point(12,1)).draw(win)
                                                       r1 = Rectangle(Point(2,(m/len(mathScore))*0.1 + 1), Point(3,1)).draw(win)
                                                       r2 = Rectangle(Point(3,( e/len(mathScore))*0.1 + 1), Point(4,1)).draw(win)
                                                       r3 = Rectangle(Point(4,(sc/len(mathScore))*0.1 + 1), Point(5,1)).draw(win)
                                                       r4 = Rectangle(Point(5,(ict/len(mathScore))*0.1 + 1), Point(6,1)).draw(win)
                                                       r5 = Rectangle(Point(6,(f/len(mathScore))*0.1 + 1), Point(7,1)).draw(win)
                                                       r6 = Rectangle(Point(7,(t/len(mathScore))*0.1 + 1), Point(8,1)).draw(win)
                                                       r7 = Rectangle(Point(8, rmee[0]/len(mathScore)*0.1 + 1), Point(9,1)).draw(win)
                                                       r8 = Rectangle(Point(9,(so/len(mathScore))*0.1 + 1), Point(10,1)).draw(win)
                                                       r9 = Rectangle(Point(10,(bdtt[0]/len(mathScore))*0.1 + 1), Point(11,1)).draw(win)
                                                       Text(Point(0.7,1), "0").draw(win)
                                                       Text(Point(0.7,2), "10").draw(win)
                                                       Text(Point(0.7,3), "20").draw(win)
                                                       Text(Point(0.7,4), "30").draw(win)
                                                       Text(Point(0.7,5), "40").draw(win)
                                                       Text(Point(0.7,6), "50").draw(win)
                                                       Text(Point(0.7,7), "60").draw(win)
                                                       Text(Point(0.7,8), "70").draw(win)
                                                       Text(Point(0.7,9), "80").draw(win)
                                                       Text(Point(0.7,10), "90").draw(win)
                                                       Text(Point(0.7,11), "100").draw(win)
                                                       Text(Point(6.5, 0.1), "SUBJECTS").draw(win)
                                                       Text(Point(2.5, 0.7), "Maths").draw(win)
                                                       Text(Point(3.5, 0.7), "English").draw(win)
                                                       Text(Point(4.5, 0.7), "Science").draw(win)
                                                       Text(Point(5.5, 0.7), "ICT").draw(win)
                                                       Text(Point(6.5, 0.7), "French").draw(win)
                                                       Text(Point(7.5, 0.7), "Twi").draw(win)
                                                       Text(Point(8.5, 0.7), "RME").draw(win)
                                                       Text(Point(9.5, 0.7), "Social").draw(win)
                                                       Text(Point(10.5, 0.7), "BDT").draw(win)
                                                       Text(Point(6.5, 13), "A Histogram Showing The Average Students Performance in the Various Subjects").draw(win)
                                                       Text(Point(1,12.5), "Average").draw(win)
                                                       

                                                       add()

                                                  elif 3<=X<=4 and 2.5<=Y<=5:
                                                       win2.close()
                                                       add()
                                                  else:
                                                       but6.setText("Click either yes or no")
                                                       time.sleep(0.05)
                                                       but6.setText("Are you sure you are done?")
                                                       done()
                                             except ZeroDivisionError:
                                                  error_occured()
                                                  add() 
                                        done()
                                   elif 3.2<=ax<=6.7 and 3<=ay<=5:
                                        win2 = GraphWin("Done", 300,200)
                                        win2.setCoords(0.0,0.0, 6.0, 6.0)
                                        
                                        but6 = Text(Point(3,5), "Are you sure you want to quit?")
                                        but6.draw(win2)
                                        but7 = Text(Point(2,3), "Yes").draw(win2)
                                        but8 = Text(Point(3.5,3), "No").draw(win2)
                                        rect6 = Rectangle(Point(1.5,2.5),Point(2.5,3.5)).draw(win2)
                                        rect7 = Rectangle(Point(3,2.5),Point(4,3.5)).draw(win2)
                                        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                                        def quits():
                                             n = win2.getMouse()
                                             X = n.getX()
                                             Y = n.getY()
                                             if 1.5<=X<=2.5 and 2.5<=Y<=3.5:
                                                  win2.close()
                                                  win.close()
                                                  winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
                                                  
                                             elif 3<=X<=4 and 2.5<=Y<=5:
                                                  win2.close()
                                                  add()
                                             else:
                                                  but6.setText("Click either yes or no")
                                                  time.sleep(0.05)
                                                  but6.setText("Are you sure you want to quit?")
                                                  quits()
                                        quits()
                                   else:
                                        add()

                              except ZeroDivisionError:
                                   error_occured()
                                   add()
                              except TypeError:
                                   error_occured()
                                   add()
                              
                                                    
                         add()
                    draw()
               sax()
          enter()                                   
     main()
clicks()
















     





