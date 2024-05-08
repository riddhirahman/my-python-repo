#Emoji converter (WIP)
def emoji_converter(message):
    words = message.split(' ')
    emoji = {
        ':)' : '😁',
        ':(' : '😒',
        'XD' : '😂',
        'love' : '❤️',
        'nice' : '👌'
}
    output = ''
    for word in words:
        output += emoji.get(word, word) + ' '
    return output

message = input('>')
print(emoji_converter(message))