class Produto:
    """Classe base para representar um produto de uma loja de eletrônicos."""

    def __init__(self, nome, preco):
        self.set_nome(nome)
        self.set_preco(preco)

    # Getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    # Setters com validação
    def set_nome(self, nome):
        if isinstance(nome, str) and len(nome.strip()) >= 3:
            self.__nome = nome.strip()
        else:
            print("Nome inválido! O nome deve ter pelo menos 3 caracteres.")
            self.__nome = "Produto"

    def set_preco(self, preco):
        if isinstance(preco, (int, float)) and preco > 0:
            self.__preco = float(preco)
        else:
            print("Preço inválido! O preço deve ser maior que zero.")
            self.__preco = 0.0


# ============================================================================== 
# TESTE DE VALIDAÇÃO DO PROJETO FINAL
# ==============================================================================
if __name__ == "__main__":
    print("=== TESTANDO A CLASSE BASE DO PROJETO FINAL ===")

    # 1. Teste de Instanciação com dados VÁLIDOS
    objeto_valido = Produto("Cadeira Gamer", 850.00)
    print(f"Objeto Criado: {objeto_valido.get_nome()} - R$ {objeto_valido.get_preco():.2f}")

    # 2. Teste de Instanciação com dados INVÁLIDOS (Provando a validação no construtor)
    print("\n--- Teste 1: Tentativa de criar com preço negativo ---")
    objeto_invalido = Produto("Mesa", -150.00)
    print(f"Resultado mantido com segurança: R$ {objeto_invalido.get_preco():.2f}")

    # 3. Teste de alteração via Setter com dado INVÁLIDO
    print("\n--- Teste 2: Tentativa de alterar o nome para um texto muito curto ---")
    objeto_valido.set_nome("AB")
    print(f"Nome do objeto protegido: {objeto_valido.get_nome()}")
