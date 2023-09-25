
def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_second[p2]):
        print("draw")
    elif(player_one[p1]=="rock" and player_second=="scissor"):
        print("player one wins")
    elif(player_one[p1]=="rock" and player_second=="paper"):
        print("player second wins")
    elif(player_one[p1]=="paper" and player_second=="scissor"):
        print("player second wins")
    elif(player_one[p1]=="paper" and player_second=="rock"):
        print("player one wins")
    elif(player_one[p1]=="scissor" and player_second=="rock"):
            print("player second wins")
    elif(player_one[p1]=="scissor" and player_second=="paper"):
            print("player second wins")
 

player_one={0:'rock',1:'paper',2:'scissor'}
player_second={0:'paper',1:'scissor',2:'rock'}
while(1):
    num1=input("player one enter your choice")
    num2=input("player second enter your choice")
    bit1=int(input("enter your secret bit position"))
    bit2=int(input("enter your sercret bit positon"))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input("do you want to continue? y/n")
    if(ch=='n'):
        break

