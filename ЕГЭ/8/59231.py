# id: 59231

s = 'ОЛЬГА'
k = 0
for c1 in s:
    for c2 in s:
        for c3 in s:
            for c4 in s:
                for c5 in s:
                    t = c1 + c2 + c3 + c4 + c5
                    if t[0] != 'Ь' and not 'ОЬ' in t and not 'АЬ' in t:
                        if t.count('О') == 1 and t.count('Л') == 1 and t.count('Ь') == 1 and t.count('Г') == 1 and t.count('А') == 1:
                            k += 1
print(k)

# output: 48