#Para desenvolver o jogo da forca em Python, você pode seguir os seguintes passos:

#Import
import random
from os import system, name

#funcao para limpar a tela a cada execucao
def limpa_tela() :

	#Windows
	if name == 'nt':
		_=system('cls')

	#Mac ou Linux
	else:
		_=system('clear')

#funcao que desenha a forca na tela
def desenho_forca(n_tentativas) :

	#lista de desenhos da forca
	desenho = [	#tentativa 1
				"""
                 ----------
                 |        |
                 |        
                 |		 
                 |        
                 |       
                 _
				""",
				#tentativa 2
				"""
                 ----------
                 |        |
                 |        0
                 |        |	
                 |        |
                 |       
                 _
				""",

				#tentativa 3
				"""
                 ----------
                 |        |
                 |        0
                 |       \\|
                 |        |
                 |      
                 _
				""",
				#tentativa 4
				"""
                 ----------
                 |        |
                 |        0
                 |       \\|/	
                 |        |
                 |       
                 _
				""",
				
				#tentativa 5
				"""
                 ----------
                 |        |
                 |        0
                 |       \\|/	
                 |        |
                 |       /
                 _
				""",
				#tentativa 6
				"""
                 ----------
                 |        |
                 |        0
                 |       \\|/	
                 |        |
                 |       / \\
                 _
				"""
	        ]
	return desenho[n_tentativas]


def game():

	limpa_tela()

	print("\nBem-vindo(a) ao jogo da forca!")
	print("Adivinhe a palavra abaixo:\n")


	#1- Definir a lista de palavras possíveis
	lista_palavras = ["banana","abacate","uva","morango","laranja", "caju"]

	#2- Escolher uma palavra aleatória da lista
	palavra = random.choice(lista_palavras)

	#3- Criar uma lista vazia para armazenar as letras adivinhadas
	letras_descobertas = ["_" for letra in palavra]

	#4- Definir o número máximo de tentativas permitidas e lista com tentativas
	chances = 6
	letras_erradas = []

	#5- Enquanto o número de tentativas não atingir o limite máximo:
	n_tentativas = 0
	while n_tentativas < 6:

		#Print
		#a. Mostrar a palavra como uma série de underscores, com as letras adivinhadas preenchidas nos espaços corretos
		print("".join(letras_descobertas))
		#print("\nChances restantes:", (chances - n_tentativas))
		print(desenho_forca(n_tentativas))
		print("Letras erradas:"," ".join(letras_erradas))

		# Tentativa
		#b. Pedir ao jogador que adivinhe uma letra
		tentativa = input("\nDigite uma letra: ").lower()

		# Checagem da tentativa
		#c. Verificar se a letra adivinhada está na palavra
		if tentativa in palavra:
			index = 0

			for letra in palavra:

				#d. Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra
				if tentativa == letra:
					letras_descobertas[index] = letra
				index +=1

		#e. Se a letra adivinhada não está na palavra, reduzir o número de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [número de tentativas restantes]"
		else:
			n_tentativas += 1
			letras_erradas.append(tentativa)

		# Checando se o usuario acertou a palavra
		#f. Verificar se todas as letras da palavra foram adivinhadas
		#g. Se todas as letras foram adivinhadas, exibir a mensagem "Você venceu!"
		if "_" not in letras_descobertas:
			print("\nVoce venceu, a palavra era: ", palavra)
			break
	
	#Checando se nao acertou a palavra		
	#h. Se o número de tentativas restantes chegar a zero, exibir a mensagem "Você perdeu. A palavra era [palavra escolhida]" e encerrar o jogo.
	if "_" in letras_descobertas:
		print("\nVoce perdeu, a palavra era :", palavra)

if __name__ == "__main__":
	game()
	print("\nParabens. Voce esta aprendendo programacao em Python com a DSA. :)\n")
		










