#1. Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o
#menor valor, sem usar as funções max e min.

#Software desenvolvido por João Pedro de Almeida

import random
num = 0
controle = 1
maior = 0
menor = 100

while(controle <=10):

    num = random.randrange(1,100)
    print("O número atual é: ", num)
    
    if(num > maior):
        maior = num

    elif(num < menor):
        menor = num

    controle += 1

print("\nO maior número é: %d" %maior)
print("\nO menor número é: %d" %menor)
input("Pressione enter para sair")
exit()#Saindo do sistema com segurança
