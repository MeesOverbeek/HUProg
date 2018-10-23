import requests
import xmltodict
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
#from Treinfuncties import * #calls upon Treinfuncties.py


def stationClick():
    vertrekker()


def vertrekker():
    try:
        stationName = stationEntry.get()
        authDetails = ('mees-overbeek@hotmail.com', 'xyy3hgLOXBq1i3sNZgp5qVwLPraeb4APZw_JI2iEB-zP3qfpfsj9fg')
        apiUrl = 'http://webservices.ns.nl/ns-api-avt?station=' + stationName
        response = requests.get(apiUrl, auth=authDetails)

        vertrekXML = xmltodict.parse(response.text)
        if "error" in vertrekXML.keys():
            print(vertrekXML["error"]["message"])
            messagebox.showerror('Foutmelding',
                                 'Invoer is ongeldig, kijk of de naam van het station correct is ingevoerd')
            return

        departureInformation = "";
        row = 0;
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:

            eindbestemming = vertrek['EindBestemming']

            vertrektijd = vertrek['VertrekTijd']

            vertrektijd = vertrektijd[11:19]

            print(vertrek)

            vertrektijdlabel = Label(master=departureframe,
                                     text=vertrektijd,
                                     background='yellow',
                                     foreground='black',
                                     font=('Helvetica', 16, 'bold italic'),
                                     anchor=W)
            vertrektijdlabel.grid(row=row, column=0, sticky=N, pady=(8, 0))
            eindbestemminglabel = Label(master=departureframe,
                                        text=eindbestemming,
                                        background='yellow',
                                        foreground='black',
                                        font=('Helvetica', 16, 'bold italic'),
                                        anchor='w')
            eindbestemminglabel.grid(row=row, column=1, sticky=N, pady=(8, 0))
            try:
                vertrekspoorlabel = Label(master=departureframe,
                                          text="Spoor " + str(vertrek["VertrekSpoor"]["#text"]),
                                          background='yellow',
                                          foreground='black',
                                          font=('Helvetica', 16, 'bold italic'))
                vertrekspoorlabel.grid(row=row, column=2, sticky=E, pady=(8, 0))
            except:
                print("geen spoor")
            row += 1;

            departureInformation += 'Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming + '\n'
        mainframe.forget();
        departureframe.pack(fill=None, expand=False);
        showinfo(message=departureInformation)

    except:
        messagebox.showerror('Foutmelding', 'U bent niet verbonden met het internet, controleer uw internetverbinding en probeer het opnieuw.')
        print("No internet connection")



#form functions to perform commands, functions need to remain outside the tkinter frame code (remain global)
root = Tk()

mainframe = Frame(master=root)
mainframe.pack(fill="both", expand=False)

mainlabel = Label(master=mainframe,
              text='Een hele goede dag\nWelkom bij NS-reisinformatie\n\n\nVanaf waar wilt u reizen?',
              background='yellow',
              foreground='blue',
              font=('Aldus', 20, 'bold'),
              width=50,
              height=15)

mainlabel.pack()

stationEntry = Entry(master=mainframe,)
stationEntry.pack()

button = Button(master=mainframe, text='Druk hier', command=stationClick)
button.pack()

departureframe = Frame(master=root, width=250, height=100)
departureframe.pack(fill=None, expand=False)

departureframe.forget()



# ensures the given command works

entry = Entry()

root.mainloop()

