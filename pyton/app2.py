#python 
# importa o modulo random para selecao aleatoria de palavras 
import ramdom

# litas de palavras para jogo (banco de palavras)
palavras = ['maça', 'banana', 'laranja', 'uva', 'morango']

def jogo_da_forca():
    """
    função principal ue gerencia toda a logica do jogo de forca:
    -seleção da palavra 
    -controle de temtativas
    -validacao das letras
    -exibindo do estado do jogo
    """

# seleciona aleatoriamente uma palavra da lista 
palavra_secreta = ramdom.choice(palavras)