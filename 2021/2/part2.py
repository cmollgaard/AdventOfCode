data = open('input1.txt','r').read().split('\n')
#  echo data = data[0]
print(data[0])

horizontal = 0
depth = 0
aim = 0

for line in data:
    command, size = line.split(' ')
    size = int(size)
    if command == 'forward':
        horizontal += size
        depth += aim * size
    elif command == 'down':
        aim += size
    elif command == 'up':
        aim -= size

print(horizontal*depth)