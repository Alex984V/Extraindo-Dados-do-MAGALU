from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# abrir o navegador
navegador = webdriver.Chrome()
navegador.get("https://www.magazineluiza.com.br/")

# localizar o campo de busca e pesquisar "geladeira"
navegador.find_element(By.ID, "suggestion-input").send_keys("geladeira")
navegador.find_element(By.ID, "suggestion-input").send_keys(Keys.RETURN)

# esperar um pouco para os resultados carregarem
time.sleep(5)

# pegar todos os nomes, preços e urls dos produtos
nomes = navegador.find_elements(By.CSS_SELECTOR, "h2[data-testid='product-title']")
precos = navegador.find_elements(By.CSS_SELECTOR, "p[data-testid='price-value']")
urls = navegador.find_elements(By.CSS_SELECTOR, "a[data-testid='product-card-container']")

# mostrar nome + preço + url (pegando pelo índice)
for i in range(min(len(nomes), len(precos), len(urls))):
    print(nomes[i].text, "-", precos[i].text, "-", urls[i].get_attribute("href"))

# criar lista de dados para o DataFrame
listaDataFrame = []
for i in range(min(len(nomes), len(precos), len(urls))):
    dadosLinha = {
        "Nome": nomes[i].text,
        "Preço": precos[i].text,
        "URL": str(urls[i].get_attribute("href"))  # transforma em string
    }
    listaDataFrame.append(dadosLinha)

print("Dados extraídos com sucesso!")

# criar DataFrame
dataFrame = pd.DataFrame(listaDataFrame)

# salvar no Excel
dataFrame.to_excel("dadosMagalu.xlsx", sheet_name="Dados", index=False)
print("Arquivo Excel 'dadosMagalu.xlsx' salvo com sucesso!")
print("Dados extraidos com sucesso!")



# esperar antes de fechar o navegador
time.sleep(5)
navegador.quit()






