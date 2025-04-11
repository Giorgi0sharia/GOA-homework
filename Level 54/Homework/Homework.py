# 1. User Input Number Division
def divide_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ValueError:
        print("Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    else:
        print(f"The result of division is: {result}")

# 2. List Index Access
def access_list_index():
    my_list = ['apple', 'banana', 'cherry']
    try:
        index = int(input(f"Enter an index (0 to {len(my_list) - 1}): "))
        print(f"Element at index {index} is {my_list[index]}")
    except IndexError:
        print("Index out of range.")
    except ValueError:
        print("Please enter a valid integer index.")

# 3. Dictionary Key Access
def access_dictionary_key():
    my_dict = {'name': 'Alice', 'age': 30}
    key = input("Enter a key to access (e.g., 'name', 'age'): ")
    try:
        print(f"The value is: {my_dict[key]}")
    except KeyError:
        print("Key not found in dictionary.")

# 4. Convert String to Integer
def convert_to_integer():
    user_input = input("Enter a number to convert to integer: ")
    try:
        number = int(user_input)
        print(f"The integer is: {number}")
    except ValueError:
        print("That's not a valid integer.")

# 5. Function as Argument – Greeting
def greet():
    print("Hello! Welcome!")

def call_function(func):
    print("Calling the function passed as argument:")
    func()

# 6. Return a Function – Multiplier
def make_multiplier(factor):
    def multiplier(number):
        return number * factor
    return multiplier

# Run the functions
if __name__ == "__main__":
    print("\n--- Division Example ---")
    divide_numbers()

    print("\n--- List Index Access ---")
    access_list_index()

    print("\n--- Dictionary Key Access ---")
    access_dictionary_key()

    print("\n--- String to Integer Conversion ---")
    convert_to_integer()

    print("\n--- Function as Argument ---")
    call_function(greet)

    print("\n--- Return a Function (Multiplier) ---")
    times_three = make_multiplier(3)
    print(f"3 multiplied by 3 is: {times_three(3)}")