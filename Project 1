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

def separator():
    print('-'*50)

def login():
    print('Welcome to the app. Please log in:')
    user = input('USERNAME: ')
    password = input('PASSWORD: ')
    if user in list(defined_users.keys()) and password == defined_users[user]:
        return True
    else:
        return False

def word_count(text):
    print(f'There are {len(text.split())} words in selected text')

def titlecase(text):
    result = 0
    for i in text:
        if i.istitle():
            result += 1
    print(f'There are {result} titlecase words')

def uppercase(text):
    text=text.split()
    result = 0
    for i in text:
        if i.isupper():
            result +- 1
        
    print(f'There are {result} uppercase words')

def lowercase(text):
    text=text.split()
    result = 0
    for i in text:
        if i.islower():
            result += 1
    print(f'There are {result} lowercase words')

def numeric(text):
    text=text.split()
    result = 0
    for i in text:
        if i.isnumeric():
            result += 1
    print(f'There are {result} numeric words') 

def frequency(text):
    text = text.replace(',','')
    text = text.replace('.','')
    text = text.split()
    freq = {}
    for i in text:
        if len(i) in freq:
            freq[len(i)] += 1
        else:
            freq.setdefault(len(i),1)
    ordered = list(freq.keys())
    ordered.sort()
    for i in ordered:
        print(f'{i}: ','*' * freq[i],freq[i])

def numbers_sum(text):
    text=text.split()
    result = 0
    for i in text:
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
    text = library[int(input(f'Enter a number between 1 and {len(library)} to select: '))-1]
    separator()
    word_count(text)
    titlecase(text)
    uppercase(text)
    lowercase(text)
    numeric(text)
    separator()
    frequency(text)
    separator()
    numbers_sum(text)
    separator()

program(TEXTS)


