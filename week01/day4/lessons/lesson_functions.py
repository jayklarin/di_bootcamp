def say_hello(language:str = 'EN', name:str = 'John Doe'):
    '''here is my docstring'''
    if language == 'PT':
        print(f'hello in {language} for {name}')
    elif language == "HE":
        print(f'hello in {language} for {name}')
    elif language == 'EN':
        print(f'message in {language} for {name}')
    else:
        print(f"{name}, this message is in and unknown langugae, {language}.")

say_hello("HE",'Bob')
say_hello()
say_hello("FR" )
say_hello(name='joe', language='PT')
say_hello(name = 'Joe')
say_hello("EN")

# create a function called country_info that receives a country name as argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed

# def country_info(country_name:str = 'Naboo'):
#     '''returns a capital from a country name'''
#     if country_name == 'Naboo':
#         print(f'the capital of {country_name} is Theed')
#     elif country_name == "America":
#         print(f'the capital of {country_name} is Washington')
#     elif country_name == "Israel":
#         print(f'the capital of {country_name} is Jerusalem')
#     else:
#         print(f"I'm just a dumb computer, I don't know the capital of {country_name}")
# print()
# country_info('Naboo')
# country_info('America')
# country_info('Israel')
# country_info('Panama')


def country_info(country_name:str = 'Naboo'):
    '''returns a capital from a country name'''
    if country_name == 'Naboo':
        print(f'the capital of {country_name} is Theed')
    elif country_name == "America":
        print(f'the capital of {country_name} is Washington')
    elif country_name == "Israel":
        print(f'the capital of {country_name} is Jerusalem')
    else:
        print(f"I'm just a dumb computer, I don't know the capital of {country_name}")
    return country_name
print()
country_info('Naboo')
country_info('America')
country_info('Israel')
country_info('Panama')
print(country_info()) # after returning country_name in the function, it prints return value.

# scope inside function is locked inside
# Local scope: inside function
def current_age():
    age = 15
    return age
#age = current_age()
print(current_age())
#print(age) # doesn't work

#scope outside the function can be accessed inside the function
# Global scope: not in the scope of the function (it is in the main file)
# we can access without modifying
# we can NOT modify it if we don't use the 'global' keyword
bar_mitzvah = 13
def current_age():
    age = 13
    if age == bar_mitzvah:
        print('Mazel Tov!!!')
    return age

print(current_age())


###### function and data structures
# lists, tuples, sets and dictionary

students = ['Harry','Hermione','Ron','Luna']
def welcome():
    for name in students:
        print(f'Welcome {name} to Hogwarts')
welcome()
print()
print(welcome())

# def get_house():
#     for i, name in enumerate(students):
#         students[i] = f'{name} - Griffyndor'
#     if name == 'Luna'


countries_capitals = {
        "USA": "Washington, D.C.",
        "UK": "London",
        "Canada": "Ottawa",
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Naboo": "Theed"
}

def country_info(country_name):
    for country_name in countries_capitals.values():
        if country_name in countries_capitals.values():
            return countries_capitals
print(country_info('Germany'))
