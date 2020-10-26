a = [[1,2,3],[4,5,6],[7,8,9]]

b = [[c[i] for c in a] for i in range(3)]
print(list([d[f]*2 for d in b] for f in range(3)))