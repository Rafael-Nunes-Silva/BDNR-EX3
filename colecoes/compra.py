from bd import BD



class Compra:
    def create(usuario: dict, produtos: list[dict]):
        data = input("|Data da compra: ")

        valor = sum([float(prod["valor"]) for prod in produtos])
        print(f"|Valor atual: {valor}")
        print("|1 - Alterar valor")
        print("|0 - Manter valor")
        if int(input("Escolha: ")) == 1:
            valor = float(input("Valor: "))

        nova_compra = {
            "usuario": usuario,
            "valor": valor,
            "data": data,
            "produtos": produtos
        }

        BD().compra_collection().insert_one(nova_compra)

    def read(filtro_compra: dict) -> dict:
        return BD().compra_collection().find_one(filtro_compra)

    def read_all(filtro_compra: dict = {}) -> list[dict]:
        return [*BD().compra_collection().find(filtro_compra)]

    def update(compra: dict):
        BD().compra_collection().update_one(
            { "_id": compra["_id"] },
            { "$set": compra }, False
        )

    def delete(compra: dict):
        BD().compra_collection().delete_one(compra)