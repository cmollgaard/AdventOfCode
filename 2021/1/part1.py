data = open('input1.txt','r').read().split('\n')
print(data[0])
res = 0

for i in range(len(data)-1):
    if data[i] < data[i+1]:
        res += 1

print(res)