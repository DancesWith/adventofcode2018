file = open("input.txt", "r").readlines()

appearsTwice = 0
twiceMatched = False
appearsThree = 0
threeMatched = False

for l in file:
    chars = list(l)

    twiceMatched = False
    threeMatched = False

    for c in chars:
        count = l.count(c)
                
        if count == 2:
            if twiceMatched == False:
                appearsTwice = appearsTwice + 1
                twiceMatched = True
            continue

        if count == 3:
            if threeMatched == False:
                appearsThree = appearsThree + 1
                threeMatched = True
            continue

output = appearsTwice * appearsThree

print(output)
