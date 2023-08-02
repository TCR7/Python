# Passo a passo
# Passo 1: Entrar no sistema da "empresa"
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import pandas
#pyautogui.write -> escrever um texto.
#pyautogui.press -> apertar um tecla do teclado.
#pyautogui.click -> click do mouse.
#pyautogui.hotkey -> apertar duas teclas, e sepera por vírgula.

pyautogui.PAUSE = 0.5

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email

pyautogui.click(x=785, y=368)

# escrever seu email

pyautogui.write("xesquedele22@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhasenhasenha")
pyautogui.click(x=968, y=526)
time.sleep(3)

# Passo 3: Importar a base de produtos para cadastrar

tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
for linha in tabela.index: #index é o numero da linha da base de dados
    # pegando a linha 0 da base de dados

    # clicar no campo de código
    pyautogui.click(x=840, y=245)
    # pegar da tabela o valor do campo que a gente quer preencher

    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo)) # lembre-se de sempre usar em string pra garantia de escrever um texto

    # passar pro proximo

    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"])) 
    pyautogui.press("tab")

    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "tipo"])) 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"])) 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) 
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"])) 
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"])) 
    pyautogui.press("tab")
    pyautogui.press("enter")
    # dar scroll pro topo da pagina

    # pyautogui.scroll(5000) se necessario descer ou subir a pagina.

    # Passo 5: Repetir o processo até o fim!


    # Lembre-se sempre de fazer o passo a passo para saber o que fazer! Isso ajuda!