# user input
change = float(input("How much change is owed?"))

while change < 0:
    change = float(input("Please give a valid input. How much change is owed?"))

#convert float to int
change = int(change*100)

#define list and total number of coins given
coins = [25, 10, 5, 1]
total = 0

#go through the list
x = 0
for x in range(len(coins)):
    if change >= coins[x]:
        total += change // coins[x]
        change = change - change // coins[x] * coins[x]
        x += 1



print(f"total is {total} coins.")