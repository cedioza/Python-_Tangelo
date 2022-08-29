import requests
import pandas as pd
import time
from ..utils.encrypt import Encrypt
from ..config.database import CountriesDb

class Country():

    def __init__(self,name):

        self.rows=[]
        self.country_db=CountriesDb(name)
        self.dataframe=None
        
    def getCountries(self,url,initial_time):

        try :
            response=requests.get(f'{url}').json()

            for country in response: 
                region=country.get('region')
                city=country.get('name')["common"]
                languajes=country.get('languages')
                languajes={value for value in languajes.values()} if languajes is not None else ["Not Registered"]
                languajes="-".join(languajes)
                encryptLanguaje= Encrypt(languajes).encryptData()
                self.rows.append([region,city,encryptLanguaje, time.time() - initial_time ])
 
        except Exception as error:
            print("Message : ",  error)

    def createDataFrame(self):
        self.dataframe = pd.DataFrame(self.rows, columns=["Región", "City", "Language", "Time"])

    def insertCountries(self):

        for row in self.rows:
            self.country_db.insertTable(row)
            
    def createTable(self):
        self.country_db.createTable()

    def getTimes(self):

        print(f"""\nTiempo total: {self.dataframe['Time'].sum()} s
        \nTiempo promedio: {self.dataframe['Time'].mean()} s
        \nTiempo minimo: { self.dataframe['Time'].min()} s 
        \nTiempo maximo: { self.dataframe['Time'].max()} s """)

    def create_json(self):
         self.dataframe.to_json(r"./json/countries.json")