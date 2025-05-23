#python 
# importa o modulo random para selecao aleatoria de palavras 
import random

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
palavra_secreta = random.choice(palavras)

    # Lista para armazenar as letras descobertas (inicialmente todas ocultas)
letras_corretas = ['_'] * len(palavra_secreta)

#Lista para registrar letras incorretas digitadas
letras_erradas = []

#define o numero maximo de tentativas permitidas 
tentativas_restantes = 6

# Mensagem inicial do jogo 
print("\nbem-vindo ao jogo da forca!")
print(f"voce tem {tentativas_restantes} tentativas para adivinhar a palavra.\n")

# Loop principal do jogo: continuo enquanto houver tentativas e letras faltando
while tentativas_restantes > 0 and "_" in letras_corretas:
# Exibe o processo atual do jogador
    print(''.join(letras_corretas))

    # Solicita e processa a tentativa do jogador 
    tentativa = input("\nDigite uma letra:").lower() # Converte para minusculo

    # Verifica se a letra esta na palavra secreta if tentativa in palavra_secreta:
    # Atualiza as letras corretas reveladas
    for indice, letra in enumerate(palavra_secreta):
        if letra ==  tentativa:
            letras_corretas[indice] = tentativa
    else:
        # trata letra incorreta
        letras_erradas.append(tentativa) # Registrar a tentativa errada
tentativas_restantes -=1 # Reduz o numero de tentativas

    # Feedback imediato para o jogador 
print(f"\nLetra incorreta! tentativas restantes: {tentativas_restantes}")
if letras_erradas: # So mostrar se houver letras erradas 
    print(f"letras erradas: {', '.join(letras_erradas)}")

# Verificação final do resultado do jogo
if '_' not in letras_corretas:
    # Vitoria: todas as letras foram reveladas 
   print(f"\nParabens! Voce ganhou! A palavra era: {palavra_secreta}")
else:
    # Derrota:acabaram as tentativas 
    print(f"letras erradas: {', '.join(letras_erradas)}")

# Inicia o jogo quando o script e executado 
if __name__=="__main__":
    jogo_da_forca