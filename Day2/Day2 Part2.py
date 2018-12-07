file = open("input.txt", "r").readlines()

firstCorrect = ""
secondCorrect = ""
correctIndex = 0

for l in file:
    for nl in file:
        if l == nl:
            continue

        lChars = list(l)
        nlChars = list(nl)
        
        count = 0
        differences = 0

        for c in lChars:
            if differences > 1:
                break

            if c != nlChars[count]:
                differences = differences + 1
                if differences == 1:
                    correctIndex = count

            count = count + 1

        if differences != 1:
                continue

        if differences == 1:
            firstCorrect = l
            secondCorrect = nl
            break

    if differences == 1:
        break 

result = list(firstCorrect)

del result[correctIndex]

print("".join(result))
    