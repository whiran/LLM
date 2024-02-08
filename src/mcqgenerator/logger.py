import logger,logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE_NAME)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE_NAME)
# logger = logging.basicConfig(level="INFO",filename=LOG_FILE_PATH,format="{time} {level} {message}")
logging.basicConfig(level=logging.INFO,filename=LOG_FILE_PATH,format="{time} {level} {message}")

# logging.basicConfig(level="INFO",filename=LOG_FILE_NAME,format="{time} {level} {message}")
# logging.basicConfig(level= logging.INFO,filename=LOG_FILE_NAME,format="{time} {level} {message}")