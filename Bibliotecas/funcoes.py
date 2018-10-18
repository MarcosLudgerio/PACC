def cabecalho():
    print("="*65)
    print("")
    print("PACC - Programa de Avaliação do Conhecimento em Computação")
    print("")
    print("="*65)

#Função para que recebe o nome do usuário e retorna a dificuldade escolhida
def escolhaDificuldade(nome):
    listaDificuldade = [[1, "Fácil"], [2, "Médio"], [3, "Difícil"]]
    print(f"\nOlá, {nome} seja muito bem vindo!")
    print("Por favor, escolha um nível: ")
    for i in range(3):
        print(f"[{listaDificuldade[i][0]}] - {listaDificuldade[i][1]}")
    dificuldade = input("Escolha uma dificuldade: ")
    validaDificuldade(dificuldade)
    confirmaDificuldade(dificuldade)
    return dificuldade

#Função queonfere se a dificuldade escolhida é válida
def validaDificuldade(dificuldade):
    possiveis = "123"
    while(dificuldade not in possiveis):
        print("Por favor informe uma reposta válida!")
        dificuldade = input("Escolha uma dificuldade: ")

    return dificuldade

#Função que confirma a dificuldade escolhida
def confirmaDificuldade(dificuldade):
    dificuldade = int(dificuldade)
    retorno = False
    if(dificuldade == 1):
        confirmaResposta = input("Você quer o nível fácil? (s/n) ")
        if(testeDificuldade(confirmaResposta)):
            retorno = True
        
    elif(dificuldade == 2):
        confirmaResposta = input("Você quer o nível médio? (s/n) ")
        testeDificuldade(confirmaResposta)
        if(testeDificuldade(confirmaResposta)):
            retorno = True
    else:
        confirmaResposta = input("Você quer o nível difícil? (s/n)")
        testeDificuldade(confirmaResposta)
        if(testeDificuldade(confirmaResposta)):
            retorno = True
    return retorno

#Função que confirma a dificuldade do usuário
def testeDificuldade(confirmaResposta):
    confirmaResposta = str(confirmaResposta).lower()
    while(confirmaResposta != 's') or (confirmaResposta != "n"):
        confirmaResposta = input("Você quer o nível fácil? (s/n) ")
    if(confirmaResposta == "s"):
        return True
    else:
        return False
        
