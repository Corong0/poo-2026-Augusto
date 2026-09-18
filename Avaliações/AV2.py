class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        if not isinstance(modelo, str) or not modelo.strip():
            raise ValueError("O modelo do veículo não pode estar vazio.")
        self.__modelo = modelo.strip().title()

    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        if not isinstance(placa, str) or not placa.strip():
            raise ValueError("A placa do veículo não pode estar vazia.")
        placa_formatada = placa.strip().upper()
        if len(placa_formatada) < 7:
            raise ValueError("A placa deve conter pelo menos 7 caracteres.")
        self.__placa = placa_formatada

    def get_valor_diaria(self):
        return self.__valor_diaria

    def set_valor_diaria(self, valor_diaria):
        if not isinstance(valor_diaria, (int, float)):
            raise ValueError("O valor da diária deve ser numérico.")
        if valor_diaria <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = float(valor_diaria)

    def calcular_aluguel(self, dias):
        if not isinstance(dias, int):
            raise ValueError("A quantidade de dias deve ser um número inteiro.")
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")
        return dias * self.__valor_diaria

    def __str__(self):
        return f"Modelo: {self.__modelo} | Placa: {self.__placa} | Diária: R$ {self.__valor_diaria:.2f}"


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)
        self.set_portas(portas)

    def get_portas(self):
        return self.__portas

    def set_portas(self, portas):
        if not isinstance(portas, int):
            raise ValueError("A quantidade de portas deve ser um número inteiro.")
        if portas <= 0:
            raise ValueError("A quantidade de portas deve ser maior que zero.")
        self.__portas = portas

    def calcular_aluguel(self, dias):
        valor_base = super().calcular_aluguel(dias)
        return valor_base + 50.00

    def __str__(self):
        return f"Carro: {super().__str__()} | Portas: {self.__portas}"


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)
        self.set_cilindradas(cilindradas)

    def get_cilindradas(self):
        return self.__cilindradas

    def set_cilindradas(self, cilindradas):
        if not isinstance(cilindradas, int):
            raise ValueError("As cilindradas devem ser um número inteiro.")
        if cilindradas <= 0:
            raise ValueError("As cilindradas devem ser maior que zero.")
        self.__cilindradas = cilindradas

    def calcular_aluguel(self, dias):
        valor_base = super().calcular_aluguel(dias)
        return valor_base * 0.90

    def __str__(self):
        return f"Moto: {super().__str__()} | Cilindradas: {self.__cilindradas}"


frota = []


def ler_inteiro(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor <= minimo:
                raise ValueError(f"O valor deve ser maior que {minimo}.")
            return valor
        except ValueError as erro:
            print(f"Entrada inválida: {erro}")


def ler_float(mensagem, minimo=None):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if minimo is not None and valor <= minimo:
                raise ValueError(f"O valor deve ser maior que {minimo}.")
            return valor
        except ValueError:
            print("Entrada inválida. Digite um valor numérico válido.")


def cadastrar_carro():
    try:
        modelo = input("Digite o modelo do carro: ").strip()
        placa = input("Digite a placa do carro: ").strip()
        diaria = ler_float("Digite o valor da diária do carro: ", minimo=0)
        portas = ler_inteiro("Digite a quantidade de portas: ", minimo=0)

        carro = Carro(modelo, placa, diaria, portas)
        frota.append(carro)
        print("Carro cadastrado com sucesso!")
    except ValueError as erro:
        print(f"Erro ao cadastrar carro: {erro}")
    except Exception as erro:
        print(f"Erro inesperado ao cadastrar carro: {erro}")
    finally:
        print("-" * 40)


def cadastrar_moto():
    try:
        modelo = input("Digite o modelo da moto: ").strip()
        placa = input("Digite a placa da moto: ").strip()
        diaria = ler_float("Digite o valor da diária da moto: ", minimo=0)
        cilindradas = ler_inteiro("Digite as cilindradas da moto: ", minimo=0)

        moto = Moto(modelo, placa, diaria, cilindradas)
        frota.append(moto)
        print("Moto cadastrada com sucesso!")
    except ValueError as erro:
        print(f"Erro ao cadastrar moto: {erro}")
    except Exception as erro:
        print(f"Erro inesperado ao cadastrar moto: {erro}")
    finally:
        print("-" * 40)


def listar_veiculos():
    try:
        if not frota:
            print("A frota está vazia.")
            return

        print("\nFrota cadastrada:")
        for indice, veiculo in enumerate(frota, start=1):
            print(f"{indice} - {veiculo}")
    except Exception as erro:
        print(f"Erro ao listar veículos: {erro}")
    finally:
        print("-" * 40)


def simular_aluguel():
    try:
        if not frota:
            print("Nenhum veículo cadastrado na frota.")
            return

        listar_veiculos()
        indice = ler_inteiro("Escolha o veículo para simular o aluguel (número da lista): ", minimo=0)
        if indice < 1 or indice > len(frota):
            raise IndexError("Opção de veículo inexistente.")

        veiculo = frota[indice - 1]
        dias = ler_inteiro("Informe a quantidade de dias de locação: ", minimo=0)

        valor = veiculo.calcular_aluguel(dias)
        print(f"\nValor do aluguel para {veiculo.get_modelo()}: R$ {valor:.2f}")

        # Polimorfismo em lista heterogênea: percorre a frota e calcula o valor de todos
        print("\nResumo da frota:")
        for item in frota:
            calculo = item.calcular_aluguel(dias)
            print(f"- {item.get_modelo()}: R$ {calculo:.2f}")
    except IndexError as erro:
        print(f"Erro de busca: {erro}")
    except ValueError as erro:
        print(f"Erro de valor: {erro}")
    except Exception as erro:
        print(f"Erro inesperado na simulação: {erro}")
    finally:
        print("-" * 40)


def menu():
    print("\n=== SISTEMA DE GESTÃO DE FROTA E LOCAÇÃO ===")
    print("1 - Cadastrar carro")
    print("2 - Cadastrar moto")
    print("3 - Listar veículos da frota")
    print("4 - Simular aluguel")
    print("0 - Sair")


while True:
    try:
        menu()
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_carro()
        elif opcao == 2:
            cadastrar_moto()
        elif opcao == 3:
            listar_veiculos()
        elif opcao == 4:
            simular_aluguel()
        elif opcao == 0:
            print("Sistema encerrado. Até logo!")
            break
        else:
            raise ValueError("Opção inexistente no menu.")
    except ValueError as erro:
        print(f"Erro: {erro}. Digite uma opção válida.")
        print("-" * 40)
    except Exception as erro:
        print(f"Erro inesperado no menu: {erro}")
        print("-" * 40)
    finally:
        if not (0 <= opcao <= 4 if 'opcao' in locals() else False):
            pass
