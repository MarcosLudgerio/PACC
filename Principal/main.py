#PACC - Programa de Avaliação do Conhecimento em Computação 
import funcoes, nivelFacil, nivelMedio, nivelDificil

#Função que exibe o cabeçalho
#funcoes.cabecalho()

#nome = "Marcos"

#Função que exibe as opções de níveis
dificuldade = funcoes.Dificuldade().lower()

print("dificuldade", dificuldade)
if(dificuldade == "facil"):
    nivelFacil.exibirQuestões()
elif(dificuldade == "medio"):
    nivelMedio.exibirQuestões()
else:
    nivelDificil.exibirQuestões()
