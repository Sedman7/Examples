#работа с лямбда функциями

#определим простую лямбду
lf = lambda x: x*2
print(lf(4))  
# => 8

#лямбды с условиями
lif = lambda x, y: x if x > y else y
print(lif(3,7))
# => 7

lif2 = lambda t: 1 if t=='m' else 0
print(lif2('z'), lif2('m'))
# => 0 1

#лямбда со списком
# map() - принимает функцию и список и применяет функцию к каждому элементу списка
my_list = [1, 2, 3, 5]
new_list = list(map(lambda x: x*x, my_list))
print(new_list)
# => 1, 2, 9, 25

my_list = ('m', 'f', 'm', 'f', 'f')
new_list = list(map(lambda x: 0 if x=='m' else 1, my_list))
print(new_list)
# => 0, 1, 0, 1, 1

#filter() - принимает функцию и список и фильтрует все что false
my_list = (1, 2, 4, 7, 10)
new_list = list(filter(lambda x: x%2 == 0, my_list))
print(new_list)

