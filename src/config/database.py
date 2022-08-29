import sqlite3

class CountriesDb() :

    def __init__(self,table):
        self.table = table
        try:
            self.con = sqlite3.connect("./database/db_contry.db")
            self.cursor = self.con.cursor() 
            
        except Exception as error:
            print("Message Error :  ",error)
        
    def showTable(self):
        try:
            self.open()
            self.cursor.execute(f"SELECT * FROM {self.table}")
            rows = self.cursor.fetchall()
            return rows        
        except Exception as error:
            print ("Message :", error)
        finally:
            self.closeConnection()


    def closeConnection(self):
        self.con.close()

    def cleanTable(self):
        try :
            self.cursor.execute(f"DELETE FROM {self.table}")
            self.con.commit()
        except Exception as error:
            print(error)


    def createTable(self):
        try :
            self.cleanTable()
            self.cursor.execute(f""" CREATE TABLE IF NOT EXISTS {self.table}  (
                                      codigo integer primary key autoincrement,
                                      Región text,
                                      City Name text,
                                      Language text,
                                      Time real
                                )""")
            self.con.commit()
        except Exception as error:
            print("Message Error :  ",error)
        finally:
            self.closeConnection()

    def insertTable(self,list):
        try :

            self.open()
            self.cursor.execute(f"INSERT INTO {self.table} (Región,City,Language,Time) VALUES (?, ?, ? ,?)",list)
            self.con.commit()
        except Exception as error:
            print("Message Error :  ",error)
        finally:
            self.closeConnection()

    def open(self):
        try:
            self.con = sqlite3.connect("./database/db_contry.db")
            self.cursor = self.con.cursor() 
            
        except Exception as error:
            print("Message Error :  ",error)

