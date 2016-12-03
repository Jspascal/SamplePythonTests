tab = [2,5,9,3,7,15,20,17,35,1]

for el in tab :
    print(el)

print("tableau trie : ")

n = len(tab)
for i in range(n) : # on cherche k tel que ak = min(aj )ji
    k = i
    for j in range(i+1,n) :
        if tab[k] > tab[j] : k = j
        tab[k],tab[i] = tab[i],tab[k]

for el in tab :
    print(el)
