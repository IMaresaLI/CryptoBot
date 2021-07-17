import requests,datetime
from DatabaseManager import *
def coinDataInsert():
    coinDataset = requests.get("https://api.binance.com/api/v3/ticker/24hr")
    sql = sqliteData()

    for coinData in coinDataset.json():
        now = datetime.datetime.now()
        lastTime = f"{now.day}.{now.month}.{now.year}//{now.hour}:{now.minute}:{now.second}"

        if coinData["symbol"].find("BTCUSDT") != -1:
            sql.dataInsert(coinData["lastPrice"],coinData["volume"],coinData["priceChange"],coinData["lowPrice"],
                coinData["highPrice"],lastTime,"BTCUSDT")

        if coinData["symbol"].find("DOGEUSDT") != -1:
            sql.dataInsert(coinData["lastPrice"],coinData["volume"],coinData["priceChange"],coinData["lowPrice"],
                coinData["highPrice"],lastTime,"DOGEUSDT")

        if coinData["symbol"].find("SHIBUSDT") != -1:
            sql.dataInsert(coinData["lastPrice"],coinData["volume"],coinData["priceChange"],coinData["lowPrice"],
                coinData["highPrice"],lastTime,"SHIBUSDT")

        if coinData["symbol"].find("BNBUSDT") != -1:
            sql.dataInsert(coinData["lastPrice"],coinData["volume"],coinData["priceChange"],coinData["lowPrice"],
                coinData["highPrice"],lastTime,"BNBUSDT")

        if coinData["symbol"].find("BTTUSDT") != -1:
            sql.dataInsert(coinData["lastPrice"],coinData["volume"],coinData["priceChange"],coinData["lowPrice"],
                coinData["highPrice"],lastTime,"BTTUSDT")

        if coinData["symbol"].find("ETHUSDT") != -1:
            sql.dataInsert(coinData["lastPrice"],coinData["volume"],coinData["priceChange"],coinData["lowPrice"],
                coinData["highPrice"],lastTime,"ETHUSDT")

        if coinData["symbol"].find("LTCUSDT") != -1:
            sql.dataInsert(coinData["lastPrice"],coinData["volume"],coinData["priceChange"],coinData["lowPrice"],
                coinData["highPrice"],lastTime,"LTCUSDT")
        
    sql.connect.close()

def coinGetAll(tableName):
    sql = sqliteData()
    dataSet = sql.getData(tableName)
    return dataSet