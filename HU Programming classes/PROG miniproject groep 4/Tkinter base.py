from tkinter import *
#from treinfuncties import * calls upon Treinfuncties.py
from Treinfuncties import *
from tkinter.messagebox import showinfo

#start a Tkinter frame/terminal
root = Tk()

#base function to make the text appear in the given make-up
label = Label(master=root,
              text='Hello World',
              background='yellow',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'),
              width=20,
              height=10)

#create (as of right now) empty buttons to press
button1 = Button(master=root, text='Button 1')
button1.place(x=10, y=10)

button2 = Button(master=root, text='Button 2')
button2.place(x=10, y=60)

button3 = Button(master=root, text='Button 3')
button3.place(x=10, y=110)

#A function to make a pop-up frame
def clicked():
    bericht = 'Dit een bericht voor de gebruiker!'
    showinfo(title='popup', message=bericht)

button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)

#make multiple frames to allow a login module on the first and your button display on the second
def toonLoginFrame():
    hoofdframe.pack_forget()
    loginframe.pack()

def toonHoofdFrame():
    loginframe.pack_forget()
    hoofdframe.pack()

def login():
    if loginfield.get() == "admin":
        toonHoofdFrame()
    else:
        print('Verkeerde gebruikersnaam!')

#following code allows for manipulation of the functions to alter the frames
loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)
loginfield = Entry(master=loginframe)
loginfield.pack(padx=20, pady=20)
loginbutton = Button(master=loginframe, text='login', command=login)
loginbutton.pack(padx=20, pady=20)

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)
backbutton = Button(master=hoofdframe, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

#allows the toonLoginFrame function to be called upon (and thus work)
toonLoginFrame()

#ensures the given command works
label.pack()

#ensures the Tkinter frame works
root.mainloop()

#makes a frame that calls upon
def berekenTarief():
    afstand = float(afstandEntry.get())
    prijs = int(standaardprijs(afstand))
    label["text"] = "De ritprijs is: {}".format(prijs)


root = Tk()

afstandEntry = Entry(master=root)
afstandEntry.pack()

button = Button(master=root, text="Druk hier", command=berekenTarief)
button.pack()

label = Label(master=root)
label.pack()

root.mainloop()

