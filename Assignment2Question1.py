sum = 0
i = int(input("enter limit: "))

try:
    for num in range(0, i+1):
        if num % 3 == 0:
            sum = sum + num
        elif num % 5 == 0:
            sum = sum + num
    print(sum)

except:
    exit()