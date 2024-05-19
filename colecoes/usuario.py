from bd import BD



def coletar_endereco() -> dict:
    print("|Endereço:")
    endereco_rua = input("|Rua: ")
    endereco_bairro = input("|Bairro: ")
    endereco_cidade = input("|Cidade: ")
    endereco_numero = input("|Número: ")
    endereco_complemento = input("|Complemento: ")

    endereco = {
        "rua": endereco_rua,
        "bairro": endereco_bairro,
        "cidade": endereco_cidade,
        "numero": endereco_numero,
        "complemento": endereco_complemento
    }
    return endereco

class Usuario:
    def create():
        nome = input("|Nome do usuário: ")

        novo_usuario = {
            "nome": nome,
            "favoritos": [],
            "compras": [],
            "endereco": coletar_endereco()
        }
        BD().usuario_collection().insert_one(novo_usuario)

    def read(filtro_usuario: dict) -> dict:
        return BD().usuario_collection().find_one(filtro_usuario)

    def read_all(filtro_usuario: dict = {}) -> list[dict]:
        return [*BD().usuario_collection().find(filtro_usuario)]

    def update(usuario: dict) -> dict:
        BD().usuario_collection().update_one(
            { "_id": usuario["_id"] },
            { "$set": usuario }, False
        )

    def delete(usuario: dict) -> dict:
        BD().usuario_collection().delete_one(usuario)
    
    def adicionar_favorito(usuario: dict, produto: dict):
        if produto in usuario["favoritos"]:
            print("|O produto já está nos favoritos")
            return
        
        usuario["favoritos"].append(produto)
        Usuario.update(usuario)
    
    def remover_favorito(usuario: dict):
        produtos = usuario["favoritos"]
        print("|Favoritos encontrados: ")
        for i in range(len(produtos)):
            print(f"{i+1} - {produtos[i]}")
        escolha = int(input("|Selecione o favorito para remover: "))
        if escolha == 0: return
        
        produto = produtos[escolha-1]
        usuario["favoritos"].remove(produto)

        Usuario.update(usuario)
    
    def adicionar_compra(usuario: dict, compra: dict):
        if compra in usuario["compras"]:
            print("|A compra já foi registrada")
            return
        
        usuario["compras"].append(compra)

        Usuario.update(usuario)