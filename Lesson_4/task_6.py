# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    for el in range(n):
        result = 1
        for i in range(el+1):
            result *= (i+1)
        yield result


n = 3
for el in fact(n):
    print(el)

#Решение преподавателя
def fibo_gen():
    prev = 1
    result = 1
    while True:
        yield result
        prev += 1
        result *= prev

for idx, itm in enumerate(fibo_gen(), 1): # enumerate это генератор, он не засоряет память. 1 - старт индекса
    print(idx, itm)
    if idx == 15:
        break
