# Read the input for number of sides each dice has

n = int(input())

# Convert to list both dices

dice1 = input().split()

dice2 = input().split()

# Start comparing every side of the first dice with all the sides and add 1 if the side is bigger in every case
sum1= 0
sum2= 0
for i in dice1:
    for j in dice2:
        if int(i) > int(j):
            sum1 += 1
        elif int(j) > int(i):
            sum2 += 1

if sum1 > sum2:
    print("first")
elif sum1 < sum2:
    print("second")
else:
    print("tie")