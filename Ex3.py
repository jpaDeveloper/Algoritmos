#3. Faça um programa que crie dois vetores com 10 elementos aleatórios
#entre 1 e 100. Gere um terceiro vetor de 20 elementos, cujos valores
#deverão ser compostos pelos elementos intercalados dos dois outros vetores.
#Imprima os três vetores.

#Software desenvolvido por João Pedro de Almeida

import random

num1 = 0
num2 = 0
controle = 0
controle2 = 0 
vetor1 = []
vetor2 = []
vetor3 = []
k , l = 0 , 0
b = True
a = 0

while(controle < 10):

    num1 = random.randrange(1,100)
    num2 = random.randrange(1,100)
    vetor1.insert(controle,num1)
    vetor2.insert(controle,num2)
    controle += 1
    
while(controle2 < 20):
    if b == True:
        vetor3.insert(a,vetor1[k])
        b = False
        k += 1

    elif b == False:
        vetor3.insert(a,vetor2[l])
        b = True
        l += 1

    a += 1
    controle2 += 1

    

print("Primeiro vetor: ", vetor1)
print("\nSegundo vetor: ", vetor2)
print("\nTerceiro vetor: ", vetor3)
input("Pressione enter para sair")
exit()#Saindo do sistema com segurança
