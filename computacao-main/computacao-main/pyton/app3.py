#ptthon
# jogo da velha (Tic Tac Toe) em Python

# Tabuleiro representado por uma lista de 9 posições (inicialmente vazias)
board = [''for _ in range(9)]

def print_board():
    """"
Exibe o tabuleiro atual formatado com as marcações dos jogadores formato:

| X | 0 | X |
| 0 | X | 0 |
| X | 0 | X |
    """
# Cria cada linha do tabuleiro usando formatação de string
row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

#Exibe o tabuleiro completo
print()
print(row1)
print(row2)
print(row3)
print()

def player_move(icon):
    """
Gerencia a jogada de um participante
:para icon: 'X' ou 'O' - simbolo do jogador atual 
"""

# Determina o numero do jogador baseado no  simbolo
if icon == 'X':
    number = 1
elif icon == 'o':
    number = 2

print("sua vez, jogador {}".format(number))

# Loop para entrada valida dad jogada
while True:
    try:
        #Converter a entrada para numero e ajusta para indice 0-8 choice = int(input("digite sua jogada (1-9):")) -1

        # Valida se a posicao esta disponivel
        if board[choice] == ' ':
            board[choice] = icon
        break
else:
    print("\nEntrada invalida! Digite um numero entre 1 e 9.")

def is_victory(icon):
    """  
    Verifica se o jogador atual venceu
    :param icon: 'X' ou 'O' - simbolo a ser verificado
    :return: True se houver vitoria, false cao contrario
    """
    # Verifica todas as combinaçoes vencedoras posiveis return (
        # Vitorias horizontais
(board[0]) == icon and board[1] == icon and board[2] == icon) or
(board[2]) == icon and board[4] == icon and board[6]