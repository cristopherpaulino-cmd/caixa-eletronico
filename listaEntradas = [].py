listaPedido = []
valor = 0


opcao = 0
print("opções de prato principal: ")
print("----------------------------------")
while opcao > 3 or opcao <= 0 :
    opcao = int(input("Digite 1 para selecionar bruschettas 20R$\n2 para selecionar enroladinho de massa 15R$\n3 para selecionar pão com pate 15R$"))
    if opcao == 1:
        print("Sua entrada foi selecionada com sucesso!")
        listaPedido.append("bruschettas")
        valor = 20
    elif opcao == 2:
        print("Sua entrada foi selecionada com sucesso!")
        listaPedido.append("enroladinho de massa")
        valor = 15
    elif opcao == 3:
        print("Sua entrada foi selecionada com sucesso!")
        listaPedido.append("pão com pate")
        valor = 15
print("opções de prato principal: ")
opcao = 0
print("------------------------------------")
while opcao > 3 or opcao <= 0 :
    opcao = int(input("Digite 1 para selecionar batatas fritas com frango frito 45R$\n2 para selecionar macarrão a bolonhesa 40R$\n3 para selecionar feijoada 40R$"))
    if opcao == 1:
        print("Seu prato principal foi selecionado!")
        valor = 45
        listaPedido.append("frango frito")
    elif opcao == 2:
        print("Seu prato principal foi selecionado!")
        valor = 40
        listaPedido.append("macarrão a bolonhesa")
    elif opcao == 3:
        print("Seu prato principal foi selecionado!")
        valor = 40
        listaPedido.append("feijoada")
print("opções de bebida: ")
opcao = 0
print("-------------------------------------")
while opcao > 3 or opcao <= 0 :
    opcao = int(input("Digite 1 para selecionar caipirinha(de qualquer sabor) R$25 \n2 para selecionar gin 20 R$\n3 para selecionar tequila 50R$"))
    if opcao == 1:
        print("Sua bebida foi selecionada! ")
        valor = 25
        listaPedido.append("caipirinha")
    elif opcao == 2:
        print("Sua bebida foi selecionada! ")
        valor = 20
        listaPedido.append("gin")
    elif opcao == 3:
        print("Sua bebida foi selecionada! ")
        valor = 50
        listaPedido.append("tequila")
print(listaPedido)