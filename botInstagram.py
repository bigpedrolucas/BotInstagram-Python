from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

print("--- BOT ENVIO DE MENSAGEM INSTAGRAM ---")
print("Entre com sua conta do Instagram")
usuario = input("Usuário: ")
senha = input("Senha: ")

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=CM().install(), options=options)

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")

        time.sleep(1)

        #//input[@name="username"]
        #//input[@name='password']

        campoUser = driver.find_element_by_xpath("//input[@name='username']")
        campoUser.click()
        campoUser.clear()
        campoUser.send_keys(self.username)

        time.sleep(4)

        campoSenha = driver.find_element_by_xpath("//input[@name='password']")
        campoSenha.click()
        campoSenha.clear()
        campoSenha.send_keys(self.password)

        time.sleep(4)

        campoSenha.send_keys(Keys.RETURN)

        time.sleep(6)

        self.enviarMensagem()

    @staticmethod
    def digite(frase, ondeDigitar):
        for letra in frase:
            ondeDigitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def enviarMensagem(self):
        seguidores = open("./followers.txt",'r',encoding='UTF-8')
        listaSeguidores = seguidores.read()
        listaSeguidores = listaSeguidores.split('\n')

        mensagem = open("./mensagem.txt", 'r', encoding='UTF-8')
        mensagem = mensagem.read()
        driver = self.driver

        for seguidor in listaSeguidores:
            driver.get("https://www.instagram.com/" + str(seguidor))
            time.sleep(4)
            try:
                driver.find_element_by_class_name("T0kll").click()
            except:
                continue
            time.sleep(4)
            try:
                driver.find_element_by_class_name("HoLwm").click()
            except:
                print("\n")

            time.sleep(4)
            try:
                campoComent = driver.find_element_by_xpath("//textarea[@placeholder='Mensagem...']")
                campoComent.click()
                time.sleep(4)
                campoComent.send_keys(mensagem)
                time.sleep(4)
                campoComent.send_keys(Keys.ENTER)
            except:
                continue
            time.sleep(15)

igBot = InstagramBot(usuario, senha)
igBot.login()