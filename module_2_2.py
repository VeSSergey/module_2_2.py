first_ = int(input('Введите целое число №1 : '))
second_ = int(input('Введите целое число №2 : '))
third_ = int(input('Введите целое число №3 : '))
if first_ == second_ == third_ :
    print(3)
elif first_ == second_ or first_ == third_ or second_ == third_:
    print(2)
else:
    print(0)

