print("A screaming comes across the sky.".replace("s","$"))

print("Hemingway".index("m"))
my_favarite_script = "立ち上がり言った．'今夜星を見に行こ'"
print(my_favarite_script)
print("three " + "three " + "three")
print("three " * 3)

a = "四月の晴れた寒い日で，時計がどれも13時を売っていた．"
print(a[:a.index("，")])

sentence = "It was a bright cold day in April, and the clocks were striking thirteen."
slce = sentence[0:33]
print(slce)

tv = ["GOT","Narcos","vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)
