import logging 
import os
from datetime import datetime


LOG_FILE= f"logs/log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
LOGS_PATH= os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(LOGS_PATH,exist_ok=True)

LOGS_FILE_PATH= os.path.join(LOGS_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,)


