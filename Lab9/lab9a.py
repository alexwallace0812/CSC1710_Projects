num = int(input("Enter a positive integer: "))
for i in range(2, num):
    num%i
    if num%i == 0:
        print(f"{i} is a factor")
