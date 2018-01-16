import sys

map = []
for alphaiter in range(20):
    map.append([])
    for betaiter in range(20):
        map[alphaiter].append("#")
fog = map
for alphaiter in range(20):
    for betaiter in range(20):
        sys.stdout.write(map[alphaiter][betaiter] + "  ")
    print("")
