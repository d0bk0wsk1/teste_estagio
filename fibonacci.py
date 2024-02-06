def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence[:-1]

def verifica_pertence(numero, sequencia):
    if numero in sequencia:
        return True
    else:
        return False


numero = int(input("Digite um número inteiro para verificar se pertence à sequência de Fibonacci: "))
sequencia = fibonacci(numero)

if verifica_pertence(numero, sequencia):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

