from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



class BD:
    def __init__(self):
        uri = "mongodb+srv://rafaelsilva690:AUWsjuMuR6keAeOW@ex1-mercado-livre.oheq8td.mongodb.net/?retryWrites=true&w=majority&appName=EX1-Mercado-Livre"
        
        client = MongoClient(uri, server_api=ServerApi('1'))
        try:
            client.admin.command('ping')
            # print("Conectado com sucesso.")
        except:
            print("A conexão falhou.")
            return

        self.bd = client["BDNR-ML-EX1"]
    
    def usuario_collection(self):
        return self.bd["Usuario"]
    
    def produto_collection(self):
        return self.bd["Produto"]
    
    def vendedor_collection(self):
        return self.bd["Vendedor"]
    
    def compra_collection(self):
        return self.bd["Compra"]