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
    print("Do you want to continue with add commit push? (y to continue):")
    confirm = input()
    if confirm !="y":
        print("Canceling", confirm)
        quit()
    else: acp()
    

if numofArgs >= 2:
    if sys.argv[1] == "-m":
        commitMessage = input('Enter your message: ')
        commitMessage = '"' + commitMessage + '"'
        acp()
    elif sys.argv[1] != "-f":
       acp()


    
if numofArgs == 3:
    if sys.argv [2] != '-f':
        if sys.argv [1] == "-m":
            commitMessage = input('Enter your message: ')
            commitMessage = '"' + commitMessage + '"'
            acp()

