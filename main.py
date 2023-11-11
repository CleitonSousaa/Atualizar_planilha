import pandas as pd

# read the file to be modified
tabela = pd.read_excel("produtos.xlsx")

# variables
imposto_maior = 1.6 #60%
imposto_menor = 1.17 #17%
desconto_mobilia = 0.07 #-7%
reajuste_games = 0.03 #+3%


# ALL PRODUCTS WITH PRICES ABOVE 50$
tabela.loc[tabela["PREÇO"] >= 50, "IMPOSTO SOB O PRODUTO"] = imposto_maior


# ALL PRODUCTS WITH PRICES LESS THAN 50$
tabela.loc[tabela["PREÇO"] < 50, "IMPOSTO SOB O PRODUTO"] = imposto_menor


for indice, linha in tabela.iterrows():
    if linha["CATEGORIA"] == "mobilia":
        novo_valor = linha["IMPOSTO SOB O PRODUTO"] - desconto_mobilia
        tabela.at[indice, "IMPOSTO SOB O PRODUTO"] = novo_valor

    if linha["CATEGORIA"] == "games":
        novo_valor = linha["IMPOSTO SOB O PRODUTO"] + reajuste_games
        tabela.at[indice, "IMPOSTO SOB O PRODUTO"] = novo_valor


# final price update
tabela["PREÇO FINAL"] = tabela["IMPOSTO SOB O PRODUTO"] * tabela["PREÇO"] 

# formatting final price
tabela["PREÇO FINAL"] = tabela["PREÇO FINAL"].round(2)


# creation of new changed file
tabela.to_excel("produto.xlsx", index=False)