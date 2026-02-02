def print_pattern(*args) :
    user_input = int(input("enter ther number:"))
    for i in range (user_input) :
        pattern = "*" * (2*i-1)
        
    
        print(" " * (user_input -i-1),pattern)

        

print_pattern()