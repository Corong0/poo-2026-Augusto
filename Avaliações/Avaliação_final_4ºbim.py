class Produto:
    """Classe que representa um produto da loja."""

    def __init__(self, nome, preco):
        self.__nome = ""
        self.__preco = 0.0
        self.set_nome(nome)
        self.set_preco(preco)

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def set_nome(self, nome):
        if not isinstance(nome, str) or len(nome.strip()) < 3:
            raise ValueError("Nome inválido! O nome deve ter pelo menos 3 caracteres.")
        self.__nome = nome.strip()

    def set_preco(self, preco):
        if not isinstance(preco, (int, float)) or preco <= 0:
            raise ValueError("Preço inválido! O preço deve ser maior que zero.")
        self.__preco = float(preco)


def cadastrar_produto():
    """Coleta os dados do produto com validação e mensagens amigáveis."""
    try:
        nome = input("Digite o nome do produto: ").strip()
        preco = float(input("Digite o preço do produto: ").replace(",", "."))
        produto = Produto(nome, preco)
        print(f"Produto cadastrado com sucesso: {produto.get_nome()} - R$ {produto.get_preco():.2f}")
        return produto
    except ValueError as erro:
        print(f"Erro ao cadastrar produto: {erro}")
        return None


def buscar_produto(produtos, nome):
    """Busca um produto pelo nome e lança erro amigável se não encontrar."""
    for indice, produto in enumerate(produtos):
        if produto.get_nome().lower() == nome.lower():
            return indice
    raise IndexError(f"Produto '{nome}' não foi encontrado.")


def calcular_media_precos(produtos):
    """Calcula a média dos preços dos produtos cadastrados."""
    if not produtos:
        raise ValueError("Nenhum produto cadastrado para calcular a média.")

    total = sum(produto.get_preco() for produto in produtos)
    try:
        return total / len(produtos)
    except ZeroDivisionError:
        raise ZeroDivisionError("Não foi possível calcular a média porque a lista está vazia.")


# ============================================================================== 
# MENU PRINCIPAL COM BLINDAGEM DE ENTRADA E TRATAMENTO DE EXCEÇÕES
# =============================================================================
if __name__ == "__main__":
    produtos = []

    while True:
        print("\n=== LOJA ELETRÔNICA ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Calcular média dos preços")
        print("5 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números de 1 a 5.")
            continue

        try:
            if opcao == 1:
                produto = cadastrar_produto()
                if produto is not None:
                    produtos.append(produto)

            elif opcao == 2:
                if not produtos:
                    raise IndexError("Nenhum produto cadastrado no momento.")
                print("\nProdutos cadastrados:")
                for produto in produtos:
                    print(f"- {produto.get_nome()} | R$ {produto.get_preco():.2f}")

            elif opcao == 3:
                nome = input("Digite o nome do produto para buscar: ").strip()
                indice = buscar_produto(produtos, nome)
                print(f"Produto encontrado na posição {indice}: {produtos[indice].get_nome()} | R$ {produtos[indice].get_preco():.2f}")

            elif opcao == 4:
                media = calcular_media_precos(produtos)
                print(f"Média dos preços: R$ {media:.2f}")

            elif opcao == 5:
                print("Programa encerrado com segurança.")
                break

            else:
                print("Opção inválida! Escolha um número entre 1 e 5.")

        except (ValueError, ZeroDivisionError, IndexError) as erro:
            print(f"Operação não pode ser concluída: {erro}")
            print("Tente novamente com dados válidos.")

    # --------------------------------------------------------------------------
    # TESTE DE VALIDAÇÃO DO PROJETO FINAL
    # --------------------------------------------------------------------------
    print("\n=== TESTE DE VALIDAÇÃO DO PROJETO FINAL ===")
    try:
        produto_valido = Produto("Cadeira Gamer", 850.00)
        print(f"Objeto criado: {produto_valido.get_nome()} - R$ {produto_valido.get_preco():.2f}")
    except ValueError as erro:
        print(f"Erro tratado no teste: {erro}")

    try:
        Produto("Mesa", -150.00)
    except ValueError as erro:
        print(f"Preço inválido tratado com segurança: {erro}")

    try:
        produto_valido = Produto("Monitor", 450.00)
        produto_valido.set_nome("AB")
    except ValueError as erro:
        print(f"Nome inválido tratado pelo setter: {erro}")

    try:
        lista_vazia = []
        print(f"Média: R$ {calcular_media_precos(lista_vazia):.2f}")
    except (ValueError, ZeroDivisionError) as erro:
        print(f"Erro de cálculo tratado: {erro}")
