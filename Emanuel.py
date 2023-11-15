#!/usr/bin/env pybricks-micropython
import random
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait
import time


ev3 = EV3Brick()

elevador = Motor(Port.D)
garra = Motor(Port.C)
motor = Motor(Port.B)

color_sensor = ColorSensor(Port.S4)

# Mapeamentos de cores para peças:
# Blue = Traco
# Red = Circulo
# Yellow = Sinal de mais
# Green = Sinal de multiplicacao

# deteta se uma cor pertença a uma peça válida
def color_is_valid(color):
    return color == Color.RED or color == Color.BLUE or color == Color.GREEN or color == Color.YELLOW

# Anda para tras até encontrar uma cor válida
# Retorna a cor válida que encontra
def busca_peca():
    color = color_sensor.color()
    motor.reset_angle(0)

    motor.run(200)

    while color_is_valid(color) is False:
        color = color_sensor.color()

    motor.brake()

    return color

def descer_elevador():
    elevador.run_until_stalled(300, then=Stop.COAST, duty_limit=15)

def subir_elevador():
    elevador.run_until_stalled(-300, then=Stop.COAST, duty_limit=15)

def abrir_garra():
    garra.reset_angle(0)
    garra.run_target(600, 600)

def fechar_garra():
    garra.run_until_stalled(-500,  then=Stop.COAST, duty_limit=50)
    garra.reset_angle(0)

def andar_para_agarrar_peca():
    motor.reset_angle(0)
    motor.run_target(200, 370, Stop.BRAKE)

def posicao_inicial():
    color = color_sensor.color()
    motor.reset_angle(0)

    motor.run(-200)

    while(color!=Color.BLACK):
        color = color_sensor.color()
    print(color)

    motor.brake()

def coloca_peca(pos):
    motor.reset_angle(0)
    motor.run_angle(400,-(360+(390*pos)), Stop.BRAKE)

def volta_inicio(pos):
    motor.reset_angle(0)
    motor.run_angle(400,(360+(390*pos)), Stop.BRAKE)

def inicializa_robo():
    descer_elevador()
    fechar_garra()
    abrir_garra()
n = 0;
while(n <=7):
    fechar_garra()
    inicializa_robo()
    busca_peca()
    andar_para_agarrar_peca()
    fechar_garra()
    subir_elevador()
    print(color_sensor.color())
    posicao_inicial()
    pos = random.randint(0, 9)
    print(n)
    coloca_peca(n)
    descer_elevador()
    abrir_garra() 
    subir_elevador()
    volta_inicio(n)
    inicializa_robo()
    n += 1

