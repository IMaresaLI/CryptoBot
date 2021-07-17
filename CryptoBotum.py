import logging
from telegram.botcommand import BotCommand
from telegram.ext import Updater, CommandHandler
from tzlocal import get_localzone
from datetime import datetime
import schedule, time, threading
import cryptoProcess

local = get_localzone()



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    timer(update,context)
    update.message.reply_text('BTC/USD - DOGE/USD - SHIB/USD - BNB/USD \nBTT/USD - ETH/USD - LTC/USD\nLast Price Application\nOperations:\n/coins >>>> BTC - DOGE - SHIB - BNB - BTT - ETH - LTC')

def help(update, context):
    update.message.reply_text('/Start >> Başlat\n/coins >> Mevcut coinlere ulaşmanızı sağlar.')

def getData(cryptoName):
    text =""
    n = 3
    for data in cryptoProcess.coinGetAll(cryptoName)[-3::]:
        text += "[%s]Current Price : %s\nPrice Change : %s\nVolume : %s\nTime : %s\n" %(n,data[1],data[3],data[2],data[-1])
        n-=1
    return text

def getBtc(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BTCUSDT\n"+getData("BTCUSDT"))

def getDoge(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="DOGEUSDT\n"+getData("DOGEUSDT"))

def getShib(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SHIBUSDT\n"+getData("SHIBUSDT"))

def getBnb(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BNBUSDT\n"+getData("BNBUSDT"))

def getBtt(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BTTUSDT\n"+getData("BTTUSDT"))

def getEth(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="ETHUSDT\n"+getData("ETHUSDT"))

def getLtc(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="LTCUSDT\n"+getData("LTCUSDT"))

def insertData():
    cryptoProcess.coinDataInsert()

def coins(update, context):
    text = "Coins in the system : \n/BTC \n/DOGE \n/SHIB \n/BNB \n/BTT \n/ETH \n/LTC"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def run_continuously(interval=0):
    cease_continuous_run = threading.Event()
    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)
                
    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def twoHour(update, context):
    text = ""
    coins = ["BTCUSDT","DOGEUSDT","SHIBUSDT","BNBUSDT","BTTUSDT","ETHUSDT","LTCUSDT"]
    for coin in coins:
        data = cryptoProcess.coinGetAll(coin)[-1]
        text+= "%s = Current Price : %s - Price Change : %s\n" %(coin,data[1],data[3])

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def timer(update, context):
    schedule.every(0.10).hours.do(twoHour,update=update, context=context)
    stop_run_continuously = run_continuously()

def timer2():
    schedule.every(0.05).hours.do(insertData)
    stop_run_continuously = run_continuously()

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    insertData()
    TOKEN = "1725617796:AAEa2tON0E4gsU8JesJahQljpehbeVbn4Rs"
    updater = Updater(TOKEN, use_context=True) 
    dp = updater.dispatcher
    timer2()
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("Coins",coins))
    dp.add_handler(CommandHandler("BTC",getBtc))
    dp.add_handler(CommandHandler("DOGE",getDoge))
    dp.add_handler(CommandHandler("SHIB",getShib))
    dp.add_handler(CommandHandler("BNB",getBnb))
    dp.add_handler(CommandHandler("BTT",getBtt))
    dp.add_handler(CommandHandler("ETH",getEth))
    dp.add_handler(CommandHandler("LTC",getLtc))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()
    

if __name__ == '__main__':
    main()
