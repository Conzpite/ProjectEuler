import math

hashset = set()
for a in range(2, 101):
    for b in range(2, 101):
        hashset.add(pow(a,b))

print(len(hashset))
