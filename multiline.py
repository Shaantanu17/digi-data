from dataclasses import dataclass

from pyparsing import line


data = ''

while True:
    line = input("line >>>")
    if not line:
        break
    data += line
print('you have entered a following data')
print(data)