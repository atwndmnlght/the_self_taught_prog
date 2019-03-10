def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(3)
even_odd(432)

def even_odd():
    n = input("type a number:")
    n = int(n)
    if n % 2 == 0:
        print("n is even.")
    else:
        print("n is odd.")

for i in range(3):
    even_odd()

def add_it(x, y=10):
    return x + y

result = add_it(3)
print(result)

z = 100

def f():
    global z
    z += 1
    print(z)

f()
