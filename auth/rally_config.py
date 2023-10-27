import os
from dotenv import load_dotenv
from datetime import datetime


def load_rally_config():
    load_dotenv()
    now = datetime.now()

    config = {
        'APIKEY': os.getenv('APIKEY'),
        'WORKSPACE': os.getenv('WORKSPACE'),
        'SERVER': os.getenv('SERVER'),
        'ITERATION_SETTING': os.getenv('ITERATION_SETTING'),
        'PROJECTS': os.getenv('PROJECTS').split(','),
        'WEEK_NUMBER': now.isocalendar()[1]
    }

    return config
