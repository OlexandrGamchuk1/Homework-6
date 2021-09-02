a = str(input())
b = a.split()
list = []
for item in b:
    list.append(len(item))
print(b[list.index(max(list))])
