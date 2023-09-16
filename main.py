start = 22
end = 58
interval = 3
total = 0

for num in range(start, end + 1, interval):
    total += num*1.05

print(f"The sum of integers from {start} to {end} in intervals of 3 plus 5% saracen interval is:", total)