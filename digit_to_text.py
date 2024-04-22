#Riddhi's Digit-to-Letter converter
digit = input('Your Digit: ')
digit_map = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten'
}
output = ''
for ch in digit:
    output += digit_map.get(ch, 'Null') + ' '
print(output)