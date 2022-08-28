import requests
import pandas as pd
import time
from ..utils.encrypt import Encrypt
from ..config.database import CountriesDb



class Country():

    def __init__(self,):
        self.initial_time=time.time()
        self.rows=[]
        self.country_db=CountriesDb("country")
        self.dataframe=None
        
    def getCountries(self,url):

        try :
            response=requests.get(f'{url}').json()

            for country in response: 
                region=country.get('region')
                city=country.get('name')["common"]
                languajes=country.get('languages')
                languajes={value for value in languajes.values()} if languajes is not None else ["Not Registered"]
                languajes="-".join(languajes)
                encryptLanguaje= Encrypt(languajes).encryptData()
                self.rows.append([region,city,encryptLanguaje, round( (time.time() * 1000) - (self.initial_time *  1000) ,5)])
 
        except Exception as error:
            print("Message : ",  error)

    def createDataFrame(self):
        self.dataframe = pd.DataFrame(self.rows, columns=["Region", "Country", "Language", "Time"])

    def insertCountries(self):

        for row in self.rows:
            self.country_db.insertTable(row)
            
    def createTable(self):
        self.country_db.createTable()

    def getTimes(self):

        print(f"Tiempo total: { self.dataframe['Time'].sum()} s")
        print(f"Tiempo promedio: {self.dataframe['Time'].mean()} s")
        print(f"Tiempo minimo: { self.dataframe['Time'].min()} s")
        print(f"Tiempo maximo: { self.dataframe['Time'].max()} s")

    def create_json(self):
         self.dataframe.to_json(r"./json/countries.json")