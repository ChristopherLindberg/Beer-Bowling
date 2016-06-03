# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:23:17 2016
@author: Lindberg
"""
import random
gamesize = 3
gameNumber = 0
table = {}
players = int(input())
for psi in range(1,players+1):
    table[psi] = input()

while gameNumber <1:
    gameNumber = int(input())    
for i in range(0,gameNumber):  
    randNumbers = []
    while len(randNumbers) < players:
        x = random.randint(1,players)
        if(x not in randNumbers):
            randNumbers.append(x)
    if players > 3:
        print(table[randNumbers[0]],"+",table[randNumbers[1]], "vs", table[randNumbers[2]], "+", table[randNumbers[3]])
    elif players == 3:
        print(table[randNumbers[0]],"+",table[randNumbers[1]], "vs", table[randNumbers[2]])
