from tkinter import *
from tkinter.ttk import Progressbar
from pygame import mixer
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

mixer.init()


# mixer.music.load('kbc.mp3')
# mixer.music.play()


def select(event):
    callButton.place_forget()
    progressbarA.place_forget()
    progressbarB.place_forget()
    progressbarC.place_forget()
    progressbarD.place_forget()

    progressbarLabelA.place_forget()
    progressbarLabelB.place_forget()
    progressbarLabelC.place_forget()
    progressbarLabelD.place_forget()

    b = event.widget
    value = b['text']

    for i in range(15):
        if value == correct_answers[i]:
            if value == correct_answers[14]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playAgain():
                    lifeLine50Button.config(state=NORMAL, image=image50)
                    lifeLineAudienceButton.config(state=NORMAL, image=imageAudience)
                    lifeLineCallButton.config(state=NORMAL, image=imageCall)
                    root2.destroy()
                    questionArea.delete(1.0, END)
                    questionArea.insert(END, questions[0])

                    optionB1.config(text=first_option[0])
                    optionB2.config(text=second_option[0])
                    optionB3.config(text=third_option[0])
                    optionB4.config(text=fourth_option[0])

                    amountLebel.config(image=amountImage1)

                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()
                root2 = Toplevel()
                root2.overrideredirect(True)
                root2.config(bg='black')
                root2.geometry('500x400+140+30')
                root2.title('You won 0 tk')
                happyImage = PhotoImage(file='smile.png')
                imageLabel = Label(root2, image=happyImage, bd=0, bg='black')
                imageLabel.pack(pady=30)

                winLebel = Label(root2, text='You Won', font=('arial', 40, 'bold'), bg='black', fg='white')
                winLebel.pack()

                playAgainButton = Button(root2, text='Play Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                         activeforeground='white', activebackground='black', bd=0, cursor='hand2',
                                         command=playAgain)

                playAgainButton.pack()

                closeAgainButton = Button(root2, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                          activeforeground='white', activebackground='black', bd=0, cursor='hand2',
                                          command=close)

                closeAgainButton.pack()
                root2.mainloop()
                break

            questionArea.delete(1.0, END)
            questionArea.insert(END, questions[i + 1])

            optionB1.config(text=first_option[i + 1])
            optionB2.config(text=second_option[i + 1])
            optionB3.config(text=third_option[i + 1])
            optionB4.config(text=fourth_option[i + 1])
            amountLebel.config(image=amountImages[i + 1])

        if value not in correct_answers:
            def close():
                root1.destroy()
                root.destroy()

            def tryAgain():
                lifeLine50Button.config(state=NORMAL, image=image50)
                lifeLineAudienceButton.config(state=NORMAL, image=imageAudience)
                lifeLineCallButton.config(state=NORMAL, image=imageCall)
                root1.destroy()
                questionArea.delete(1.0, END)
                questionArea.insert(END, questions[0])

                optionB1.config(text=first_option[0])
                optionB2.config(text=second_option[0])
                optionB3.config(text=third_option[0])
                optionB4.config(text=fourth_option[0])

                amountLebel.config(image=amountImage1)

            root1 = Toplevel()
            root1.overrideredirect(True)
            root1.config(bg='black')
            root1.geometry('500x400+140+30')
            root1.title('You won 0 tk')
            sadImage = PhotoImage(file='sad.png')
            imageLabel = Label(root1, image=sadImage, bd=0, bg='black')
            imageLabel.pack(pady=30)

            loseLebel = Label(root1, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
            loseLebel.pack()

            tryAgainButton = Button(root1, text='Try Again', font=('arial', 20, 'bold'), bg='black', fg='white',
                                    activeforeground='white', activebackground='black', bd=0, cursor='hand2',
                                    command=tryAgain)

            tryAgainButton.pack()

            closeAgainButton = Button(root1, text='Close', font=('arial', 20, 'bold'), bg='black', fg='white',
                                      activeforeground='white', activebackground='black', bd=0, cursor='hand2',
                                      command=close)

            closeAgainButton.pack()

            root1.mainloop()
            break


def lifeLine50():
    lifeLine50Button.config(image=image50not, state=DISABLED)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        optionB1.config(text='')
        optionB4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        optionB2.config(text='')
        optionB4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        optionB3.config(text='')
        optionB4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        optionB2.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        optionB1.config(text='')
        optionB4.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        optionB1.config(text='')
        optionB3.config(text='')

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        optionB1.config(text='')
        optionB4.config(text='')


def audiencePoleLifeline():
    lifeLineAudienceButton.config(image=imageAudiencePol, state=DISABLED)
    progressbarA.place(x=580, y=190)
    progressbarB.place(x=620, y=190)
    progressbarC.place(x=660, y=190)
    progressbarD.place(x=700, y=190)

    progressbarLabelA.place(x=580, y=320)
    progressbarLabelB.place(x=620, y=320)
    progressbarLabelC.place(x=660, y=320)
    progressbarLabelD.place(x=700, y=320)

    if questionArea.get(1.0, 'end-1c') == questions[0]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[1]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[2]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[3]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[4]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=40)

    if questionArea.get(1.0, 'end-1c') == questions[5]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[6]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[7]:
        progressbarA.config(value=30)
        progressbarB.config(value=90)
        progressbarC.config(value=60)
        progressbarD.config(value=50)

    if questionArea.get(1.0, 'end-1c') == questions[8]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[9]:
        progressbarA.config(value=90)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=30)

    if questionArea.get(1.0, 'end-1c') == questions[10]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[11]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)

    if questionArea.get(1.0, 'end-1c') == questions[12]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[13]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=60)
        progressbarD.config(value=90)

    if questionArea.get(1.0, 'end-1c') == questions[14]:
        progressbarA.config(value=30)
        progressbarB.config(value=50)
        progressbarC.config(value=90)
        progressbarD.config(value=60)


def phoneLifeline():
    mixer.music.load('calling.mp3')
    mixer.music.play()
    callButton.place(x=70, y=260)
    lifeLineCallButton.config(image=imageCallX, state=DISABLED)


def phoneClick():
    for i in range(15):
        if questionArea.get(1.0, 'end-1c') == questions[i]:
            engine.say(f'The answer is{correct_answers[i]}')
            engine.runAndWait()


questions = ["What is the maximum length of a Python identifier?",
             "Which one of the following has the highest precedence in the expression?",
             "What is the return type of function id?",
             "Which of the following statements are used in Exception Handling in Python?",
             "Guido van Rossum in 1991 designed which language?",
             "Finish the sequence: 9, 18, 27, _?",
             "Which one is the first fully supported 64-bit operating system?",
             "Which animal is called the king of the jungle?",
             "The format function, when applied on a string returns:",
             "Which of the following refers to mathematical function?",
             "Which is the largest planet in our Solar system?",
             "How many continents are there in the world?",
             "How many years are there in one Millenium?",
             "ipad is manufactured by?",
             "Who founded Microsoft?"]

first_option = ["31", "Addition",
                "float", "try",
                "Javascript", "36",
                "Windows 7", "Elephant", "list", "sqrt",
                "Earth", "8",
                "100 years", "Google", "Monty Ritz"]

second_option = ["16", "Multiplication",
                 "bool", "except ",
                 "Python", "34",
                 "Linux", "Lion", "bool", "add",
                 "Uranus", "5",
                 "50 years",
                 "Microsoft", "Danis Lio"]

third_option = ["55", "Exponential",
                "dict", "finally",
                "Java", "30",
                "Mac", "Tiger", "int", "rhombus",
                "Mars", "7",
                "500 years",
                "Amazon", "Bill Gates"]

fourth_option = ["not fixed", "Parentheses",
                 "int", "All of above",
                 "C++", "37",
                 "Windows XP", "Cow", "str", "int",
                 "Jupiter",
                 "6",
                 "1000 years", "Apple",
                 "Jeff Bezos"]

correct_answers = ["not fixed", "Parentheses", "int", "All of above", "Python", "36",
                   "Linux", "Lion", "str", "sqrt", "Jupiter", "7", "1000 years", "Apple",
                   "Bill Gates"]

root = Tk()

root.geometry('1270x680+0+0')

root.title('Ke Hobe KotiPoti')

root.config(bg='black')

leftframe = Frame(root, bg='black', padx=90)
leftframe.grid(row=0, column=0)

topframe = Frame(leftframe, bg='black')
topframe.grid()

centerframe = Frame(leftframe, bg='black')
centerframe.grid(row=1, column=0)

bottomframe = Frame(leftframe)
bottomframe.grid(row=2, column=0)

rightframe = Frame(root, pady=25, padx=50, bg='black')
rightframe.grid(row=0, column=1)

# Button 50-50 life Line
image50 = PhotoImage(file='50-50.png')
image50not = PhotoImage(file='not50.png')

lifeLine50Button = Button(topframe, image=image50, bg='black', bd=0, activebackground='black', width=180, height=180,
                          command=lifeLine50)
lifeLine50Button.grid(row=0, column=0)

# Button Audience life Line
imageAudience = PhotoImage(file='aduience.png')
imageAudiencePol = PhotoImage(file='audiencePol.png')

lifeLineAudienceButton = Button(topframe, image=imageAudience, bg='black', bd=0, activebackground='black', width=180,
                                height=180, command=audiencePoleLifeline)
lifeLineAudienceButton.grid(row=0, column=1)

# Button Call life Line
imageCall = PhotoImage(file='call.png')
imageCallX = PhotoImage(file='callNot.png')

lifeLineCallButton = Button(topframe, image=imageCall, bg='black', bd=0, activebackground='black', width=180,
                            height=180, command=phoneLifeline)
lifeLineCallButton.grid(row=0, column=2)

# Button ring call
callImage = PhotoImage(file='phone.png')
callButton = Button(root, image=callImage, bd=0, bg='black', activebackground='black', cursor='hand2',
                    command=phoneClick)

centerImage = PhotoImage(file='millonaire.png')
logoLabel = Label(centerframe, image=centerImage, bg='black', width=300, height=200)
logoLabel.grid(row=0, column=0)

# set all amount image
amountImage1 = PhotoImage(file='1.png')
amountImage2 = PhotoImage(file='2.png')
amountImage3 = PhotoImage(file='3.png')
amountImage4 = PhotoImage(file='4.png')
amountImage5 = PhotoImage(file='5.png')
amountImage6 = PhotoImage(file='6.png')
amountImage7 = PhotoImage(file='7.png')
amountImage8 = PhotoImage(file='8.png')
amountImage9 = PhotoImage(file='9.png')
amountImage10 = PhotoImage(file='10.png')
amountImage11 = PhotoImage(file='11.png')
amountImage12 = PhotoImage(file='12.png')
amountImage13 = PhotoImage(file='13.png')
amountImage14 = PhotoImage(file='14.png')
amountImage15 = PhotoImage(file='15.png')
amountImage16 = PhotoImage(file='17.png')

amountImages = [amountImage2, amountImage3, amountImage4, amountImage5, amountImage6,
                amountImage7, amountImage8, amountImage9, amountImage10, amountImage11, amountImage12,
                amountImage13, amountImage14, amountImage15, amountImage16]

amountLebel = Label(rightframe, image=amountImage1, bg='black')
amountLebel.grid(row=0, column=0)

layoutImage = PhotoImage(file='lay.png')
layoutLabel = Label(bottomframe, image=layoutImage, bg='black')
layoutLabel.grid(row=0, column=0)

questionArea = Text(bottomframe, font=('arial', 18, 'bold'), width=34, height=2, wrap='word', bg='black'
                    , fg='white', bd=0)
questionArea.place(x=70, y=10)
questionArea.insert(END, questions[0])

# option button 1-(A)
labelA = Label(bottomframe, text='A:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelA.place(x=60, y=110)

optionB1 = Button(bottomframe, text=first_option[0], font=('arial', 18, 'bold'),
                  bg='black', fg='white', bd=0, activebackground='black', activeforeground='white')
optionB1.place(x=100, y=100)

# option button 2-(B)
labelbB = Label(bottomframe, text='B:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelbB.place(x=330, y=110)

optionB2 = Button(bottomframe, text=second_option[0], font=('arial', 18, 'bold'),
                  bg='black', fg='white', bd=0, activebackground='black', activeforeground='white')
optionB2.place(x=370, y=100)

# option button 3-(C)
labelbC = Label(bottomframe, text='C:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelbC.place(x=60, y=190)

optionB3 = Button(bottomframe, text=third_option[0], font=('arial', 18, 'bold'),
                  bg='black', fg='white', bd=0, activebackground='black', activeforeground='white')
optionB3.place(x=100, y=180)

# option button 4-(D)
labelbD = Label(bottomframe, text='D:', bg='black', fg='white', font=('arial', 16, 'bold'))
labelbD.place(x=330, y=190)

optionB4 = Button(bottomframe, text=fourth_option[0], font=('arial', 18, 'bold'),
                  bg='black', fg='white', bd=0, activebackground='black', activeforeground='white')
optionB4.place(x=370, y=180)

progressbarA = Progressbar(root, orient=VERTICAL, length=120)
progressbarB = Progressbar(root, orient=VERTICAL, length=120)
progressbarC = Progressbar(root, orient=VERTICAL, length=120)
progressbarD = Progressbar(root, orient=VERTICAL, length=120)

progressbarLabelA = Label(root, text='A', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelB = Label(root, text='B', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelC = Label(root, text='C', font=('arial', 20, 'bold'), bg='black', fg='white')
progressbarLabelD = Label(root, text='D', font=('arial', 20, 'bold'), bg='black', fg='white')

optionB1.bind('<Button-1>', select)
optionB2.bind('<Button-1>', select)
optionB3.bind('<Button-1>', select)
optionB4.bind('<Button-1>', select)

root.mainloop()
