import random

def exercicio_1():
    nu1 = int(input("Escreve"))
    nu2 = int(input("escreve outro número:"))
    resoltado = nu1 + nu2
    print("O resoltado é:", resoltado)

def exercicio_2():
    numero_secreto = random.randint(1, 100)
    palpite = int(input("Qual é seu palpite: "))
    tentativa = 1
    
    if numero_secreto < palpite:
        print("Erraste, o número secreto não é {palpite} pequeno")
        tentativa += 1
    elif numero_secreto > palpite:
        print("Erraste, o número secreto não é {palpite} grande")
        tentativa += 1
    elif numero_secreto == palpite:
        print("Wow acertaste com um total de {tentativa} tentativa(s)")  
    

def menu():
    while True:
        print("\n" + "="*30)
        print(" Menu de Exercícios")
        print("\n" + "="*30)
        print("1. Soma de dois números")
        print("2. Adivinha o número")
        print("0. Sair do Exercício")

        escolha = input("Escolha uma opção de (0-2)")

        if escolha == '1':
            exercicio_1()
        elif escolha == '2':
            exercicio_2()
        elif escolha == '0':
            print("tchauzinho...")
            break
        else:
            print("Opção inválida, tente um número (0-2)")

menu()