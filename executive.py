# Author: Talha Naseer

# Lab (EECS 268) 

# Purpose: This file contains the Executive class, which manages the functionality of the whole program. It scans the board game data from a user-specified file, and in return provides a menu interface for various operations on the data, while controlling user interaction. The class also includes methods for reading board games from a file and running the program's menu.


from boardgame import Boardgame

class Executive:

    def __init__(self):
        #Initializes Executive class, prompt user for the input filename, and create an empty list for board games.
        self.fileName = input("\nEnter the filename: ")
        self.boardGames = []
        self.scanBoardGames(self.fileName)

    def scanBoardGames(self, fileName):
        #Opens and reads the file, parsing its contents to the boardGames list.
        with open(fileName, encoding="utf8") as f:
            for line in f:
                if "name" not in line:
                    lineNum = line.strip('\n').split('\t')
                    self.boardGames.append(Boardgame(lineNum[0], lineNum[1], lineNum[2], lineNum[3], lineNum[4],  lineNum[5]))

    def runTheMenu(self):
        #Displays a menu and handle user interaction based on their choice.
        output = ""
        print('\n1. Print games in order of Gibbon\'s rating\n2. Print all games from a year\n3. Print all games given weight\n4. The People VS Dr. Gibbons\n5. Print based on player count\n6. Exit the program')
        userChoice = input("\nEnter a choice: ")

        if userChoice == "1":
            #Sorts and prints games by Gibbon's rating in reverse order.
            print(sorted(self.boardGames, key=lambda x: float(x.gibbonsrating), reverse=True))

        elif userChoice == "2":
            year = input("\nPlease enter a year you are searching for: ")
            for object in self.boardGames:
                output += str(object) * int(object.yearpublished == year)
            if output == "":
                print("\nSorry, No Games Were Found\n")
            else:
                print(output, "\n")

        elif userChoice == "3":
            weight = float(input("\nPlease enter a weight: "))
            for object in self.boardGames:
                output += str(object) * (float(object.avgweight) <= weight)
            print(output, "\n")

        elif userChoice == "4":
            difference = float(input("\nPlease enter a difference value: "))
            for object in self.boardGames:
                output += str(object) * (abs(float(object.gibbonsrating) - float(object.baverage)) > difference)
            print(output, "\n")

        elif userChoice == "5":
            playerCount = int(input("\nEnter a player count: "))
            for object in self.boardGames:
                output += str(object) * (str(playerCount) in object.bggbestplayers)
            print(output, "\n")

        elif userChoice == "6":
            print("\nThank you for using this program. Goodbye!\n")
            exit()
