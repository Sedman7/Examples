
lst = {'one':1, 'two':2, 'txt':'text'}
sex = ['m', 'f', 'f', 'm', 'f']

new_sex = list(lambda x: 0 if x=='m' else 1, sex)
print(new_sex)

lf = lambda x: x*x
l = lf(4)
print (l)

for a in sex:
	print(a)

my_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x == 4) , my_list))
print(new_list)

for a in lst:
	print(lst[a])

print(lst['one'])

