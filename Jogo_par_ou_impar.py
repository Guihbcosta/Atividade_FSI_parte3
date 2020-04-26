#autor: Guilherme Henrique Battista Costa

import random

escolha = input("Digite  sua escolha, par ou ímpar (P ou I): ")

if escolha=="P" or escolha=="I":
    njogador = int(input("Digite um número de 1 a 10: "))
    
    if njogador>=1 and njogador<=10:
        nadversa = random.randrange(1,10)
        soma = nadversa+njogador
        
        if escolha=="P" and soma%2==0:
            print("Parabéns você ganhou o par ou ímpar")
            
        elif escolha=="I" and soma%2!=0:
            print("Parabéns você ganhou o par ou ímpar")

        else:
            print("Você perdeu o par ou ímpar")
           
    else:
        print("Número inválido")        
else:
    print("Escolha inválida")
