favarite_musicians = list()
favarite_musicians = ["Bump of chicken","people in the box", "RADWIMPS"]

locations =((129.52,32.45),)

me = {"height":175,"weight":60, "favarite_color": "blue"}

key = input("key?:")
if key in  me:
    print(me[key])
else:
    print("It is invalid")

music = {"Bump of chicken": ["Ray", "Hello,world","No hit no run"],"RADWIMPS"\
         :["me me she","your name"]}
print(music["RADWIMPS"])

