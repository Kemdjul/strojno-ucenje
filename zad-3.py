list = []

def average(list):
    total = 0;
    for number in list:
        total += number
        
    return total / len(list)

while True:
    userInput = input()
    
    if (userInput.lower() == "done"):
        break;
    
    try:
        inputCastToInt = int(userInput)
        list.append(inputCastToInt)
    except:
        print("Not a number")
   
print("Unijeli ste " + str(len(list)) + " brojeva")
print("Srednja vrijednost: " + str(average(list)))
print("Minimalna vrijednost: " + str(min(list)))
print("Maksimalna vrijednost: " + str(max(list)))
print("Sortirana lista:")
list.sort()
print(list)