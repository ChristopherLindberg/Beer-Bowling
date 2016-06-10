# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 18:23:17 2016
@author: Lindberg
"""
import random
gameNumber = 0 #init
table = {} #init
players = int(input('Enter Number of players: ')) #number of players

for psi in range(1,players+1): #indices increased so that player 1 is assosiated with 1
    table[psi] = input('Enter player name ')

while gameNumber <1: #must be at least one game
    gameNumber = int(input('Enter Number of games! '))    
    
for i in range(0,gameNumber):  #Who is going to play - randomnization
    randNumbers = []
    while len(randNumbers) < players:
        x = random.randint(1,players)
        if(x not in randNumbers):
            randNumbers.append(x)
            #Print statements
    if players > 3:
        print(table[randNumbers[0]],"+",table[randNumbers[1]], "vs", table[randNumbers[2]], "+", table[randNumbers[3]])
    elif players == 3:
        print(table[randNumbers[0]],"+",table[randNumbers[1]], "vs", table[randNumbers[2]])
Stop = int(input("0 to exit")) #to stop display of who are going to play
while Stop != 0:
    Stop = int(input())
