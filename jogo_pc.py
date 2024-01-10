from Jogo import Tabuleiro
from JogoHeuristica import *

tabuleiro.geraFila()

while(tabuleiro.getFila() != []):
    print("Pontos:", tabuleiro.pontos)
    tabuleiro.print()

    input()
    pos = heuristica_fila9(tabuleiro)
    # pos = heuristica_pecaGrande(tabuleiro)
    # pos = heristica_gulosa(tabuleiro)

    pos1 = int(pos)%5 #x
    pos2 = int(pos)/5 #y
    while (False == tabuleiro.posicaoValida(int(pos1),int(pos2))):
        pos = heuristica_fila9(tabuleiro)
        # pos = heuristica_pecaGrande(tabuleiro)
        # pos = heristica_gulosa(tabuleiro)

        pos1 = int(pos)%5 #x
        pos2 = int(pos)/5 #y

    tabuleiro.insereSimbolo(int(pos1),int(pos2))
    tabuleiro.atualizaPontuacao()

print("Pontos:", tabuleiro.pontos)
tabuleiro.print()
