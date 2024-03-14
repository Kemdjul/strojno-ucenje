a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(max(c))
c[0] = 7
c.pop()
for number in c:
    print('List number ', number)
    print('Done!')