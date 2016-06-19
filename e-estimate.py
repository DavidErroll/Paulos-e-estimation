# John Allen Paulos tweeted this method of estimating e:
# Pick a random number between 0 & 1. 
# Pick 2nd number & add it to the 1st.
# Repeat until sum exceeds 1.
# The average number of picks is e.
# https://twitter.com/JohnAllenPaulos/status/744227797468581890

from random import random

# from math import e

def randomize():
    accumulator = 0
    count = 0
    while accumulator <= 1:
        accumulator += random()
        count += 1
    return count

def sample(size):
    total = 0
    for x in range(1, size):
        total = total + randomize()
    average = total / size
    return average

def output():
    for size in range(1000000, 10000001, 1000000):
        estimate = sample(size)
        print(estimate)
#       print(estimate - e)
    
def main():
    output()

main()    
