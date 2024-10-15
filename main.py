#Passo 1: entrar no sistema do projeto
import pandas as pd
import pyautogui as gui
import time 

gui.PAUSE = 1
gui.press("win")
gui.write("google chrome")
gui.press("enter")
gui.click(x=1160, y=203)
gui.click(x=428, y=65)
gui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
gui.press("enter")
time.sleep(2)

#Passo 2: Fazer o login
gui.moveTo(x=614, y=429)
gui.click(x=614, y=429)
gui.write('jeanhand06@gmail.com')
gui.press("tab")
gui.write("Senha")
gui.press('tab')
gui.press('enter')

#Passo 3: Importar a base de dados
tabela = pd.read_csv('produtos.csv')
print(tabela)

#Passo 4: Cadastrar um produto
for linha in tabela.index:
    gui.click(x=491, y=302)
    #codigo
    gui.write(str(tabela.loc[linha, "codigo"]))
    gui.press('tab')
    #marca
    gui.write(str(tabela.loc[linha, "marca"]))
    gui.press('tab')
    #tipo
    gui.write(str(tabela.loc[linha, "tipo"]))
    gui.press('tab')
    #categoria
    gui.write(str(tabela.loc[linha, "categoria"]))
    gui.press('tab')
    #preço unitário
    gui.write(str(tabela.loc[linha, "preco_unitario"]))
    gui.press('tab')
    #custo
    gui.write(str(tabela.loc[linha, "custo"]))
    gui.press('tab')
    #observação
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        gui.write(str(tabela.loc[linha, "obs"]))
    gui.press('tab')
    gui.press('enter')

    time.sleep(1)
    gui.scroll(1000)    