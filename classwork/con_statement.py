
user_input = input("Enter a number: ")

try:
    
    num = float(user_input)
    
    
    if num == int(num):
        print("The number is an integer.")
    else:
        
        decimal_component = num - int(num)
        print(f"The number is a float with decimal component: {decimal_component}")
except ValueError:
    print("The input is not a valid number.")
