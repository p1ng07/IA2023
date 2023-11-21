import numpy as np
import random

tabuleiro = np.matrix([[" " ," " ," " ," ", " "], 
                       [" " ," " ," " ," ", " "],
                       [" " ," " ," " ," ", " "],
                       [" " ," " ," " ," ", " "],
                       [" " ," " ," " ," ", " "]])

fila = []

pontos = 0

def desenhaTabuleiro():
    print("+---+---+---+---+---+")
    print("|",tabuleiro.item(0,0),"|",tabuleiro.item(0,1),"|",tabuleiro.item(0,2),"|",tabuleiro.item(0,3),"|",tabuleiro.item(0,4),"|")
    print("+---+---+---+---+---+")
    print("|",tabuleiro.item(1,0),"|",tabuleiro.item(1,1),"|",tabuleiro.item(1,2),"|",tabuleiro.item(1,3),"|",tabuleiro.item(1,4),"|")
    print("+---+---+---+---+---+")
    print("|",tabuleiro.item(2,0),"|",tabuleiro.item(2,1),"|",tabuleiro.item(2,2),"|",tabuleiro.item(2,3),"|",tabuleiro.item(2,4),"|")
    print("+---+---+---+---+---+")
    print("|",tabuleiro.item(3,0),"|",tabuleiro.item(3,1),"|",tabuleiro.item(3,2),"|",tabuleiro.item(3,3),"|",tabuleiro.item(3,4),"|")
    print("+---+---+---+---+---+")
    print("|",tabuleiro.item(4,0),"|",tabuleiro.item(4,1),"|",tabuleiro.item(4,2),"|",tabuleiro.item(4,3),"|",tabuleiro.item(4,4),"|")
    print("+---+---+---+---+---+")
    print("Next:", fila[0] if len(fila) > 0 else " ", "\nFila : ",fila)


def verificaMenos(x, y):
    global pontos
    if(tabuleiro.item(x,y) == "-" and y < 4):
        if(tabuleiro.item(x, y+1) == "-"):
            if(y+2 <= 4 and tabuleiro.item(x,y+2) == "-"):
                pontos = pontos + 8 #pow(2, 2) 
                tabuleiro.itemset((x,y)," ")
                tabuleiro.itemset((x,y+1)," ")
                tabuleiro.itemset((x,y+2)," ")
            else:
                pontos = pontos + 4 #pow(2, 3) 
                tabuleiro.itemset((x,y)," ")
                tabuleiro.itemset((x,y+1)," ")
        
def verificaBola(x,y):
    global pontos

    # Verificar Bola 5x5
    if(tabuleiro.item(x,y) == "O" and x == 0 and y == 0):
        if(tabuleiro.item(x+1,y) == "O" and
           tabuleiro.item(x+2,y) == "O" and 
           tabuleiro.item(x+3,y) == "O" and 
           tabuleiro.item(x+4,y) == "O" and 
           tabuleiro.item(x,y+1) == "O" and 
           tabuleiro.item(x,y+2) == "O" and 
           tabuleiro.item(x,y+3) == "O" and 
           tabuleiro.item(x+4,y+1) == "O" and 
           tabuleiro.item(x+4,y+2) == "O" and 
           tabuleiro.item(x+4,y+3) == "O" and 
           tabuleiro.item(x,y+4) == "O" and 
           tabuleiro.item(x+1,y+4) == "O" and 
           tabuleiro.item(x+2,y+4) == "O" and 
           tabuleiro.item(x+3,y+4) == "O" and 
           tabuleiro.item(x+4,y+4) == "O"):
            
            pontos += pow(2,16)

            # Apagar peças
            tabuleiro.itemset((x,y), " ") 
            tabuleiro.itemset((x+1,y), " ") 
            tabuleiro.itemset((x+2,y), " ")  
            tabuleiro.itemset((x+3,y), " ")  
            tabuleiro.itemset((x+4,y), " ")  
            tabuleiro.itemset((x,y+1), " ")  
            tabuleiro.itemset((x,y+2), " ")  
            tabuleiro.itemset((x,y+3), " ")  
            tabuleiro.itemset((x+4,y+1), " ")  
            tabuleiro.itemset((x+4,y+2), " ")  
            tabuleiro.itemset((x+4,y+3), " ")  
            tabuleiro.itemset((x,y+4), " ")  
            tabuleiro.itemset((x+1,y+4), " ")  
            tabuleiro.itemset((x+2,y+4), " ")  
            tabuleiro.itemset((x+3,y+4), " ")  
            tabuleiro.itemset((x+4,y+4), " ")

    # bola 4x4
    if(tabuleiro.item(x,y) == "O" and x < 2 and y < 2):
            if(tabuleiro.item(x+1,y) == "O" and
            tabuleiro.item(x+2,y) == "O" and 
            tabuleiro.item(x+3,y) == "O" and 
            tabuleiro.item(x,y+1) == "O" and 
            tabuleiro.item(x,y+2) == "O" and 
            tabuleiro.item(x,y+3) == "O" and 
            tabuleiro.item(x+3,y+1) == "O" and 
            tabuleiro.item(x+3,y+2) == "O" and 
            tabuleiro.item(x+3,y+3) == "O" and 
            tabuleiro.item(x,y+3) == "O" and 
            tabuleiro.item(x+1,y+3) == "O" and 
            tabuleiro.item(x+2,y+3) == "O" and 
            tabuleiro.item(x+3,y+3) == "O"): 
                
                pontos += pow(2,12)

                # Apagar peças
                tabuleiro.itemset((x,y), " ") 
                tabuleiro.itemset((x+1,y), " ") 
                tabuleiro.itemset((x+2,y), " ")  
                tabuleiro.itemset((x+3,y), " ")  
                tabuleiro.itemset((x,y+1), " ")  
                tabuleiro.itemset((x,y+2), " ")  
                tabuleiro.itemset((x,y+3), " ")  
                tabuleiro.itemset((x+3,y+1), " ")  
                tabuleiro.itemset((x+3,y+2), " ")  
                tabuleiro.itemset((x+3,y+3), " ")  
                tabuleiro.itemset((x,y+3), " ")  
                tabuleiro.itemset((x+1,y+3), " ")  
                tabuleiro.itemset((x+2,y+3), " ")  
                tabuleiro.itemset((x+3,y+3), " ")  

    # Bola 3x3
    if(tabuleiro.item(x,y) == "O" and x < 3 and y < 3):
        if(tabuleiro.item(x+1,y) == "O" and
            tabuleiro.item(x+2,y) == "O" and 
            tabuleiro.item(x,y+1) == "O" and 
            tabuleiro.item(x,y+2) == "O" and 
            tabuleiro.item(x+2,y+1) == "O" and 
            tabuleiro.item(x+2,y+2) == "O" and 
            tabuleiro.item(x+1,y+2) == "O"): 
                
                pontos += pow(2,8)

                # Apagar peças
                tabuleiro.itemset((x,y), " ") 
                tabuleiro.itemset((x+1,y), " ") 
                tabuleiro.itemset((x+2,y), " ")  
                tabuleiro.itemset((x,y+1), " ")  
                tabuleiro.itemset((x,y+2), " ")  
                tabuleiro.itemset((x+2,y+1), " ")  
                tabuleiro.itemset((x+2,y+2), " ")  
                tabuleiro.itemset((x+1,y+2), " ")
    # Bola 2x2
    if(tabuleiro.item(x,y) == "O" and x < 4 and y < 4):
        if(tabuleiro.item(x+1,y) == "O" and
            tabuleiro.item(x,y+1) == "O" and 
            tabuleiro.item(x+1,y+1) == "O"):
                
                pontos += pow(2,4)

                # Apagar peças
                tabuleiro.itemset((x,y), " ") 
                tabuleiro.itemset((x+1,y), " ") 
                tabuleiro.itemset((x+1,y+1), " ")  
                tabuleiro.itemset((x,y+1), " ")  

def verificaMais(x, y):
    global pontos

    # Mais 3x3
    if(tabuleiro.item(x,y) == "+" and x != 0 and x!= 4 and  y<3 ):
        if(tabuleiro.item(x,y+1) == "+" and
            tabuleiro.item(x,y+2) == "+" and 
            tabuleiro.item(x-1,y+1) == "+" and 
            tabuleiro.item(x+1,y+1) == "+" ): 
            pontos += pow(2,5)
            tabuleiro.itemset((x,y), " ") 
            tabuleiro.itemset((x,y+1), " ") 
            tabuleiro.itemset((x,y+2), " ")  
            tabuleiro.itemset((x-1,y+1), " ")  
            tabuleiro.itemset((x+1,y+1), " ")  

def verificaMaisGrande():
     global pontos

     # Mais 5x5
     if(tabuleiro.item(0,2) == "+" and
        tabuleiro.item(1,2) == "+" and
        tabuleiro.item(2,2) == "+" and
        tabuleiro.item(3,2) == "+" and
        tabuleiro.item(4,2) == "+" and
        tabuleiro.item(2,0) == "+" and
        tabuleiro.item(2,1) == "+" and
        tabuleiro.item(2,3) == "+" and
        tabuleiro.item(2,4) == "+"):
          pontos += pow(2,9)
          tabuleiro.itemset((0,2)," ")
          tabuleiro.itemset((1,2)," ")
          tabuleiro.itemset((2,2)," ")
          tabuleiro.itemset((3,2)," ")
          tabuleiro.itemset((4,2)," ")
          tabuleiro.itemset((2,0)," ")
          tabuleiro.itemset((2,1)," ")
          tabuleiro.itemset((2,3)," ")
          tabuleiro.itemset((2,4)," ")

def verificaX(x, y):
    global pontos

    # verificar x 9 peças 5x5
    if(tabuleiro.item(x,y) == "x" and y == 0 and x == 0):
        if(tabuleiro.item(x+1,y+1) == "x" and
           tabuleiro.item(x+2, y+2) == "x" and 
           tabuleiro.item(x+3,y+3) == "x" and
           tabuleiro.item(x+4, y+4)=="x" and
           tabuleiro.item(x, y+4) == "x" and
           tabuleiro.item(x+4, y) == "x" and
           tabuleiro.item(x+1, y+3) == "x" and
           tabuleiro.item(x+3, y+1) == "x"):
            pontos = pontos + pow(2,9) 
            tabuleiro.itemset((x,y)," ")
            tabuleiro.itemset((x+1,y+1)," ")
            tabuleiro.itemset((x+2, y+2) ," ")
            tabuleiro.itemset((x+3,y+3)," ")
            tabuleiro.itemset((x+4, y+4)," ")
            tabuleiro.itemset((x, y+4)," ")
            tabuleiro.itemset((x+4, y)," ")
            tabuleiro.itemset((x+1, y+3)," ")
            tabuleiro.itemset((x+3, y+1)," ")

    # verificar x 5 peças 3x3
    if(tabuleiro.item(x,y) == "x" and y < 3 and x < 3): 
        if(tabuleiro.item(x, y+2) == "x" and #
           tabuleiro.item(x+2,y) == "x" and
           tabuleiro.item(x+1, y+1)=="x" and
           tabuleiro.item(x+2, y+2) == "x"):
                pontos = pontos + pow(2, 5) 
                tabuleiro.itemset((x,y)," ")
                tabuleiro.itemset((x,y+2)," ")
                tabuleiro.itemset((x+1,y+1)," ")
                tabuleiro.itemset((x+2,y+2)," ")
                tabuleiro.itemset((x+2,y)," ")

def verificaPontuacao():
    verificaMaisGrande()
    for i in range(5):
        for j in range(5):
            verificaMenos(i,j)
            verificaX(i,j)
            verificaBola(i,j)
            verificaMais(i,j)

def insereSimbulo( x, y):
    global fila
    if(tabuleiro.item(x,y)==" "):
        if(len(fila) > 0):
            tabuleiro.itemset((x,y),fila[0])
            fila.pop(0)


def geraFila():
    global fila
    
    for x in range(20):
        ran = random.randint(0,3)
        if(ran == 0):
            fila.append("O")
        elif(ran == 1):
            fila.append("x")
        elif(ran == 2):
            fila.append("+")
        else:
            fila.append("-")
                

geraFila()
while(1):
    print("\n\n\n\n\n\n")
    print("Pontuação: ",pontos)
    desenhaTabuleiro()
    print("Escolha a posição:")
    n = input()
    pos1 = int(n)%5
    pos2 = int(n) / 5
    insereSimbulo(int(pos2),int(pos1))
    verificaPontuacao()
