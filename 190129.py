class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")


or1 = Orange(10,"dark orange")
print(or1)
print(or1.weight)
or1.weight = 25
print(or1.weight)
