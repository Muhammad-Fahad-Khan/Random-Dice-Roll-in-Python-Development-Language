# Hi everyone how are you?
# In today video we are ggoing to make a random dice roll number by using python development

# So let's get Started

import random   # this library is used to get random numbers from buildin func

while True:    # This is for infinite time run program
    print("""Do you want to Roll Dice? 
      If yes then  Enter \"Yes" or \"y\" to Roll a Dice.
      Othrwise it will stopped.""")
    opt = input("Enter: ")      # this is for user choose to roll a dice oor not
    if opt == 'Yes' or 'y':
        output = random.randint(1,6)       # This will allow to select number between in 1 to 6
    
    if output == 1:
        print("""
 _______
|       |
|   *   |
|_______|
""")
    elif output == 2:
        print("""
 _______
|  *    |
|       |
|____*__|
""")
    elif output == 3:
        print("""
 _______
| *     |
|   *   |
|_____*_|
""")
    
    elif output == 4:
        print("""
 ________
|  *   * |
|        |
|__*___*_|
""")
        
    elif output == 5:
        print("""
 _______
| *   * |
|   *   |
|_*___*_|
""")

    elif output == 6:
        print("""
 ________
|  *   * |
|  *   * |
|__*___*_|
""")
    else:
        print("Thanks For Playing With Coding By Kingsamn!!") 
        break   # This Will Break the While Loop When if you not enter Yes, y   



            # Thank You For Watching & And Like This Video..
            #  Don't Forget To Subscribe "Coding By Kingsman" 