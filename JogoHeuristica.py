#!/usr/bin/env pybricks-micropython
import random
import time
from Jogo import Tabuleiro

tabuleiro = Tabuleiro()

tabuleiroHeuristica = [" "]*25
pecaX = 0
pecaMenos = 0
pecaMais = 0
pecaBola = 0
tamanhoTabuleiro = 25
arrayX = []
arrayMais = []
arrayMenos = []
arrayBola = []


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
def getNumeroPecas(tabuleiro):
    global pecaBola, pecaMais, pecaMenos, pecaX
    pecaX = 0
    pecaMenos = 0
    pecaMais = 0
    pecaBola = 0
    for peca in tabuleiro.getFila():
        if(peca == "x"):
            pecaX += 1
        elif(peca == "-"):
            pecaMenos += 1
        elif(peca == "+"):
            pecaMais += 1
        else:
            pecaBola += 1

def reservaPosicao(pos, peca):
    global tabuleiroHeuristica
    if(tabuleiroHeuristica[pos] == " "):
        tabuleiroHeuristica[pos] = peca

def pecasReserva(tabuleiro):
    global pecaBola, pecaMais, pecaMenos, pecaX, tabuleiroHeuristica

    while(1):
        if(pecaBola >= 16):
            if(
                (tabuleiroHeuristica[0] == " " or tabuleiroHeuristica[0] == "O" )and
                (tabuleiroHeuristica[1] == " " or tabuleiroHeuristica[1] == "O") and
                (tabuleiroHeuristica[2] == " " or tabuleiroHeuristica[2] == "O") and
                (tabuleiroHeuristica[3] == " " or tabuleiroHeuristica[3] == "O") and
                (tabuleiroHeuristica[4] == " " or tabuleiroHeuristica[4] == "O") and
                (tabuleiroHeuristica[5] == " " or tabuleiroHeuristica[5] == "O") and
                (tabuleiroHeuristica[9] == " " or tabuleiroHeuristica[9] == "O") and
                (tabuleiroHeuristica[10] == " " or tabuleiroHeuristica[10] == "O") and
                (tabuleiroHeuristica[14] == " " or tabuleiroHeuristica[14] == "O") and
                (tabuleiroHeuristica[15] == " " or tabuleiroHeuristica[15] == "O") and
                (tabuleiroHeuristica[20] == " " or tabuleiroHeuristica[20] == "O") and
                (tabuleiroHeuristica[21] == " " or tabuleiroHeuristica[21] == "O") and
                (tabuleiroHeuristica[22] == " " or tabuleiroHeuristica[22] == "O") and
                (tabuleiroHeuristica[23] == " " or tabuleiroHeuristica[23] == "O") and
                (tabuleiroHeuristica[24] == " " or tabuleiroHeuristica[24] == "O") 
               ):
                reservaPosicao(0, 0)
                reservaPosicao(1, 0)
                reservaPosicao(2, 0)
                reservaPosicao(3, 0)
                reservaPosicao(4, 0)
                reservaPosicao(5, 0)
                reservaPosicao(9, 0)
                reservaPosicao(10, 0)
                reservaPosicao(14, 0)
                reservaPosicao(15, 0)
                reservaPosicao(20, 0)
                reservaPosicao(21, 0)
                reservaPosicao(22, 0)
                reservaPosicao(23, 0)
                reservaPosicao(24, 0)
                print("Figura de 16 com a peça Bola.")
                pecaBola -= 16
        elif(pecaBola >= 12):
            for i in range(24):
                if(i == 0 or i == 1 or i == 5 or i == 6):
                    if(
                        (tabuleiroHeuristica[i] == " " or tabuleiroHeuristica[i] == "O") and
                        (tabuleiroHeuristica[i+1] == " " or tabuleiroHeuristica[i+1] == "O") and
                        (tabuleiroHeuristica[i+2] == " " or tabuleiroHeuristica[i+2] == "O") and
                        (tabuleiroHeuristica[i+3] == " " or tabuleiroHeuristica[i+3] == "O") and
                        (tabuleiroHeuristica[i+5] == " " or tabuleiroHeuristica[i+5] == "O") and
                        (tabuleiroHeuristica[i+8] == " " or tabuleiroHeuristica[i+8] == "O") and
                        (tabuleiroHeuristica[i+10] == " " or tabuleiroHeuristica[i+10] == "O") and
                        (tabuleiroHeuristica[i+13] == " " or tabuleiroHeuristica[i+13] == "O") and
                        (tabuleiroHeuristica[i+15] == " " or tabuleiroHeuristica[i+15] == "O") and
                        (tabuleiroHeuristica[i+16] == " " or tabuleiroHeuristica[i+16] == "O") and
                        (tabuleiroHeuristica[i+17] == " " or tabuleiroHeuristica[i+17] == "O") and
                        (tabuleiroHeuristica[i+18] == " " or tabuleiroHeuristica[i+18] == "O" )
                    ):
                        reservaPosicao(i,0)
                        reservaPosicao(i+1,0)
                        reservaPosicao(i+2,0)
                        reservaPosicao(i+3,0)
                        reservaPosicao(i+5,0)
                        reservaPosicao(i+8,0)
                        reservaPosicao(i+10,0)
                        reservaPosicao(i+13,0)
                        reservaPosicao(i+15,0)
                        reservaPosicao(i+16,0)
                        reservaPosicao(i+17,0)
                        reservaPosicao(i+18,0)
                        print("Figura de 12 com a peça Bola.")
                        pecaBola -= 12
                        break
        elif(pecaX >= 9):
            if(
                (tabuleiroHeuristica[0] == " " or tabuleiroHeuristica[0] == "x") and
                (tabuleiroHeuristica[4] == " " or tabuleiroHeuristica[4] == "x") and
                (tabuleiroHeuristica[6] == " " or tabuleiroHeuristica[6] == "x") and
                (tabuleiroHeuristica[8] == " " or tabuleiroHeuristica[8] == "x") and
                (tabuleiroHeuristica[12] == " " or tabuleiroHeuristica[12] == "x") and
                (tabuleiroHeuristica[16] == " " or tabuleiroHeuristica[16] == "x") and
                (tabuleiroHeuristica[18] == " " or tabuleiroHeuristica[18] == "x") and
                (tabuleiroHeuristica[20] == " " or tabuleiroHeuristica[20] == "x") and
                (tabuleiroHeuristica[24] == " " or tabuleiroHeuristica[24] == "x") 
               ):
                reservaPosicao(0 ,2)
                reservaPosicao(2 ,2)
                reservaPosicao(6 ,2)
                reservaPosicao(8 ,2)
                reservaPosicao(12 ,2)
                reservaPosicao(16 ,2)
                reservaPosicao(18 ,2)
                reservaPosicao(20 ,2)
                reservaPosicao(24 ,2)
                print("Figura de 9 com a peça X.")
                pecaX -= 9
        elif(pecaMais >= 9):
            if(
                (tabuleiroHeuristica[0] == " " or tabuleiroHeuristica[0] == "+") and
                (tabuleiroHeuristica[4] == " " or tabuleiroHeuristica[4] == "+") and
                (tabuleiroHeuristica[6] == " " or tabuleiroHeuristica[6] == "+") and
                (tabuleiroHeuristica[8] == " " or tabuleiroHeuristica[8] == "+") and
                (tabuleiroHeuristica[12] == " " or tabuleiroHeuristica[12] == "+") and
                (tabuleiroHeuristica[16] == " " or tabuleiroHeuristica[16] == "+") and
                (tabuleiroHeuristica[18] == " " or tabuleiroHeuristica[18] == "+") and
                (tabuleiroHeuristica[20] == " " or tabuleiroHeuristica[20] == "+") and
                (tabuleiroHeuristica[24] == " " or tabuleiroHeuristica[24] == "+") 
               ):
                reservaPosicao(0 ,1)
                reservaPosicao(2 ,1)
                reservaPosicao(6 ,1)
                reservaPosicao(8 ,1)
                reservaPosicao(12 ,1)
                reservaPosicao(16 ,1)
                reservaPosicao(18 ,1)
                reservaPosicao(20 ,1)
                reservaPosicao(24 ,1)
                print("Figura de 9 com a peça Mais.")
                pecaMais -= 9
        elif(pecaBola >= 8):
            for i in range(24):
                if( (i >= 0 and i<=2) or (i >= 5 and i<=7) or (i>=10 and i<=12)):
                    if(
                         (tabuleiroHeuristica[i] == " " or tabuleiroHeuristica[i] == "O") and
                         (tabuleiroHeuristica[i+1] == " " or tabuleiroHeuristica[i+1] == "O") and
                         (tabuleiroHeuristica[i+2] == " " or tabuleiroHeuristica[i+2] == "O") and
                         (tabuleiroHeuristica[i+5] == " " or tabuleiroHeuristica[i+5] == "O") and
                         (tabuleiroHeuristica[i+7] == " " or tabuleiroHeuristica[i+7] == "O") and
                         (tabuleiroHeuristica[i+10] == " " or tabuleiroHeuristica[i+10] == "O") and
                         (tabuleiroHeuristica[i+11] == " " or tabuleiroHeuristica[i+11] == "O") and
                         (tabuleiroHeuristica[i+12] == " " or tabuleiroHeuristica[i+12] == "O") 
                    ):
                        reservaPosicao(i, 0)
                        reservaPosicao(i+1, 0)
                        reservaPosicao(i+2, 0)
                        reservaPosicao(i+5, 0)
                        reservaPosicao(i+7, 0)
                        reservaPosicao(i+10, 0)
                        reservaPosicao(i+11, 0)
                        reservaPosicao(i+12, 0)
                        print("Figura de 8 com a peça Bola.")
                        pecaBola -= 8
                        break
        elif(pecaX >= 5):
            for i in range(24):
                if((i >= 0 and i<=2) or (i >= 5 and i<=7) or (i>=10 and i<=12)):
                    if(
                        (tabuleiroHeuristica[i] == " " or tabuleiroHeuristica[i] == "x") and
                        (tabuleiroHeuristica[i+2] == " " or tabuleiroHeuristica[i+2] == "x") and
                        (tabuleiroHeuristica[i+6] == " " or tabuleiroHeuristica[i+6] == "x") and
                        (tabuleiroHeuristica[i+10] == " " or tabuleiroHeuristica[i+10] == "x") and
                        (tabuleiroHeuristica[i+12] == " " or tabuleiroHeuristica[i+12] == "x") 
                    ):
                        reservaPosicao(i, 2)
                        reservaPosicao(i+2, 2)
                        reservaPosicao(i+6, 2)
                        reservaPosicao(i+10, 2)
                        reservaPosicao(i+12, 2)
                        print("Figura de 5 com a peça X.")
                        pecaX -= 5
                        break
        elif(pecaMais >= 5):
            print("Figura de 5 com a peça Mais.")
            pecaMais -= 5
        elif(pecaBola >= 4):
            print("Figura de 4 com a peça Bola.")
            pecaBola -= 4
        elif(pecaMenos >= 3):
            print("Figura de 3 com a peça Menos.")
            pecaMenos -= 3
        elif(pecaMenos >= 2):
            print("Figura de 2 com a peça Menos.")
            pecaMenos -= 2
        else:
            break

def heuristica_pecaGrande(tabuleiro):
    getNumeroPecas(tabuleiro)
    #pecasReserva(tabuleiro)

    return 0

n = 0;
tabuleiro.geraFila()

while(1):
    print("Pontos: ", tabuleiro.pontos)
    tabuleiro.print()
    heuristica_pecaGrande(tabuleiro)
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
