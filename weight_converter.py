#Riddhi Rahman's Weight Converter
weight = int(input('Enter your weight : '))
choice = input('L(bs) or (K)g : ')
if choice == 'L' or choice == 'l':
    convert_to = input('To convert to L(bs) or (K)g? ')
    if convert_to == 'L' or convert_to == 'l':
        converted_weight = weight
        print(f'Your converted weight is {converted_weight} pounds')
    elif convert_to == 'K' or convert_to == 'k':
        converted_weight = weight * 0.45
        print(f'Your converted weight is {converted_weight} kilos')
    else:
        print('Invalid choice')
elif choice == 'K' or choice == 'k':
    convert_to = input('To convert to L(bs) or (K)g? ')
    if convert_to == 'K' or convert_to == 'k':
        converted_weight = weight
        print(f'Your converted weight is {converted_weight} kilos')
    elif convert_to == 'L' or convert_to == 'l':
        converted_weight = weight // 0.45
        print(f'Your converted weight is {converted_weight} pounds')
    else:
        print('Invalid choice')
else:
    print('Invalid choice')
