#Medidor de pica.py
import math
import os

"""
    Calcula o volume do pau baseado na fórmula 
    de volume de cilindros (diâmetro X base)
"""
def calcularVolumeDoPau(tamanho, grossura):
    return tamanho*grossura*math.pi

"""
    Calcula o peso do pau utilizando 
    as bolas como Peso Teórico
"""
def calcularPesoDoPau(volume, pesoBolas):
    return volume*pesoBolas

"""
    Limpa o terminal
"""
def cls():
    os.system("cls")

"""
    Rotina padrão (main)
"""
def medirPica():
    tamanho = int(input("Tamanho do pau: ")) #cm
    cls()

    grossura = int(input("Grossura: ")) #cm
    cls()

    pesoBolas = int(input("Peso das bolas: ")) #g
    cls()

    volume = calcularVolumeDoPau(tamanho, grossura)
    peso = calcularPesoDoPau(volume, pesoBolas)

    #Printa os resultado
    print("Volume do pau {} /n Peso: {}".format(volume, peso))

#Roda a rotina padrão
medirPica()