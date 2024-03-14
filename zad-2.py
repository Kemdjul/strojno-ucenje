try:
    grade = float(input("Unesite ocjenu izmedju 0 i 1:"))
    print(grade);
    if (grade < 0 or grade > 1):
        raise Exception("Number not in between 0 and 1")
except:
    print("Input error")
    exit()

if (grade > 0.9):
    print("Vasa rezultanta ocjena je A")
elif (grade > 0.8):
    print("Vasa rezultanta ocjena je B")
elif (grade > 0.7):
    print("Vasa rezultanta ocjena je C")
elif (grade > 0.6):
    print("Vasa rezultanta ocjena je D")
else:
    print("Vasa rezultanta ocjena je F")