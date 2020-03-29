#Добуток цифр натурального числа
my_num=9876
my_num=str(my_num)
my_result2=int(my_num[0])*int(my_num[1])*int(my_num[2])*int(my_num[3])
print(my_result2)
#Реверсне число до попереднього добутку
n1 = my_result2
n2 = 0
while n1 > 0:
	digit = n1 % 10
	n1 = n1 // 10
	n2 = n2 * 10 
	n2 = n2 + digit 
print("Реверсне чило :",n2)
#Посортований кінцевий результат
a = str(n2)
b = list(a)
b.sort()
print("Sorted:",b)




