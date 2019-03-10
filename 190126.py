import csv

with open("film.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for list_row in [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]:
        w.writerow(list_row)

