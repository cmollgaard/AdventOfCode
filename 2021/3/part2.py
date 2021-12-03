
import collections

data = open('input1.txt','r').read().split('\n')
print(data[0])

def calc(data: list, targetPref: str, counterIndex: int) -> int:
    
    for i in range(12):
        dataZipped = list(map(list, zip(*data)))
        counter = collections.Counter(dataZipped[i])
        if counter['1'] == counter['0']:
            target = targetPref
        else:
            target = counter.most_common(2)[counterIndex][0]
        data = [x for x in data if x[i] == target]
        if len(data) == 1:
            return int(data[0], 2)

oxygen = calc(data, '1', 0)
CO2 = calc(data, '0', 1)

print(oxygen * CO2)