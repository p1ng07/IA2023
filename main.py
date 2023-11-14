#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.tools import wait
import time

angulo_abrir = 700
angulo_fechar = 900
ev3 = EV3Brick()

garra_motor = Motor(Port.C)
elevador = Motor(Port.D)

color_sensor = ColorSensor(Port.S4)

rat_wheels = Motor(Port.B)


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
def procura_peca(color_sensor, motor):
    color = color_sensor.color()
    motor.reset_angle(0)

    motor.run(200)

    while color_is_valid(color) is False:
        color = color_sensor.color()

    motor.brake()

    return color

def dar_passo(motor):
    motor.reset_angle(0)
    motor.run_angle(400,-720, Stop.BRAKE)

def dar_passo_atras(motor):
    motor.reset_angle(0)
    motor.run_angle(100,360, Stop.Brake)

def descer_elevador(elevador):
    elevador.run_until_stalled(300, then=Stop.COAST, duty_limit=15)

def subir_elevador(elevador):
    elevador.run_until_stalled(-300, then=Stop.COAST, duty_limit=15)

def abrir(garra_motor):
    garra_motor.run_target(600, 460)

def fechar(garra_motor):
    garra_motor.run_until_stalled(-500,  then=Stop.COAST, duty_limit=30)
    garra_motor.reset_angle(0)

def andar_para_tras_para_agarrar_cor(motor):
    motor.run_target(200, 720, Stop.BRAKE)

def avancar_e_largar_peca(motor, garra_motor, elevador):
    dar_passo(motor)
    dar_passo(motor)
    descer_elevador(elevador)
    abrir(garra_motor)
    subir_elevador(elevador)

def andar_para_tras_e_agarrar_peca(motor, garra_motor, elevador):
    abrir(garra_motor)
    descer_elevador(elevador)
    cor = procura_peca(color_sensor, rat_wheels)
    andar_para_tras_para_agarrar_cor(motor)
    fechar(garra_motor)
    subir_elevador(elevador)

# template de funcoes a utilizar
#fechar(garra_motor)
#abrir(garra_motor)

#subir_elevador(elevador)
#descer_elevador(elevador)
#fechar(garra_motor)
#cor = procura_peca(color_sensor, rat_wheels)

#andar_para_tras_para_agarrar_cor(rat_wheels)

#fechar(garra_motor)

#subir_elevador(elevador)

#dar_passo(rat_wheels)
#dar_passo(rat_wheels)


#dar_passo(rat_wheels)
#dar_passo_atras(rat_wheels)

#andar_para_tras_para_agarrar_cor(rat_wheels)

andar_para_tras_e_agarrar_peca(rat_wheels, garra_motor, elevador)

avancar_e_largar_peca(rat_wheels, garra_motor, elevador)