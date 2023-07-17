
#создадим процедуру поиска
def binary_search(list, item):
	low = 0 					#задаем границы поиска
	high = len(list) - 1		#изначально весь массив
	
	while low <= high:
		mid = round((low + high)/2)	#берем средний элемент
		guess = list[mid]		#если он вдруг дробный то python округлит его в меньшую сторону
		print(str(mid), ' (', str(list[mid]), ')')
		if guess == item:
			return mid
		if guess < item:
			low = mid + 1
		if guess > item:
			high = mid - 1
	return None

data = [1, 2, 5, 8, 10, 12, 17, 20, 25, 30, 31, 34, 40, 42]

s = binary_search(data, 18)

print(s) 
