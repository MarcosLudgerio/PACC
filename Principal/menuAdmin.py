import nivelFacil, nivelMedio, nivelDificil, time

def menu():
    print("Escolha uma opção:")
    print("[1] - Cadastrar uma nova questão")
    print("[3] - Ver questões")
    print("[4] - Voltar ao menu inical")
    print("[5] - Fechar programa")

    opcao = input("Sua resposta: ")
    #Lista para verificação e validação da resposta
    valido = "123456"
    
    #Lista para verificar e validar a confirmação
    confirma = "sn"
    
    #Verificar se a resposta fornecida é válida, só saíra do loop quando a resposta estiver
    while(opcao not in valido) or (opcao == ""):
        time.sleep(0.3)
        print("Opção inválida!")
        time.sleep(0.5)
        opcao = input("Por favor, informe novamente: ")
    #Nível é convertido para inteiro, já que foi verificado se ele é um número válido
    for i in range(len(valido)):
        #Percorre a lista e retorna a informada
        print(valido[i], opcao)
        if(valido[i] == opcao):
            #Confirma se a resposta informada foi realmente a desejada ou um engano
            confirmacao = input(f"Você quer realmente quer: {valido[i]}? (s/n) ").lower()
            
            #Confere se a confirmação foi válida 
            while confirmacao not in confirma:
                print("Resposta inválida!")
                confirmacao = input(f"Você quer realmente o nível: {valido[i]} (s/n) ").lower()
            if(confirmacao == "s"):
                opcao = int(opcao)
                if(opcao == 1):
                    print("Escolha em que arquivo você quer adicionar a questão: ")
                    print("[1] - Fácil")
                    print("[2] - Médio ")
                    print("[3] - Difícil")
                    print("[4] - Voltar")
                    nivel = input("Escolha uma opção: ")
                    nivelConferido = confereNivel(nivel)
                    if(nivelConferido == 1):
                        nivelFacil.adicionarQuestão()
                    elif(nivelConferido == 2):
                        nivelMedio.adicionarQuestão()
                    elif(nivelConferido == 3):
                        nivelDificil.adicionarQuestão()
                    else:
                        menu()
                if(opcao == 2):
                    print("Escolha em que arquivo você quer ver: ")
                    print("[1] - Fácil")
                    print("[2] - Médio ")
                    print("[3] - Difícil")
                    print("[4] - Voltar")
                    nivel = input("Escolha uma opção: ")
                    nivelConferido = confereNivel(nivel)
                    if(nivelConferido == 1):
                    elif(nivelConferido == 2):
                        nivelMedio.adicionarQuestão()
                    elif(nivelConferido == 3):
                        nivelDificil.adicionarQuestão()
                    else:
                        menu()
            else:
                menu()


def confereNivel(nivel):
    possivel = "1234"
    while(nivel not in possivel) or (nivel == ""):
        print("Opção inválida!")
        nivel = input("Escolha outra opção: ")
    nivel = int(nivel)
    return nivel
menu()
