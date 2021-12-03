data = open('input1.txt','r').read().split('\n')
#  echo data = data[0]
print(data[0])

data = list(map(list, zip(*data)))
# print(len(data))

import collections
data = [collections.Counter(x) for x in data]
print(data)

epsilon = [c.most_common(2)[0][0] for c in data]
epsilon = ''.join(epsilon)
epsilon = int(epsilon, 2)


gamma = [c.most_common(2)[1][0] for c in data]
gamma = ''.join(gamma)
gamma = int(gamma, 2)
print(epsilon, gamma)
print(gamma * epsilon)