#Порівняння двох чисел
a=int(input("enter your number a "))
b=int(input("enter your number b "))
if a>b:
    print("a>b")
else:
    print ("a<b")
#Перевірка на парність числа
a = int(input("Enter_your_number "))
if a%2==0:
    print("Парне")
else:
    print("Непарне")  
#Знаходження факторіалу         
n = int(input("Введіть число,факторіал якого ви хочете визначити "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1 
print(factorial)