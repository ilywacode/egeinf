# Катя составляет шестибуквенные слова перестановкой букв слова КАПКАН. При этом она избегает слов с двумя подряд одинаковыми буквами.
# Сколько различных кодов может составить Катя?

s = 'КАПКАН'
c = set()

for c1 in s:
    for c2 in s:
        for c3 in s:
            for c4 in s:
                for c5 in s:
                    for c6 in s:
                        t = c1 + c2 + c3 + c4 + c5 + c6
                        if t.count('К') == 2 and t.count('А') == 2 and t.count('П') == 1 and t.count('Н') == 1:
                            if 'АА' not in t and 'КК' not in t:
                                c.add(t)
print(len(c))