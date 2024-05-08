from .vendedor import Vendedor
from bd import BD



def escolher_vendedor() -> dict:
    nome = input("|Nome do vendedor: ")
    vendedores = Vendedor.read_all({"nome": nome})

    print("|Vendedores encontrados: ")
    for i in range(len(vendedores)):
        print(f"{i+1} - {vendedores[i]}")
    escolha = int(input("|Selecione o vendedor: "))
    if escolha == 0: return
    
    return vendedores[escolha-1]

class Produto:
    def create():
        nome = input("|Nome do produto: ")
        descricao = input("|Descrição do produto: ")
        valor = float(input("|Valor do produto: "))
        
        vendedor = escolher_vendedor()
        del vendedor["produtos"]

        novo_produto = {
            "nome": nome,
            "descricao": descricao,
            "valor": valor,
            "vendedor": vendedor
        }
        
        BD().produto_collection().insert_one(novo_produto)

    def read(filtro_produto: dict) -> dict:
        return BD().produto_collection().find_one(filtro_produto)

    def read_all(filtro_produto: dict = {}) -> list[dict]:
        return [*BD().produto_collection().find(filtro_produto)]

    def update(produto: dict):
        BD().produto_collection().update_one(
            { "_id": produto["_id"] },
            { "$set": produto }, False
        )

    def delete(produto: dict):
        BD().produto_collection().delete_one(produto)