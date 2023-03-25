text_file = open('/Users/emily/text.txt', 'w')
text_file.write('this is my test file')
text_file.close()

text_file = open('text.txt')
print(text_file.read())