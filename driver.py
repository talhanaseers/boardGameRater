# Author: Talha Naseer

# (EECS 268) — LAB

# Purpose: This script serves as the entry point of the program. It imports the Executive class from the executive.py file and contains the main() function that initializes an instance of the Executive class and runs the main menu loop.


from executive import Executive

def main():
    #Creates an Executive instance and runs the menu loop.
    myExec = Executive()
    while True:
        myExec.runTheMenu()

if __name__ == "__main__":
    main()
