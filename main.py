#from analysis.analysisQualityAir import *
#from analysis.analysisQualityNoise import *
#from analysis.analysisConsumption import *

from robot.web_scraper import scrape_data
from robot.utils import log


USERNAME = ''
PASSWORD = ''
LOGIN_URL = ''
DATA_URL = ''
PLATE = 'DDP16C'

def robot():
    log('Automatizando navegación web y extrayendo datos...')
    data = scrape_data(USERNAME, PASSWORD, LOGIN_URL, DATA_URL, PLATE)
    log(f'Datos extraídos: {data}')


if __name__ == '__main__':
    robot()    


    