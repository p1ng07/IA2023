#!/usr/bin/env pybricks-micropython
import random
import time
from Jogo import Tabuleiro

tabuleiro = Tabuleiro()

def heristica_gulosa(tabuleiro):
    if(tabuleiro.fila[0] == "x"):
        if(tabuleiro.posicaoValida(0,0)):
            return 0
        elif(tabuleiro.posicaoValida(0,2)):
            return 2
        elif(tabuleiro.posicaoValida(1,1)):
            return 6
        elif(tabuleiro.posicaoValida(2,0)):
            return 10
        elif(tabuleiro.posicaoValida(2,2)):
            return 12
        
    if(tabuleiro.fila[0] == "+"):
        if(tabuleiro.posicaoValida(2,1)):
            return 11
        elif(tabuleiro.posicaoValida(3,0)):
            return 15
        elif(tabuleiro.posicaoValida(3,1)):
            return 16
        elif(tabuleiro.posicaoValida(3,2)):
            return 17
        elif(tabuleiro.posicaoValida(4,1)):
            return 21
        
    if(tabuleiro.fila[0] == "O"):
        if(tabuleiro.posicaoValida(0,3)):
            return 3
        elif(tabuleiro.posicaoValida(0,4)):
            return 4
        elif(tabuleiro.posicaoValida(1,3)):
            return 8
        elif(tabuleiro.posicaoValida(1,4)):
            return 9

    if(tabuleiro.fila[0] == "-"):
        if(tabuleiro.posicaoValida(4,3)):
            return 23
        elif(tabuleiro.posicaoValida(4,4)):
            return 24
        
    return 0

def heuristica_maxpontos(tabuleiro):
    return 0

n = 0;
tabuleiro.geraFila()

while(1):
    print("Pontos: ", tabuleiro.pontos)
    tabuleiro.print()
    user_input = input();
    pos = heristica_gulosa(tabuleiro)
    pos1 = int(pos)%5
    pos2 = int(pos)/5
    while (False == tabuleiro.posicaoValida(int(pos2),int(pos1))):
        # pos = random.randint(0,24)
        pos = heristica_gulosa(tabuleiro)
        user_input = input();
        pos1 = int(pos)%5
        pos2 = int(pos)/5

    tabuleiro.insereSimbolo(int(pos2),int(pos1))
    print(pos," x:",int(pos2), " y:", int(pos1))
   
    tabuleiro.atualizaPontuacao()
    n += 1
