#define height, hash
height = int(input("What height should the pyramid be?"))
hash = "#"

#while loop to get a value within the range
while height < 1 or height > 23:
    height = int(input("Please provide a value within 1 to 23."))

for x in range(height):               #when number within value, create height
    for y in range(height):
        if y > height - (x + 2):
            print(hash, end = " ")
        else:
            print(" ", end = " ")
    print(hash, end = "")
    print()