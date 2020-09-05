import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


os.system('taskkill /f /im geckodriver.exe')
endereco = 'https://www.facebook.com/'

#inicia a instancia do google chrome e acessa o facebook
driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
driver.maximize_window()
driver.get('https://www.facebook.com/')

#insere o email e senha e acessa
email = WebDriverWait(driver, 5000).until(ec.presence_of_element_located((By.ID, 'email')))
email.send_keys('') #adicione seu email do facebook

senha = WebDriverWait(driver, 5000).until(ec.presence_of_element_located((By.ID, 'pass')))
senha.send_keys('')#adicione sua senha do facebook

login = WebDriverWait(driver, 5000).until(ec.presence_of_element_located((By.NAME, 'login')))
login.send_keys(Keys.ENTER)

#acessa a area de perfil do usuario
perfil = WebDriverWait(driver, 5000).until(ec.presence_of_element_located((By.LINK_TEXT, ''))) #insira seu nome de usuario do facebook
perfil.click()

#aguarda ate que a pagina de perfil esteja toda carregada no DOM do navegador
while driver.current_url == endereco:
    window0 = driver.window_handles[0]
    driver.switch_to.window(window0)
else:
    print(driver.current_url)

#acessa a area de editar perfil
editar = WebDriverWait(driver, 5000).until(ec.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div[1]')))
editar.click()

sleep(15)
#acessa a area de editar apresentacao
editar2 = WebDriverWait(driver, 5000).until(ec.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div[6]/div/div[1]/div/div/div/div/div/h2/span/div/div[2]/div/div[2]/div/div/span')))
editar2.click()


sleep(10)
window0 = driver.window_handles[0]
driver.switch_to.window(window0)

#checa o status de relacionamento

# proposta do teste:
# O usuario tem um relacionamento cadastrado no facebook
# O usuario quer desabilitar o estado de relacionamento
# Caso desabilite com sucesso o teste retorna PASS
# Caso contrario retorna FAIL
status = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div/ul/li[5]/ul/li/div[1]/div/input')
if status.is_selected():
    print('Estado de relacionamento habilitado')
    print('Desabilitando estado de relacionamento')
    sleep(2)
    driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div/ul/li[5]/ul/li/div[1]/div/input').click()
    sleep(5)
    print('Estado de relacionamento desabilitado')
    driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div[2]/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div/div[2]/div/div[2]/div').click()
    print('Salvando informacoes')
    print('Test Result: PASS')
else:
    print('Estado de relacionamento ja esta desabilitado')
    print('Test Result: FAIL')

sleep(5)
driver.quit()

