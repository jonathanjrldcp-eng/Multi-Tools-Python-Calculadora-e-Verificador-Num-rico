import time
import os


def calculadora(a, b, operacao):
    operacoes = {"+": lambda: a + b,
                 "-": lambda: a - b,
                 "*": lambda: a * b,
                 "/": lambda: a / b}
    if operacao == "/" and b == 0:
        return "Erro: Não é possível dividir por zero!"
    elif operacao not in operacoes:
        return "Erro: Operação inválida!"
    return operacoes[operacao]()


def iniciar_calculadora():
    while True:
        print("-"*35)
        print(">>>------|> CALCULADORA <|------<<<")
        try:
            a = float(input("DIGITE O 1º NUMERO: "))
            b = float(input("DIGITE O 2º NUMERO: "))
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos!")
            continue
        operacao = input("DIGITE A OPERAÇÃO DESEJADA: ").strip()
        print("\nCalculando...")
        time.sleep(1)
        resultado = calculadora(a, b, operacao)
        if isinstance(resultado, (int, float)):
            print(f"\nResultado da Operação: {resultado:.2f}")
        else:
            print(f"\n{resultado}")
        continuar = input(
            "\nDeseja fazer outro cálculo? (S/N): ").strip().upper()
        if continuar != 'S':
            break


def limpar_tela():
    input("\nPressione ENTER para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')


def verificar_numero():
    limpar_tela()
    print("-" * 35)
    print(">>>---|> POSITIVO, NEGATIVO OU IGUAL A ZERO <|---<<<")
    try:
        numero = float(input("DIGITE O NÚMERO A SER VERIFICADO: "))
        time.sleep(1)
        if numero > 0:
            print("NÚMERO POSITIVO")
        elif numero < 0:
            print("NÚMERO NEGATIVO")
        else:
            print("IGUAL A ZERO")
    except ValueError:
        print("\nErro: Por favor, digite um número válido!")


def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 35)
        print("       MULTI-TOOLS PYTHON       ")
        print("=" * 35)
        print("1. Calculadora Básica")
        print("2. Verificador de Números (Sinais)")
        print("3. Sair")
        print("=" * 35)

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            iniciar_calculadora()
        elif escolha == '2':
            verificar_numero()
            limpar_tela()
        elif escolha == '3':
            print("\nFINALIZANDO O PROGRAMA!!!")
            time.sleep(1)
            break
        else:
            print("\nOpção inválida! Tente novamente.")
            time.sleep(1.5)


if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado pelo usuário.")
