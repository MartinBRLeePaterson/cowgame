randtest = []
for goes in range(100):
    """
    TRAITS FOR TESTING
    000000:000000
    x/y
    Black/Red
    Poll/Horns
    Short Hair/Fluffy
    Favourite Number 1
    Favourite Number 2
    """
    import random

    mother = "0"
    father = "0"
    for goes in range(11):
        if not goes == 5:
            mother += str(random.randint(0, 1))
            father += str(random.randint(0, 1))
        else:
            mother += "0"
            father += "1"
    print(mother)
    print(father)
    mothergene = ""
    fathergene = ""
    for goes in range(6):
        if random.randint(0, 1) == 0:
            mothergene = mothergene + mother[goes]
        else:
            mothergene = mothergene + mother[goes + 6]
        if random.randint(0, 1) == 0:
            fathergene = fathergene + father[goes]
        else:
            fathergene = fathergene + father[goes + 6]
    endcont = mothergene + fathergene
    print(endcont)
    if endcont[6] == "0":
        print("The calf is male")
    else:
        print("The calf is female")
    traitarray = [
        ["Black", "Red", "The calf's fur is "],
        ["No Horns", "Horns", "The calf has "],
        ["Short", "Fluffy", "The calf's fur is "],
    ]
    numbertable = [
        ["1", "2"],
        ["3", "4"]
    ]
    for goes in range(3):
        if endcont[goes + 1] < endcont[goes + 7]:
            print(traitarray[goes][2] + traitarray[goes][int(endcont[goes + 1])])
        else:
            print(traitarray[goes][2] + traitarray[goes][int(endcont[goes + 7])])
    digit = [0, 0]
    if int(str(endcont)[4]) < int(str(endcont)[10]):
        digit[0] = int(str(endcont)[4])
    elif int(str(endcont)[10]) < int(str(endcont)[4]):
        digit[0] = int(str(endcont)[10])
    elif int(str(endcont)[4]) == int(str(endcont)[10]):
        digit[0] = int(str(endcont)[4])
    if int(str(endcont)[5]) < int(str(endcont)[11]):
        digit[1] = int(str(endcont)[5])
    elif int(str(endcont)[11]) < int(str(endcont)[5]):
        digit[1] = int(str(endcont)[11])
    elif int(str(endcont)[5]) == int(str(endcont)[11]):
        digit[1] = int(str(endcont)[5])
    print(digit)
    print("The calf's favourite number is " + numbertable[digit[0]][digit[1]])
    randtest.append(int(numbertable[digit[0]][digit[1]]))
print(randtest)
