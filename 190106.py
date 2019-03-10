try:
    a = input("type a number:")
    b = input("type another:")
    a = int(a)
    b = int(b)
    print(a/b)
except (ZeroDivisionError,ValueError):
    print("Invalid input.")

def add(x, y):
    """
    docstring
    Returns x + y.
    :param x: int.
    :param y: int.
    :return: int sum of x and y.
    """
    return x + y

def squared(x):
    return x ** 2

print(squared(3))

def print_string(string):
    print(string)

print_string("hello")

def quadratic_equation(a,b,c,feet = False, binary = False):
    anser1 = (-b + (b*b -4*a*c)**0.5) /(2 * a)
    anser2 = (-b - (b*b -4*a*c)**0.5) /(2 * a)

    if feet == True:
        anser1 = anser1 / 30
        anser2 = anser2 / 30
    print(anser1)
    print(anser2)

quadratic_equation(1,0,4)
