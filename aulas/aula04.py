class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_bonus(self):
        return self.salario_base * 0.05

class Gerente(Funcionario):
    def calcular_bonus(self):
        bonus_padrao = super().calcular_bonus()
        return bonus_padrao + 1000

class Vendedor(Funcionario):
    def __init__(self, nome, salario_base, total_vendas):
        super().__init__(nome, salario_base)
        self.total_vendas = total_vendas
    def calcular_bonus(self):
        return self.total_vendas * 0.10