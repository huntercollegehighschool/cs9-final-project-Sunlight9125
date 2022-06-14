"""
Name(s): Albert Lin
Name of Project: Hard Hangman
"""

#Write the main part of your program here. Use of the other pages is optional.
import os
from random import choice
from art import stages, logo
from wordlist import wordList
def playerGuess(guess: str):
  global guessesLeft, wordLetters, guessedLetters
  guess = guess.lower()
  if len(guess) > 1 or not guess.isalpha():
    graphics(" ".join(wordLetters), "Not a valid guess.")
  elif guess.upper() in guessedLetters or guess in word and guess in wordLetters:
    graphics(" ".join(wordLetters), "You already guessed that.")
  elif guess in word:
    wordLetters = [letter if letter == guess or wordLetters[word.index(letter)] != '_' else '_' for letter in word ]
    graphics(" ".join(wordLetters), "That was correct!")
  else:
    guessedLetters.append(guess.upper())
    graphics(" ".join(wordLetters), "Not quite right.", False)
def graphics(display: str, message: str, correct=True, override=False):
  global guessesLeft, game_status, guessedLetters
  os.system('clear')
  if not override:
    if not correct:
      guessesLeft -= 1
  print(f"{logo}\n\n\n\n{stages[guessesLeft]}                     {display}            Wrong: {' '.join(guessedLetters)}\n{message}")
  if guessesLeft <= 0:
    game_status = 2
  elif "".join(wordLetters) == word:
    game_status = 1
def game():
  global guessesLeft, word, wordLetters, game_status, winstreak, guessedLetters
  guessesLeft = 6
  word = choice(wordList)
  wordLetters = ['_' for letter in word]
  guessedLetters = []
  game_status = 0
  graphics(" ".join(wordLetters), '', override=True)
  while game_status == 0:
    playerGuess(input("\n\nGuess a letter: "))
  if game_status == 1:
    winstreak += 1
  else:
    winstreak = 0
  print(f'\n\n{"Right on the spot!" if game_status == 1 else f"Game over—the word was [{word}]."}\nYour current winstreak is {winstreak}.\n')
  if input("Would you like to play again? [Y/N]\n").upper() == 'Y':
    game()
winstreak = 0
game()