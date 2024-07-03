print("1- Hambúguer -  R$10,00")
print("2- Batata Frita - R$5,00")
print("3- Refrigerante - R$4,00")
print("4- Sorvete - 2,00") 

opcão = int(input("Digite o nº da opção desejado: "))
quantidade = int(input("Digite a quantidade desejada: "))
nome = input("Digite o nome do cliente: ")

if opcão == 1:
    print("Hambúguer sendo preparado para: ", nome)
    print("Tempo de espera de 15 minutos")
    total = quantidade * 10 
    print("Total: R$", total)

if opcão == 2:
    print("Batata frita sendo preparado para: ", nome)
    print("Tempo de espera de 15 minutos")
    total = quantidade * 5 
    print("Total: R$", total)

if opcão == 3:
    print("Refrigerante ja vai ser entregue: ", nome)
    print("Tempo de espera de 3 minutos")
    total = quantidade * 4
    print("Total: R$", total)

if opcão == 4:
    print("sorvete sendo preparado para: ", nome)
    print("Tempo de espera de 2 minutos")
    total = quantidade * 2 
    print("Total: R$", total)


