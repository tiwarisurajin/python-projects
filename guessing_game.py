print ("\t\t\tGuess The Number\n")
while True :
    try :
        game_mode_input = int(input("press 1 for Normal and 2 for Casino style: "))
    except :
        print("Invalid Input!")
        continue
    if game_mode_input == 1 :
        print("Welcome to casual mode.")
        correct_number1 = 6
        try :
            casual_mode1 =int(input("Guess the number between 1 to 10: "))
        except :
            print("Invalid Input!")
            continue
        if casual_mode1 == correct_number1 :
            print(f"You guessed it right!,{casual_mode1} is correct number ")
        elif casual_mode1 < correct_number1 :
             print(f"{casual_mode1} is smaller than the Number")
        elif casual_mode1 > correct_number1 :
             print(f"{casual_mode1} is greater than the Number")

        exit1 =input("To exit press x: ")
        exit1=exit1.lower()
        if exit1 != "x" :
         print()
        else :
            break

    elif game_mode_input == 2 :
        
        print("Welcome to casino  mode.")
        import random
        correct_number2 = random.randint(1,10)
        try :
            casual_mode2 =int(input("Guess the number between 1 to 10: "))
        except :
            print("Invalid Input!")
            continue
        if casual_mode2 == correct_number2 :
            print(f"You guessed it right!,{casual_mode2} is correct number ")
        elif casual_mode2 < correct_number2 :
             print(f"{casual_mode2} is smaller than the Number")
        elif casual_mode2 > correct_number2 :
             print(f"{casual_mode2} is greater than the Number")

        exit2 =input("To exit press x: ")
        exit2=exit2.lower()
        if exit2 != "x" :
            print()
        else:
            break    
