# variable_one = 10

# print (type(10))


# class Int():
#     pass

# new_obj = Int()

# print(type(new_obj))




# "Examlple String".lower()
# new_obj.func_example()

# list_example = []


# 3.14152.as_integer_ratio


# def func_2 ():
#     return "this is function 2"

# class Blah():
#     def function_3():
#         return "Boo"


# #Objects have two things associated with them. Attributes - What it has, and Method - What it does


# car_one = {
#     "name": "Andy the Aygo",
#     "colour": "blue",
#     "brand": "Toyota",

# }



class Person():
    def __init__(self, name, age, height):      #arguments, in this case 4
        #constructor method
        self.name = name              #using "name" rather than "None" makes having a name a requirement to creating a new character with this class
        self.age = age
        self.profession = None
        self.height = height
        self.hobbies = []
    def set_hair(self, person_hair):
        self.hair = person_hair
    def get_hair(self):
        print(self.hair)
    def set_hobby(self, person_hobby):
        self.hobbies.append(person_hobby)
    def get_hobby(self):
        print(self.hobbies)

person_x = Person("George", 81, "5'3")

# print(person_x.age)


# new_person = Person("Chris")


# print(new_person.name)

# jay_person = Person("Jay")

# jay_person.age = 31
# jay_person.profession = "Intstructor"

# print(jay_person.profession)

# # new() # looks like a function

# # New() # looks like a class

#from person import Person

#lima = person("Liam")

def set_hair(self, person_hair):
    self.hair = person_hair