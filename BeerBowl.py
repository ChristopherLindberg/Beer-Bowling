# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:23:17 2016

@author: Lindberg
"""
import random
gamesize = 3
gameNumber = 0
players = 0
table = {}
while players < 4:
    players = int(input('Enter Number of players: '))
for psi in range(1,players+1):
    table[psi] = input('Enter player name ')

while gameNumber <1:
    gameNumber = int(input('Enter Number of games! '))    
for i in range(0,gameNumber):  
    randNumbers = []
    while len(randNumbers) <= gamesize:
        x = random.randint(1,players)
        if(x not in randNumbers):
            randNumbers.append(x)
    print(table[randNumbers[0]],"+",table[randNumbers[1]], "vs", table[randNumbers[2]], "+", table[randNumbers[3]])