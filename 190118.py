number_list = [2,41,83,5,19]

while True:
    answer = input("type number(quit> q):")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Please type a number or q to quit.")
    if answer in number_list:
        print("yes")
    else:
        print("no")
    
list_1 = [8, 19, 148, 4]
list_2 = [9, 1, 33, 83]
answer = []
for i in list_1:
    for j in list_2:
        answer.append(i * j)

print(answer)
        
