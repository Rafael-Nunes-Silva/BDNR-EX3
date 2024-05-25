from os import system
from colecoes.usuario import Usuario, coletar_endereco
from colecoes.produto import Produto
from colecoes.vendedor import Vendedor
from colecoes.compra import Compra
from redisbd import REDIS
import json



def escolher_usuario() -> dict:
    print("|Busca por usuário:")
    nome = input("|Nome do usuário: ")
    usuarios = Usuario.read_all({"nome": nome})

    print("|Usuários encontrados: ")
    for i in range(len(usuarios)):
        print(f"{i+1} - {usuarios[i]}")
    escolha = int(input("|Selecione o usuário: "))
    if escolha == 0: return
    
    return usuarios[escolha-1]

def escolher_vendedor() -> dict:
    print("|Busca por vendedor:")
    nome = input("|Nome do vendedor: ")
    vendedores = Vendedor.read_all({"nome": nome})

    print("|Vendedores encontrados: ")
    for i in range(len(vendedores)):
        print(f"{i+1} - {vendedores[i]}")
    escolha = int(input("|Selecione o vendedor: "))
    if escolha == 0: return
    
    return vendedores[escolha-1]

def escolher_produto() -> dict:
    print("|Buscar por produto:")
    nome = input("|Nome do produto: ")

    redis = REDIS()
    produtos = json.loads(redis.get("usuario:produtos"))
    produtos = [p for p in produtos if p["nome"] == nome]

    print("|Produtos encontrados: ")
    for i in range(len(produtos)):
        print(f"|{i+1} - {produtos[i]}")
    escolha = int(input("|Selecione o produto: "))
    if escolha == 0: return
    
    return produtos[escolha-1]

def escolher_compra() -> dict:
    print("|Buscar por compra:")
    data = input("|Data da compra: ")
    
    redis = REDIS()
    compras = json.loads(redis.get("usuario:produtos"))
    compras = [c for c in compras if c["data"] == data]

    print("|Compras encontradas: ")
    for i in range(len(compras)):
        print(f"|{i+1} - {compras[i]}")
    escolha = int(input("|Selecione a compra: "))
    if escolha == 0: return
    
    return compras[escolha-1]

def crud_usuario():
    EXECUTANDO = True
    while EXECUTANDO:
        print("|CRUD Usuário           |")
        print("|1 - Cadastro           |")
        print("|2 - Buscar usuário     |")
        print("|3 - Listar usuários    |")
        print("|4 - Atualizar usuário  |")
        print("|5 - Deletar usuário    |")
        print("|6 - Adicionar favorito |")
        print("|7 - Remover favorito   |")
        print("|8 - Adicionar compra   |")
        print("|0 - Voltar             |")

        entrada = int(input("|Escolha: "))
        if entrada == 1:# Cadastro
            Usuario.create()
        elif entrada == 2:# Buscar usuário
            nome = input("|Nome do usuário: ")
            usuarios = Usuario.read_all({"nome": nome})

            print("|Usuários encontrados: ")
            for i in range(len(usuarios)):
                print(f"{usuarios[i]}\n")
        elif entrada == 3:# Listar usuários
            print("|Usuários encontrados: ")
            for usuario in Usuario.read_all():
                print(f"{usuario}\n")
        elif entrada == 4:# Atualizar usuários
            usuario = escolher_usuario()
            if input("|Editar nome? (Sim/Não): ").upper() == "SIM":
                usuario["nome"] = input("|Nome do usuário: ")
            if input("|Editar endereço? (Sim/Não): ").upper() == "SIM":
                usuario["endereco"] = coletar_endereco()
            Usuario.update(usuario)
        elif entrada == 5:# Deletar usuários
            Usuario.delete(escolher_usuario())
        elif entrada == 6:# Adicionar favorito
            produto = escolher_produto()
            del produto["vendedor"]
            Usuario.adicionar_favorito(
                escolher_usuario(),
                produto
            )
        elif entrada == 7:# Remover favorito
            Usuario.remover_favorito(escolher_usuario())
        elif entrada == 8:# Adicionar compra
            Usuario.adicionar_compra(
                escolher_usuario(),
                escolher_compra()
            )
        else:
            system("cls")
            EXECUTANDO = False
        if not is_logged(): login()

def crud_vendedor():
    EXECUTANDO = True
    while EXECUTANDO:
        print("|CRUD Vendedor          |")
        print("|1 - Cadastro           |")
        print("|2 - Buscar vendedor    |")
        print("|3 - Listar vendedores  |")
        print("|4 - Atualizar vendedor |")
        print("|5 - Deletar vendedor   |")
        print("|6 - Adicionar produto  |")
        print("|7 - Remover produto    |")
        print("|0 - Voltar             |")

        entrada = int(input("|Escolha: "))
        if entrada == 1:# Cadastro
            Vendedor.create()
        elif entrada == 2:# Buscar vendedor
            nome = input("|Nome do vendedor: ")
            vendedores = Vendedor.read_all({"nome": nome})

            print("|Vendedores encontrados: ")
            for i in range(len(vendedores)):
                print(f"{vendedores[i]}\n")
        elif entrada == 3:# Listar vendedores
            print("|Vendedores encontrados: ")
            for vendedor in Vendedor.read_all():
                print(f"{vendedor}\n")
        elif entrada == 4:# Atualizar vendedor
            vendedor = escolher_vendedor()
            if input("|Editar nome? (Sim/Não): ").upper() == "SIM":
                vendedor["nome"] = input("|Nome do vendedor: ")
            if input("|Editar CNPJ? (Sim/Não): ").upper() == "SIM":
                vendedor["cnpj"] = input("|CNPJ do vendedor: ")
            Vendedor.update(vendedor)
        elif entrada == 5:# Deletar vendedor
            Vendedor.delete(escolher_vendedor())
        elif entrada == 6:# adicionar produto
            produto = escolher_produto()
            del produto["vendedor"]
            Vendedor.adicionar_produto(
                escolher_vendedor(),
                produto
            )
        elif entrada == 7:# remover produto
            Vendedor.remover_produto(escolher_vendedor())
        else:
            system("cls")
            EXECUTANDO = False
        if not is_logged(): login()

def crud_produto():
    EXECUTANDO = True
    while EXECUTANDO:
        print("|CRUD Produto          |")
        print("|1 - Cadastro          |")
        print("|2 - Buscar produto    |")
        print("|3 - Listar produtos   |")
        print("|4 - Atualizar produto |")
        print("|5 - Deletar produto   |")
        print("|0 - Voltar            |")

        entrada = int(input("|Escolha: "))
        if entrada == 1:# Cadastro
            Produto.create()
        elif entrada == 2:# Buscar produto
            nome = input("|Nome do produto: ")
            produtos = Produto.read_all({"nome": nome})

            print("|Produtos encontrados: ")
            for i in range(len(produtos)):
                print(f"{produtos[i]}\n")
        elif entrada == 3:# Listar produto
            print("|Produtos encontrados: ")
            redis = REDIS()
            for produto in json.loads(redis.get("usuario:produtos")):
                print(f"{produto}\n")
        elif entrada == 4:# Atualizar produto
            produto = escolher_produto()
            if input("|Editar nome? (Sim/Não): ").upper() == "SIM":
                produto["nome"] = input("|Nome do produto: ")
            if input("|Editar descrição? (Sim/Não): ").upper() == "SIM":
                produto["descricao"] = input("|Descrição do produto: ")
            if input("|Editar valor? (Sim/Não): ").upper() == "SIM":
                produto["valor"] = input("|Valor do produto: ")
            if input("|Editar vendedor? (Sim/Não): ").upper() == "SIM":
                vendedor = escolher_vendedor()
                del vendedor["produtos"]
                produto["vendedor"] = vendedor
            
            redis = REDIS()
            produtos = json.loads(redis.get("usuario:produtos"))
            for i in range(len(produtos)):
                if produtos[i]["_id"] == produto["_id"]:
                    produtos[i] = produto
                    break
            redis.set("usuario:produtos", json.dumps(produtos))
        elif entrada == 5:# Deletar produto
            Produto.delete(escolher_produto())
        else:
            system("cls")
            EXECUTANDO = False
        if not is_logged(): login()

def crud_compra():
    EXECUTANDO = True
    while EXECUTANDO:
        print("|CRUD Compra        |")
        print("|1 - Cadastro       |")
        print("|2 - Buscar compra  |")
        print("|3 - Listar compras |")
        print("|0 - Voltar         |")

        entrada = int(input("|Escolha: "))
        if entrada == 1:# Cadastro
            print("|Usuário da compra: ")
            usuario = escolher_usuario()
            del usuario["endereco"]
            del usuario["favoritos"]
            del usuario["compras"]

            produtos = []
            print("Produtos da compra: ")
            while True:
                produtos.append(escolher_produto())
                print("|1 - Adicionar produto|")
                print("|0 - Finalizar        |")
                if int(input("Escolha: ")) != 1:
                    break
            
            Compra.create(
                usuario,
                produtos
            )
        elif entrada == 2:# Buscar compra
            data = input("|Data da compra: ")
            compras = Compra.read_all({"data": data})

            print("|Compras encontradas: ")
            for i in range(len(compras)):
                print(f"{compras[i]}\n")
        elif entrada == 3:# Listar compras
            print("|Compras encontradas: ")
            redis = REDIS()
            for compra in json.loads(redis.get("usuario:compras")):
                print(f"{compra}\n")
            # for compra in Compra.read_all():
            #     print(compra)
        else:
            system("cls")
            EXECUTANDO = False
        if not is_logged(): login()
    sync_compras()

def is_logged() -> bool:
    redis = REDIS()
    return True if redis.get("logintoken") is not None else False

def login():
    print("|Insira o nome de úsuario e senha")
    usuario = input("|Nome de úsuario: ")
    senha = input("|Senha de úsuario: ")
    redis = REDIS()
    redis.set("logintoken", f"{usuario}:{senha}")
    redis.expire("logintoken", 30)

def sync_up_produtos():
    print("|Sincronizando cache de produtos...")
    redis = REDIS()
    for produto in Produto.read_all():
        Produto.update(produto)
    redis.delete("usuario:produtos")

def sync_down_produtos():
    print("|Baixando cache de produtos...")
    redis = REDIS()
    cache = []
    for produto in Produto.read_all():
        cache.append({
            "_id": str(produto["_id"]),
            "nome": produto["nome"],
            "descricao": produto["descricao"],
            "valor": produto["valor"]
        })
    redis.set("usuario:produtos", json.dumps(cache))

def sync_compras():
    print("|Sincronizando cache de compras...")
    redis = REDIS()
    cache = []
    for compra in Compra.read_all():
        cache.append({
            "_id": str(compra["_id"]),
            "valor": compra["valor"],
            "data": compra["data"],
            "produtos": [{
                "nome": produto["nome"],
                "descricao": produto["descricao"],
                "valor": produto["valor"],
                "vendedor": { "nome": produto["vendedor"]["nome"] }
            } for produto in compra["produtos"]],
            "usuario": { "nome": compra["usuario"]["nome"] }
        })
    redis.set("usuario:compras", json.dumps(cache))

def main():
    sync_down_produtos()
    sync_compras()
    login()

    EXECUTANDO = True
    while EXECUTANDO:
        print("|Menu Principal    |")
        print("|1 - CRUD Usuário  |")
        print("|2 - CRUD Vendedor |")
        print("|3 - CRUD Produto  |")
        print("|4 - CRUD Compra   |")
        print("|0 - Sair          |")

        entrada = int(input("|Opção: "))
        if entrada == 1:
            crud_usuario()
        elif entrada == 2:
            crud_vendedor()
        elif entrada == 3:
            crud_produto()
        elif entrada == 4:
            crud_compra()
        else: EXECUTANDO = False
    sync_up_produtos()
    print("|Saindo...")
main()