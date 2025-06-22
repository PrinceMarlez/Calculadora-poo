class CALCULATOR:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        # Inicializa a classe com dois números

    def sum(self):
        return self.num1 + self.num2
        # Soma

    def sub(self):
        return self.num1 - self.num2
        # Subtração

    def mult(self):
        return self.num1 * self.num2
        # Multiplicação

    def div(self):
        if self.num2 == 0:
            return "Erro: divisão por zero"
        return self.num1 / self.num2
        # Divisão com verificação


# Parte que interage com o usuário
print("Bem-vindo a Calculadora!")

try:
    num1 = float(input("Coloque seu primeiro número: "))
    num2 = float(input("Coloque seu segundo número: "))
    calc = int(input(
        "Coloque sua operação:\n"
        "1. Soma\n"
        "2. Subtração\n"
        "3. Multiplicação\n"
        "4. Divisão\n"
        "Sua escolha: "
    ))

    calculator = CALCULATOR(num1, num2)

    if calc == 1:
        print("Resultado:", calculator.sum())
    elif calc == 2:
        print("Resultado:", calculator.sub())
    elif calc == 3:
        print("Resultado:", calculator.mult())
    elif calc == 4:
        print("Resultado:", calculator.div())
    else:
        print("Operação inválida.")

except ValueError:
    print("Coloque número válidos.")
