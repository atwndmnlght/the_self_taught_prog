import os
os.path.join("Uswers", "bob", "st.txt")

st = open("st.txt", "w", encoding="utf-8")
st.write("Hi from Python! やあ")
st.close()

with open("st2.txt", "w") as f:
    f.write("Hi from Python!")

my_list = []

with open("st.txt", "r", encoding="utf-8") as f:
    my_list.append(f.read())

print(my_list)
