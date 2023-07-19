#работа со словарями

#создаем словарь используя синтаксис {}
my_dict = {"Car":"Ford",
		   "Model":"Focus",
		   "Value":3500,
		   "Year":1970, #дубликаты ключей не работаю
		   "Year":1980  #если будет дублироваться ключ - то буде обновлено значение
		  }

#создаем словарь используя метор dict()
dict2 = dict(Car = "Subaru",
			 Model = "Legacy",
			 Value = 2000,
			 Year = 1999 
			)

print(type(my_dict))  #посмотрим какой присвоился класс
print(my_dict)
print(dict2)
print()

#получаем значение по ключу, два способа:
old_car = my_dict["Car"]
mod_car = my_dict.get("Model") 
print(old_car,"-", mod_car)
print()

#добавим элемент в список
my_dict["Color"] = "Blue"

#изменим элемент, 2 способа
my_dict["Model"] = "Model T"
my_dict.update({"Car":"Tesla"})  #если такого ключа нет - будет создан

#получаем список ключей, значений и пар ключ-значение
k = my_dict.keys()
v = my_dict.values()
p = my_dict.items()
print("\n", k, "\n", v, "\n\n", p)
print()

#проверяем наличие элементов
if "Model" in my_dict:	#по умолчанию идет проверка по ключу
	print("Tag 'Model' is already in dictionary...")


