# Erick Hernandez
# Add Commit Push
# Intro To Computer Science
# Credit to Eric Pogue for helping on getting started

import os
import sys
# I commented out this part because it wouldn't make sense to assign an alias each time it's run
# os.system(echo 'alias g5="cd/Users/kairos8ight/Lewis/cpsc-20000/sprint5/add-commit-push"' >> ~/.zshrc)
# os.system(echo 'alias acp="python3 /Users/kairos8ight/Lewis/cpsc-20000/sprint5/add-commit-push"' >> ~/.zshrc)
# os.system('source ~/.zshrc)

# text colors, for clarity and accessibility
red = '\033[91m'
yellow = '\033[93m'
green = '\033[92m'
magenta = '\033[95m'
reset = '\033[0m'

# default value for commit message
commitMessage = '"Update files"'

numofArgs = len(sys.argv)
print('Total Arguments Passed: ', numofArgs)

print(f'{green}git status{reset}')
os.system('git status')

# defining the add commit push portion
def acp():
    print(f'{magenta}Add, Commit, Push\n {reset}')
    print(f'{green}git add -A {reset}\n')
    os.system('git add -A')
    print(f'{green}git commit -m  + {commitMessage} {reset}\n')
    os.system('git commit -m' + commitMessage)
    print(f'{green}git push {reset}\n')
    os.system('git push')
    print(f"{magenta} Add, Commit, Push: Complete {reset}")

# one argument 
if numofArgs == 1:
    print(f"{yellow}Do you want to continue with add commit push? git add -A, git commit -m {commitMessage} and git push will be run. (y to continue):{reset}")
    confirm = input()
    if confirm !="y":
        print(f'{red} Canceling, {confirm} {reset}')
        quit()
    else: acp()
    
# two arguments
if numofArgs == 2:
    if sys.argv[1] == "-m":
        commitMessage = input(f'{green} Enter your message: {reset}')
        commitMessage = '"' + commitMessage + '"'
        print(f"{yellow}Do you want to continue with add commit push? git add -A, git commit -m {commitMessage} and git push will be run. (y to continue):{reset}")
        confirm = input()
        if confirm !="y":
            print(f'{red}Canceling, {confirm} {reset}')
    elif sys.argv[1] == "-f":
       acp()


# three arguments
if numofArgs == 3:
    if sys.argv [2] == "-m":
            commitMessage = input(f'{green}Enter your message: {reset}')
            commitMessage = '"' + commitMessage + '"'
            if sys.argv [1] == "-f":
                acp()
    elif sys.argv [1] == "-m":
            commitMessage = input(f'{green}Enter your message: {reset}')
            commitMessage = '"' + commitMessage + '"'
            if sys.argv [2] == "-f":
                acp()



