file = open("input.txt", "r").readlines()

output = 0

for l in file:
    output = output + int(l)

print(output)
