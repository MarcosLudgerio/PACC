import time, random

#Abre o arquivo
arquivo = open("Questoes/Facil", "a")
    
def adicionarQuestão():
    #Solicita o enunciado
    print("Informe enunciado: ")
    enunciado = input("")

    #Solicita as alternativas e resposta correta
    print("Informe as alternativas: ")
    a = input("A) ")
    b = input("B) ")
    c = input("C) ")
    d = input("D) ")
    resposta = input("Alternativa correta: ").upper() 
    
    #Confere se a resposta é válida ou não
    while resposta not in "ABCD" or resposta == "":
        print("Informe uma resposta válida!")
        resposta = input("Alternativa correta: ").upper()
    
    confereAlternativas = [a, b, c, d]
    #Confere se já tem alternativa igual a A   
    while (a in confereAlternativas[1:]):
        print("Já existe uma alternativa igual a essa!")
        print("Por favor, altere ela!")
        a = input("A) ")
        confereAlternativas[0] = a

    #Confere se já tem alternativa igual a B   
    while (b in confereAlternativas[:1]) or (b in confereAlternativas[2:]):
        print("Já existe uma alternativa igual a essa!")
        print("Por favor, altere ela!")
        b = input("B) ")
        confereAlternativas[1] = b
    
    #Confere se já tem alternativa igual a C   
    while (c in confereAlternativas[:2]) or (c in confereAlternativas[3:]):
        print("Já existe uma alternativa igual a essa!")
        print("Por favor, altere ela!")
        c = input("C) ")
        confereAlternativas[2] = c

    #Confere se já tem alternativa igual a D   
    while (d in confereAlternativas[:3]):
        print("Já existe uma alternativa igual a essa!")
        print("Por favor, altere ela!")
        d = input("D) ")
        confereAlternativas[3] = d

    #Escreve no arquivo
    arquivo.write("\n")
    arquivo.write("\n" + enunciado)
    arquivo.write("\nA) " + a)
    arquivo.write("\nB) " + b)
    arquivo.write("\nC) " + c)
    arquivo.write("\nD) " + d)
    arquivo.write("\n" + resposta.upper())


def exibirQuestões():  
    #Váriavel que recebem o arquivo em forma de listas
    arquivoCompleto = []

    #Contador de respostas certas
    contCertas = 0

    #Contador de Respostas erradas
    contErradas = 0

    #Abrindo o arquivo
    arquivo2 = open("Questoes/Facil", "r")

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
    arquivo2 = open("Questoes/Facil", "r")

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
        print("\n")
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
        resposta = input("Informe a sua resposta ").upper()
        confereResposta = validaResposta(resposta)
        
        #Confere se a resposta fornecida está certa
        if(repostaCorreta(respostaCerta, confereResposta)):
            time.sleep(3)
            print("Meus parabéns, você acertou!")
            time.sleep(2)
            #Caso a resposta estivejA correta, conta para no final da um feedback
            contCertas += 1
        else:
            time.sleep(3)
            print("Que pena resposta errada!")
            time.sleep(3)
            #Caso a resposta estiver errada
            contErradas += 1
    #Essa função altera a ordem das questões e grava no arquivo txt de maneira aleatoria    
    alteraOrdem(arquivoCompleto)

    #Função que retorna o nível do jogador
    resultado(contCertas, contErradas)

def validaResposta(resposta):
    #Valido recebe as respostas possíveis
    valido = "ABCD"
    
    #Enquanto a resposta não for válida deverá ser solicitada novamente
    while(resposta not in valido) or (resposta == ""):
        print("Resposta inválida!")
        resposta = input("Digite novamente: ").upper()
    return resposta

def repostaCorreta(certa, errada):
    #Confere se a resposta é certa ou não
    if(certa == errada):
        return True
    else:
        return False
    
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

def resultado(certas, erradas):
    #Total de questões respondida
    total = 10
    
    #Percentual de acertos
    percentualCertas = certas/total
    
    #Percentual de erros
    percentualErradas = erradas/total
    time.sleep(2)
    
    #Feedback
    print(f"Você acertou {certas} de {total}, aproveitamento de {percentualCertas}%")
    time.sleep(2)
    if(percentualCertas >= 0.7):
        time.sleep(2)
        print("Muito bom!")
        time.sleep(2)
    elif(percentualCertas >= 0.5):
        time.sleep(2)
        print("Normal!")
        time.sleep(2)    
    else:
        time.sleep(2)
        print("Você precisa estudar um pouco mais!")
        time.sleep(2)