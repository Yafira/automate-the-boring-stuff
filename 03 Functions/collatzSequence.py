#! /usr/bin/python3
# Collatz sequence

# Determine collatz sequence
def collatz(anyNumber):
    if anyNumber % 2 == 0:
        return anyNumber // 2 #Even
    elif anyNumber % 2 == 1:
        return 3 * anyNumber + 1 #Odd

# Check if user value is a valid integer number.
# Will request untill true
def userInput():
    while True:    
        try:
            return int(input())
            break
        except ValueError:
            print('Error: Number not a valid integer number.')
            print('Please select a valid integer number...')


# Ask the player to guess a number.
print('Please select any number...')
myNumber = userInput()
while myNumber != 1:
    myNumber = collatz(myNumber)
    print(myNumber)
