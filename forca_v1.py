# Jogo da Forca

import random
import os

# Tabuleiro
board = ['''
>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+----+ 
|    |
|
|
|
|
=========''', """
>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+----+ 
|    |
|    O
|
|
|
=========
""", """
>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+----+ 
|    |
|    O
|    |
|
|
=========
""", """
>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+----+ 
|    |
|    O
|   /|
|
|
=========
""", """
>>>>>>>>>>Jogo da Forca<<<<<<<<<<

+----+ 
|    |
|    O
|   /|\ 
|
|
=========
""", """
>>>>>>>>>>Jogo da Forca<<<<<<<<<<
 
+----+ 
|    |
|    O
|   /|\ 
|   /
|
=========
""", """
>>>>>>>>>>Jogo da Forca<<<<<<<<<<
 
+----+ 
|    |
|    O
|   /|\ 
|   / \ 
|
=========
"""]


class Hangman:


    # Método Construtor
    def __init__(self, word):
        self.word = word  # Entrada randômica
        self.wrong_letters = []  # lista vazia para armazenar letras erradas
        self.right_letters = []  # lista vazia para armazenar letras corretas
        self.hided = []  # Atribui underline para cara caracter da palavra
        self.screen = board  # Variável que atualiza o bord
        self.i = 0  # Variável para atualizar o board quando o jogador errar
        self.check = False  # Variável para checar se alguma das condições para encerrar o jogo foi atingida

    # Método para advinhar a palavra
    def guess(self, letter):
        if letter.islower():
            if letter in self.word:
                if letter not in self.right_letters:
                    self.right_letters.append(letter)
                for i in self.word:
                    if letter == i:
                        lista = list(enumerate(self.word))
                        for j in range(len(lista)):
                            if self.word[j] == letter:
                                self.hided[j] = letter
                    else:
                        continue
            else:
                if letter not in self.wrong_letters:
                    self.wrong_letters.append(letter)
                    self.i += 1
        else:  # loop para evitar letras maiúsculas
            while letter.isupper():
                letter = input("CAPSLOCK ligado. Desligue e digite novamente a letra: ")
                if letter.islower():
                    if letter in self.word:
                        if letter not in self.right_letters:
                            self.right_letters.append(letter)
                        for i in self.word:
                            if letter == i:
                                lista = list(enumerate(self.word))
                                for j in range(len(lista)):
                                    if self.word[j] == letter:
                                        self.hided[j] = letter
                            else:
                                continue
                    else:
                        if letter not in self.wrong_letters:
                            self.wrong_letters.append(letter)
                            self.i += 1

    # Verifica se o homem foi enforcado
    def hangman_over(self):
        if self.i == 6:
            Hangman.print_game_status(self)
            print("Game Over!")
            self.check = True

    # Verifica se o jogador completou a palavra
    def hangman_won(self):
        if self.hided.count('_ ') == 0:
            Hangman.print_game_status(self)
            print("Parabéns, você acertou!")
            self.check = True

    # Exibe o status
    def print_game_status(self):
        os.system('cls')
        print(self.screen[self.i])
        print('Palavra: ',*self.hided, sep='')
        print('Letras certas: ', *self.right_letters, sep=' ')
        print('Letras erradas:', *self.wrong_letters, sep=' ')

    # Cria uma lista com underlines
    def hide_word(self):
        for i in range(len(self.word)):
            self.hided.append('_ ')


# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip()


# Função Main - Execução do código
def main():
    game = Hangman(rand_word())  # Objeto
    game.hide_word()  # Chama o método hide_word()

    while not game.check:
        game.print_game_status()  # Chama o método print_game_status()
        game.guess(input('Digite uma letra: '))  # Chama o método guess() e recebe o input do usuário
        game.hangman_won()  # Chama o método hangman_won()
        game.hangman_over()  # Chama o método hangman_over

# Executa o programa
if __name__ == "__main__":
	main()
