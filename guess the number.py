# project pertama
name = input(" input your name = ")


import random
secrate_number = random.randint(1,100)

print ("================================================================")
print (f"                 Lest get Strart the game {name}               ")
print ("================================================================")
print ("             we already have a number, pleasse guess!           ")
print ("================================================================")
print ("-----rules-----")
print ("1. having fun")
print ("2. you have only 5 chances")
print ("3. guess the number 1 - 100")
print ("================================================================\n")

chances = 5
for i in range (chances):

    answer = int(input(f'[chance {i + 1}]\n Input The Number = '))

    if answer == secrate_number:
        print("congratulation, your answer is correct ")
        break
    else :
        print('(your guess is too',' low)' if answer < secrate_number else 'big)')
else :
    print ("================================================================")
    print (f"       oooh unluckly :( , ypu have spend {chances}x chance     ")
    print ("================================================================")