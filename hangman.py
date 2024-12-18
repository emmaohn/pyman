import os
import time
import re
clear = lambda: os.system('clear')

def noneWrong():
  print(' ______  ')
  print(' |    |  ')
  print(' |       ')
  print(' |       ')
  print(' |       ')
  print(' |______ ')

def oneWrong():
  print(' ______  ')
  print(' |    |  ')
  print(' |    O  ')
  print(' |       ')
  print(' |       ')
  print(' |______ ')

def twoWrong():
  print(' ______  ')
  print(' |    |  ')
  print(' |    O  ')
  print(' |    |  ')
  print(' |       ')
  print(' |______ ')

def threeWrong():
  print(' ______  ')
  print(' |    |  ')
  print(' |    O  ')
  print(r' |   /|  ')
  print(' |       ')
  print(' |______ ')

def fourWrong():
  print(' ______  ')
  print(' |    |  ')
  print(' |    O  ')
  print(r' |   /|\ ')
  print(' |       ')
  print(' |______ ')

def fiveWrong():
  print(' ______  ')
  print(' |    |  ')
  print(' |    O  ')
  print(r' |   /|\ ')
  print(r' |   /   ')
  print(' |______ ')

def allWrong():
  print(' ______  ')
  print(' |    |  ')
  print(' |    O  ')
  print(r' |   /|\ ')
  print(r' |   / \ ')
  print(' |______ ')

def jumpFrame1():
  print()
  print('     O  ')
  print(r'    /|\ ')
  print(r'    / \ ')
  print("Congrats, player 2!")
  print("You beat that other loser lol")

def jumpFrame2():
  print('     O  ')
  print(r'    \|/ ')
  print(r'    / \ ')
  print()
  print("Congrats, player 2!")
  print("You beat that other loser lol")

def victoryAnimation():
  clear()
  jumpFrame1()
  time.sleep(.4)
  clear()
  jumpFrame2()
  time.sleep(.4)
  clear()
  jumpFrame1()
  time.sleep(.4)
  clear()
  jumpFrame2()
  time.sleep(.4)
  clear()
  jumpFrame1()
  time.sleep(.4)
  clear()
  jumpFrame2()
  time.sleep(.4)

# isCorrect = False
guesses = []
magicKey = []
magicWord = ''
userInput1 = ''
wrong = 0
right = 0
guess = ''
i = 0


clear()

print("Welcome to your doom")
time.sleep(1)
clear()

print()
print('  O  ')
print(r' /|\ ')
print(r' / \ ')
print()
print("Here you are! ^^^")
time.sleep(2)
clear()

noneWrong()
print("Here's where you're going. ^^^")
time.sleep(2)
clear()

# this is where it begins
print("This is where it begins")
time.sleep(1)

# get the magic word from player 1
print("Player 1, choose your word")
magicWord = input().lower()
clear()
x = re.search("^[a-zA-Z\s]+$", magicWord)
if x:
  # is player 2 ready or not?
  while userInput1 != 'y':
    userInput1 = input("player 2, are you ready? (y / n) ")

    if userInput1.lower() == 'y':
      print("Great! Let's continue.")
      time.sleep(2)
    elif userInput1.lower() == 'n':
      print("* cough *")
      time.sleep(.3)
      clear()
      time.sleep(.6)
      print("Loser")
      time.sleep(.6)
      clear()
      time.sleep(.3)
      print("* cough *")
      time.sleep(.3)
      clear()
      time.sleep(.3)
      print("k bye")
      quit()
    else:
      print("Ok, let's try that again")
  else:
    print("Please only use letters and spaces")

#  magic key is a list of dashes the length of the word
for i in range(len(magicWord)):
  magicKey.append('_ ')

# player 2 is ready!
while wrong != 6 or right != len(magicWord):
  # check if user has won or lost
  if wrong == 6:
    clear()
    allWrong()
    print("Nice try... loser.")
    print("You lose")
    quit()

  if right == len(magicWord):
    victoryAnimation()
    quit()

  # print prompt
  print("Take a guess")

  # print board
  if wrong == 0:
    noneWrong()
  elif wrong == 1:
    oneWrong()
  elif wrong == 2:
    twoWrong()
  elif wrong == 3:
    threeWrong()
  elif wrong == 4:
    fourWrong()
  elif wrong == 5:
    fiveWrong()
  elif wrong == 6:
    allWrong()

  # print dashes and correct guesses
  for i in range(len(magicKey)):
    print(magicKey[i], end='')

  # print guesses
  print(f"Guesses: {guesses}")

  # get the guess
  guess = input().lower()

  # for each letter in the magic word, compare to the guess, 
  # then remove and insert at a specific position in the list
  for i in range(len(magicWord)):
    if magicWord[i] == guess:
      magicKey.pop(i)
      magicKey.insert(i, f'{magicWord[i]} ')
      right += 1

  # add guess to guess list and and to wrong count
  if guess not in guesses and guess != '':
    guesses.append(guess)
    if guess not in magicWord:
      wrong += 1

  # print(f"wrong {wrong}")
  # print(f"right {right}")
  clear()