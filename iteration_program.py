# Riddhi's iteration program
print('What method do you want to iterate?')
choice = int(input('1. Addition 2. Subtraction 3. Multiplication 4. Division: '))
if choice == 1:
    num = int(input('Enter the number to iterate by addition: '))
    num1 = int(input('Enter the addition number: '))
    num2 = int(input('Enter the end number: '))
    if num2 < num:
        print('The end number cannot be less than the addition number!')
    else:
        while num <= num2:
            print(num)
            num += num1
        print('Done')
elif choice == 2:
    num = int(input('Enter the number to iterate by subtraction: '))
    num1 = int(input('Enter the subtract number: '))
    num2 = int(input('Enter the end number: '))
    if num2 > num:
        print('The end number cannot be bigger than the subtraction number!')
    else:
        while num >= num2:
            print(num)
            num -= num1
        print('Done')
elif choice == 3:
    num = int(input('Enter the number to iterate by multiplication: '))
    num1 = int(input('Enter the multiply number: '))
    num2 = int(input('Enter the end number: '))
    if num2 < num:
        print('The end number cannot be less than the multiplication number!')
    else:
        while num < num2:
            print(num)
            num *= num1
        print('Done')
elif choice == 4:
    num = int(input('Enter the number to iterate by division: '))
    num1 = int(input('Enter the division number: '))
    num2 = int(input('Enter the end number: '))
    if num2 > num:
        print('The end number cannot be bigger than the division number!')
    else:
        while num > num2:
            print(num)
            num /= num1
        print('Done')
else:
    print('Invalid Choice')
