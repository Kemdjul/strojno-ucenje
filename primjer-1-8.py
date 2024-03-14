line = "Dobrodosli u nas grad"
if line.startswith("Dobrodosli"):
    print("Prva rijec je Dobrodosli")

elif line.startswith("dobrodosli"):
    print("Prva rijec je dobrodosli")

line.lower()
print(line)

data = "From: pero@yahoo.com"
atpos = data.find("@")
print(atpos)
