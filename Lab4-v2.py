# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman():

	# Método Construtor
     def __init__(self):
          # Board (tabuleiro)
          self.board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']
          self.arquivo = open("C:\\PythonDSA\\Cap07\\Projetos_DSA\\palavras_jogo_forca.csv", "r", encoding="utf-8-sig")
          self.conteudo = self.arquivo.read()
          self.lista_palavras = self.conteudo.split()
          self.palavra = random.choice(self.lista_palavras)
          self.letras_descobertas = ["_" for letra in self.palavra]
          self.chances = 6
          self.letras_erradas = []
          self.n_tentativas = 0   
          self.victory = False 
          print("Construtor sucesso")

	# Método para adivinhar a letra
     def guessLetter(self, tentativa):
          # Checagem da tentativa
          #c. Verificar se a letra adivinhada está na palavra
          if tentativa in self.palavra:
               index = 0

               for letra in self.palavra:

                    #d. Se a letra adivinhada está na palavra, adicionar a letra à lista de letras adivinhadas e atualizar a exibição da palavra
                    if tentativa == letra:
                         self.letras_descobertas[index] = letra
                    index +=1

          #e. Se a letra adivinhada não está na palavra, reduzir o número de tentativas restantes e exibir a mensagem "Letra incorreta. Tentativas restantes: [número de tentativas restantes]"
          else:
               self.n_tentativas += 1
               self.letras_erradas.append(tentativa)

	# Método para verificar se o jogo terminou
     def checkEndGame(self, foundLetters):
          if "_" in foundLetters:
               print("\nVoce perdeu, a palavra era: ", self.palavra)
     
		
	# Método para verificar se o jogador venceu
     def checkWiner(self, foundLetters):
          if "_" not in foundLetters:
               print("\nVoce venceu, a palavra era: ", self.palavra)
               self.victory = True
		
	# Método para não mostrar a letra no board
     def dontShowLetter():
          pass
		
	# Método para checar o status do game e imprimir o board na tela
     def showDisplay(self, hangmanDraw, foundLetters, wrongLetters) :

          print(self.board[hangmanDraw])
          print("Letras descobertas: ","".join(foundLetters))
          print("\n")
          print("Letras erradas: "," ".join(wrongLetters))

def limpa_tela() :

     #Windows
     if name == 'nt':
          _=system('cls')

     #Mac ou Linux
     else:
          _=system('clear')



def game ():

     limpa_tela()

     jogo = Hangman()
     print(jogo.palavra)

     while jogo.n_tentativas < 6 and jogo.victory == False:

          tentativa = input("\nDigite uma letra: ").lower()

          jogo.guessLetter(tentativa)
          jogo.showDisplay(jogo.n_tentativas, jogo.letras_descobertas, jogo.letras_erradas)
          jogo.checkWiner(jogo.letras_descobertas)
          
     jogo.checkEndGame(jogo.letras_descobertas)


if __name__ == "__main__":
     game()
     print("\nParabens. Voce esta aprendendo programacao em Python com a DSA. :)\n")
     