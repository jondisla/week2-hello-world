# Jonathan Disla
    
# 1. greets the user in English

print('Hello user!')
print('Type the number 1, 2 or 3 to choose your spoken language.') 

# 2. asks the user to choose from 1 of 3 spoken languages

print('1. Spanish')
print('2. English')
print('3. French')

lang = input()
lang = int(lang)

# 3. displays the greeting in the chosen language
if lang == 1:
    print('Hola mundo!')

elif lang == 2:
    print('Hello world!')

elif lang == 3:
    print('Salut monde!')
    