#Riddhi Rahman's Weight Converter
weight = int(input('Enter your weight : '))
choice = input('L(bs) or (K)g : ')
convert_to =  input('To convert to L(bs) or (K)g? ')
if choice == 'L' or choice == 'l':
    if convert_to == 'L' or convert_to == 'l':
        converted_weight = weight
    elif convert_to == 'K' or convert_to == 'k':
        converted_weight = weight * 0.45
    else:
        print('Invalid choice')
elif choice == 'K' or choice == 'k':
    if convert_to == 'K' or convert_to == 'k':
        converted_weight = weight
    elif convert_to == 'L' or convert_to == 'l':
        converted_weight = weight // 0.45
    else:
        print('Invalid choice')
else:
    print('Invalid choice')
print('Your converted weight is', converted_weight)
