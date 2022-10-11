import csv

with open('ads.csv', 'r') as f:
    a = list(csv.reader(f))
    print(a)


s = []
s2 = []
for i in a:
    s.append(i[2])
    s2.append(i[5])

print(s)
print(len(s))
sa = set(s[1:])
sa2 = set(s2[1:])
print(sa)


with open('people.csv', 'w') as f:
    sd = csv.writer(f)
    people_dict = {}
    for i, j in enumerate(list(sa)):
        sd.writerow([i + 1, j])
        people_dict[j] = str(i + 1)

with open('address.csv', 'w') as f:
    sd = csv.writer(f)
    address_dict = {}
    for i, j in enumerate(list(sa2)):
        sd.writerow([i + 1, j])
        address_dict[j] = str(i + 1)


with open('all_ads.csv', 'w') as f:
    sd = csv.writer(f)
    for i in a[1:]:
        i[2] = people_dict[i[2]]
        i[5] = address_dict[i[5]]
        sd.writerow(i)

