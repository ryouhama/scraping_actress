import os
from dotenv import find_dotenv
from dotenv import load_dotenv


load_dotenv(find_dotenv())
# CSV
CSV_DIR = os.getcwd()
CSV_FILE_NAME = os.environ.get('CSV_FILE_NAME')
CSV_FILE_PATH = CSV_DIR + '/' + CSV_FILE_NAME

# Log Setting
LOG_FORMAT = os.environ.get('LOG_FORMAT')
