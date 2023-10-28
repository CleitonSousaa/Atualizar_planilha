import pandas as pd

# ler o arquivo a ser modificado
tabela = pd.read_excel("produtos.xlsx")

# variaveis
imposto_maior = 1.6
imposto_menor = 1.17
desconto_mobilia = 0.07
reajuste_games = 0.03


#TODOS OS PRODUTOS COM VALORES ACIMA DE 50$
tabela.loc[tabela["PREÇO"] >= 50, "IMPOSTO SOB O PRODUTO"] = imposto_maior


#TODOS OS PRODUTO COM VALORES INFERIORES A 50$
tabela.loc[tabela["PREÇO"] < 50, "IMPOSTO SOB O PRODUTO"] = imposto_menor


for indice, linha in tabela.iterrows():
    if linha["CATEGORIA"] == "mobilia":
        novo_valor = linha["IMPOSTO SOB O PRODUTO"] - desconto_mobilia
        tabela.at[indice, "IMPOSTO SOB O PRODUTO"] = novo_valor

    if linha["CATEGORIA"] == "games":
        novo_valor = linha["IMPOSTO SOB O PRODUTO"] + reajuste_games
        tabela.at[indice, "IMPOSTO SOB O PRODUTO"] = novo_valor


# atualizacao do preco final
tabela["PREÇO FINAL"] = tabela["IMPOSTO SOB O PRODUTO"] * tabela["PREÇO"] 

# formatando preco final
tabela["PREÇO FINAL"] = tabela["PREÇO FINAL"].round(2)


tabela.to_excel("produto.xlsx", index=False)# cria novo arquivo alterado