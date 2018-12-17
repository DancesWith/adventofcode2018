file = open("C:\\Users\\alexw\\Documents\\adventofcode2018\\Day5\\input.txt").readlines()

l = file[0]

characters = list(l)

notFinished = True

while notFinished:
    index = 0

    print(len(characters))

    for c in characters:
        
        index += 1
        if index >= len(characters):
            notFinished = False
            break

        if c.lower() == characters[index].lower():

            if c.isupper() and characters[index].islower():
                del characters[index]
                del characters[index - 1]
                break
            elif c.islower() and characters[index].isupper():
                del characters[index]
                del characters[index - 1]
                break

print(len(characters))
        