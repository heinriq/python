# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:31:36 2017

@author: Jones
"""
import numpy as np

#entradas = np.array([[0,0],[0,1], [1,0], [1,1]])
#saidas = np.array([0,1,1,0])
pesos = np.array([0.0, 0.0])
taxaAprendizagem = 0.1

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculaSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar(entradas, saidas):
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculaSaida(np.asarray(entradas[i]))
            erro = saidas[i] - saidaCalculada
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaAprendizagem * entradas[i][j] * erro)
                print('Peso atualizado: ' + str(pesos[j]))
        print('Total de erros: ' + str(erroTotal))

def AndOperator():
    entradas = np.array([[0,0],[0,1], [1,0], [1,1]])
    saidas = np.array([0,0,0,1])
    Execute(entradas, saidas, "AND")

def OrOperator():
    entradas = np.array([[0,0],[0,1], [1,0], [1,1]])
    saidas = np.array([0,1,1,1])
    Execute(entradas, saidas, "OR")

def Execute(entradas, saidas, operator):
    
    print(operator + " sem treino")
    for i in range(len(entradas)):
        print(calculaSaida(entradas[i]))
    
    treinar(entradas, saidas)
    print('Rede neural treinada')

    for i in range(len(entradas)):
        print(calculaSaida(entradas[i]))

AndOperator()
OrOperator()        

            
            