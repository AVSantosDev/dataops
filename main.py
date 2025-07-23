import pandas as pd
from pymongo import MongoClient


dfCarros = pd.DataFrame({"Carro":["Onix", "Polo", "Sandero", "Fiesta", "City"], 
                         "Cor":["Prata", "Branco", "Prata","Vermelho", "Preto"],
                         "Montadora":["Chevrolet","Volkswagen", "Renault","Ford","Honda"]})

dfMontadora = pd.DataFrame({"Montadora":["Chevrolet","Volkswagen", "Renault","Ford","Honda"],
                            "País":["EUA","Alemanha","Franca","EUA","Japão"]})


# "Verificando o DataFrame"
print(dfCarros)
print(dfMontadora)

#realizando conecção com o BD local e reverenciando cada collection do bd
con = MongoClient('mongodb://localhost:27017')
db = con.get_database("dataops")
colecaoCarros = db.get_collection('carros')
colecaoMontadoras = db.get_collection('montadoras')


#converte o dataFrame em um dicionario para que possa ser inserido no Banco de dados
inserirDadosCarros = dfCarros.to_dict(orient='records')
InserirDadosMont = dfMontadora.to_dict(orient='records')

# "-Verifica conversao dos DataFrame para orientRecord tipo dicionario"
print(inserirDadosCarros)
print(InserirDadosMont)

#realiza o insert de varios arquivos ao mesmo tempo no banco de dados utilizando o _many
colecaoCarros.insert_many(inserirDadosCarros)
colecaoMontadoras.insert_many(InserirDadosMont)

# "Verifica se foi feito o update no banco de dados"
print(colecaoCarros)
print(colecaoMontadoras)