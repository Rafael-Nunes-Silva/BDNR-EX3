from bd import BD



class Vendedor:
    def create():
        nome = input("Nome do vendedor: ")
        cnpj = input("CNPJ do vendedor: ")

        novo_vendedor = {
            "nome": nome,
            "cnpj": cnpj,
            "produtos": []
        }
        
        BD().vendedor_collection().insert_one(novo_vendedor)

    def read(filtro_vendedor: dict) -> dict:
        return BD().vendedor_collection().find_one(filtro_vendedor)

    def read_all(filtro_vendedor: dict = {}) -> list[dict]:
        return [*BD().vendedor_collection().find(filtro_vendedor)]

    def update(vendedor: dict):
        BD().usuario_collection().update_one(
            { "_id": vendedor["_id"] },
            { "$set": vendedor }, False
        )

    def delete(vendedor: dict):
        BD().usuario_collection().delete_one(vendedor)
    
    def adicionar_produto(vendedor: dict, produto: dict):
        if produto in vendedor["produtos"]:
            print("|O produto já está vinculado ao vendedor")
            return
        
        vendedor["produtos"].append(produto)
        Vendedor.update(vendedor)
    
    def remover_produto(vendedor: dict):
        produtos = vendedor["produtos"]
        print("|Produtos encontrados: ")
        for i in range(len(produtos)):
            print(f"{i+1} - {produtos[i]}")
        escolha = int(input("|Selecione o produto para remover: "))
        if escolha == 0: return
        
        produto = produtos[escolha-1]

        vendedor["produtos"].remove(produto)
        Vendedor.update(vendedor)
    