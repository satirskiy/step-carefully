print("hi!")
def int_func(number):
    latin_char = 'yrjrkikwtwetwyrkkul'
    return number.title() if set(number).difference(latin_char) else False

number = input('введите строку из слов с пробелами:').split()
for i in number:
    result = int_func(i)
    if result:
        print(int_func(i), ' ')