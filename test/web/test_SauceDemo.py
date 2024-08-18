import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classes e metodos (def)
class Test_TestSauceDemo():
    def setup_method(self):
        # Declarar o obj do selenium e instaciar como navegador desejado
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(50)

    def teardown_method(self):
        self.driver.quit()

    #Definição do teste
    def test_tela_login(self):
        self.driver.get('https://www.saucedemo.com')
        self.driver.find_element(By.ID,'user-name').click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="user-name"]').send_keys('standard_user')
        self.driver.find_element(By.ID,'password').click()
        self.driver.find_element(By.ID,'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID,'login-button').click()
# Transição de tela - vai abrir janela products
        # verifica se estou na pagina certa products
        assert self.driver.find_element(By.CSS_SELECTOR,'span.title').text == 'Products'\
        # add no carrinho bolsa Sauce Labs Backpack valor de 29.99
        self.driver.find_element(By.ID,'add-to-cart-sauce-labs-backpack').click()
        # clicar no carrinho
        self.driver.find_element(By.CSS_SELECTOR,'a.shopping_cart_link').click()
# Transição de tela
        #Verifica se está na pagina Your Cart
        assert self.driver.find_element(By.CSS_SELECTOR,'span.title').text == 'Your Cart'
        #Verifica o nome do item está no carrinho
        assert self.driver.find_element(By.CSS_SELECTOR,'div.inventory_item_name').text == 'Sauce Labs Backpack'
        #Verifica valor $29.99
        assert self.driver.find_element(By.CSS_SELECTOR,'div.inventory_item_price').text == '$29.99'
        #Verifica a quantidade
        assert self.driver.find_element(By.CSS_SELECTOR,'div.cart_quantity').text == '1'
        #Clicar em chechout
        self.driver.find_element(By.ID,'checkout').click()
# Transição de tela
        # Verificar se está na pagina Checkout: Your Information
        assert self.driver.find_element(By.CSS_SELECTOR,'span.title').text == 'Checkout: Your Information'
        #cliclar em fistName
        self.driver.find_element(By.ID,'first-name').click()
        #Preencher fistName
        self.driver.find_element(By.ID,'first-name').send_keys('Leandro')
        # cliclar em lastName
        self.driver.find_element(By.ID,'last-name').click()
        # Preencher lastame
        self.driver.find_element(By.ID,'last-name').send_keys('Macedo Cardinho')
        #cliclar em zip/postal
        self.driver.find_element(By.ID,'postal-code').click()
        #Preencher zip/postal
        self.driver.find_element(By.ID, 'postal-code').send_keys('999900000')
        #cliclar em continue
        self.driver.find_element(By.XPATH,'//*[@id="continue"]').click()
    def _test_finaizar_compra(self):
#Transição de tela
        #Verificar se está na tela Checkout: Overview
        assert self.driver.find_element(By.CSS_SELECTOR,'span.title').text == 'Checkout: Overview'
        #Verifica o nome do produto
        assert self.driver.find_element(By.CSS_SELECTOR, 'div.inventory_item_name').text == 'Sauce Labs Backpack'
        #Verifica valor
        assert self.driver.find_element(By.CSS_SELECTOR, 'div.inventory_item_price'). text == '$29.99'
        #Verifica quantidade
        assert self.driver.find_element(By.CSS_SELECTOR,'div.cart_quantity').text == '1'
        #clicar em finish
        self.driver.find_element(By.CSS_SELECTOR,'.btn.btn_action.btn_medium.cart_button').click()