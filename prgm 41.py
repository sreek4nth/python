import csv
with open("40.csv", newline='') as csvfile:
    d = csv.DictReader(csvfile)
    print("ROLLNO  STUDENTNAME")
    print("--------------------")
    for i in d:
        print(i['ROLLNO'],'    ',i['STUDENTNAME'])
