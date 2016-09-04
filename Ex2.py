#2. Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números
#pares na lista PAR e os números ímpares na lista IMPAR. Imprima as três listas.

import random
num = 0
controle = 0
pares = []
impares = []
todos = []
a , b = 0 , 0

while(controle <=19):

    num = random.randrange(1,100)
    todos.insert(controle,num)
    print(num)
    
    if(num % 2 == 0) and (num > 0):
        pares.insert(a,num)
        a += 1

    elif(num > 0):
        impares.insert(b,num)
        b += 1

    controle += 1

print("A lista de todos os números: ", todos)
print("\nOs números pares são: ", pares)
print("\nOs números impares são: ", impares)
input("Pressione enter para sair")
exit()#Saindo do sistema com segurança
