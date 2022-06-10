

#Dictionaries are a data type, unlike the usual kind of dictionary, that are used to stores data 


from cgitb import grey


my_cat = ["Salem", "black", "sassy"]

my_cat1 = {
    "name":"Ziggy", "colour":"white", "mood":"shy"
}

dict_of_players = {
    1:"Bob", 2:"Steve", 3:"Zander", 4:"Helena", 5:"Prudence"
}

print("My Cat is a little " + my_cat1["mood"])

for x in my_cat1:
    print(x)                                  #will print the values, so "name", "colour", "mood"

my_cat1["colour"] = "grey"                    #updates the value within the dictionary from "white" to "grey"

print(my_cat1["colour"])


#Activity 1   -   Dictionary of deception game players

complex_dict = {
    "one" : {
        "name":"Bob",
        "age": 44,
        "gender": "Male",
        "traitor": True
    },
    "two" : {
        "name":"Steve",
        "age": 27,
        "gender": "Male",
        "traitor": False
    },
    "three" : {
        "name":"Zander",
        "age": 19,
        "gender": "Male",
        "traitor": False
    },
    "four" : {
        "name":"Helena",
        "age": 23,
        "gender": "Female",
        "traitor": False
    },
    "five" : {
        "name":"Prudence",
        "age": 9,
        "gender": "Female",
        "traitor": True
    }
}


print(list(complex_dict.get("one").values()))           #"Bob", "44", "Male", True will come up


for h in complex_dict.keys():                           #one,two,three,four,five
    print(h)

for h in complex_dict.values():                         #{'name': 'Bob', 'age': 44, 'gender': 'Male', 'traitor': True}
                                                        # {'name': 'Steve', 'age': 27, 'gender': 'Male', 'traitor': False}
                                                        # {'name': 'Zander', 'age': 19, 'gender': 'Male', 'traitor': False}
                                                        # {'name': 'Helena', 'age': 23, 'gender': 'Female', 'traitor': False}
                                                        # {'name': 'Prudence', 'age': 9, 'gender': 'Female', 'traitor': True}
    print(h)

for h in complex_dict.items():                          #('one', {'name': 'Bob', 'age': 44, 'gender': 'Male', 'traitor': True})
                                                        # ('two', {'name': 'Steve', 'age': 27, 'gender': 'Male', 'traitor': False})
                                                        # ('three', {'name': 'Zander', 'age': 19, 'gender': 'Male', 'traitor': False})
                                                        # ('four', {'name': 'Helena', 'age': 23, 'gender': 'Female', 'traitor': False})
                                                        # ('five', {'name': 'Prudence', 'age': 9, 'gender': 'Female', 'traitor': True})
    print(h)


complex_dict["five"].setdefault("adult", False)         #Will assign Prudence the value of adult = false
complex_dict["five"].setdefault("name", "Belinda")      #Belinda Will NOT assign, as it already exists as Prudence, "setdefault" cannot alter existing values

for x in complex_dict.items():
    print(x)

complex_dict["one"].pop("gender")                       #Removes the gender of Bob
print(complex_dict)

#Activity 2


countries_dict = {
    "one" : {
        "country" : "United Kingdom",
        "capital" : "London",
        "flag colour" : " blue " + " red " + " white ",
        "eu" : False
    },
        "two" : {
        "country" : "Germany",
        "capital" : "Berlin",
        "flag colour" : " yellow " + " red " + " black ",
        "eu" : True
    },
        "three" : {
        "country" : "Italy",
        "capital" : "Rome",
        "flag colour" : " green " + " red" + " white ",
        "eu" : True
    },
        "four" : {
        "country" : "France",
        "capital" : "Paris",
        "flag" : " blue " + " red " + " white ",
        "eu" : True
    },
        "five" : {
        "country" : "Spain",
        "capital" : "Madrid",
        "flag" : " yellow " + " red ",
        "eu" : True
    }
}

countries_dict.setdefault("Japan", "Tokyo")
countries_dict.setdefault("China", "Beijing")

for x in countries_dict.items():                #Will print the dictionary chronologically           
    print(x)                                    #('one', {'country': 'United Kingdom', 'capital': 'London', 'flag colour': 'blueredwhite', 'eu': False})
                                                # ('two', {'country': 'Germany', 'capital': 'Berlin', 'flag colour': 'yellowredblack', 'eu': True})
                                                # ('tree', {'country': 'Italy', 'capital': 'Rome', 'flag colour': 'greenredwhite', 'eu': True})
                                                # ('four', {'country': 'France', 'capital': 'Paris', 'flag': 'blueredwhite', 'eu': True})
                                                # ('five', {'country': 'Spain', 'capital': 'Madrid', 'flag': 'yellowred', 'eu': True})
                                                # ('Japan', 'Tokyo')
                                                # ('China', 'Beijing')



#Activity 3


# music_dict = {
#     "one" : {

#     }
# }



# list_of_music = []

# list_of_music[0]["artist"] = "xyz"
# list_of_music[0]["song"]
# list_of_music[0]["genre"]
# list_of_music[0]["year"]

