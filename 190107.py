def half(x):
    """
    docstring
    Return x // 2
    :param x: int.
    :return : int quotient by 2.
    """
    return x // 2

def four_times(x):
    """
    docstring
    Return 4 * x.
    :param x: int.
    :return: 4 times x.
    """
    return 4 * x

x = half(13)
print(four_times(x))

def convert(strings):
    """Converts passed in str to float.
    :param strings: str.
    :return: string converted to float.
    """
    try:
        return  float(strings)
    except ValueError:
        return "Invalid input."

print(convert("5.3"))

print(4.2 + convert("4.4"))
print(convert("sori"))

"heLlo".upper()
"Hello".replace("o","@")
