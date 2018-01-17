import sys

map = []
for alphaiter in range(40):
    map.append([])
    for betaiter in range(40):
        map[alphaiter].append("#")
fog = map
for alphaiter in range(40):
    for betaiter in range(40):
            sys.stdout.write(map[alphaiter][betaiter] + "  ")
    print("")
