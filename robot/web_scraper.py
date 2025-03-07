import logging
import os
import time
import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def guardar_datos_incrementales(data, excel_file="datos_extraidos.xlsx", json_file="datos_extraidos.json"):
    # Guardar en Excel
    df = pd.DataFrame([data])  # Crear un DataFrame con solo un registro
    if not os.path.exists(excel_file):
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Datos')
        logging.info(f"Archivo de Excel creado con la primera placa.")
    else:
        with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
            startrow = writer.sheets['Datos'].max_row if writer.sheets['Datos'].max_row else 0
            df.to_excel(writer, index=False, sheet_name='Datos', startrow=startrow)
        logging.info(f"Datos de la placa añadidos al archivo de Excel existente.")

    # Guardar en JSON
    try:
        with open(json_file, "a") as json_file:
            json.dump(data, json_file, indent=4)
            json_file.write("\n")
        logging.info(f"Datos de la placa guardados en formato JSON.")
    except Exception as e:
        logging.error(f"Error al guardar en formato JSON: {e}")

def scrape_data(username, password, login_url, data_url, plates):
    logging.info("Inicio del proceso de extracción de datos para múltiples placas.")
    driver = webdriver.Chrome()
    driver.get(login_url)

    try:

        email_field = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, 'email'))
        )
        email_field.send_keys(username)

        password_field = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.NAME, 'password'))
        )
        password_field.send_keys(password)

        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        login_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'placa'))
        )

        driver.get(data_url)

        all_data = []
        placas_sin_datos = []
        total_placas = len(plates)
        consultas_completadas = 0

        for plate in plates:
            logging.info(f"Procesando placa {consultas_completadas + 1} de {total_placas}: {plate}")

            plate_input = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'placa'))
            )
            plate_input.clear()
            plate_input.send_keys(plate)

            consult_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.boton_form'))
            )
            consult_button.click()

            time.sleep(5)

            try:
                WebDriverWait(driver, 10).until(
                    EC.any_of(
                        EC.presence_of_element_located((By.CLASS_NAME, 'doc_list')),
                        EC.presence_of_element_located((By.CLASS_NAME, 'custom-modal-content'))
                    )
                )

                try:
                    error_modal = driver.find_element(By.CLASS_NAME, 'custom-modal-content')
                    close_button = error_modal.find_element(By.CLASS_NAME, 'close-button')
                    close_button.click()
                    logging.warning(f"Modal de error cerrado para la placa: {plate}")
                    placas_sin_datos.append(plate)
                    continue
                except:
                    pass

                ver_mas_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[text()='Ver Más']"))
                )
                ver_mas_button.click()

                modal = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'modal-content'))
                )

                data = {'Placa': plate}
                fields = {
                    'Línea': 'Línea',
                    'Marca': 'Marca',
                    'Modelo': 'Modelo',
                    'Estado Vehículo': 'Estado Vehículo',
                    'Nro. historico de Propietarios': 'Nro. historico de Propietarios',
                    'Tiene Embargo': 'Tiene Embargo',
                    'Es Robado': 'Es Robado',
                    'Medida cautelar embargo': 'Medida cautelar embargo',
                    'Orden de Decomiso': 'Orden de Decomiso',
                    'Medida cautelar Secuestro': 'Medida cautelar Secuestro',
                    'Denuncio robo Vehículo': 'Denuncio robo Vehículo',
                    'Abstención de trámite por Hurto': 'Abstención de trámite por Hurto',
                    'Accidente con Muerto': 'Accidente con Muerto',
                    'Otros': 'Otros',
                    'Edad Actual': 'Edad Actual',
                    'Tipo Documento': 'Tipo Documento',
                    'Nro. Documento': 'Nro. Documento',
                    'Nombre': 'Nombre',
                    'Meses de Expedición': 'Meses de Expedición',
                    'Categoría': 'Categoría',
                    'Estado': 'Estado',
                    'No.Multas Actuales': 'No.Multas Actuales',
                    'No.Historico Multas': 'No.Historico Multas',
                    'Gravedad Alta': 'Gravedad Alta',
                    'Gravedad Media': 'Gravedad Media',
                }

                for field, label in fields.items():
                    try:
                        element = modal.find_element(By.XPATH, f"//li[b[contains(text(), '{field}')]]")
                        if element:
                            data[label] = element.text.split(": ")[1]
                        else:
                            element = modal.find_element(By.XPATH, f"//*[contains(@class, 'doc_list')]/li[b[contains(text(), '{field}')]]")
                            if element:
                                data[label] = element.text.split(": ")[1]
                            else:
                                data[label] = "No disponible"
                    except:
                        data[label] = "No disponible"

                try:
                    documents = modal.find_elements(By.XPATH, "//div[@id='rtm']")
                    for i, doc in enumerate(documents):
                        doc_type = doc.find_element(By.TAG_NAME, "h4").text
                        issue_date = doc.find_element(By.XPATH, ".//li[b[contains(text(), 'Fecha Expedición')]]/text()").get_attribute("textContent").strip()
                        expiration_date = doc.find_element(By.XPATH, ".//li[b[contains(text(), 'Fecha Vencimiento')]]/text()").get_attribute("textContent").strip()
                        
                        data[f'Documento {i+1} - Tipo'] = doc_type
                        data[f'Documento {i+1} - Fecha Expedición'] = issue_date
                        data[f'Documento {i+1} - Fecha Vencimiento'] = expiration_date
                except:
                    logging.warning(f"No se pudieron extraer los datos de documentos del vehículo para la placa: {plate}")

                all_data.append(data)

                guardar_datos_incrementales(data)
                
                close_modal_button = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.close'))
                )
                close_modal_button.click()

            except TimeoutException:
                logging.warning(f"No se encontraron datos para la placa: {plate}")
                placas_sin_datos.append(plate)
                continue

            clear_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Limpiar']"))
            )
            clear_button.click()

            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'placa'))
            )

            consultas_completadas += 1
            logging.info(f"Consultas completadas: {consultas_completadas} de {total_placas}")

        excel_file = "datos_extraidos.xlsx"
        df = pd.DataFrame(all_data)

        if not os.path.exists(excel_file):
            with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
                df.to_excel(writer, index=False, sheet_name='Datos')
            logging.info(f"Archivo de Excel creado con datos de múltiples placas.")
        else:
            with pd.ExcelWriter(excel_file, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, index=False, sheet_name='Datos', startrow=writer.sheets['Datos'].max_row if writer.sheets else 0)
            logging.info(f"Datos de múltiples placas añadidos al archivo de Excel existente.")

        try:
            with open("datos_extraidos.json", "a") as json_file:
                json.dump(all_data, json_file, indent=4)
                json_file.write("\n")
            logging.info(f"Datos de múltiples placas guardados en formato JSON.")
        except Exception as e:
            logging.error(f"Error al guardar en formato JSON: {e}")

        if placas_sin_datos:
            with open("placas_sin_datos.txt", "w") as f:
                for placa in placas_sin_datos:
                    f.write(f"{placa}\n")
            logging.info(f"Se guardaron {len(placas_sin_datos)} placas sin datos en 'placas_sin_datos.txt'")

    except Exception as e:
        logging.error(f"Error general: {e}")
    finally:
        driver.quit()
        logging.info("Fin del proceso de extracción de datos para múltiples placas.")
    return all_data

def leer_placas_excel(archivo):
    df = pd.read_excel(archivo)
    return df['PLACA'].tolist()

USERNAME = 'mayepes@sura.com.co'
PASSWORD = 'Devmaster01*#3589'
LOGIN_URL = 'https://vdr.suramericana.com/'
DATA_URL = 'https://vdr.suramericana.com/home'
ARCHIVO_PLACAS = 'Placas 1.xlsx'

if __name__ == '__main__':
    placas = leer_placas_excel(ARCHIVO_PLACAS)
    scrape_data(USERNAME, PASSWORD, LOGIN_URL, DATA_URL, placas)
