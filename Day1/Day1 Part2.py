file = open("input.txt", "r").readlines()

matches = False
frequencies = []
output = 0

frequencies.append(output)

while matches == False:
    for l in file:
        output = output + int(l)

        matches = output in frequencies

        if matches == True:
            break
        
        frequencies.append(output)
        
print(output)
