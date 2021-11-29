#!/usr/bin/env python


"""
Name: Brooke Higgins

Course: CSC 119801 Into to Programming: Python

Date: 11/27/2021

Program Description: Gymnastics/Diving Scoring Program

"""
#All of the judges scores
scores = [9.2, 8.6, 9.9, 9.4, 9.4, 9.8, 8.8, 9.1]
#Removing the highest score
scores.remove(max(scores))
#Removing the lowest score
scores.remove(min(scores))
#Adding the remaining scores
totalScore = sum(scores)
#Prints final score
print("Score = %5.2f" % totalScore)