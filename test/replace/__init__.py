f = open('1.txt', 'r', encoding='utf8')
a = f.read().replace('(1560', '(1561')
a = a.replace('-09-29', '-09-28')
f.close()

f = open('1.txt', 'w', encoding='utf8')
f.write(a)
f.close()
