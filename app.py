#to build guessing a secret code game

secCode = input('Enter the secret code: ')
guess = ''
while guess != secCode:
    guess = input("Enter code: ")
print("YOU WON!")
