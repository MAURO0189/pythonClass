from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os
import json

def scrape_data(username, password, login_url, data_url, plates):
    print("Inicio del proceso de extracción de datos para múltiples placas.")
    driver = webdriver.Chrome()
    driver.get(login_url)

    try:
        email_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'email'))
        )
        email_field.send_keys(username)

        password_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'password'))
        )
        password_field.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'placa'))  
        )

        driver.get(data_url)

        all_data = []

        for plate in plates:
            print(f"Procesando placa: {plate}")

            plate_input = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, 'placa'))
            )
            plate_input.clear()
            plate_input.send_keys(plate)

            consult_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.boton_form'))  
            )
            consult_button.click()
            
            time.sleep(5)  

            data = {}
            fields = {
                'Placa': 'Placa',
                'Línea': 'Línea',
                'Marca': 'Marca',
                'Modelo': 'Modelo',
                'Color': 'Color',
                'Peso': 'Peso',
                'País origen': 'País origen',
                'Clase Vehículo': 'Clase Vehículo',
                'Cilindraje': 'Cilindraje',
                'Transmisión tipo': 'Transmisión tipo',
                'Tracción tipo': 'Tracción tipo',
                'Tipo de combustible': 'Tipo de combustible',
                'Capacidad de carga': 'Capacidad de carga',
                'Capacidad de pasajeros': 'Capacidad de pasajeros',
                'Estado Vehículo': 'Estado Vehículo',
                'Transito de': 'Transito de',
                'Fecha matrícula': 'Fecha matrícula',
                'Tipo servicio': 'Tipo servicio',
                'Nro. historico de Propietarios': 'Nro. historico de Propietarios',
                'Blindaje': 'Blindaje',
                'Detalle blindaje': 'Detalle blindaje',
                'Tiene prenda': 'Tiene prenda',
                'Entidad prenda': 'Entidad prenda',
                'Nro. Vin': 'Nro. Vin',
                'Nro. Motor': 'Nro. Motor',
                'Nro. Serie': 'Nro. Serie',
                'Nro. Chasis': 'Nro. Chasis',
                'Nro. Registro': 'Nro. Registro',
                'Nro. de ejes': 'Nro. de ejes',
                'Nro. de llantas': 'Nro. de llantas',
                'Nro. licencia transíto': 'Nro. licencia transíto',
                'Fecha de importación': 'Fecha de importación',
                'Nro. Manifiesto de importación': 'Nro. Manifiesto de importación',
                'Nro. regrabación Vin': 'Nro. regrabación Vin',
                'Nro. regrabación Motor': 'Nro. regrabación Motor',
                'Nro. regrabación Serie': 'Nro. regrabación Serie',
                'Nro. regrabación Chasis': 'Nro. regrabación Chasis',
                'Tiene Embargo': 'Tiene Embargo',
                'Es Robado': 'Es Robado',
                'Medida cautelar embargo': 'Medida cautelar embargo',
                'Orden de Decomiso': 'Orden de Decomiso',
                'Medida cautelar Secuestro': 'Medida cautelar Secuestro',
                'Denuncio robo Vehículo': 'Denuncio robo Vehículo',
                'Abstención de trámite por Hurto': 'Abstención de trámite por Hurto',
                'Accidente con Muerto': 'Accidente con Muerto',
                'Otros': 'Otros'
            }

            for field, label in fields.items():
                try:
                    data[label] = driver.find_element(By.XPATH, f"//li[b[contains(text(), '{field}')]]").text.split(": ")[1]
                except:
                    data[label] = "No disponible"

            all_data.append(data)

            clear_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Limpiar']"))
            )
            clear_button.click()

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'placa'))
            )

       
        excel_file = "datos_extraidos.xlsx"
        df = pd.DataFrame(all_data)

        if not os.path.exists(excel_file):
            with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Datos')
            print(f"Archivo de Excel creado con datos de múltiples placas.")
        else:
            with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, index=False, sheet_name='Datos', startrow=writer.sheets['Datos'].max_row if writer.sheets else 0)
            print(f"Datos de múltiples placas añadidos al archivo de Excel existente.")

        
        try:
            with open("datos_extraidos.json", "a") as json_file:
                json.dump(all_data, json_file, indent=4)
                json_file.write("\n")  
            print(f"Datos de múltiples placas guardados en formato JSON.")
        except Exception as e:
            print(f"Error al guardar en formato JSON: {e}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
        print("Fin del proceso de extracción de datos para múltiples placas.")
    return all_data

USERNAME = 'mayepes@sura.com.co'
PASSWORD = 'Devmaster01*#3589'
LOGIN_URL = 'https://test-vdr.suramericana.com/'
DATA_URL = 'https://test-vdr.suramericana.com/home'
PLATES = ['DDP16C','ITE22G','XKD77G','HXT148','VMV34F','LRY66G','MUB24F','CDO575','GXQ35D','ETP16D']

if __name__ == '__main__':
    scrape_data(USERNAME, PASSWORD, LOGIN_URL, DATA_URL, PLATES)