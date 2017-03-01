def extract_avg(json):
    try:
        return json['avg']
    except KeyError:
        return 0


dict = {}
arr = []
res = 0

with open("p079_keylog.txt") as f:
    for line in f.read().split("\n"):
        for i in range(len(line)):
            c = line[i]
            if c not in dict:
                dict[c] = {'char': int(c), 'pos':[]}
            dict[c]['pos'].append(i)

    for c in dict:
        dict[c]['avg'] = 0.0
        for pos in dict[c]['pos']:
            dict[c]['avg'] += pos
        dict[c]['avg'] /= len(dict[c]['pos'])
        arr.append(dict[c])

    arr.sort(key=extract_avg, reverse=False)

    for obj in arr:
        res *= 10
        res += obj['char']
        
print res
