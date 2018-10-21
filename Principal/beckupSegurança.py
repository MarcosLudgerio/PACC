#PACC - Programa de Avaliação do Conhecimento em Computação 
import funcoes

#Função que exibe o cabeçalho
#funcoes.cabecalho()

#nome = "Marcos"

#Função que exibe as opções de níveis
#funcoes.Dificuldade()



#arquivo = open("Questoes/teste", "r+")

print("\n")
texto = input("Digite um titulo para acrescentar ao arquivo:\n")
arquivo = open('Questoes/teste','r+')
arquivo.seek(100)
arquivo.write(texto + '\n')
arquivo.close()

print("\nTexto alterado:")
arquivo = open('Questoes/teste','r')
for linha in arquivo:
    linha = linha.rstrip()
    print (linha)
arquivo.close()

# arquivoConsulta = open("Questoes/teste", "r")
# lista = []
# for i in range(7):
#     teste = arquivoConsulta.readline()
#     lista.append(teste)



# arquivoConsulta = open("Questoes/teste", "a")
# for i in range(len(lista)):
#     if("linha 3" in lista[i]):
#         varivael = "\nEssa linha deve ser adicionada!"
#         print(varivael)
#         arquivoConsulta.seek(i)
#         arquivoConsulta.write(varivael)
# arquivoConsulta.close()




# print("\n")
# texto = input("Digite uma frase para acrescentar ao arquivo:\n")
# #arquivo = open('arq01.txt','a')
# arquivo.write(texto + "\n")
# print("Operação concluída no arquivo " + arquivo.name + " usando o modo de acesso " + arquivo.mode)
# arquivo.close()

# print("\nTexto alterado:")
# arquivo = open("Questoes/teste", "r")
# for linha in arquivo:
#     linha = linha.rstrip()
#     print (linha)
# arquivo.close()


# lista = []
# lista2 = []
# listao = []
# for j in range(1):
#     for i in range(7):
#         teste = arquivoConsulta.readline()
#         lista.append(teste)
#     listao.append(lista)

#     for i in range(7):
#         teste2 = arquivoConsulta.readline()
#         lista2.append(teste2)
#     listinha = [lista, lista2]
#     listao.append(listinha)





# arquivoConsulta.close()
# for i in range(len(listao)):
#     print(len(listao))
#     print(listao[i][1])


# for i in range(len(lista)):
#     print(len(lista))
#     questao = lista[i]
#     print(questao)

# print(questao)

# arquivoConsulta = open("Questoes/teste", "a")
# for i in range(len(lista)):
#     if("linha 3" in lista[i]):
#         varivael = "\nEssa linha deve ser adicionada!"
#         print(varivael)
#         arquivoConsulta.seek(i)
#         arquivoConsulta.write(varivael)
# arquivoConsulta.close()

# arquivoAlterar = open("Questoes/teste", "a")
# print("Informe enunciado: ")
# enunciado = input("")
# print("Informe as alternativas: ")
# a = input("A) ")
# b = input("B) ")
# c = input("C) ")
# d = input("D) ")
# resposta = input("Alternativa correta ")
# separador = "\n"
# enunciado = "\n" + enunciado
# a = "\nA) " + a
# b = "\nB) " + b
# c = "\nC) " + c
# d = "\nD) " + d
# resposta = "\n" + resposta.upper()

# arquivoAlterar.write(separador)
# arquivoAlterar.write(enunciado)
# arquivoAlterar.write(a)
# arquivoAlterar.write(b)
# arquivoAlterar.write(c)
# arquivoAlterar.write(d)
# arquivoAlterar.write(resposta)
# arquivoAlterar.close()




# Este é apenas um arquivo teste

# vamos tenter ler essas linhas 
# linha 1
# linha 2
# linha 3

# e essas linhas devem ser excluidas
# excluidas 1
# excluidas 2
# excluidas 3

# a partir daqui vamos alterar
# alterar 1
# alterar 2
# alterar 3

# Qual a máquina de calcular?
# A) abaco
# B) calculadora
# C) monitor
# D) teclado
# o que é um abaco
# A) maquina
# B) de
# C) fazer
# D) calculo
# a
# qunado sai o auxilio
# A) amanha
# B) deoius
# C) final do mes
# D) nunca
# D

# quanto vale pi?
# A) 3.14
# B) 3.15
# C) 3.16
# D) 0.0
# A
