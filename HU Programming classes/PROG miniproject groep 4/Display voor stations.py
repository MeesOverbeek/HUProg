import requests
import xmltodict
from tkinter import *
#from treinfuncties import * calls upon Treinfuncties.py
from Treinfuncties import *
from tkinter.messagebox import showinfo

authDetails = ('mees-overbeek@hotmail.com', 'xyy3hgLOXBq1i3sNZgp5qVwLPraeb4APZw_JI2iEB-zP3qfpfsj9fg')
apiUrl = 'http://webservices.ns.nl/ns-api-avt?station=ut'
response = requests.get(apiUrl, auth = authDetails)

vertrekXML = xmltodict.parse(response.text)
print('dit zijn de vertrekkende treinen: ')


def stationlijst():
    'stopt de api info in een dictionary'
    eindbestemming = {}
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming[vertrek['EindBestemming']] = vertrek['VertrekTijd']
    return eindbestemming
def vertrekker():
    'gebruikt de dictionary en geeft de vertrektijd'
    lst = stationlijst()
    entry = afstandEntry.get()
    for vertrek in lst:
        if vertrek == entry:
            vertrektijd = lst[vertrek]

            showinfo(message='Om ' + vertrektijd + ' vertrekt een trein naar ' + vertrek)

StationLister()
