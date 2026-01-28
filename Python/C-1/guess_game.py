import random

choice = 'y'               # Variable to store the choice of the user, Whether he wants to play again

print(" ")
print("-------------NUMBER GUESSING GAME -------------")
print(" ")

while choice == 'y':                      # Loop to make the game run as long as the choice is 'y'
    rand_num = random.randint(0,10)       # Generating a random integer from 0 to 10

    chance = 0                            # Counting the number of the chances that the user has used

    while chance<3:                       # Loop to keep asking for the user_num as long as the chance is less than 3

        chance += 1                       # Incrementing chance by 1

        print(f"------------------ Chance {chance} ------------------")

        

        while True:                                             # Loop to keep asking for the input as long as the the input is not valid
            user_num = input("Enter a number from 0 to 10 : ")
            try:                                                 # Try and except block to except the ValueError
                user_num = int(user_num)
                break
            except ValueError:
                
                print("Error!, Enter a valid number!!!")


        if user_num == rand_num:                              # If-else statements to check if the number entered by the user is correct
            print("Correct Guess")
            print(f"The number is indeed {rand_num}")
            break
        else:
            print("Wrong Guess")
            print(" ")
            if chance == 3:
                print(f"The correct number is {rand_num}")

    
    print(" ")
        
    
    choice = input("Would you like to play again ? (y for (yes) /any other symbol for (no))  : ")   #Asking the user if he wants to play again
print("Exiting the game...")      # Message showing the player that the game has stopped
    




