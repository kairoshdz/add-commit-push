import os
import sys
# I commented out this part because it wouldn't make sense to assign an alias each time it's run
# os.system(echo 'alias g5="cd/Users/kairos8ight/Lewis/cpsc-20000/sprint5/add-commit-push"' >> ~/.zshrc)
# os.system(echo 'alias acp="python3 /Users/kairos8ight/Lewis/cpsc-20000/sprint5/add-commit-push"' >> ~/.zshrc)
# os.system('source ~/.zshrc)

print("testing")
numofArgs = len(sys.argv)
print('Total Arguments Passed: ', numofArgs)

if numofArgs == 2:
    print("Do you want to continue with add commit push? (y to continue):")
    confirm = input()
    if confirm !="y":
        print("Canceling", confirm)
    quit()
    

if numofArgs >= 3:
    if sys.argv[1] == "-m":
        commitMessage = input('Enter your message: ')
    elif sys.argv[1] != "-f":
        print("Do you want to continue with add commit push? (y to continue):")
        confirm = input()
        if confirm !="y":
            print("Canceling", confirm)
    else:
        commitMessage = '"Update files"'

    
if numofArgs >= 4:
        if sys.argv [3] != '-f':
            print("Do you want to continue with add commit push? (y to continue):")
            confirm = input()
        if confirm !="y":
            print("Canceling", confirm)
        quit()

print('Add, Commit, Push\n')
print('git status\n')
os.system('git status')
print('git add -A')
os.system('git add -A')
print('git commit -m + "{commitMessage}"')
os.system('git commit -m "{commitMessage}"')
print('git push')
os.system('git push')