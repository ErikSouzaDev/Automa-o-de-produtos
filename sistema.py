import pyautogui
import time
#Passo 1: Acessar o site

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)
#Passo 2: Fazer login no site

pyautogui.click(x=936, y=358)
pyautogui.write('seulogin@gmail.com')
pyautogui.press('tab')
pyautogui.write('senha123')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

#Passo 3: Preencher o site
import pandas
tabela = pandas.read_csv('produtos.csv')
linha = 0
for linha in tabela.index:
    #Codigo 
    codigo = tabela.loc[linha,'codigo']
    pyautogui.click(x=799, y=247)
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    #Marca
    marca = tabela.loc[linha,'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    #Tipo
    tipo = tabela.loc[linha,'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    #Categoria
    categoria = tabela.loc[linha,'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    #Preco unitario
    preco = tabela.loc[linha,'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')
    #Custo
    custo = tabela.loc[linha,'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    #Observação
    obs = tabela.loc[linha,'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('tab')

    #Botão enviar
    pyautogui.press('enter')
    pyautogui.scroll(5000)

#Sistema de automação
#Feito por: Erik Souza

