# Author: Talha Naseer

# Lab (EECS 268) 

# Purpose: This file defines the Boardgame class. This class represents a board game with attributes such as name, Gibbon's rating, BGG (BoardGameGeek) average rating, average weight, year it was published, and the player count information. This class also includes a __repr__ method to provide a formatted string representation of a board game object whenever it's printed.


class Boardgame:
    def __init__(self, name, gibbonsrating, baverage, avgweight, yearpublished, bggbestplayers):
        #Initializes a Boardgame object with attributes.
        self.name = name
        self.gibbonsrating = gibbonsrating
        self.baverage = baverage
        self.avgweight = avgweight
        self.yearpublished = yearpublished
        self.bggbestplayers = bggbestplayers

    def __repr__(self):
        #Returns a string representation of the Boardgame object.
        return f"\n===============\n{self.name}\n{self.gibbonsrating}\n{self.baverage}\n{self.avgweight}\n{self.yearpublished}\n{self.bggbestplayers}\n===============\n"
