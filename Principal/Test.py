# File created in 2022 for test if the questions is fine

nivel = "Principal\Facil.txt"

arquivoCompleto = []

contCertas = 0

contErradas = 0

arquivo2 = open(nivel, "r")


lista = arquivo2.readlines()

arquivo2.close()
quantQuestoes = 0

for i in range(len(lista) - 1):
    #Sempre que encontrar uma linha vazia e a próxima com conteudo quer dizer que uma questão acabou, então ele conta
    if(lista[i] == "\n") and (lista[i + 1] != "\n"):
        quantQuestoes += 1
