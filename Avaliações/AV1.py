class Funcionário:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        if novo_salario >= 0:
            self.__salario_base = novo_salario
        else:
            raise ValueError("Salário não pode ser negativo")

    def calcular_salario_final(self):
        return self.get_salario_base()


class Gerente(Funcionário):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        return super().calcular_salario_final() + self.bonus_gestao


class Desenvolvedor(Funcionário):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        if isinstance(self.nivel, str) and self.nivel.lower() == "senior":
            return super().calcular_salario_final() + 1500
        return super().calcular_salario_final()


if __name__ == "__main__":
    gerente = Gerente("Carlos", "G100", 8000, 2000)
    desenvolvedor = Desenvolvedor("Mariana", "D200", 6000, "Senior")

    print(f"{gerente.nome}: R$ {gerente.calcular_salario_final():.2f}")
    print(f"{desenvolvedor.nome}: R$ {desenvolvedor.calcular_salario_final():.2f}")

    gerente.__salario_base = -100
    print("Após atribuição direta de gerente.__salario_base = -100")
    print(f"{gerente.nome} get_salario_base(): R$ {gerente.get_salario_base():.2f}")
    print(f"Atributo criado ger.__salario_base (valor bruto): {getattr(gerente, '__salario_base')}")

    print(f"{gerente.nome} salário final: R$ {gerente.calcular_salario_final():.2f}")
    print(f"{desenvolvedor.nome} salário final: R$ {desenvolvedor.calcular_salario_final():.2f}")

