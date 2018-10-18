import time
#Váriavel com as dificuldades
listaDificuldade = [[1, "Fácil"], [2, "Médio"], [3, "Difícil"]]

#Váriavel inteira que recebe o tamanho da lista, ela será usada em funções que utilize for para percorrer ela
limite = len(listaDificuldade)

def cabecalho():
    print("="*65)
    print("")
    print("PACC - Programa de Avaliação do Conhecimento em Computação")
    print("")
    print("="*65)

#Apenas exibe os níveis do jogo
# def Dificuldade():
#     print("Por favor, escolha um nível: ")
#     time.sleep(0.75)
#     for i in range(limite):
#         print(f"[{listaDificuldade[i][0]}] - {listaDificuldade[i][1]}")
#         time.sleep(0.75)
#     #Variavel que recebe a resposta do usuário
#     nivel = input("Informe o seu nível: ")

#     #Enquanto o nível informado não for válido eu pergunto novamente
#     nivel = validaDificuldade(nivel)

#     #Confirma se a resposta do usuário foi realmente a informada
#     print("Cheguei aqui!")
#     print(confirmaDificuldade(nivel))
#     print("Passei daqui!")
#     if not (confirmaDificuldade(nivel)):
#         print("Vamos novamente!")
#         Dificuldade()
#         print(variavel)
#     return
def Dificuldade(nivel):
    listaLocal = ['1', '2', '3']
    lista = ['s', 'n']
    while(nivel not in listaLocal):
        time.sleep(0.3)
        print("Resposta inválida!")
        time.sleep(0.5)
        nivel = input("Por favor, informe um nível válido: ")
    nivel = int(nivel)
    for i in range(limite):
        print(listaDificuldade[i][0], nivel)
        if(listaDificuldade[i][0] == nivel):
            print("Não da mais!")
            confirma = input(f"Você quer realmente o nível: {listaDificuldade[i][1]}? (s/n) ").lower()
            while confirma not in lista:
                print("Respondir errado!!")
                confirma = input(f"Você quer realmente o nível: {listaDificuldade[i][1]}? (s/n) ").lower()
                print(confirma)
            if(confirma == "s"):
                print("Ótimo!")
                return listaDificuldade[i][1]
            else:
                nivel = str(nivel)
                Dificuldade(nivel)







#Função que confere se a dificuldade escolhida é válida
#Função que confirma a dificuldade escolhida
# def confirmaDificuldade(nivel):
#     lista = ['s', 'n']
#     nivel = int(nivel)
#     for i in range(limite):
#         print(listaDificuldade[i][0], nivel)
#         if(listaDificuldade[i][0] == nivel):
#             print("Não da mais!")
#             confirma = input(f"Você quer realmente o nível: {listaDificuldade[i][1]}? (s/n) ").lower()
#             while confirma not in lista:
#                 print("Respondir errado!!")
#                 confirma = input(f"Você quer realmente o nível: {listaDificuldade[i][1]}? (s/n) ").lower()
#                 print(confirma)
#         print(confirma)
#         if(confirma == "s"):
#             return True
#         else:
#             return False

# #Função que confirma a dificuldade do usuário
# def testeDificuldade(confirmaResposta):
#     confirmaResposta = str(confirmaResposta).lower()
#     while(confirmaResposta != 's') or (confirmaResposta != "n"):
#         confirmaResposta = input("Você quer o nível fácil? (s/n) ")
#     if(confirmaResposta == "s"):
#         return True
#     else:
#         return False
        
