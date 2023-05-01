# 1. Explique como utilizar tratamento de exceção, demonstre através
# de um código onde vai quebrar intencionalmente.

# O tratamento de exceção é uma técnica utilizada para lidar com situações 
# imprevistas que podem ocorrer durante a execução de uma aplicação.
# Quando uma exceção é lançada, o programa interrompe a execução normal e 
# procura por um bloco de tratamento de exceção correspondente que possa 
# lidar com a exceção. Se um bloco de tratamento de exceção for encontrado, 
# ele será executado e o programa poderá continuar a executar normalmente.
# Caso contrário, o programa será encerrado e uma mensagem de erro será exibida.

try:
    number = int(input("Digite um número inteiro: "))
    result = 10 / numero
    print("O resultado é:", result)
except ValueError:
    print("Você digitou um número inteiro inválido.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
except Exception as e:
    print("Ocorreu uma exceção:", e)