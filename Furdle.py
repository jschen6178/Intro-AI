from random import randint
import string
#word is an array
#guesses will be strings
#match is an array

def guess(lettRemain):
    g = input("Enter a 5 letter word: ")
    if len(g) != 5:
        return guess(lettRemain)
    if len(g) == 5:
        for i in range(5):
            if g[i] not in lettRemain:
                print("You used forbidden letters!")
                return guess(lettRemain)
    return g   
    
    
def check(word, guess):
    match = []
    garbage = []
    for i in range(5):
        if guess[i].lower() == word[i]:
            match.append(guess[i].upper())
        elif guess[i].lower() in word:
            match.append(guess[i].lower())
        else:
            match.append("#")
            garbage.append(guess[i].lower())
        
    return (match, garbage) 
            
def turn(word, lettRemain):
    g = guess(lettRemain)
    print('-'*20)
    (match, garbage) = check(word, g)   
    print("Your word: " + g + ' '*5 + "Matches:   " + str(match))
    if str(match) == word:
        print("Correct! You guessed the word!")
    lettRemain[:] = [' ' if letter in garbage else letter for letter in lettRemain]
    return lettRemain

def main():
    print("*"*15 + " Welcome to Furdle " + "*"*15)
    print("Guess a 5 letter animal!")
    print("If you guessed a letter in the correct position, you will see it as a capital letter")
    print("If you guessed a letter in the word but wrong position, you will see it as a lower case letter")
    print("Let's begin!")

    wordList = ["panda", "koala", "horse", "sheep", "whale", "camel", "zebra", "tiger", "otter", "mouse", "eagle", "goose", "cobra", "bunny", "bison", "badger", "hyena", "squid", "rhino", "quail", "shark"]
    word = list(wordList[randint(0, len(wordList)-1)])
    count = 0
    lettRemain = list(string.ascii_lowercase)
    print(lettRemain)
    while(count < 6):
        lettRemain = turn(word, lettRemain)

    print("You ran out of turns! Try again next time")
    
main()
