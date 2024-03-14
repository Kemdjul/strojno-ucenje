fileName = input("Unesite ime datoteke: ")

print(fileName)

if (fileName != "mbox.txt" and fileName != "mbox-short.txt"):
    print("Ta datoteka ne postoji")
    exit()

fopen = open("C:/Users/student/Documents/kemal-strojno/lv1/" + fileName)
totalConfidence = 0.0;
countConfidence = 0;

for line in fopen:
    line = line.rstrip()
    
    words = line.split(' ')
    if (words[0] == 'X-DSPAM-Confidence:'):
        totalConfidence += float(words[1])
        countConfidence += 1
        
print("Average X-DSPAM-Confidence: " + str(totalConfidence / countConfidence))