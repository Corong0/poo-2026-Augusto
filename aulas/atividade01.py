from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, modelo: str):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print(f"O carro {self.modelo} acelerou de 0 a 100 km/h em 8 segundos!")


class Moto(Veiculo):
    def acelerar(self):
        print(f"A moto {self.modelo} empinou e acelerou rapidamente!")


class Caminhao(Veiculo):
    def acelerar(self):
        print(f"O caminhão {self.modelo} acelerou lentamente com som pesado!")


# Veículos participantes da corrida
pista_de_corrida = [
    Carro("Toyota Corolla"),
    Carro("Chevrolet Camaro"),
    Moto("Honda CB 500"),
    Moto("Yamaha MT-07"),
    Caminhao("Volvo FH"),
    Caminhao("Scania R450")
]


# Largada da simulação
print("===================================")
print("       SIMULAÇÃO DE CORRIDA")
print("===================================")
print("Preparar...")
print("3...")
print("2...")
print("1...")
print("VALENDO!")
print("===================================")

# Execução polimórfica
for veiculo in pista_de_corrida:
    veiculo.acelerar()

print("===================================")
print("       FIM DA SIMULAÇÃO")
print("===================================")
