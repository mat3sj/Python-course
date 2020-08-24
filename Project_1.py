'''
author = Mates - Martin Jasan  
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
defined_users = {'bob':'123','ann':'pass123','mike':'password123','liz':'pass123'}
splitted_text = []
def separator():
    print('-'*50)

def login():
    print('Welcome to the app. Please log in:')
    user = input('USERNAME: ')
    password = input('PASSWORD: ')
    if user in defined_users and password == defined_users[user]: # Changed from 'in list(defined_users.keys())'
        return True
    else:
        return False

def word_count(splitted_text):
    print(f'There are {len(splitted_text)} words in selected text')

def titlecase(splitted_text):  # logical mistake - it was counting all capital letters
    result = 0
    for i in splitted_text:
        if i[0].istitle(): # fix?
            result += 1
    print(f'There are {result} titlecase words')

def uppercase(splitted_text):
    result = 0
    for i in splitted_text:
        if i.isupper():
            result +- 1
        
    print(f'There are {result} uppercase words')

def lowercase(splitted_text):
    result = 0
    for i in splitted_text:
        if i.islower():
            result += 1
    print(f'There are {result} lowercase words')

def numeric(splitted_text):
    result = 0
    for i in splitted_text:
        if i.isnumeric():
            result += 1
    print(f'There are {result} numeric words') 

def frequency(splitted_text):
    freq = {}
    for i in splitted_text:
        if len(i) in freq:
            freq[len(i)] += 1
        else:
            freq.setdefault(len(i),1)
    ordered = list(freq.keys())
    ordered.sort()
    for i in ordered:
        print(f'{i}: ','*' * freq[i],freq[i])

def numbers_sum(splitted_text):
    result = 0
    for i in splitted_text:
        if i.isnumeric():
            result += float(i)
    print(f'If we summed all the numbers in this text we would get: {result}')

def program(library):
    separator()
    if not login():
        print ('Your credentials are not valid')
        return
    separator()
    print(f'We have {len(library)} texts to be analyzed.')
    user_choice = int(input(f'Enter a number between 1 and {len(library)} to select: '))-1
    if user_choice in range(int(len(library)-1)):
        text = library[user_choice]
    else:
        print ('You have entered text number which is out of range, please run the task again')
        return
    
    splitted_text = text.replace(',','')
    splitted_text = splitted_text.replace('.','')
    splitted_text = splitted_text.split()

    separator()
    word_count(splitted_text)
    titlecase(splitted_text)
    uppercase(splitted_text)
    lowercase(splitted_text)
    numeric(splitted_text)
    separator()
    frequency(splitted_text)
    separator()
    numbers_sum(splitted_text)
    separator()

program(TEXTS)


