import requests
import xmltodict
import time
from tkinter import *
from tkinter.messagebox import showinfo
#from Treinfuncties import * #calls upon Treinfuncties.py

authDetails = ('mees-overbeek@hotmail.com', 'xyy3hgLOXBq1i3sNZgp5qVwLPraeb4APZw_JI2iEB-zP3qfpfsj9fg')
apiUrl = 'http://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(apiUrl, auth = authDetails)

vertrekXML = xmltodict.parse(response.text)


#form functions to perform commands, functions need to remain outside the tkinter frame code (remain global)
root = Tk()

label = Label(master=root,
              text='Een hele goede dag',
              background='pink',
              foreground='blue',
              font=('Helvetica', 16, 'bold italic'),
              width=20,
              height=10)
def clicked():
    bericht = 'Dit een bericht voor de gebruiker!'
    showinfo(master=root, title='popup', message=bericht)

def stationClick():
    showinfo(master=root, title='treinen', message=vertrekker())

def vertrekker():
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']

        vertrektijd = vertrektijd[11:19]

        showinfo(message='Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming)


button = Button(master=root, text='Druk hier', command=stationClick())
button.pack()

afstandEntry = Entry(master=root)
afstandEntry.pack()

label.pack()

#ensures the given command works

entry = Entry()

root.mainloop()

