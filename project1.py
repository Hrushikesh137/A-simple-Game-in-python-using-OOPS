'''
1 for Paper 
-1 for Stone
0 for Cisor
'''
computer=-1 
youstr= input("Enter your choice: ")
youDict={"p":1,"s":-1,"c":0}
reverseDict={1:"Paper",-1:"Stone",0:"Cisor"}
you=youDict[youstr]

print(f"you choice {reverseDict[you]}\nComputer choice {reverseDict[computer]} ")
if(computer == you):
    print("Its a draw")
else:
    if(computer==-1 and you==1):
        print("you win!")
    elif(computer==-1 and you==0):
        print("You Lose!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    elif(computer==1 and you==0):
        print("You Win!")
    elif(computer==0 and you==-1):
        print("You Win!")
    elif(computer==0 and you==1):
        print("You Lose!")
    
    else:
        print("Something went wrong")

