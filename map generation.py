import sys

map = []
for alphaiter in range(41):
    map.append([])
    if alphaiter%2 == 0:
        for betaiter in range(41):
            map[alphaiter].append("W")
    else:
        for betaiter in range(41):
            if betaiter%2 == 0:
                map[alphaiter].append("W")
            else:
                map[alphaiter].append("#")
fog = map
for alphaiter in range(41):
    for betaiter in range(41):
            sys.stdout.write(map[alphaiter][betaiter] + "  ")
    print("")
