from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempoEspera

navegador = opcoesSelenium.Chrome()

navegador.get('https://form.jotform.com/221436066464051')
tempoEspera.sleep(1)

navegador.find_element(By.ID,"first_3").send_keys('Vascaino')

navegador.find_element(By.ID,"last_3").send_keys('Flamenguista da Silva')

navegador.find_element(By.ID,"input_4").send_keys('queria_Chutar_aquele_cão@gmail.com')

tempoEspera.sleep(4)






