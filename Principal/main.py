#PACC - Programa de Avaliação do Conhecimento em Computação 
import funcoes, TOM, time

funcoes.cabecalho()

TOM.boasVindas()
time.sleep(2)
TOM.depoisDasBoasVindas()
time.sleep(2)
TOM.apresentacao()
time.sleep(2)
nome = input("Me diga o seu nome: ")
time.sleep(2)
TOM.iniciarJogo(nome)
time.sleep(2)
TOM.jogadorouadmin(nome)

funcoes.menu(nome)

