#converting data types
#Truthy/falsy with if/else
#Try/except, scope with functions
#Tuples in list
#while true loops

#float () - floating point interger

from unicodedata import name


inter = int(5.8)                    #Always rounds down to non decimal, so the number will be 5
minter = int("54")                  #54

print(inter)
print(minter)

print(int(round(5.99999)))          #Rounds up properly

print(float(54))                    #54.0
print(float("54"))                  #54.0


print(str(54))
print(str("54"))

variable_one = 54                                       #Having the variable be either blank, none or 0 will cause Falsy, otherwise it will be Truthy
if variable_one:                                        #using "0" will be truthy as it is a string
    print(f"this is truthy: {variable_one}")
else:
    print("This is falsy")


# print("What is your name?   ")
# name = input()

# if name:
#     print(f"Hello {name}, how are you?")
# elif name == int:
#     print("Letters only!")

# else:
#     print("You did not give me your name!")



list_of_cards = [
    "Jack",
    "Queen",
    "King",
    "Ace"
]

if "Ace" not in list_of_cards:
    print ("The Ace is missing")
elif "2" not in list_of_cards and 3 not in list_of_cards:
    print("The list has positive equity")

if "Ten" not in list_of_cards:
    print("Ten is missing")
    list_of_cards.append("Ten")


def add_up():
    num1 = input("First number to add? \n")
    num2 = input("Second number to add? \n")
    print(num1 + num2)                                  #will not add properly as these values are str, not ints

# add_up()

def add_up1():
    num1 = input("First number to add? \n")
    num2 = input("Second number to add? \n")

    try:
        print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")  #Converts to interger
    except:
        print("\n Error: Pleaae input a number! \n")             #"Tracing", you can put a print like this to show the "try" hasn't activated properly
        add_up1()

# add_up1()


# def add_up2():
#     num1 = input("First number to add? \n")
#     num2 = input("Second number to add? \n")

#     try:
#         if (num1 + num2).isnumeric():
#             print(num1 + num2)
#     except:
#             print("Howdy")
#     else:
#             print("Error Howdy")
#     finally:
#             print("Your done!")


light = False

def light_switch():
    global light
    if light:
        print("Shine a light!")
        light = False
    else:
        print("Who turned out the lights?")
        light = True

light_switch()
light_switch()

num = 10    #-------------------------Will not show as 10 when "show_num" is run, unless "global num" is written within function

def show_num():
    num = 13#-------------------------Despite num globally = 10, you can define num to be whatever within a function and it wont affect the global value
    print(num)                       #If you want to change the value of global num such as "num =+ 3", you would need to insert "global num"

show_num()

#Try to keep variables local, avoid assigning it as a global value as it can be hard to keep track of if you use several functions to change the value


def show_num():
    num = 13
    return num

def add_num(x):
    x = x % 3
    print(x)


#list is mutable (can change), tuples immutable (can't change)


even_nums = [2, 4, 6, 8, 10]          #Mutable
odd_nums = (1, 3, 5, 7, 9)            #Immutable

even_nums[-1] = "ten"

for z in even_nums:
    print(z)


array_example = [1, 2, 6, 7, 8, 4]
final_score = []
for numo in odd_nums:
    final_score.append(numo)

for p in final_score:
    print(p)

print(type((3,4)))                    #<class 'tuple'>
print(type([3,4]))                    #<class 'list'>

my_list = [
    1, 2, 3, 4, 5, 6, 7, 8, 9
]

print(my_list[-1])                   #9
print(my_list[0:5])                  #[1, 2, 3, 4, 5] ------ the second value represents when it will end
print(my_list[1:-2])                 #[2, 3, 4, 5, 6, 7]
print(my_list[1: -1:2])              #[2, 4, 6, 8]

# for i in range(0, 10, 1):
#     print(i)


loop_runs = True

# while loop_runs:                      #Doesn't need to be defined as True because of truthy
#     print("Run the loop")             #This will run forever as it will always be True, you would need to add a "break" to stop it

loop = True
name = "Admin"

while loop:
    if name =="Admin":
        print(f"Go away {name}!")
        break
    else:
        print(f"Welcome {name}!")
        continue



#Activity 1 

# def act1():
#     num1 = input("First number to add? \n")
#     num2 = input("Second number to add? \n")

#     try:
#         print(f"{num1} + {num2} is {(int(num1) + int(num2))}!")  
#     except:
#         print("\n Error: Pleaae input a number! \n")             
#         act1()

# act1()

#Activity 2

director = "Ivan Reitman"
writer = [
    "Dan Akyroyd", 
    "Harold Ramis", 
    "Rick Moranis"
]
starring = [
    "Dan Akroyd",
    "Bill Murray",
    "Sigourney Weaver",
    "Rick Moranis",
    "Harold Ramis",
    "Annie Potts",
    "William Atherton",
    "Ernie Hudson"
]
year = 1984
length = "1 Hour and 45 minutes"
city_base = "New York City" or "new york" or "new york city" or "New York"



def ghost_bust2():
    Q2 = input("How long is Ghostbusters? \n a. 1h 45m \n b. 2h \n c. 2h 15m\n")
    if Q2 == "a":
        print("Lucky guess...")
    elif Q2 == "b" or "c":
        print("You're very incorrect unfortunately. It was A.")
    else:
        print("Try typing 'A' 'B' 'C'")
        ghost_bust2()

def ghost_bust():
    Q1 = input("Which city is the film Ghostbusters located? \n")
    if Q1 == "new york".capitalize or "new york city".capitalize:
        print("Correct! \n")
        ghost_bust2()
    else:
        print("Do you think that was correct? Maybe do some research...")



# ghost_bust()