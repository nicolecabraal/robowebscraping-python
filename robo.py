from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import time 

print ('Iniciando o nosso robô...\n')

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging") 
options.add_argument("--log-level=3")

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = s, options=options)
driver.get("https://registro.br/")

dominios = ["roboscompython.com.br", "hotmart.com.br", "uol.com.br","pyhtoncurso.com.br"]

for dominios in dominios:
    pesquisa = driver.find_element(By.ID, "is-avail-field")
    pesquisa.clear()
    dominio = "roboscompython.com.br"
    pesquisa.send_keys(dominios)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong')
print("Donínio %s %s" % (dominio, driver.find_element(By.XPATH, '//*[@id="conteudo"]/div/section/div[2]/div/p/span/strong').text))

time.sleep(8)
driver.close()