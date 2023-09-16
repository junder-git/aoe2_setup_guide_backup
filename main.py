start = 70
end = 100
interval = 3
total = 0

for num in range(start, end + 1, interval):
    total += num

print("The sum of integers from 70 to 100 in intervals of 3 is:", total)