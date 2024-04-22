#Emoji converter (WIP)
message = input('>')
words = message.split(' ')
emoji = {
    ':)' : '😁',
    ':(' : '😒',
    'XD' : '😂'
}
output = ''
for word in words:
    output += emoji.get(word, word) + ' '
print(output)