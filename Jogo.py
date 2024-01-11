import random

class Tabuleiro:
  # Inicializa a classe Tabuleiro com os atributos pontos, fila e tabuleiro 
  def __init__(self):
    self.pontos = 0
    self.fila = []
    self.tabuleiro = [" "] * 25

  # Retorna a fila atual de símbolos.
  def getFila(self):
    return self.fila
  
  # Retorna o símbolo na posição especificada (x, y) no tabuleiro do jogo 
  def item(self,x,y):
    return self.tabuleiro[x + y*5]
  
  # Verifica se a posição especificada (x, y) no tabuleiro do jogo está vazia 
  def posicaoValida(self,x,y):
    if(self.tabuleiro[x+y*5] == " "):
       return True
    else:
       return False

  # Imprime o estado atual do tabuleiro do jogo com símbolos, incluindo o próximo símbolo na fila 
  def print(self):
    print("+---+---+---+---+---+")
    print("|",self.item(0,0),"|",self.item(1,0),"|",self.item(2,0),"|",self.item(3,0),"|",self.item(4,0),"|")
    print("+---+---+---+---+---+")
    print("|",self.item(0,1),"|",self.item(1,1),"|",self.item(2,1),"|",self.item(3,1),"|",self.item(4,1),"|")
    print("+---+---+---+---+---+")
    print("|",self.item(0,2),"|",self.item(1,2),"|",self.item(2,2),"|",self.item(3,2),"|",self.item(4,2),"|")
    print("+---+---+---+---+---+")
    print("|",self.item(0,3),"|",self.item(1,3),"|",self.item(2,3),"|",self.item(3,3),"|",self.item(4,3),"|")
    print("+---+---+---+---+---+")
    print("|",self.item(0,4),"|",self.item(1,4),"|",self.item(2,4),"|",self.item(3,4),"|",self.item(4,4),"|")
    print("+---+---+---+---+---+")
    print("Next:", self.fila[0] if len(self.fila) > 0 else " ", "\nFila : ",self.fila)

  # Define o símbolo na posição especificada (x, y) no tabuleiro do jogo como o símbolo fornecido por parâmetro
  def itemset(self, x,y, piece: str):
    self.tabuleiro[x + y*5] = piece

  # Verifica linhas horizontais de símbolos "-" e calcula os pontos conforme o tamanho da peça formada
  # Remove os símbolos do tabuleiro após dar a respetiva pontuação
  def verificaMenos(self,x, y):
      if(self.item(x,y) == "-" and x < 4):
          if(self.item(x+1, y) == "-"):
              if(x+2 <= 4 and self.item(x+2,y) == "-"):
                self.pontos += 8 #pow(2, 2) 
                self.itemset(x,y," ")
                self.itemset(x+1,y," ")
                self.itemset(x+2,y," ")
              else:
                self.pontos += 4 #pow(2, 3) 
                self.itemset(x,y," ")
                self.itemset(x+1,y," ")
                
  # Verifica símbolos "O" e calcula os pontos conforme o tamanho da peça formada (5x5, 4x4, 3x3)
  # Remove os símbolos do tabuleiro após dar a respetiva pontuação            
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
                  self.itemset(x+1,y+3, " ")  
                  self.itemset(x+2,y+3, " ")  

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

  # Verifica símbolos "+" e calcula os pontos para o tamanho da peça formada (3x3)
  # Remove os símbolos do tabuleiro após dar a respetiva pontuação  
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

  # Verifica o padrão específico (5x5) símbolos "+" e calcula os pontos para o tamanho da peça formada 
  # Remove os símbolos do tabuleiro após dar a respetiva pontuação
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

  # Verifica símbolos "X" e calcula os pontos conforme o tamanho da peça formada (5x5, 3x3)
  # Remove os símbolos do tabuleiro após dar a respetiva pontuação 
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

  # Adiciona o simbolo passado por parâmetro à fila
  def insereNaFila(self, piece: str):
    self.fila.append(piece)

  # Atualiza a pontuação do jogo verificando os diferentes padrões possiveis pelas 
  # funções verificaMenos, verificaX, verificaBola e verificaMais no tabuleiro do jogo
  def atualizaPontuacao(self):
    self.verificaMaisGrande()
    # percorre cada coluna de cada linha, perfazendo todo o tabuleiro
    for j in range(5):
        for i in range(5):
          self.verificaMenos(i,j)
          self.verificaX(i,j)
          self.verificaBola(i,j)
          self.verificaMais(i,j)

  # Insere um símbolo na posição (x, y) do tabuleiro do jogo, no caso dessa estar vazia, usando o próximo símbolo na fila
  def insereSimbolo(self, x, y):
      if(self.item(x,y)==" "):
          if(len(self.fila) > 0):
            self.itemset(x,y,self.fila[0])
            self.fila.pop(0)

  # Gera a fila com itens aleatorios de tamanho 25 
  def geraFila(self):
    for x in range(25):
      ran = random.randint(0,3)
      if(ran == 0):
        self.fila.append("O")
      elif(ran == 1):
        self.fila.append("x")
      elif(ran == 2):
        self.fila.append("+")
      else:
        self.fila.append("-")
