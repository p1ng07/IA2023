from Jogo import Tabuleiro
from JogoHeuristica import *

tabuleiro.geraFila()

# corremos este ficheiro para fazer a simulação, sem utilizar o robot

# enquanto a fila não está vazia significa que ainda há peças a serem colocadas no tabuleiro 
while(tabuleiro.getFila() != []):
    print("Pontos:", tabuleiro.pontos)
    tabuleiro.print()

    ##################################################
    
    # Comentamos as heuristicas que não estão a ser usadas
    
    ##################################################
    input()
    # pos = heuristica_fila9(tabuleiro)
    pos = heuristica_pecaGrande(tabuleiro)
    # pos = heristica_gulosa(tabuleiro)

    pos1 = int(pos)%5 #x
    pos2 = int(pos)/5 #y
    while (False == tabuleiro.posicaoValida(int(pos1),int(pos2))):
        ##################################################
        
        # Comentamos as heuristicas que não estão a ser usadas
        
        ##################################################
        # pos = heuristica_fila9(tabuleiro)
        pos = heuristica_pecaGrande(tabuleiro)
        # pos = heristica_gulosa(tabuleiro)

        pos1 = int(pos)%5 #x
        pos2 = int(pos)/5 #y

    # Insere um símbolo na posição (pos1, pos2) do tabuleiro do jogo
    tabuleiro.insereSimbolo(int(pos1),int(pos2))
    tabuleiro.atualizaPontuacao()

# atualiza os pontos após a colocação da peça no tabuleiro
print("Pontos:", tabuleiro.pontos)
# apresenta o desenho do tabuleiro atualizado 
tabuleiro.print()
