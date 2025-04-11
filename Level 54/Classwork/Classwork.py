def division_calculator():
    try:

        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        result = numerator / denominator
        print(f"The result of {numerator} divided by {denominator} is: {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers.")
    
    except ZeroDivisionError:
        raise ValueError("Error: Cannot divide by zero.")
    
    finally:
        print("Operation complete.")



def apply_to_list(func, values):
    return [func(value) for value in values]


def square(x):
    return x * x


values = [1, 2, 3, 4, 5]
squared_values = apply_to_list(square, values)
print(squared_values)