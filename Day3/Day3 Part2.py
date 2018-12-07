file = open("input.txt", "r").readlines()

w, h = 1000, 1000
fabric = [[0 for x in range(w)] for y in range(h)]

overlaps = 0

for l in file:
    lineSplit = l.split("@")
    id = lineSplit[0].strip()
    coords = lineSplit[1].strip().split(":")

    xy = coords[0].split(",")
    size = coords[1].strip().split("x")

    x = int(xy[0])
    y = int(xy[1])

    width = int(size[0])
    height = int(size[1])

    heightCounter = 0

    while heightCounter < height:
        line = fabric[y + heightCounter]

        heightCounter = heightCounter + 1

        widthCounter = 0
        while widthCounter < width:
            line[x + widthCounter] = line[x + widthCounter] + 1
            widthCounter = widthCounter + 1

for f in fabric:
        for d in f:
            if d > 1:
                overlaps = overlaps + 1

print(overlaps)

for l in file:
    lineSplit = l.split("@")
    id = lineSplit[0].strip()
    coords = lineSplit[1].strip().split(":")

    xy = coords[0].split(",")
    size = coords[1].strip().split("x")

    x = int(xy[0])
    y = int(xy[1])

    width = int(size[0])
    height = int(size[1])

    heightCounter = 0
    
    unclaimed = True

    while heightCounter < height:
        line = fabric[y + heightCounter]

        heightCounter = heightCounter + 1

        widthCounter = 0
        while widthCounter < width:
            if line[x + widthCounter] > 1:
                unclaimed = False
                break
            widthCounter = widthCounter + 1
        
        if unclaimed == False:
            break

    if unclaimed == True:
        print(id)
        break
