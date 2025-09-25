from cs50 import get_float

# initializing change and coin
change = 0
coins = 0

# to get a float value
while change <= 0:
    change = get_float("Change: ")

# reducer function to subtract coins


def reducer(valueToReduce):
    global change
    global coins
    while (change >= valueToReduce):
        change = round(change - valueToReduce, 10)
        coins += 1


reducer(0.25)
reducer(0.10)
reducer(0.05)
reducer(0.01)

# to show total number of coins
print(coins)
