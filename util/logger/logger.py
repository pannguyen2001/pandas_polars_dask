import logging
import os
from icecream import ic
from loguru import logger
from config.setup import unixTimestamp, local_time_date

if not os.path.exists('./log'):
  os.makedirs('./log')

handler = logging.FileHandler(filename= f'./log/{local_time_date}.log')

# logger.add(handler)
# can replace handle by sys.stdrr
logger.add(handler,
  format="{time:YYYY-MM-DD HH:mm:ss}|{level}|{name}|{module}:{line}| \n{message}",
  colorize= False)

ic.configureOutput(includeContext=True, prefix=unixTimestamp)
ic.lineWrapWidth= 80
logger.info('🚀 Start app')

logger.info('💯 End app')

def hello_ic():
    ic('🚀 End app')
hello_ic()

'''
# ========== Rich logger ==========
from rich.traceback import install
install(show_locals=True)
from rich.console import Console
console = Console(record=True, width= 100)
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    format="[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: \n%(message)s",
    datefmt="[%Y-%m-%d %H:%M:%S]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

ric_log = logging.getLogger("test_finance")
except Exception as e:
            console.print_exception()
            console.save_text(f"./Z_my_log/{local_time_date_time}.txt")
            
'''