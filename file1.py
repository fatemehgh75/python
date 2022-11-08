number = int(input('Enter your number: '))
for i in range(1, number):
    if number % i == 0:
        print(i)
print(number)