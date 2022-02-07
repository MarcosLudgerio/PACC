import TOM, time, getpass, random
#Váriavel com as dificuldades
listaDificuldade = [[1, "Fácil"], [2, "Médio"], [3, "Difícil"]]

#Váriavel inteira que recebe o tamanho da lista, ela será usada em funções que utilize for para percorrer ela
limite = len(listaDificuldade)

def cabecalho():
    print("="*65)
    print("")
    print("   PACC - Programa Avaliativo do Conhecimento em Computação")
    print("")
    print("="*65)
    time.sleep(0.2)

def cabecalhoDificuldade(nome):
    TOM.selecionarNivel(nome)
    time.sleep(1)
    for i in range(limite):
        print(f"[{listaDificuldade[i][0]}] - {listaDificuldade[i][1]}")
        time.sleep(1)

def validaOpcao(opcao):
    #Lista para verificação e validação da resposta
    listaLocal = ['1', '2', '3']
    
    #Verificar se a resposta fornecida é válida, só saíra do loop quando a resposta estiver
    if(opcao not in listaLocal):
        return False
    else:
        return True


def confirmaDifculdade(nivel):
    #Nível é convertido para inteiro, já que foi verificado se ele é um número válido
    nivel = int(nivel)
    for i in range(limite):
        #Percorre a lista e retorna a informada
        if(listaDificuldade[i][0] == nivel):
            #Confirma se a resposta informada foi realmente a desejada ou um engano
            time.sleep(1)
            print(f"Você quer realmente o nível: {listaDificuldade[i][1]}?")
#Exibe as opções do jogador
def cabecalhoMenu(nome):
    print("[1] - Inciar o jogo")
    print("[2] - Administrar")
    print("[3] - Sair do jogo")

#Função que confirma a resposta para o usuário
def confirmaRespostaMenu(escolha):
    #O -1 diminui uma unidade da escolha para que possa ser incrementado na lista, ficar de 0 a 2
    escolha = int(escolha) - 1
    lista = ['Jogar', 'Administrador', 'Sair']
    for i in range(len(lista)):
        if(lista[i] == lista[escolha]):
            print(f"Você realmente quer: {lista[i]}")
    
#Função que retorna caso a opção seja válida ou não
def validaRespostaMenu(escolha):
    #Escolhas possiveis
    listaLocal = ['1', '2', '3']
    
    if (escolha in listaLocal):
        return True
    else:
        return False

#Função que embaralha todo o arquivo e regrava as questões
def alteraOrdem(arquivoCompleto):
        #Isso acontece para que a ordem das questões sejam alterada
        random.shuffle(arquivoCompleto)
       
        #Depois de alterar a ordem o arquivo será gravado de novo com essa ordem nova
        arquivoRetorno = open("Questoes/Facil", "w")
        for i in range(len(arquivoCompleto)):
            for j in range(len(arquivoCompleto[i])):
                arquivoRetorno.write(arquivoCompleto[i][j])
            arquivoRetorno.write("\n")
        arquivoRetorno.close()

def resultado(certas, erradas, nome):
    #Total de questões respondida
    total = 10
    
    #Percentual de acertos
    percentualCertas = certas/total
    
    #Percentual de erros
    percentualErradas = erradas/total
    time.sleep(2)
    
    #Feedback
    print(f"\nVocê acertou {certas} de {total}, aproveitamento de {percentualCertas *100}%")
    time.sleep(2)
    if(percentualCertas == 1):
        time.sleep(2)
        TOM.rendimentoExcelente(nome)
        time.sleep(2)
    elif(percentualCertas >= 0.75):
        time.sleep(2)
        TOM.rendimentobom(nome)
        time.sleep(2)
    elif(percentualCertas >= 0.5):
        time.sleep(2)
        TOM.rendimentoMedio(nome)
        time.sleep(2)    
    else:
        time.sleep(2)
        TOM.rendimentoBaixo(nome)
        time.sleep(2)

def validaResposta(resposta):
    #Valido recebe as respostas possíveis
    valido = ["A", "B", "C", "D", "E"]
    
    #Enquanto a resposta não for válida deverá ser solicitada novamente
    while(resposta not in valido) or (resposta == ""):
        TOM.respostaInvalida()
        resposta = input("Digite novamente: ").upper()
    return resposta


def repostaCorreta(certa, errada):
    #Confere se a resposta é certa ou não
    if(certa == errada):
        return True
    else:
        return False

#Função que exibe as questões
def exibirQuestões(nivel, nome):  
    #Váriavel que recebem o arquivo em forma de listas
    arquivoCompleto = []

    #Contador de respostas certas
    contCertas = 0

    #Contador de Respostas erradas
    contErradas = 0

    #Abrindo o arquivo
    arquivo2 = open(nivel, "r")

    #Lendo ele como lista e salvando numa várivel 
    lista = arquivo2.readlines()

    #Fechando o arquivo
    arquivo2.close()

    #Contando as questões
    #Váriaveis que recebe a quantidade de questões
    quantQuestoes = 0

    for i in range(len(lista) - 1):
        #Sempre que encontrar uma linha vazia e a próxima com conteudo quer dizer que uma questão acabou, então ele conta
        if(lista[i] == "\n") and (lista[i + 1] != "\n"):
            quantQuestoes += 1

    #Agora separando as questões

    #Abrindo o arquivo
    arquivo2 = open(nivel, "r")

    #Váriavel de controle
    i = 0

    #Enquanto i for menor que o total de questões
    while i  < quantQuestoes + 1:
        #Bloco é uma lista com o enunciado e as alternativas da questão
        bloco = []
        
        #Linha é cada linha do arquivo, do tipo lista
        linha = arquivo2.readline()
        
        #Enquanto a linha não for quebrada ou nula eu adiciono no bloco
        while linha != "\n" and len(linha) != 0:
            bloco.append(linha)
            
            #Linha recebe a próxima linha do arquivo, caso ela não seja nula, é adicionada em bloco
            linha = arquivo2.readline()
        #Caso o bloco não esteja vazio ou nulo então eu adiciono ele em arquivoCompleto
        if bloco != []:
            arquivoCompleto.append(bloco)       
        else:
            break
        #Alteração a variável de controle
        i += 1
    arquivo2.close()

    #Percorrendo a lista arquivo completo, ela é formada por sublistas que são as questões. 
    for i in range(10):
        print("")
        time.sleep(1)
        print("-"*20, f"QUESTÃO {i + 1}", "-"*20)
        time.sleep(1)
        #Aqui eu leio a sublista e axibo para o usuário o - 1 é para que a resposta correta não seja mostrada
        for j in range(len(arquivoCompleto[i]) - 1):
            time.sleep(1)
            print(arquivoCompleto[i][j], end='')
        
        #Confere se a resposta está correta
        #Esse +1 indica a resposta certa, pois for só está lendo até a penultima linha
        respostaCerta = arquivoCompleto[i][j + 1][0]
        
        time.sleep(1)
        #A resposta é informada e válidada. Se está entre as alternativas possiveis
        resposta = input("Informe a sua resposta: ").upper()
        confereResposta = validaResposta(resposta)
        
        #Confere se a resposta fornecida está certa
        if(repostaCorreta(respostaCerta, confereResposta)):
            time.sleep(3)
            TOM.frasesDeAcertos()
            time.sleep(2)
            #Caso a resposta estiveja correta, conta para no final da um feedback
            contCertas += 1
        else:
            time.sleep(3)
            TOM.frasesDeErros()
            time.sleep(3)
            #Caso a resposta estiver errada
            contErradas += 1
    #Essa função altera a ordem das questões e grava no arquivo txt de maneira aleatoria    
    alteraOrdem(arquivoCompleto)

    #Função que retorna o nível do jogador
    resultado(contCertas, contErradas, nome)



def adicionarQuestão(nivel):
    #Abre o arquivo de acordo com o nível
    arquivo = open("Questoes/" + nivel, "a")
    
    print("-"*20, " ADICIONAR", "-"*20)
    time.sleep(1)
    print("Lembre-se da fonte de onde a quesão foi tirada!")
    time.sleep(1)
    #Solicita o enunciado
    print("Informe enunciado: ")

    enunciado = input("")
    #Solicita as alternativas e resposta correta
    time.sleep(1)
    print("Informe as alternativas: ")
    a = input("A) ")
    b = input("B) ")
    c = input("C) ")
    d = input("D) ")
    e = input("E) ")
    resposta = input("Alternativa correta: ").upper() 
    time.sleep(1)
    confirmaA = ['A', 'B', 'C', 'D', 'E']
    #Confere se a resposta é válida ou não ou se ela é nula ou não
    while resposta not in confirmaA or resposta == "":
        time.sleep(1)
        TOM.respostaInvalida()
        time.sleep(1)
        resposta = input("Alternativa correta: ").upper()
    confereAlternativas = [a, b, c, d, e]
    #Confere se já tem alternativa igual a A ou se ela é nula ou não
    while (a in confereAlternativas[1:]) or (a == ""):
        time.sleep(1)
        TOM.mudaAlternativa()
        time.sleep(1)
        a = input("A) ")
        confereAlternativas[0] = a

    #Confere se já tem alternativa igual a B ou se ela é nula ou não  
    while (b in confereAlternativas[:1]) or (b in confereAlternativas[2:]) or (b == ""):
        time.sleep(1)
        TOM.mudaAlternativa()
        time.sleep(1)
        b = input("B) ")
        confereAlternativas[1] = b
    
    #Confere se já tem alternativa igual a C ou se ela é nula ou não   
    while (c in confereAlternativas[:2]) or (c in confereAlternativas[3:]) or (c == ""):
        time.sleep(1)
        TOM.mudaAlternativa()
        time.sleep(1)
        c = input("C) ")
        confereAlternativas[2] = c

    #Confere se já tem alternativa igual a D ou se ela é nula ou não 
    while (d in confereAlternativas[:3]) or (d in confereAlternativas[4:]) or (d == ""):
        time.sleep(1)
        TOM.mudaAlternativa()
        time.sleep(1)
        d = input("D) ")
        confereAlternativas[3] = d
    
    #Confere se já tem alternativa igual a E ou se ela é nula ou não  
    while (e in confereAlternativas[:4]) or (e == ""):
        time.sleep(1)
        TOM.mudaAlternativa()
        time.sleep(1)
        e = input("E) ")
        confereAlternativas[4] = e

    #Escreve no arquivo
    arquivo.write("\n"+enunciado)
    arquivo.write("\nA) " + a)
    arquivo.write("\nB) " + b)
    arquivo.write("\nC) " + c)
    arquivo.write("\nD) " + d)
    arquivo.write("\nE) " + e)
    arquivo.write("\n" + resposta.upper() + "\n")

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
                #Exibe quantas tentativas ainda restam
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
        time.sleep(1)
        TOM.loginIncorreto()
        return False
    #Fecha novamente o arquivo
    arquivoAdmin.close()

#Função que confere o nivel escolhido, se é possivel ou não
def confereNivel(nivel):
    possivel = ["1", "2", "3", "4"]
    while(nivel not in possivel) or (nivel == ""):
        TOM.respostaInvalida()
        nivel = input("Escolha outra opção: ")
    nivel = int(nivel)
    return nivel

#Fução que exibe as questões de acordo com o nível
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
        time.sleep(0.5)
        print(lista[i], end='')
    arquivo2.close()
#Exibe o que o administrador pode fazer no sistema
def menuAdmin():
    #Lista para conferir aas rresposta
    ListaNivel = [1, 2, 3]
    TOM.notificandoAdministrador()
    time.sleep(1)
    
    print("Escolha uma opção:")
    time.sleep(1)
    print("[1] - Cadastrar uma nova questão")
    print("[2] - Ver questões")
    print("[3] - Voltar ao menu inical")
    print("[4] - Sair do sistema")
    time.sleep(1)
    opcao = input("Sua resposta: ")
    time.sleep(1)
    #Lista para verificação e validação da resposta
    valido = ["1", "2", "3", "4"]
    
    #Lista para verificar e validar a confirmação
    confirma = ['s', 'n']
    
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
            confirmacao = input(f"Você quer realmente quer: {valido[i]}? (s/n): ").lower()
            
            #Confere se a confirmação foi válida 
            while confirmacao not in confirma:
                TOM.respostaInvalida()
                confirmacao = input(f"Isso mesmo? {valido[i]} (s/n): ").lower()
            if(confirmacao == "s"):
                opcao = int(opcao)
                #Opção 1 - Cadastrar uma nova questão
                if(opcao == 1):
                    #While para tornar possivel retorna no algoritimo quando necessário
                    while True:
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
                        #Se for no nivel fácil
                        if(nivelConferido == 1):
                            nivel = "Facil"
                            #Chama a função passando como parametro o nivel facil
                            adicionarQuestão(nivel)
                            #Pergunta se deseja-se cadastrar uma nova questão
                            voltar = input("Deseja cadastrar outra questão? (s/n): ")
                            #Caso a resposta seja inválida é solicitada novamente
                            while voltar not in confirma:
                                TOM.respostaInvalida()
                                voltar = input(f"Isso mesmo? {valido[i]} (s/n): ").lower()
                            if(voltar == "s"):
                                #Voltando do while
                                print("OK, voltando ao cadastro de questões!") 
                            else:
                                menuAdmin()
                        elif(nivelConferido == 2):
                            nivel = "Medio"
                            adicionarQuestão(nivel)
                            voltar = input("Deseja cadastrar outra questão? (s/n): ")
                            while voltar not in confirma:
                                TOM.respostaInvalida()
                                voltar = input(f"Isso mesmo? {valido[i]} (s/n): ").lower()
                            if(voltar == "s"):
                                print("OK, voltando ao cadastro de questões!") 
                            else:
                                menuAdmin()
                        elif(nivelConferido == 3):
                            nivel = "Dificil"
                            adicionarQuestão(nivel)
                            voltar = input("Deseja cadastrar outra questão?")
                            while voltar not in confirma:
                                TOM.respostaInvalida()
                                voltar = input(f"Isso mesmo? {valido[i]} (s/n): ").lower()
                            if(voltar == "s"):
                                print("OK, voltando ao cadastro de questões!") 
                            else:
                                menuAdmin()
                        #Voltaar ao menu inicial
                        elif(nivelConferido == 4):
                            menuAdmin()
                        else:
                            #Essa opção, teoricamente, nunca será possivel
                            print("ERROR 404, procurar o programdor com urgência!")
                #Opção 2 - Consultar arquivos
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
                    if(nivelArquivo in ListaNivel):
                        consultaQuestao(nivelArquivo)
                    else:
                        menuAdmin()
                    time.sleep(1)
                    menuAdmin()                    
                
                elif(opcao == 3):
                    time.sleep(1)
                    #Retorna 3 para que o while seja interrompido no arquivo main
                    return '3'
                elif(opcao == 4):
                    time.sleep(1)
                    TOM.saindoDoSistema()
                    exit()
                else:
                    print("Essa mensagem nunca deve aparecer, caso ela apareça chame o programador com urgência!")
            else:
                time.sleep(1)
                menuAdmin()
