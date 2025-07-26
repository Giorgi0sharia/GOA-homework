# Kata 1: Array plus array
# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b
def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


# Kata 2: Welcome!
# https://www.codewars.com/kata/545a4c5a61aa4c6916000755
def greet(language):
    greetings = {
        'english': 'Welcome',
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }
    return greetings.get(language, 'Welcome')


# Kata 3: Multiply Word in String
# https://www.codewars.com/kata/5a03b3f6a1c9040084001765
def explode(s):
    return ''.join(char * int(char) for char in s)


# Kata 4: How many arguments
# https://www.codewars.com/kata/55d1d6d5955ec6365400006d
def args_count(*args):
    return len(args)


# Kata 5: Basic Training: Add item to an Array
# https://www.codewars.com/kata/511f11d355fe575d2c000001
def add(arr, item):
    arr.append(item)
    return arr


# Example usage (for testing)
if __name__ == "__main__":
    print(array_plus_array([1, 2, 3], [4, 5, 6]))  # 21
    print(greet('french'))  # Bienvenue
    print(explode("312"))  # "333122"
    print(args_count(1, 2, 3))  # 3
    print(add([1, 2, 3], 4))  # [1, 2, 3, 4]
