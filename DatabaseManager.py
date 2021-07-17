import sqlite3


class sqliteData():
    def __init__(self):
        self.connect = sqlite3.connect("cryptoSQL.db",check_same_thread=False)
        self.cursor = self.connect.cursor()

   
    def dataInsert(self,currentPrice,volume,priceChange,lowPrice,highPrice,DataTime,coinSymbol):
        self.cursor.execute(f"INSERT INTO {coinSymbol} (currentPrice,volume,priceChange,lowPrice,highPrice,DataTime) VALUES (?,?,?,?,?,?)",
                       (currentPrice, volume,priceChange,lowPrice, highPrice,DataTime))
        self.connect.commit()
        print("İşlem Tamamlandı.")

    def getData(self,tblname):
        self.cursor.execute(f"Select * from {tblname}")
        data = self.cursor.fetchall()
        self.connect.close()
        return data
