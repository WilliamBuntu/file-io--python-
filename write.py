import sys
if len(sys.argv) != 2:
    sys.exit(' please provide name')
name = sys.argv[1]

with open('names.txt', 'a') as file:
    file.write(f'{name}\n')
