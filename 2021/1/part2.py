data = open('input1.txt', 'r').read().split('\n')
print(data[0:3])

def wind(data, i):
    return sum([int(x) for x in data[i:(i+3)]])

print(wind(data, 0))
res = 0

for i in range(len(data)-2):
    if wind(data, i) < wind(data, i+1):
        res += 1

print(res)