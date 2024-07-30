#from analysis.analysisQualityAir import *
#from analysis.analysisQualityNoise import *
#from analysis.analysisConsumption import *

from robot.web_scraper import scrape_data
from robot.utils import log


USERNAME = 'mayepes@sura.com.co'
PASSWORD = 'Devmaster01*#3589'
LOGIN_URL = 'https://test-vdr.suramericana.com/'
DATA_URL = 'https://test-vdr.suramericana.com/home'
PLATE = 'DDP16C'

def robot():
    log('Automatizando navegación web y extrayendo datos...')
    data = scrape_data(USERNAME, PASSWORD, LOGIN_URL, DATA_URL, PLATE)
    log(f'Datos extraídos: {data}')


if __name__ == '__main__':
    robot()    