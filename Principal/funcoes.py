import TOM, time, getpass, nivelDificil, nivelFacil, nivelMedio
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
    time.sleep(0.2)

def Dificuldade():
     #Lista para verificação e validação da resposta
    listaLocal = ['1', '2', '3']
    
    #Lista para verificar e validar a confirmação
    lista = ['s', 'n']
    #A partir daqui começa o script que exibe o cabeçaho com as opções de níveis
    print("Por favor, escolha um nível: ")
    time.sleep(1)
    for i in range(limite):
        print(f"[{listaDificuldade[i][0]}] - {listaDificuldade[i][1]}")
        time.sleep(1)
    #Variavel que recebe a resposta
    nivel = input("Informe o seu nível: ")
    
    #Verificar se a resposta fornecida é válida, só saíra do loop quando a resposta estiver
    while(nivel not in listaLocal):
        time.sleep(1)
        TOM.respostaInvalida()
        time.sleep(1)
        nivel = input("Por favor, informe um nível válido: ")

    #Nível é convertido para inteiro, já que foi verificado se ele é um número válido
    nivel = int(nivel)
    for i in range(limite):
        #Percorre a lista e retorna a informada
        if(listaDificuldade[i][0] == nivel):
            #Confirma se a resposta informada foi realmente a desejada ou um engano
            time.sleep(1)
            confirma = input(f"Você quer realmente o nível: {listaDificuldade[i][1]}? (s/n) ").lower()
            
            #Confere se a confirmação foi válida 
            while confirma not in lista:
                time.sleep(1)
                TOM.respostaInvalida()
                time.sleep(1)
                confirma = input(f"Você quer realmente o nível: {listaDificuldade[i][1]}? (s/n) ").lower()
                time.sleep(1)
            if(confirma == "s"):
                print("UAU, que incrivel!")
                time.sleep(1)
                DificuldadeEscolhida = str(listaDificuldade[i][1]).lower()
                if(DificuldadeEscolhida == "fácil"):
                    time.sleep(1)
                    TOM.nivelFacil()
                    QuestoesFaceis()

                elif(DificuldadeEscolhida == "médio"):
                    time.sleep(1)
                    TOM.nivelMedio()
                    QuestaoMedia()
                else:
                    time.sleep(1)
                    TOM.nivelDificil()
                    QuestaoDificil()
            else:
                time.sleep(1)
                TOM.respostaInvalida()    
                Dificuldade()
def QuestoesFaceis():
    time.sleep(1)
    nivelFacil.exibirQuestões()
def QuestaoDificil():
    time.sleep(1)
    nivelDificil.exibirQuestões()
def QuestaoMedia():
    time.sleep(1)
    nivelMedio.exibirQuestões()
def confereNivel(nivel):
    possivel = "1234"
    while(nivel not in possivel) or (nivel == ""):
        TOM.respostaInvalida()
        nivel = input("Escolha outra opção: ")
    nivel = int(nivel)
    return nivel
def consultaQuestao(nivelArquivo):

    #Selecionando qual arquivo deve ser aberto
    if(nivelArquivo == 1):
        nivel = "Questoes/Facil"
    elif(nivelArquivo == 2):
        nivel = "Questoes/Medio"
    else:
        nivel = "Questoes/Dificil"
    
    #Abrindo o arquivo
    arquivo2 = open(nivel, "r")
    
    
    #Lendo ele como lista e salvando numa várivel 
    lista = arquivo2.readlines()

    #Fechando o arquivo
    #arquivo2.close()

    #Contando as questões
    #Váriaveis que recebe a quantidade de questões
    quantQuestoes = 0

    for i in range(len(lista) - 1):
        time.sleep(0.01)
        print(lista[i], end='')
    arquivo2.close()
def menuAdmin():
    time.sleep(1)
    print("Escolha uma opção:")
    time.sleep(1)
    print("[1] - Cadastrar uma nova questão")
    print("[2] - Ver questões")
    print("[3] - Voltar ao menu inical")
    print("[4] - Sair")
    time.sleep(1)
    opcao = input("Sua resposta: ")
    #Lista para verificação e validação da resposta
    valido = "123456"
    
    #Lista para verificar e validar a confirmação
    confirma = "sn"
    
    #Verificar se a resposta fornecida é válida, só saíra do loop quando a resposta estiver
    while(opcao not in valido) or (opcao == ""):
        time.sleep(1)
        TOM.respostaInvalida()
        time.sleep(1)
        opcao = input("Por favor, informe novamente: ")
    #Nível é convertido para inteiro, já que foi verificado se ele é um número válido
    for i in range(len(valido)):
        #Percorre a lista e retorna a informada
        if(valido[i] == opcao):
            #Confirma se a resposta informada foi realmente a desejada ou um engano
            time.sleep(1)
            confirmacao = input(f"Você quer realmente quer: {valido[i]}? (s/n) ").lower()
            time.sleep(1)
            #Confere se a confirmação foi válida 
            while confirmacao not in confirma:
                TOM.respostaInvalida()
                confirmacao = input(f"Você quer realmente o nível: {valido[i]} (s/n) ").lower()
            if(confirmacao == "s"):
                opcao = int(opcao)
                if(opcao == 1):
                    time.sleep(1)
                    print("Escolha em que arquivo você quer adicionar a questão: ")
                    time.sleep(1)
                    print("[1] - Fácil")
                    print("[2] - Médio ")
                    print("[3] - Difícil")
                    print("[4] - Voltar")
                    time.sleep(1)
                    nivel = input("Escolha uma opção: ")
                    nivelConferido = confereNivel(nivel)
                    if(nivelConferido == 1):
                        nivelFacil.adicionarQuestão()
                    elif(nivelConferido == 2):
                        nivelMedio.adicionarQuestão()
                    elif(nivelConferido == 3):
                        nivelDificil.adicionarQuestão()
                    else:
                        time.sleep(1)
                        menuAdmin()
                elif(opcao == 2):
                    time.sleep(1)
                    print("Escolha em que arquivo você quer ver: ")
                    time.sleep(1)
                    print("[1] - Fácil")
                    print("[2] - Médio ")
                    print("[3] - Difícil")
                    print("[4] - Voltar")
                    time.sleep(1)
                    nivel = input("Escolha uma opção: ")
                    time.sleep(1)
                    nivelArquivo = int(confereNivel(nivel))
                    consultaQuestao(nivel)
                    time.sleep(1)
                    menuAdmin()                    
                elif(opcao == 3):
                    time.sleep(1)
                    menu()
            else:
                menuAdmin()

def login():
    #Abrindo o arquivo administrador
    arquivoAdmin = open("Questoes/Administrador", "r")
    
    #Salva todas as linhas em forma de lista
    bloco = arquivoAdmin.readlines()
    #Váriavel que irá receber as listas
    lista = []
    #Fecha o arquivo
    arquivoAdmin.close()
    #Abre novamente
    arquivoAdmin = open("Questoes/Administrador", "r")
    #Salva cada linha do arquivo em lista
    for i in range(len(bloco)):
        linha = arquivoAdmin.readline()
        lista.append(linha)
    time.sleep(1)
    print("-"*20, "Administrador", "-"*20)
    time.sleep(1)
    #Pede que o login seja informado
    login = input("Inform o seu login: ").strip()
    time.sleep(1)
    i = 0
    while i < len(lista):
        loginA = str(lista[i]).strip()
        #Confere se existi algum login igual ao informado
        if (loginA == login):
            #Caso exista autenticador recebe verdadeiro
            autenticador = True
            break
        else:
            #Caso contrário autenticador recbe falso
            autenticador = False
            break
        #Váriavel de controle
        i += 1
    #Confere se exste no arquivo algum login igual ao informado
    if(autenticador):
        #Caso exista, então é solicitado a senha
        time.sleep(1)
        senha = getpass.getpass("Informe sua senha: ")
        time.sleep(1)
        senhaA = str(lista[i]).strip()
        #Confere se a senha associado ao administrador é verdadeota
        if (senha == senhaA):
                #Caso seja então retorna verdadeiro
                return True
        else:
            #Enquanto a senha informada não estiver no arquivo então ela será solicitada novamente 3 vezes
            j = 1
            while (senha != senhaA) and (j <= 3):
                time.sleep(1)
                TOM.senhaIncorreta()
                print("Você tem", 4 - j, "tentativas")
                time.sleep(1)
                senha = getpass.getpass("Informe sua senha: ")
                time.sleep(1)
                if (senha == senhaA):
                    #Caso seja então retorna verdadeiro
                    return True
                j += 1
            TOM.senhaIncorreta()
            return False
    else:
        TOM.loginIncorreto()
        return False
    arquivoAdmin.close()

def menu(nome):
    #Confere se a resposta está válida ou não
    lisaLocal = "123"
    #Exibe as opções do jogador
    print(nome, "O que você deseja?")
    print("[1] - Inciar o jogo")
    print("[2] - Administrar")
    print("[3] - Sair do jogo")
    escolha = input("Informe a sua reposta: ")
    
    #Valida a opção escolhida
    while(escolha not in lisaLocal) or escolha == "":
        TOM.respostaInvalida()
        escolha = input("Tente de novo: ")
    escolha = int(escolha)
    if escolha == 1:
        Dificuldade()
    
    elif(escolha == 2):
        if(login()):
            menuAdmin()
        else:
           TOM.loginIncorreto()
           menu()
    else:
        TOM.saindoDoSistema()
        time.sleep(4)

def confereNivel(nivel):
    possivel = "1234"
    while(nivel not in possivel) or (nivel == ""):
        TOM.respostaInvalida()
        nivel = input("Escolha outra opção: ")
    nivel = int(nivel)
    return nivel

def consultaQuestao(nivelArquivo):
    #Selecionando qual arquivo deve ser aberto
    if(nivelArquivo == 1):
        nivel = "Questoes/Facil"
    elif(nivelArquivo == 2):
        nivel = "Questoes/Medio"
    else:
        nivel = "Questoes/Dificil"
    
    #Abrindo o arquivo
    arquivo2 = open(nivel, "r")
    
    
    #Lendo ele como lista e salvando numa várivel 
    lista = arquivo2.readlines()

    #Fechando o arquivo
    #arquivo2.close()

    #Contando as questões
    #Váriaveis que recebe a quantidade de questões
    quantQuestoes = 0

    for i in range(len(lista) - 1):
        time.sleep(0.01)
        print(lista[i], end='')
    arquivo2.close()

def menuAdmin():
    TOM.notificandoAdministrador()
    time.sleep(1)
    print("Escolha uma opção:")
    time.sleep(1)
    print("[1] - Cadastrar uma nova questão")
    print("[2] - Ver questões")
    print("[3] - Voltar ao menu inical")
    print("[4] - Sair")
    time.sleep(1)
    opcao = input("Sua resposta: ")
    time.sleep(1)
    #Lista para verificação e validação da resposta
    valido = "123456"
    
    #Lista para verificar e validar a confirmação
    confirma = "sn"
    
    #Verificar se a resposta fornecida é válida, só saíra do loop quando a resposta estiver
    while(opcao not in valido) or (opcao == ""):
        time.sleep(0.3)
        TOM.respostaInvalida()
        time.sleep(0.5)
        opcao = input("Por favor, informe novamente: ")
    #Nível é convertido para inteiro, já que foi verificado se ele é um número válido
    for i in range(len(valido)):
        #Percorre a lista e retorna a informada
        if(valido[i] == opcao):
            #Confirma se a resposta informada foi realmente a desejada ou um engano
            confirmacao = input(f"Você quer realmente quer: {valido[i]}? (s/n) ").lower()
            
            #Confere se a confirmação foi válida 
            while confirmacao not in confirma:
                TOM.respostaInvalida()
                confirmacao = input(f"Isso mesmo? {valido[i]} (s/n) ").lower()
            if(confirmacao == "s"):
                opcao = int(opcao)
                if(opcao == 1):
                    time.sleep(1)
                    print("Escolha em que arquivo você quer adicionar a questão: ")
                    time.sleep(1)
                    print("[1] - Fácil")
                    print("[2] - Médio ")
                    print("[3] - Difícil")
                    print("[4] - Voltar")
                    time.sleep(1)
                    nivel = input("Escolha uma opção: ")
                    nivelConferido = confereNivel(nivel)
                    if(nivelConferido == 1):
                        nivelFacil.adicionarQuestão()
                    elif(nivelConferido == 2):
                        nivelMedio.adicionarQuestão()
                    elif(nivelConferido == 3):
                        nivelDificil.adicionarQuestão()
                    else:
                        menuAdmin()
                elif(opcao == 2):
                    time.sleep(1)
                    print("Escolha em que arquivo você quer ver: ")
                    time.sleep(1)
                    print("[1] - Fácil")
                    print("[2] - Médio ")
                    print("[3] - Difícil")
                    print("[4] - Voltar")
                    time.sleep(1)
                    nivel = input("Escolha uma opção: ")
                    nivelArquivo = int(confereNivel(nivel))
                    consultaQuestao(nivel)
                    time.sleep(1)
                    menuAdmin()                    
                elif(opcao == 3):
                    time.sleep(1)
                    menu()
                else:
                    time.sleep(1)
                    TOM.saindoDoSistema()
            else:
                time.sleep(1)
                
                menuAdmin()
            