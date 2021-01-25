def my_f(x, y):
    try:
       x, y = float(x), int(y)
       if x <= 0 or y >= 0:
          return 'не верное значение:\nx должен быть больше 0\ny должен быть меньше 0'
       else:
           result = 1
           for _ in range(abs(y)):
               result /= x
           return f'Результат: {round(result, 6)}'
    except ValueError:
        return "неверные данные"

number1 = input("введите действительное положительное число, x =")
number2 = input("Введите целое отрицательное число, y =")
print(my_f(number1, number2))

            




