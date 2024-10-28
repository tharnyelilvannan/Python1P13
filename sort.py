# Author: Tharny Elilvannan
# Last Updated: October 28, 2024
# Purpose: Sorts numbers in a small list.

num = [100, 9, 4, 1010, 3, 55, 234, 943]
newNum = []

for i in range(len(num)):

    if (i + 1 == len(num)):
        break
    else:
        if (num[i] > num[i+1]):
            bigger = num[i]
            num[i] = num[i+1]
            num[i+1] = bigger

print(num)