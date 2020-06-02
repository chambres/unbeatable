
from time import sleep
import sys
import re
import time
from os import system

def rules():
  print("The game is this: ")

  print("We start with 1, then you choose a number from 1 - 10.")

  print("The computer chooses a number, then those 2 numbers are added.")

  print("This repeats until someone can add a number to the current number and reach 100!")

  print("You will always lose!")

  print("Type 'clear' and hit enter to clear all text on screen.")
  print("We start with 1.")
  print("")

def clear(): 

        _ = system('clear') 
class cheater_text(object):
  def __init__(self, str):
    
    self.wordsshort = "Hey. Are you playing around? "
    self.wordsabove = "Don't you know that " + mystr + " is above 10? Try again.\n"
    self.wordsbelow = "Don't you know that " + mystr + " is below 1? Try again.\n"
    self.wordsfloat = "Don't you know that " + mystr + " is a decimal? Try again.\n"
    self.wordsweirdnumber = "Don't you know that " + mystr + " isn't a valid number here? Try again.\n"
    self.wordswords = "Don't you know that " + mystr + " isn't a number, but part of the alphabet? Try again.\n"
    self.wordsblank = "That was blank. Try again.\n"

class cheating(object):
    def cheaterabove(self):
        for char in text.wordsshort:
            sleep(0.3)
            sys.stdout.write(char)
            sys.stdout.flush()
        for char in text.wordsabove:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

    def cheaterbelow(self):
        for char in text.wordsshort:
            sleep(0.3)
            sys.stdout.write(char)
            sys.stdout.flush()
        for char in text.wordsbelow:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

    def cheaterfloat(self):
        for char in text.wordsshort:
            sleep(0.3)
            sys.stdout.write(char)
            sys.stdout.flush()
        for char in text.wordsfloat:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

    def cheaterwords(self):
        for char in text.wordsshort:
            sleep(0.3)
            sys.stdout.write(char)
            sys.stdout.flush()
        for char in text.wordswords:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()

    def cheaterweirdnumber(self):
        for char in text.wordsshort:
            sleep(0.3)
            sys.stdout.write(char)
            sys.stdout.flush()
        for char in text.wordsweirdnumber:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
    def cheaterblank(self):
        for char in text.wordsblank:
            sleep(0.1)
            sys.stdout.write(char)
            sys.stdout.flush()
combinednum = 1

cheat = cheating()

def main():
    global combinednum
    while combinednum < 100:
        try:
        
            print("Your turn:")
            print(" ")
            global mystr
            mystr = str(input("> "))
            

            
            myfloat = float(mystr)
            mycheck = myfloat.is_integer()
            global text
            
            if myfloat > 10:
                #above
                text = cheater_text(mystr)
                cheat.cheaterabove()
                continue
            if myfloat < 1:
                #below
                text = cheater_text(mystr)
                cheat.cheaterbelow()
                continue
            if mycheck == False:
                #float
                text = cheater_text(mystr)
                cheat.cheaterfloat()
                continue


            comnum = 11 - myfloat
            print("My number is: " + str(int(comnum)))
            combinednum += comnum + myfloat
            print("The new total: " + str(int(combinednum)))
        except ValueError:
            if mystr == "clear":
              clear()
              continue
            search = re.search('[a-zA-Z]', mystr)
            if mystr == "":
                text = cheater_text(mystr)
                cheat.cheaterblank()
            elif search == None:
                text = cheater_text(mystr)
                cheat.cheaterweirdnumber()
                continue
            elif search != None:
                text = cheater_text(mystr)
                cheat.cheaterwords()
                continue
    print("Tsk. Tsk. Tsk. I win once again. ")

rules()
playing = True
while playing:
    main()
    a = input("Do you want to play again? (Y/N)\n> ")
    continues = {"yes", "y", "Y", "YES", "Yes", "sure"}
    ending = {"n", "N", "No", "NO", "no"}
    if a in continues:
        combinednum = 1
        continue
    if a in ending:
        print("Exiting game...")
        playing = False
    else:
        print("You sure that's a valid command?")
        
