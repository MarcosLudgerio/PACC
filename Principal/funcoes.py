import time
#Váriavel com as dificuldades
listaDificuldade = [[1, "Fácil"], [2, "Médio"], [3, "Difícil"]]

#Váriavel inteira que recebe o tamanho da lista, ela será usada em funções que utilize for para percorrer ela
limite = len(listaDificuldade)

def cabecalho():
    print("="*65)
    print("")
    print("   PACC - Programa de Avaliação do Conhecimento em Computação")
    print("")
    print("="*65)

def Dificuldade():



    #Lista para verificação e validação da resposta
    listaLocal = ['1', '2', '3']
    
    #Lista para verificar e validar a confirmação
    lista = ['s', 'n']
    #A partir daqui começa o script que exibe o cabeçaho com as opções de níveis
    print("Por favor, escolha um nível: ")
    time.sleep(0.75)
    for i in range(limite):
        print(f"[{listaDificuldade[i][0]}] - {listaDificuldade[i][1]}")
        time.sleep(0.75)
    #Variavel que recebe a resposta
    nivel = input("Informe o seu nível: ")
    
    #Verificar se a resposta fornecida é válida, só saíra do loop quando a resposta estiver
    while(nivel not in listaLocal):
        time.sleep(0.3)
        print("Resposta inválida!")
        time.sleep(0.5)
        nivel = input("Por favor, informe um nível válido: ")

    #Nível é convertido para inteiro, já que foi verificado se ele é um número válido
    nivel = int(nivel)
    for i in range(limite):
        #Percorre a lista e retorna a informada
        if(listaDificuldade[i][0] == nivel):
            #Confirma se a resposta informada foi realmente a desejada ou um engano
            confirma = input(f"Você quer realmente o nível: {listaDificuldade[i][1]}? (s/n) ").lower()
            
            #Confere se a confirmação foi válida 
            while confirma not in lista:
                print("Resposta inválida!")
                confirma = input(f"Você quer realmente o nível: {listaDificuldade[i][1]}? (s/n) ").lower()
            if(confirma == "s"):
                print("Ótimo, vamos começar a nossa brincadeira!")
                return listaDificuldade[i][1]
            else:
                nivel = str(nivel)
                Dificuldade()
            
