#!/usr/bin/env python

"""
Game of Nim from Python for Everyone 3rd edition
"""

from random import seed, randint

"""
Name: Brooke Higgins

Course: CSC 119801 Into to Programming: Python

Date: 11/21/2021

Program Description: Nim Game vs. Computer

"""

#Function for game against Computer, Easy
def computerStupid(ballCount):
    if ballCount == 1:
        ballsTaken = 1
    else:
        ballsTaken= randint(1, ballCount//2)
    return ballsTaken

#Function for game against Computer, Hard
def computerSmart(ballCount):
    if ballCount > 63:
        ballsTaken = ballCount - 63
    elif ballCount > 31 and ballCount < 63:
        ballsTaken = ballCount - 31
    elif ballCount > 15 and ballCount < 31:
        ballsTaken=ballCount - 15
    elif ballCount > 7 and ballCount < 15:
        ballsTaken=ballCount - 7
    elif ballCount > 3 and ballCount < 7:
        ballsTaken=ballCount - 3
    else:
        if ballCount == 1:
            ballsTaken = 1
        elif ballCount == 63 or ballCount == 31 or ballCount == 15 or ballCount == 7 or ballCount == 3:
            ballsTaken= randint(1, ballCount//2)
    return ballsTaken

def main():                     # definition of main program
    seed()                      # initialize the random number generator for the game play

    # -------------------------------------------------------
    # INPUT - to randomize the game play
    # -------------------------------------------------------
    ballCount = randint(10, 100)# randomly generate the amount of balls to play
    turn = randint(0,1)         # randomly generate who goes first (0) player (1) computer
    mode = randint(0,1)         # randomly generate mode of computer (0) smart (1) stupid

    # -------------------------------------------------------
    # PROCESS - play the game of NIM taking turns
    # -------------------------------------------------------
    print("***** Game of NIM Starts *****")
    while ballCount > 0:     # if there are still balls left, then keep playing
        print("\t\tBall count:", ballCount)
        if turn == 0:           # player turn
            print("\n\tPLAYER TURN")
            gone = int(input("How many balls would you like to remove? "))
            ballCount = ballCount - gone
            if ballCount - gone < 0:
                print("There are not that many balls left!")
            elif ballCount - gone > 0:
                print("You removed " + str(gone) + " balls. There are " + str(ballCount) + " balls left")
            # TODO: call the playerTurn function
            turn = 1
        else:
 
            if mode == 0: #Computer Smart Mode
                print("COMPUTER TURN- Mode: Smart")
                computerRemoves = computerSmart(ballCount)
                ballCount = ballCount - computerRemoves
                print( "The Computer removed " + str(computerRemoves) + " ball(s)! The current ball count is: " + str(ballCount) )
            else:    
                print("\n\tCOMPUTER TURN - Mode: Stupid")
                computerRemoves = computerStupid(ballCount)
                ballCount = ballCount - computerRemoves
                print( "The Computer removed " + str(computerRemoves) + " ball(s)! The current ball count is: " + str(ballCount) )
                # TODO: call the computerStupid function
            turn = 0            # switch the turn 0 - for player turn next
        # TODO: ballCount needs to be updated for each turn
                
    # -------------------------------------------------------
    # OUTPUT - The player who takes the last ball loses.
    # once the ballCount goes to 0, the turn switches, so it is the other
    # player then that wins
    # -------------------------------------------------------
    print("\t\tBall count:", ballCount)
    if turn == 0 and ballCount == 0:
        print("\n***** GAME of NIM Winner! PLAYER *****\n\n")
    else:
        print("\n***** Game of NIM Winner! COMPUTER *****\n\n")

main()          # execution of main program

