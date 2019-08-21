import randomSeating

def main():
    filePath = input("Enter the file path of ID's: ")
    nums = open(filePath, 'r')

    roll_no = []

    for n in nums:
        roll_no.append(n.strip())

    nums.close()

    randomSeating.arrangeSeating(roll_no)

if __name__ == "__main__":
    main()
