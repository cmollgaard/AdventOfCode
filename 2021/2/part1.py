data = open('input1.txt','r').read().split('\n')
#  echo data = data[0]
print(data[0])

h = 0
d = 0

for line in data:
    command, size = line.split(' ')
    size = int(size)
    if command == 'forward':
        h += size
    elif command == 'down':
        d += size
    elif command == 'up':
        d -= size
    else:
        h -= size

print(h*d)