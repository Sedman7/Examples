#
#  Алгоритм бинарного поиска
#  дополнено поиском наиболее ближзкого элемента в случае
#  если искомое значение не найдено
#

#создадим процедуру поиска
def binary_search(list, item):
	low = 0 					#задаем границы поиска
	high = len(list) - 1		#изначально весь массив
	
	while low <= high:
		mid = round((low + high)/2)	#берем средний элемент
		guess = list[mid]		#если он вдруг дробный то python округлит его в меньшую сторону
		#print(str(mid), ' (', str(list[mid]), ')')
		if guess == item:
			return mid
		if guess < item:
			low = mid + 1
		if guess > item:
			high = mid - 1
	return mid

data = [1, 2, 5, 8, 10, 12, 17, 20, 25, 30, 31, 34, 40, 42]

g = 0
while g !=999:
	g = int(input('\nВведите число для поиска: '))

	search_res = binary_search(data, g)
	print("список для поиска: ", data)
	if data[search_res] == g:
		print("Заданное число", str(g)," найдено в позиции: ",search_res)
	else:
		#если число не найдено то ищем ближайшее
		#определяем наиболее подходящее из 2-х крайних относительно того, но котором остановились
		#проверяем чтобы не выйти за левую границу массива
		if search_res > 0:
			lval = search_res - 1
		else:
			lval = search_res
			
		#проверяем чтобы не выйти за правую границу массива	
		if search_res + 1 <= len(data)-1:
			rval = search_res + 1
		else:
			rval = search_res
		
		#определяем наименьшее отклонение слева и справа от места где остановился поиск	
		if abs(data[lval] - g) < abs(data[rval] - g):
			smallest = lval
		else:
			smallest = rval
			
		#определяем наименьшее из 2-х предыдущих и текущего
		if abs(data[search_res] - g) < abs(data[smallest] - g):	
			print("Заданное число", str(g)," не найдено, ближайшее к нему: ", data[search_res])
		else:
			print("Заданное число", str(g)," не найдено, ближ айшее к нему: ", data[smallest])
