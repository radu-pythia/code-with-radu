prev = 1
cur = 1

cat = int(input('cate: '))

if cat == 1:
    print(prev)
elif cat == 2:

    print(cur)
else:
 for _ in range(cat-2):
    next = prev + cur
    prev = cur
    cur = next

print(next)
    

