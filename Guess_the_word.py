# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 12:42:28 2023

@author: Anusmita Adhikary
"""


import random
def choose():
    words=['rainbow','computer','programming','player']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled    

def thank(p1n,p2n,p1,p2):
    print(p1n,p1)
    print(p2n,p2)
    print('Thanks for playing.....have a nice day!!')
    
def play():
    p1name=input("Enter your name, player1")
    p2name=input("Enter your name, player2")
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computer's task
        picked_word=choose()
        #create question
        qn=jumble(picked_word)
        print(qn)
        #player1
        if turn%2==0:
            print(p1name,'Your turn')
            ans=input('Whats on my mind')
            if ans==picked_word:
                pp1=pp1+1
                print('Right!Score=',pp1)
            else:
                print('Better luck next time',picked_word)
            c=int(input('0---->Discontinue\n1----->Continue'))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
#player2
        else:
            print(p2name,'Your turn')
            ans=input('Whats on my mind')
            if ans==picked_word:
                pp2=pp2+1
                print('Right!Score=',pp2)
            else:
                print('Better luck next time',picked_word)
            c=int(input('0---->Discontinue\n1----->Continue'))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn=turn+1
    if pp1>pp2:
        print(p1name,'won')
    elif pp2>pp1:
        print(p2name,'won')
    else:
        print('It is a draw')
    
play()