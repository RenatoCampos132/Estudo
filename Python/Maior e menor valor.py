#Forma extremamente mal otimizada de saber qual é o maior e menor valor

#Recebe os valores

num_1 = float(input("Digite o primeiro valor:"))
num_2 = float(input("Digite o segundo valor:"))
num_3 = float(input("Digite o terceiro valor:"))

#Verifica qual é o maior valor

if num_1 > num_2 and num_1 > num_3:
    print("O maior valor é o {:.1f}".format(num_1))
    
elif num_2 > num_1 and num_2 > num_3:
    print("O maior valor é o {:.1f}".format(num_2))
    
elif num_3 > num_1 and num_3 > num_2:
    print("O maior valor é o {:.1f}".format(num_3))

#Verifica qual é o menor valor

if num_1 < num_2 and num_1 < num_3:
    print("O menor valor é o {:.1f}".format(num_1))
    
elif num_2 < num_1 and num_2 < num_3:
    print("O menor valor é o {:.1f}".format(num_2))
    
elif num_3 < num_1 and num_3 < num_2:
    print("O menor valor é o {:.1f}".format(num_3))
