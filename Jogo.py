import random

class Tabuleiro:
  def __init__(self):
    self.pontos = 0
    self.fila = []
    self.tabuleiro = [" "] * 25

  def getFila(self):
    return self.fila
  
  def item(self,x,y):
    return self.tabuleiro[x + y*5]
    
  def print(self):
    print("+---+---+---+---+---+")
    print("|",self.item(0,0),"|",self.item(0,1),"|",self.item(0,2),"|",self.item(0,3),"|",self.item(0,4),"|")
    print("+---+---+---+---+---+")
    print("|",self.item(1,0),"|",self.item(1,1),"|",self.item(1,2),"|",self.item(1,3),"|",self.item(1,4),"|")
    print("+---+---+---+---+---+")
    print("|",self.item(2,0),"|",self.item(2,1),"|",self.item(2,2),"|",self.item(2,3),"|",self.item(2,4),"|")
    print("+---+---+---+---+---+")
    print("|",self.item(3,0),"|",self.item(3,1),"|",self.item(3,2),"|",self.item(3,3),"|",self.item(3,4),"|")
    print("+---+---+---+---+---+")
    print("|",self.item(4,0),"|",self.item(4,1),"|",self.item(4,2),"|",self.item(4,3),"|",self.item(4,4),"|")
    print("+---+---+---+---+---+")
    print("Next:", self.fila[0] if len(self.fila) > 0 else " ", "\nFila : ",self.fila)

  def itemset(self, x,y, piece: str):
    self.tabuleiro[x + y*5] = piece

  def verificaMenos(self,x, y):
      if(self.item(x,y) == "-" and y < 4):
          if(self.item(x, y+1) == "-"):
              if(y+2 <= 4 and self.item(x,y+2) == "-"):
                self.pontos += 8 #pow(2, 2) 
                self.itemset(x,y," ")
                self.itemset(x,y+1," ")
                self.itemset(x,y+2," ")
              else:
                self.pontos += 4 #pow(2, 3) 
                self.itemset(x,y," ")
                self.itemset(x,y+1," ")
              
  def verificaBola(self,x,y):
      # Verificar Bola 5x5
      if(self.item(x,y) == "O" and x == 0 and y == 0):
          if(self.item(x+1,y) == "O" and
            self.item(x+2,y) == "O" and 
            self.item(x+3,y) == "O" and 
            self.item(x+4,y) == "O" and 
            self.item(x,y+1) == "O" and 
            self.item(x,y+2) == "O" and 
            self.item(x,y+3) == "O" and 
            self.item(x+4,y+1) == "O" and 
            self.item(x+4,y+2) == "O" and 
            self.item(x+4,y+3) == "O" and 
            self.item(x,y+4) == "O" and 
            self.item(x+1,y+4) == "O" and 
            self.item(x+2,y+4) == "O" and 
            self.item(x+3,y+4) == "O" and 
            self.item(x+4,y+4) == "O"):

              self.pontos += pow(2,16)

              # Apagar peças
              self.itemset(x,y, " ") 
              self.itemset(x+1,y, " ") 
              self.itemset(x+2,y, " ")  
              self.itemset(x+3,y, " ")  
              self.itemset(x+4,y, " ")  
              self.itemset(x,y+1, " ")  
              self.itemset(x,y+2, " ")  
              self.itemset(x,y+3, " ")  
              self.itemset(x+4,y+1, " ")  
              self.itemset(x+4,y+2, " ")  
              self.itemset(x+4,y+3, " ")  
              self.itemset(x,y+4, " ")  
              self.itemset(x+1,y+4, " ")  
              self.itemset(x+2,y+4, " ")  
              self.itemset(x+3,y+4, " ")  
              self.itemset(x+4,y+4, " ")

      # bola 4x4
      if(self.item(x,y) == "O" and x < 2 and y < 2):
              if(self.item(x+1,y) == "O" and
                self.item(x+2,y) == "O" and 
                self.item(x+3,y) == "O" and 
                self.item(x,y+1) == "O" and 
                self.item(x,y+2) == "O" and 
                self.item(x,y+3) == "O" and 
                self.item(x+3,y+1) == "O" and 
                self.item(x+3,y+2) == "O" and 
                self.item(x+3,y+3) == "O" and 
                self.item(x,y+3) == "O" and 
                self.item(x+1,y+3) == "O" and 
                self.item(x+2,y+3) == "O" and 
                self.item(x+3,y+3) == "O"): 

                  self.pontos += pow(2,12)

                  # Apagar peças
                  self.itemset(x,y, " ") 
                  self.itemset(x+1,y, " ") 
                  self.itemset(x+2,y, " ")  
                  self.itemset(x+3,y, " ")  
                  self.itemset(x,y+1, " ")  
                  self.itemset(x,y+2, " ")  
                  self.itemset(x,y+3, " ")  
                  self.itemset(x+3,y+1, " ")  
                  self.itemset(x+3,y+2, " ")  
                  self.itemset(x+3,y+3, " ")  
                  self.itemset(x,y+3, " ")  
                  self.itemset(x+1,y+3, " ")  
                  self.itemset(x+2,y+3, " ")  
                  self.itemset(x+3,y+3, " ")  

      # Bola 3x3
      if(self.item(x,y) == "O" and x < 3 and y < 3):
          if(self.item(x+1,y) == "O" and
            self.item(x+2,y) == "O" and 
            self.item(x,y+1) == "O" and 
            self.item(x,y+2) == "O" and 
            self.item(x+2,y+1) == "O" and 
            self.item(x+2,y+2) == "O" and 
            self.item(x+1,y+2) == "O"): 

                  self.pontos += pow(2,8)

                  # Apagar peças
                  self.itemset(x,y, " ") 
                  self.itemset(x+1,y, " ") 
                  self.itemset(x+2,y, " ")  
                  self.itemset(x,y+1, " ")  
                  self.itemset(x,y+2, " ")  
                  self.itemset(x+2,y+1, " ")  
                  self.itemset(x+2,y+2, " ")  
                  self.itemset(x+1,y+2, " ")
                  # Bola 2x2
      if(self.item(x,y) == "O" and x < 4 and y < 4):
          if(self.item(x+1,y) == "O" and
            self.item(x,y+1) == "O" and 
            self.item(x+1,y+1) == "O"):

                  self.pontos += pow(2,4)

                  # Apagar peças
                  self.itemset(x,y, " ") 
                  self.itemset(x+1,y, " ") 
                  self.itemset(x+1,y+1, " ")  
                  self.itemset(x,y+1, " ")  

  def verificaMais(self,x, y):
      # Mais 3x3
      if(self.item(x,y) == "+" and x != 0 and x!= 4 and  y<3 ):
          if(self.item(x,y+1) == "+" and
            self.item(x,y+2) == "+" and 
            self.item(x-1,y+1) == "+" and 
            self.item(x+1,y+1) == "+" ): 
            self.pontos += pow(2,5)
            self.itemset(x,y, " ") 
            self.itemset(x,y+1, " ") 
            self.itemset(x,y+2, " ")  
            self.itemset(x-1,y+1, " ")  
            self.itemset(x+1,y+1, " ")  

  def verificaMaisGrande(self):
      # Mais 5x5
      if(self.item(0,2) == "+" and
          self.item(1,2) == "+" and
          self.item(2,2) == "+" and
          self.item(3,2) == "+" and
          self.item(4,2) == "+" and
          self.item(2,0) == "+" and
          self.item(2,1) == "+" and
          self.item(2,3) == "+" and
          self.item(2,4) == "+"):
        self.pontos += pow(2,9)
        self.itemset(0,2," ")
        self.itemset(1,2," ")
        self.itemset(2,2," ")
        self.itemset(3,2," ")
        self.itemset(4,2," ")
        self.itemset(2,0," ")
        self.itemset(2,1," ")
        self.itemset(2,3," ")
        self.itemset(2,4," ")

  def verificaX(self,x, y):
      # verificar x 9 peças 5x5
      if(self.item(x,y) == "x" and y == 0 and x == 0):
          if(self.item(x+1,y+1) == "x" and
            self.item(x+2, y+2) == "x" and 
            self.item(x+3,y+3) == "x" and
            self.item(x+4, y+4)=="x" and
            self.item(x, y+4) == "x" and
            self.item(x+4, y) == "x" and
            self.item(x+1, y+3) == "x" and
            self.item(x+3, y+1) == "x"):
            self.pontos = self.pontos + pow(2,9) 
            self.itemset(x,y," ")
            self.itemset(x+1,y+1," ")
            self.itemset(x+2, y+2 ," ")
            self.itemset(x+3,y+3," ")
            self.itemset(x+4, y+4," ")
            self.itemset(x, y+4," ")
            self.itemset(x+4, y," ")
            self.itemset(x+1, y+3," ")
            self.itemset(x+3, y+1," ")

      # verificar x 5 peças 3x3
      if(self.item(x,y) == "x" and y < 3 and x < 3): 
          if(self.item(x, y+2) == "x" and #
            self.item(x+2,y) == "x" and
            self.item(x+1, y+1)=="x" and
            self.item(x+2, y+2) == "x"):
            self.pontos = self.pontos + pow(2, 5) 
            self.itemset(x,y," ")
            self.itemset(x,y+2," ")
            self.itemset(x+1,y+1," ")
            self.itemset(x+2,y+2," ")
            self.itemset(x+2,y," ")

  def insereNaFila(self, piece: str):
    self.fila.append(piece)

  def atualizaPontuacao(self):
    self.verificaMaisGrande()
    for i in range(5):
        for j in range(5):
          self.verificaMenos(i,j)
          self.verificaX(i,j)
          self.verificaBola(i,j)
          self.verificaMais(i,j)

  def insereSimbolo(self, x, y):
      if(self.item(x,y)==" "):
          if(len(self.fila) > 0):
            self.itemset(x,y,self.fila[0])
            self.fila.pop(0)


def geraFila(fila):
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
          

tabuleiro = Tabuleiro()

geraFila(tabuleiro.getFila())
while(1):
  print("\n\n\n\n\n\n")
  print("Pontuação: ",tabuleiro.pontos)
  tabuleiro.print()
  print("Escolha a posição:")
  user_input = input();
  if user_input != "" and user_input.isnumeric():
    n = int(user_input)
    pos1 = int(n)%5
    pos2 = int(n) / 5
    tabuleiro.insereSimbolo(int(pos2),int(pos1))
    tabuleiro.atualizaPontuacao()
