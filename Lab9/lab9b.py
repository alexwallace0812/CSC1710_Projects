import statistics
nums = []
cycle = 0
while cycle >= 0 and cycle <= 100:
    cycle = int(input("Please enter an integer 0 to 100, or -1 to stop): "))
    if cycle < 0:
        break
    elif cycle > 100:
        break
    nums.append(cycle)
mean = statistics.mean(nums)
mode = statistics.mode(nums)
median = statistics.median(nums)
print(f"The mean is {mean:.2f}")
print(f"The median is {median}")
print(f"The mode is {mode}")
