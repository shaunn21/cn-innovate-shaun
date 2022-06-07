

# inp = input("Enter a number: ")
# converted_num = int(num)

# def light_switch():
#     if inp:
#         print("Whoa! its bright in here")
#         light = False
#     else:
#         print("who turned out the lights?")
#         light = True



# #! Activity 1

def user_choice():
    x = False
    while x == False:
        y = input('Please enter a number: \n')
        if y.isnumeric():
            print(f'{y} is a number!')
            y = int(y)
            print(type(y))
            choice_check = True
        else:
            print(f'{y} is not a number!')
            

user_choice()


#! Activity 2

import random

cast = ["Bill Murray", 
"Dan aykro", 
"Rick Moranis", 
"Annie Potter"
]

Ques = [
    ["1. The first ghost to appear in Ghostbusters is a female apparition seen where?", "libray"],
    ["2. The movie takes place in what major city?" "new york"],
    ["3. What television show does Venkman host?", "world of the psychic"]
]

def getRandomName():
    print (random.choice(cast))

getRandomName()

def answerQuestion():
    while True:
        currentIndex = random.choice(range(0,3))
        print (Ques[currentIndex][0])
        answer = input("What is your answer? ")
        if answer == Ques[currentIndex][1]:
            print("congratulations you rock ")
            break
        else: 
            print ("Try again... ")
        

answerQuestion()

