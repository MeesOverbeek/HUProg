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


def StationLister():
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']

        vertrektijd = vertrektijd[11:16]

        print('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming)


StationLister()
