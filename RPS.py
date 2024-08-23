import random

# print multiline instruction
print("Winning rules  of gamr ROCK PAPER SCISSOR are :\n "
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissor -> Rock wins \n"
      + "Paper vs Scissor -> Scissor wins\n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3- Scissor \n")
    
    #take input from the user
    choice =int(input("Enter your choice"))
    
    #looping until user enter the invalid input
    
    while choice >3 or choice<1 :
        choice = int(input("enter a valid choice please ☺"))
        
    #initialize value of choice_name variable
    # corresponding to the choice value
    if choice ==1:
        choice_name="Rock"
    elif choice==2:
        choice_name="Paper"
    else:
        choice_name="Scissor"
        
    #print users choice
    print("User's choice is \n ", choice_name)
    print("Now it's computer's turn...")
    
    #Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    comp_choice=random.randint(1,3)
    
    while comp_choice == choice:
        comp_choice=random.randint(1,3)
        
    if comp_choice==1:
        comp_choice_name="Rock"
    elif comp_choice==2:
        comp_choice_name="Paper"
    else :
        comp_choice_name="Scissor"
        
    print("Computer choice is \n ",comp_choice_name)
    print(choice_name,"Vs",comp_choice_name)
    
    #we need to check for draw
    if choice==comp_choice:
        print("It's a Draw", end="")
        result="DRAW"
      
    else:
        #condition for winning
        if (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
            result = "Paper"
        elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            result = "Rock"
        elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
            result = "Scissor"
        
        print(result, "wins")
        
        # Printing either user or computer wins
        if result == choice_name:
            print("<== User Wins!! ==>")
        else:
            print("<== Computer Wins!! ==>")
            
     # Printing the final result for a draw
    if result == "DRAW":
        print("<== It's a Tie ==>")
          
  
    print("Do you want to play again? (Y/N)")
    
    #if user inputs n or Nthen condition is true 
    ans=input().lower()
    if ans=="n":
        break
    
#after coming out of of while loop we print thanks for playing 
print("Thanks For playing !! ")
        