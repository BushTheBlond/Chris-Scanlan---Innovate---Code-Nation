import random

greeting = "Hey World"
print(greeting)

# interger = number
# floating point = decimal number
# None = null (falsy) eg num1 + num2 def add_up(num1,num2): without "return" be nothing

def add_up(num1, num2):
    return num1 + num2

print (add_up(1, 2))

example_string = "one upon a time..." # start from 0 when considering interger

print(len(example_string))
print(example_string [5])             # = "p"

print(example_string.count("o"))      # = "2"

num3 = random.randint (1, 50)

print(random.random())
print(random.uniform(1, 10))

print(example_string.strip())

example_string = example_string.replace("one", "once")

print(example_string)



# Variable Box


variable_one = 10

variable_one = "cat"
print(variable_one)

def function_example():
    pass

name = "Chris"
age = 29
email = "chris@chris.chris"
hair_colour = "blond"

#print = to trace value, sends to terminal
#return = giving out the result of whatever code happens in the fuction. Acts as an equals function.
# print("Welcome, {}, are you staying long? you are ".format(name)) -------- old method of format
print(f"{name} is a dude, he is {age} years old, his email is {email} and his hair colour is {hair_colour}.")

#modulus operator gives remainder = %


num = 16
num += 3

result = num % 5

print (result) 


if num % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")

#right click format document to clean up spacing/make code more reader friendly.

# x = input("What is the first number you'd like to add?  ")
# y = input("What is the second number you'd like to add? ")

# x = int(x)
# y = int(y)
# print(add_up(x,y))


music = "Death Metal"
music_list = [
    "Rock"
    "Samba"
    "Jazz"
    "Metal"
]

music_tuple = ("Rap", "Grindcore")

if "Metal" in music or music == "Jazz":
    print("Chris is okay")
elif music == "samba":
    print("Peter is dancing")
elif music != "k-pop":
    print("When it rains, bring out the wellingtons")

def function_one(name):
    return f"Hello {name}!"

print(function_one("Brian"))

def multiply(num5, num6):
    num5 * num6

multiply(2,12)

def string_test(str1, str2):
    return f"{str1} is my fav food, and {str2} is my fav colour."

print(string_test("Pizza", "Purple I guess"))

w_amount = 100
acount_num = 12345678

def cash_withdrawal (amount, accnum):
    print(f"Withdrawing {amount} from account {accnum} ")

cash_withdrawal(w_amount, acount_num)
cash_withdrawal(300, 50449921)
cash_withdrawal(30, 50449921)


list_of_players = [
    "Kane",
    "Son",
    "Emerson"
]

for player in list_of_players:          
    print(player)                       #Prints list of players without square bracket

list_of_players[2] = "Davies"           #Chsnge "Emerson" to "Davies"

print(list_of_players)

print(len(list_of_players))             #Number of items in list
print(len(list_of_players[2]))          #Number of letters for item specified in list = 2 is Davies, so 6

coffee_order = [
    "Alex - Tea",
    "Ben - Mocha",
    "Betty - Latte"
]

coffee_order.append("Julie - Tea")      #Add an item to the list with "append"
print(coffee_order)

coffee_order.pop()                      #Will remove any item specified, if no value, removes last item listed ("Julie" in this sceneario)
print(coffee_order)

first_entry = list_of_players.pop(0)   #Pulls "Kane", the 0th value, shows it on its own when printed

print(first_entry)

# for i in range(0,10,2):
#     print(i)

# for b in range(0,21,3):
#     print(b)

# for j in range (0, 31, 3):
#     print(j)

nu = 0

while nu <10:                          #Prints up to 10 in increments of 2
    nu += 2
    print(nu)

from random import randint          

nombre = randint(0, 50)

while nombre != 29:                    #Prints random numbers from 0,50 until it hits the specified number of 29
    nombre= randint(0, 50)
    print(nombre)


code_string = str("Welcome to Code Nation")



alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# for x in alphabet :
#     print(x)

# input("Enter a number between 1-26: ")


# alphaindex = 0
# for i in range (len(alphabet)):
#     print(alphabet[alphaindex])
#     alphaindex += 1

# def numinput():
#     usernum = input("Enter a Number from 1 to 26: ")
#     usernum = int(usernum-1)
#     for i in alphabet:
#         if usernum == 

def get_usernum():
    usernum = input("Please choose a number between 1 and 26: ")
    usernum = int(usernum) -1
    print(alphabet[usernum].upper())                                #allows you to use 1-26 to highlight a letter
get_usernum()