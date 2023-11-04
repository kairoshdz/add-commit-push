#Erick Hernandez
#Add Commit Push
#Intro To Computer Science
#Credit to Eric Pogue for helping on getting started

import os
import sys
# I commented out this part because it wouldn't make sense to assign an alias each time it's run
# os.system(echo 'alias g5="cd/Users/kairos8ight/Lewis/cpsc-20000/sprint5/add-commit-push"' >> ~/.zshrc)
# os.system(echo 'alias acp="python3 /Users/kairos8ight/Lewis/cpsc-20000/sprint5/add-commit-push"' >> ~/.zshrc)
# os.system('source ~/.zshrc)

#text colors, for clarity and accessibility
red = '\033[91m'
yellow = '\033[93m'
green = '\033[92m'
reset = '\033[0m'

#default value for commit message
commitMessage = '"Update files"'

numofArgs = len(sys.argv)
print('Total Arguments Passed: ', numofArgs)

print('git status\n')
os.system('git status')

def acp():
    print('Add, Commit, Push\n')
    print('git add -A')
    os.system('git add -A')
    print('git commit -m ' + commitMessage)
    os.system('git commit -m' + commitMessage)
    print('git push')
    os.system('git push')

if numofArgs == 1:
    print(f"{red}Do you want to continue with add commit push? (y to continue):{reset}")
    confirm = input()
    if confirm !="y":
        print("Canceling", confirm)
        quit()
    else: acp()
    

if numofArgs >= 2:
    if sys.argv[1] == "-m":
        commitMessage = input(f'{green} Enter your message: {reset}')
        commitMessage = '"' + commitMessage + '"'
        print(f"{yellow}Do you want to continue with add commit push? (y to continue):{reset}")
        confirm = input()
        if confirm !="y":
            print(f'{red}Canceling, confirm {reset}')
            acp()
    elif sys.argv[1] != '-f':
       acp()


    
if numofArgs == 3:
    if sys.argv [2] != "-f":
        if sys.argv [1] == "-m":
            commitMessage = input(f'{green}Enter your message: {reset}')
            commitMessage = '"' + commitMessage + '"'
            acp()

