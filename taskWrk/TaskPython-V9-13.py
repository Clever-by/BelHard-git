# Логирование logging и loguru
# Логирование — это запись куда-то данных о работе программы. Место, куда эти данные записываются называется «лог».

import logging
from datetime import datetime

dtn = datetime.strftime(datetime.now(), "%d%m%Y_%H%M%S")
#print(dtn)
    
logging.basicConfig(
    #filename="taskWrk\logs\sample_"+dtn+".log", 
    # Если имя файла тоже, то дописываем в файл
    #filename="taskWrk\logs\sample.log", 
    level=logging.ERROR
)

 
logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

#logging.DEBUG
#logging.INFO
#logging.WARN
#logging.ERROR
#ogging.FATAL

# 
# Форматоры - что и как будем писать
# Хандлеры - что с этим будем делать, записывать в файл, выводвить в консоль

from loguru import logger

a = {}
logger.info('Start programm...')

try:
    1/0

except:
    logger.exception("An error has happened!")

# Декоратор для перехватывания всех сообщений
@logger.catch()
def f():
    return 1/0

f() 


# End