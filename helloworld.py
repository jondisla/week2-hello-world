    # Jonathan Disla
    
print('Hello user!')
    # 1. greets the user in English

print('Type the number 1, 2 or 3 to choose your spoken language.')
    # 2. asks the user to choose from 1 of 3 spoken languages
    # Used the print function to write the instructions and the choices

print('1. Spanish')
print('2. English')
print('3. French')

lang = input()
    #creates the lang variable that stores the input(1, 2 or 3) entered by user.
    #This will give the lang variable a new value.

lang = int(lang)
    #converts the new value inserted by the user assigned to lang which is in
    #string format ('1','2'or '3') into an integer (1, 2 or 3) to be used in the
    #lang equal to if statements following...

    # 3. displays the greeting in the chosen language
if lang == 1: #if the lang variable is equal to the integer 1, print...
    print('Hola mundo!')

elif lang == 2:
    print('Hello world!')

elif lang == 3:
    print('Salut monde!')

# 4. exits
import sys
sys.exit()
    
