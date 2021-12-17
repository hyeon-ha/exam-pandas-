import sys
a = sys.argv

a.pop(0)
print(a)
a = list(map(int, a))
print(a)
print(sum(a))

# sum = 0
# for i in a:
#     sum += int(i)
# print(sum)