#!/usr/bin/env pybricks-micropython
import random
import time
from Jogo import Tabuleiro

tabuleiro = Tabuleiro()

# lista que servirá para fazer a reserva de posições para o tabuleiro 
tabuleiroHeuristica = [" "]*25
# contadores para a quantidade de cada peça 
pecaX = 0
pecaMenos = 0
pecaMais = 0
pecaBola = 0
tamanhoTabuleiro = 25

# decide se é para por a próxima peça no início ou fim do tabuleiro relativamente à heurística
por_inicio_da_heuristica = True

# Heurística onde cada peça tem posições pré-determinadas para onde ir  
def heristica_gulosa(tabuleiro):
    # verifica se o 1º elemento na fila é 'X'
    # se sim, verifica sequencialmente cada posição destinada a esta peça e coloca a peça na primeira posição válida encontrada  
    if(tabuleiro.fila[0] == "x"):
        if(tabuleiro.posicaoValida(0,0)):
            return 0
        elif(tabuleiro.posicaoValida(2,0)):
            return 2
        elif(tabuleiro.posicaoValida(1,1)):
            return 6
        elif(tabuleiro.posicaoValida(0,2)):
            return 10
        elif(tabuleiro.posicaoValida(2,2)):
            return 12
    
    # verifica se o 1º elemento na fila é '+'
    # se sim, verifica sequencialmente cada posição destinada a esta peça e coloca a peça na primeira posição válida encontrada 
    if(tabuleiro.fila[0] == "+"):
        if(tabuleiro.posicaoValida(1,2)):
            return 11
        elif(tabuleiro.posicaoValida(0,3)):
            return 15
        elif(tabuleiro.posicaoValida(1,3)):
            return 16
        elif(tabuleiro.posicaoValida(2,3)):
            return 17
        elif(tabuleiro.posicaoValida(1,4)):
            return 21
    
    # verifica se o 1º elemento na fila é 'O'
    # se sim, verifica sequencialmente cada posição destinada a esta peça e coloca a peça na primeira posição válida encontrada 
    if(tabuleiro.fila[0] == "O"):
        if(tabuleiro.posicaoValida(3,0)):
            return 3
        elif(tabuleiro.posicaoValida(4,0)):
            return 4
        elif(tabuleiro.posicaoValida(3,1)):
            return 8
        elif(tabuleiro.posicaoValida(4,1)):
            return 9

    # verifica se o 1º elemento na fila é '-'
    # se sim, verifica sequencialmente cada posição destinada a esta peça e coloca a peça na primeira posição válida encontrada 
    if(tabuleiro.fila[0] == "-"):
        if(tabuleiro.posicaoValida(3,4)):
            return 23
        elif(tabuleiro.posicaoValida(4,4)):
            return 24
        
    return 0

# conta o número de cada tipo de peça na fila e atualiza os contadores 
def getNumeroPecas(fila):
    global pecaBola, pecaMais, pecaMenos, pecaX
    pecaX = 0
    pecaMenos = 0
    pecaMais = 0
    pecaBola = 0
    for peca in fila:
        if(peca == "x"):
            pecaX += 1
        elif(peca == "-"):
            pecaMenos += 1
        elif(peca == "+"):
            pecaMais += 1
        else:
            pecaBola += 1

# Reserva uma posição no tabuleiroHeuristica, se essa estiver vazia
def reservaPosicao(pos, peca):
    global tabuleiroHeuristica, tabuleiro
    if(tabuleiro.tabuleiro[pos] == " "):
        tabuleiroHeuristica[pos] = str(peca)

# Reserva posições especifícas no tabuleiroHeuristica consoante o nº de peças disponíveis
def pecasReserva(tabuleiro):
    global pecaBola, pecaMais, pecaMenos, pecaX, tabuleiroHeuristica

    # se o número de peças do tipo 'O' for maior ou igual a 16 (é possível fazer a maior peça grande com este símbolo) verifica-se se  
    # no tabuleiro real as posições onde seria feita esta peça estão vazias ou já reservadas com essa peça
    # se sim, é feita a reserva no tabuleiroHeuristica nessas posições com o respetivo símbolo
    # caso contrário tenta fazer peças mais pequenas
    if(pecaBola >= 16):
        if(
            (tabuleiro.tabuleiro[0] == " " or tabuleiro.tabuleiro[0] == "O" )and
            (tabuleiro.tabuleiro[1] == " " or tabuleiro.tabuleiro[1] == "O") and
            (tabuleiro.tabuleiro[2] == " " or tabuleiro.tabuleiro[2] == "O") and
            (tabuleiro.tabuleiro[3] == " " or tabuleiro.tabuleiro[3] == "O") and
            (tabuleiro.tabuleiro[4] == " " or tabuleiro.tabuleiro[4] == "O") and
            (tabuleiro.tabuleiro[5] == " " or tabuleiro.tabuleiro[5] == "O") and
            (tabuleiro.tabuleiro[9] == " " or tabuleiro.tabuleiro[9] == "O") and
            (tabuleiro.tabuleiro[10] == " " or tabuleiro.tabuleiro[10] == "O") and
            (tabuleiro.tabuleiro[14] == " " or tabuleiro.tabuleiro[14] == "O") and
            (tabuleiro.tabuleiro[15] == " " or tabuleiro.tabuleiro[15] == "O") and
            (tabuleiro.tabuleiro[20] == " " or tabuleiro.tabuleiro[20] == "O") and
            (tabuleiro.tabuleiro[21] == " " or tabuleiro.tabuleiro[21] == "O") and
            (tabuleiro.tabuleiro[22] == " " or tabuleiro.tabuleiro[22] == "O") and
            (tabuleiro.tabuleiro[23] == " " or tabuleiro.tabuleiro[23] == "O") and
            (tabuleiro.tabuleiro[24] == " " or tabuleiro.tabuleiro[24] == "O") 
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
            return
      
    if(pecaBola >= 12):
        for i in range(24):
            if(i == 0 or i == 1 or i == 5 or i == 6):
                if(
                    (tabuleiro.tabuleiro[i] == " " or tabuleiro.tabuleiro[i] == "O") and
                    (tabuleiro.tabuleiro[i+1] == " " or tabuleiro.tabuleiro[i+1] == "O") and
                    (tabuleiro.tabuleiro[i+2] == " " or tabuleiro.tabuleiro[i+2] == "O") and
                    (tabuleiro.tabuleiro[i+3] == " " or tabuleiro.tabuleiro[i+3] == "O") and
                    (tabuleiro.tabuleiro[i+5] == " " or tabuleiro.tabuleiro[i+5] == "O") and
                    (tabuleiro.tabuleiro[i+8] == " " or tabuleiro.tabuleiro[i+8] == "O") and
                    (tabuleiro.tabuleiro[i+10] == " " or tabuleiro.tabuleiro[i+10] == "O") and
                    (tabuleiro.tabuleiro[i+13] == " " or tabuleiro.tabuleiro[i+13] == "O") and
                    (tabuleiro.tabuleiro[i+15] == " " or tabuleiro.tabuleiro[i+15] == "O") and
                    (tabuleiro.tabuleiro[i+16] == " " or tabuleiro.tabuleiro[i+16] == "O") and
                    (tabuleiro.tabuleiro[i+17] == " " or tabuleiro.tabuleiro[i+17] == "O") and
                    (tabuleiro.tabuleiro[i+18] == " " or tabuleiro.tabuleiro[i+18] == "O" )
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
                    return
    if(pecaX >= 9):
        if(
            (tabuleiro.tabuleiro[0] == " " or tabuleiro.tabuleiro[0] == "x") and
            (tabuleiro.tabuleiro[4] == " " or tabuleiro.tabuleiro[4] == "x") and
            (tabuleiro.tabuleiro[6] == " " or tabuleiro.tabuleiro[6] == "x") and
            (tabuleiro.tabuleiro[8] == " " or tabuleiro.tabuleiro[8] == "x") and
            (tabuleiro.tabuleiro[12] == " " or tabuleiro.tabuleiro[12] == "x") and
            (tabuleiro.tabuleiro[16] == " " or tabuleiro.tabuleiro[16] == "x") and
            (tabuleiro.tabuleiro[18] == " " or tabuleiro.tabuleiro[18] == "x") and
            (tabuleiro.tabuleiro[20] == " " or tabuleiro.tabuleiro[20] == "x") and
            (tabuleiro.tabuleiro[24] == " " or tabuleiro.tabuleiro[24] == "x") 
            ):
            reservaPosicao(0 ,2)
            reservaPosicao(4 ,2)
            reservaPosicao(6 ,2)
            reservaPosicao(8 ,2)
            reservaPosicao(12 ,2)
            reservaPosicao(16 ,2)
            reservaPosicao(18 ,2)
            reservaPosicao(20 ,2)
            reservaPosicao(24 ,2)
            print("Figura de 9 com a peça X.")
            pecaX -= 9
            return
    if(pecaMais >= 9):
        if(
            (tabuleiro.tabuleiro[0] == " " or tabuleiro.tabuleiro[0] == "+") and
            (tabuleiro.tabuleiro[4] == " " or tabuleiro.tabuleiro[4] == "+") and
            (tabuleiro.tabuleiro[6] == " " or tabuleiro.tabuleiro[6] == "+") and
            (tabuleiro.tabuleiro[8] == " " or tabuleiro.tabuleiro[8] == "+") and
            (tabuleiro.tabuleiro[12] == " " or tabuleiro.tabuleiro[12] == "+") and
            (tabuleiro.tabuleiro[16] == " " or tabuleiro.tabuleiro[16] == "+") and
            (tabuleiro.tabuleiro[18] == " " or tabuleiro.tabuleiro[18] == "+") and
            (tabuleiro.tabuleiro[20] == " " or tabuleiro.tabuleiro[20] == "+") and
            (tabuleiro.tabuleiro[24] == " " or tabuleiro.tabuleiro[24] == "+") 
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
            return
    if(pecaBola >= 8):
        for i in range(24):
            if( (i >= 0 and i<=2) or (i >= 5 and i<=7) or (i>=10 and i<=12)):
                if(
                        (tabuleiro.tabuleiro[i] == " " or tabuleiro.tabuleiro[i] == "O") and
                        (tabuleiro.tabuleiro[i+1] == " " or tabuleiro.tabuleiro[i+1] == "O") and
                        (tabuleiro.tabuleiro[i+2] == " " or tabuleiro.tabuleiro[i+2] == "O") and
                        (tabuleiro.tabuleiro[i+5] == " " or tabuleiro.tabuleiro[i+5] == "O") and
                        (tabuleiro.tabuleiro[i+7] == " " or tabuleiro.tabuleiro[i+7] == "O") and
                        (tabuleiro.tabuleiro[i+10] == " " or tabuleiro.tabuleiro[i+10] == "O") and
                        (tabuleiro.tabuleiro[i+11] == " " or tabuleiro.tabuleiro[i+11] == "O") and
                        (tabuleiro.tabuleiro[i+12] == " " or tabuleiro.tabuleiro[i+12] == "O") 
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
                    return
    if(pecaX >= 5):
        for i in range(24):
            if((i >= 0 and i<=2) or (i >= 5 and i<=7) or (i>=10 and i<=12)):
                if(
                    (tabuleiro.tabuleiro[i] == " " or tabuleiro.tabuleiro[i] == "x") and
                    (tabuleiro.tabuleiro[i+2] == " " or tabuleiro.tabuleiro[i+2] == "x") and
                    (tabuleiro.tabuleiro[i+6] == " " or tabuleiro.tabuleiro[i+6] == "x") and
                    (tabuleiro.tabuleiro[i+10] == " " or tabuleiro.tabuleiro[i+10] == "x") and
                    (tabuleiro.tabuleiro[i+12] == " " or tabuleiro.tabuleiro[i+12] == "x") 
                ):
                    reservaPosicao(i, 2)
                    reservaPosicao(i+2, 2)
                    reservaPosicao(i+6, 2)
                    reservaPosicao(i+10, 2)
                    reservaPosicao(i+12, 2)
                    print("Figura de 5 com a peça X.")
                    pecaX -= 5
                    return
    if(pecaMais >= 5):
        for i in range(24):
            if((i>=1 and i<=3) or (i>=6 and i<=8) or (i>= 11 and i<=13)):
                if(
                    (tabuleiro.tabuleiro[i] == " " or tabuleiro.tabuleiro[i] == "+") and
                    (tabuleiro.tabuleiro[i+4] == " " or tabuleiro.tabuleiro[i+4] == "+") and
                    (tabuleiro.tabuleiro[i+5] == " " or tabuleiro.tabuleiro[i+5] == "+") and
                    (tabuleiro.tabuleiro[i+6] == " " or tabuleiro.tabuleiro[i+6] == "+") and
                    (tabuleiro.tabuleiro[i+10] == " " or tabuleiro.tabuleiro[i+10] == "+")
                ):   
                    reservaPosicao(i,1)
                    reservaPosicao(i+4,1)
                    reservaPosicao(i+5,1)
                    reservaPosicao(i+6,1)
                    reservaPosicao(i+10,1)
                    print("Figura de 5 com a peça Mais.")
                    pecaMais -= 5
                    return
    if(pecaBola >= 4):
        for i in range(24):
            if((i>=0 and i<=3) or (i>=5 and i<=8) or (i>= 10 and i<=13) or (i<=15 and i<= 18)):
                if(
                    (tabuleiro.tabuleiro[i] == " " or tabuleiro.tabuleiro[i] == "O") and
                    (tabuleiro.tabuleiro[i+1] == " " or tabuleiro.tabuleiro[i+1] == "O") and
                    (tabuleiro.tabuleiro[i+5] == " " or tabuleiro.tabuleiro[i+5] == "O") and
                    (tabuleiro.tabuleiro[i+6] == " " or tabuleiro.tabuleiro[i+6] == "O") 
                ):
                    reservaPosicao(i,0)
                    reservaPosicao(i+1,0)
                    reservaPosicao(i+5,0)
                    reservaPosicao(i+6,0)
                    print("Figura de 4 com a peça Bola.")
                    pecaBola -= 4
                    return
    if(pecaMenos >= 3):
        for i in range(24):
            if((i>=0 and i<=2) or (i>=5 and i<=7) or (i>=10 and i<=12) or (i>=15 and i<=17) or (i>=20 and i<=22)):
                if(
                    (tabuleiro.tabuleiro[i] == " " or tabuleiro.tabuleiro[i] == "-") and
                    (tabuleiro.tabuleiro[i+1] == " " or tabuleiro.tabuleiro[i+1] == "-")  and
                    (tabuleiro.tabuleiro[i+2] == " " or tabuleiro.tabuleiro[i+2] == "-") 
                    ):
                    reservaPosicao(i, 3)
                    reservaPosicao(i+1, 3)
                    reservaPosicao(i+2, 3)
                    print("Figura de 3 com a peça Menos.")
                    pecaMenos -= 3
                    return
    if(pecaMenos >= 2):
        for i in range(24):
            if((i>=0 and i<=3) or (i>=5 and i<=8) or (i>=10 and i<=13) or (i>=15 and i<=18) or (i>=20 and i<=23)):
                if(
                    (tabuleiro.tabuleiro[i] == " " or tabuleiro.tabuleiro[i] == "-") and
                    (tabuleiro.tabuleiro[i+1] == " " or tabuleiro.tabuleiro[i+1] == "-") 
                    ):
                    reservaPosicao(i, 3)
                    reservaPosicao(i+1, 3)
                    print("Figura de 2 com a peça Menos.")
                    pecaMenos -= 2
                    return
 
def heuristica_fila9(tabuleiro):
  global por_inicio_da_heuristica
  
  # se o jogo ainda não tiver começado, vai buscar os primeiros 9 elementos da fila 
  # e reserva as peças consoante isso
  if tabuleiroHeuristica == [" "] * 25:
    getNumeroPecas(tabuleiro.getFila()[0:9])
    pecasReserva(tabuleiro)

  # Determinar onde colocar a proxima peça
  # Determinar porque reserva procurar
  peca = tabuleiro.fila[0]

  # os valores passados na função 'pecasReserva' são associados ao seu simbolo
  caracteres = {"-": "3", "+": "1", "x": "2", "O": "0"}
  carater_reserva = caracteres.get(peca, None)

  if por_inicio_da_heuristica:
    indices_lista = range(0, 25, 1)
  else:
    indices_lista = range(24, -1, -1)

  # retornar o indice da posição
  for i in indices_lista:
    pos1 = int(i)%5 #x
    pos2 = int(i)/5 #y
    if tabuleiroHeuristica[i] == carater_reserva and tabuleiro.posicaoValida(int(pos1),int(pos2)):
      tabuleiroHeuristica[i] = " "
      print("Peça Sitio encontrado" + str(i))

      # Virar se é para por no inicio ou fim da heuristica
      por_inicio_da_heuristica = not por_inicio_da_heuristica
      return i

  for i in range(25):
    pos1 = int(i)%5 #x
    pos2 = int(i)/5 #y
    if tabuleiro.posicaoValida(int(pos1),int(pos2)) and tabuleiroHeuristica[i] == " ":
      print("Sitio vazio: " + str(i))
      return i

  # retornar -1 em caso do tabuleiro estar cheio
  return -1

def heuristica_pecaGrande(tabuleiro):
  global por_inicio_da_heuristica
  
  # se o jogo ainda não tiver começado, vai buscar os elementos da fila 
  # e reserva as peças consoante isso
  if tabuleiroHeuristica == [" "] * 25:
    getNumeroPecas(tabuleiro.getFila())
    pecasReserva(tabuleiro)

  # Determinar onde colocar a proxima peça
  # Determinar porque reserva procurar
  peca = tabuleiro.fila[0]

  # os valores passados na função 'pecasReserva' são associados ao seu simbolo
  caracteres = {"-": "3", "+": "1", "x": "2", "O": "0"}
  carater_reserva = caracteres.get(peca, None)

  if por_inicio_da_heuristica:
    indices_lista = range(0, 25, 1)
  else:
    indices_lista = range(24, -1, -1)

  # retornar o indice da posição
  for i in indices_lista:
    pos1 = int(i)%5
    pos2 = int(i)/5
    if tabuleiroHeuristica[i] == carater_reserva and tabuleiro.posicaoValida(int(pos1),int(pos2)):
      tabuleiroHeuristica[i] = " "
      print("Peça Sitio encontrado:" + str(i))

      # Virar se é para por no inicio ou fim da heuristica
      por_inicio_da_heuristica = not por_inicio_da_heuristica
      return i

  for i in range(25):
    pos1 = int(i)%5 #x
    pos2 = int(i)/5 #y
    if tabuleiro.posicaoValida(int(pos1),int(pos2)) and tabuleiroHeuristica[i] == " ":
      print("Sitio vazio: " + str(i))
      return i

  # retornar -1 em caso do tabuleiro estar cheio
  n = 0 / 0;
  return -1
