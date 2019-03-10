author = "Camus"

for i in range(5):
    print(author[i])

input1 = input("what:")
input2 = input("who:")
r = "私は昨日{}を書いて，{}に送った！".format(input1,input2)
print(r)

print("aldous Huxley was born in 1894.".capitalize())
w5h1 = "Where now? Who now? When now?".split("?")
print(w5h1)

lst = "Where now? Who now? When now?".split("?")
print(lst)

a = ["The","fox", "jumped", "over", "the", "fence", "."]
a = " ".join(a)
print(a[:-2] +".")
