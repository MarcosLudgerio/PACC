#PACC - Programa de Avaliação do Conhecimento em Computação 
import funcoes, TOM, time

#Lista para verificar e validar a confirmação
lista = ['s', 'n']

#Nome do programa e apresentação do TOM
funcoes.cabecalho()
TOM.boasVindas()

#Mensagem do TOM
time.sleep(2)
TOM.depoisDasBoasVindas()

time.sleep(2)
TOM.apresentacao()
#Pede o nome da pessoa que tá usando
time.sleep(2)
nome = input("Me diga o seu nome: ")

time.sleep(2)
TOM.iniciarJogo(nome)

#Pergunta se a pessoa quer jogar ou fazer alguum tipo de alteração
time.sleep(2)
TOM.jogadorouadmin(nome)
# While que permite o sistema voltar ao inicio quando conviniente
while True:
    while True:
        time.sleep(1)
        #Essa função exibe as opões
        funcoes.cabecalhoMenu(nome)
        escolha = input("Informe a sua reposta: ")
        #Confere se a respostado usuário é aceita ou não
        valido = funcoes.validaRespostaMenu(escolha)
        time.sleep(1)
        #Enquanto não for, terá que ser informado novamente
        while(valido != True):
            #O TOM da uma chamda de antenção
            TOM.respostaInvalida()
            escolha = input("Tente de novo: ")
            valido = funcoes.validaRespostaMenu(escolha)
            time.sleep(1)
        #Aqui é solicitado uma confirmação se a opção escolhida foi a desejada
        funcoes.confirmaRespostaMenu(escolha)
        confirma13 = input("(s/n): ")
        time.sleep(1)
        #Confere se a reposta é aceita ou não
        while confirma13 not in lista:
                time.sleep(1)
                TOM.respostaInvalida()
                time.sleep(1)
                confirma13 = input("Tente novemente: ").lower()
                time.sleep(1)
        #Caso seja o primeiro while é parado e entra no segundo
        if confirma13 == "s":
            break
        time.sleep(1)
    print("")
    #Se a escolha for pra jogar
    if (escolha == '1'):
        #While para voltar quando for solicitaado
        while True:
            time.sleep(1)
            #Aqui é exibido as dificuldades possíveis - Fácil, Médio e Difícil
            funcoes.cabecalhoDificuldade(nome)
            time.sleep(1)
            opcao = input("Informe o seu nível: ")
            #Confere se a resposta é válida ou não
            opcaoValida = funcoes.validaOpcao(opcao)
            #Caso não seja é solicitada novamente receber uma resposta válida
            while opcaoValida != True:
                time.sleep(1)
                TOM.respostaInvalida()
                time.sleep(1)
                opcao = input("Informe o seu nível: ")
                opcaoValida = funcoes.validaOpcao(opcao)
            #Confirma se a dificuldade escolhida era a desejada
            funcoes.confirmaDifculdade(opcao)
            confirma = input("(s/n): ").lower()
            #Confere se a confirmação foi válida 
            while confirma not in lista:
                time.sleep(1)
                TOM.respostaInvalida()
                time.sleep(1)
                confirma = input("Tente novemente: ").lower()
                time.sleep(1)
            #Se for, então a variavel opcao recebe o titulo do arquivo escolhido
            if(confirma == "s"):
                if (opcao == '1'):
                    print("")
                    time.sleep(1.5)
                    TOM.nivelFacil()
                    time.sleep(1.5)
                    nivel = "Facil"
                elif (opcao == '2'):
                    print("")
                    time.sleep(1.5)
                    TOM.nivelMedio()
                    time.sleep(1.5)
                    nivel = "Medio"
                else:
                    print("")
                    time.sleep(1.5)
                    TOM.nivelDificil()
                    time.sleep(1.5)
                    nivel = "Dificil"
                #Chama a função exibir questoes com o respectivo nivel
                funcoes.exibirQuestões("Questoes/" + nivel, nome)
                time.sleep(2)
                #Quando acaba, é perguntado se quer jogar novamente
                parar = input("Você deseja jogar novamente? (s/n): ")
                #Confere se a resposta é aceita ou não
                while parar not in lista:
                    time.sleep(1)
                    TOM.respostaInvalida()
                    time.sleep(1)
                    parar = input("Tente novemente: ").lower()
                    time.sleep(1)
                #Caso ele não queira o while dde dentro é interrompido, retornando para o principal
                if (parar == "n"):
                    TOM.jogoEncerrado()
                    break
                else:
                    print("")
            else:
                print("")
                
    #Caso seja administrador é exibido a tela de login
    elif(escolha == '2'):
        #É chamado o autenticador de login, é uma função boolean
        if(funcoes.login()):
            #Caso a auutenticação seja verdadeira, é exibido as opções de administrador
            retorno = funcoes.menuAdmin()
            if(retorno == '3'):
                print("O retorno", retorno)
            elif(retorno == '4'):
                break
            else:
                print("")
        else:
            #Caso não, então é exibido uma mensagem de erro e o programa retorna para o menu inicial
            time.sleep(1)
            TOM.erroDeLogin()
    else:
        #Caso seja solicitado a saída do sistema
        TOM.saindoDoSistema()
        break
        time.sleep(4)

