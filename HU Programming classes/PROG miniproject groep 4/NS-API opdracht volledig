import requests
import xmltodict
import dicttoxml
import datetime
import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.messagebox import showinfo
#from Treinfuncties import * #calls upon Treinfuncties.py

#makes a connection with the api
def connectAPI(stationName):
    lastStationName = ""
    #try to open a file
    try:
        stationNameFile = open("lastStationName.txt", "r+")
        lastStationName = stationNameFile.read()
        stationNameFile.close()
    #if failing to open the file because it doesn't exist, create a new one
    except:
        stationNameFile = open("lastStationName.txt", "w")
        stationNameFile.close()

    #try to make a connection with the api
    try:
        authDetails = ('mees-overbeek@hotmail.com', 'xyy3hgLOXBq1i3sNZgp5qVwLPraeb4APZw_JI2iEB-zP3qfpfsj9fg')
        apiUrl = 'http://webservices.ns.nl/ns-api-avt?station=' + stationName
        response = requests.get(apiUrl, auth=authDetails)

        vertrekXML = xmltodict.parse(response.text)

        #if the api responded with an error code, show it in a messagebox
        if "error" in vertrekXML.keys():
            print(vertrekXML["error"]["message"])
            messagebox.showerror('Foutmelding',
                                 'Invoer is ongeldig, kijk of de naam van het station correct is ingevoerd')
            return

        departuresFile = open("departures.xml", "w")
        departuresFile.write(response.text)
        departuresFile.close()
        stationNameFile = open("lastStationName.txt", "w")
        stationNameFile.write(stationName)
        stationNameFile.close()
    #if there was no connection with the api, check for a local file
    except:

        #if the last looked up station has the same name as the current looked up station then open the local file and show that data.
        if lastStationName == stationName:
            departuresFile = open("departures.xml", "r")
            vertrekXML = xmltodict.parse(departuresFile.read())
            departuresFile.close()
        #else show a messagebox that there was no connection with the internet
        else:
            messagebox.showerror('Foutmelding', 'U bent niet verbonden met het internet, controleer uw internetverbinding en probeer het opnieuw.')


    return vertrekXML

#when clicking the look up button, show a screen with all the departures of the filled in station.
def stationClick():
    vertrekker()

#when clicking the back button, go back to the previous screen
def backClick():
    mainframe.pack()
    for widget in departureframe.winfo_children():
        widget.destroy()
    departureframe.forget()

#show the visuals of all the departures
def showDepartureVisuals(vertrekXML, stationName):
    departureInformation = "";
    row = 0;

    backButton = Button(master=departureframe, text='<', command=backClick)
    backButton.grid(row=row, column=0, sticky="ns", pady=(8, 0))
    vertrektijdlabel = Label(master=departureframe,
                             text=stationName,
                             background='yellow',
                             foreground='Blue',
                             font=('Helvetica', 20, 'bold'),
                             anchor=W)
    vertrektijdlabel.grid(row=row, column=1, pady=(8, 0))

    row += 1;
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        if row >= 39:
            break

        vertrektijd = vertrek['VertrekTijd']
        vertrektijd = vertrektijd[11:19]
        eindbestemming = vertrek['EindBestemming']


        vertrektijdlabel = Label(master=departureframe,
                                 text=vertrektijd,
                                 background='yellow',
                                 foreground='black',
                                 font=('Helvetica', 10, 'bold italic'),
                                 anchor=W)
        vertrektijdlabel.grid(row=row, column=0, sticky="ns", pady=(8, 0))
        eindbestemminglabel = Label(master=departureframe,
                                    text=eindbestemming,
                                    background='yellow',
                                    foreground='black',
                                    font=('Helvetica', 10, 'bold italic'),
                                    anchor='w')
        eindbestemminglabel.grid(row=row, column=1, sticky="ns", pady=(8, 0), padx=10)
        try:
            vertrekspoorlabel = Label(master=departureframe,
                                      text="Spoor " + str(vertrek["VertrekSpoor"]["#text"]),
                                      background='yellow',
                                      foreground='black',
                                      font=('Helvetica', 10, 'bold italic'))
            vertrekspoorlabel.grid(row=row, column=2, sticky="ns", pady=(8, 0))
        except:
            print("geen spoor")
        row += 1;
        treinSoortLabel = Label(master=departureframe,
                                text=eindbestemming + " (" + str(vertrek['TreinSoort']) + ")",
                                background='yellow',
                                foreground='black',
                                font=('Helvetica', 10, 'bold italic'),
                                anchor='w')
        treinSoortLabel.grid(row=row, column=1, sticky="ns")
        row += 1;
        try:
            viaLabel = Label(master=departureframe,
                             text=vertrek['RouteTekst'],
                             background='yellow',
                             foreground='black',
                             font=('Helvetica', 10, 'bold italic'),
                             anchor='w')
            viaLabel.grid(row=row, column=1, sticky="ns", padx=10)
        except:
            print("Geen via")
        row += 1

#handles all the data and show the departure frame
def vertrekker():
    stationName = stationEntry.get()

    vertrekXML = connectAPI(stationName)

    showDepartureVisuals(vertrekXML, stationName)


    mainframe.forget()
    departureframe.pack(fill=None, expand=False)


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

departureframe = Frame(master=root, width=500, height=100, background="yellow")
departureframe.pack(fill=None, expand=False)

departureframe.forget()


button = Button(master=mainframe, text='Druk hier', command=stationClick)
button.pack()

# ensures the given command works

entry = Entry()

root.mainloop()

