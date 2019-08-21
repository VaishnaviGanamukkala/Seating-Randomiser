import random

def arrangeSeating(roll_no):
    arrangement = []
    while roll_no:
        index = random.randint(0, len(roll_no) - 1)
        arrangement.append(roll_no[index])
        roll_no.pop(index)

    seating = open("seating.txt", "w+")

    for (index, n) in enumerate(arrangement):
        s = str(index + 1) + " " + n + "\n"
        seating.write(s)

    seating.close()
