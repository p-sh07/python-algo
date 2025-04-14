import sys

def main():
    num_lines = int(input())
    output_numbers = []
    for i in range(num_lines):
        line = sys.stdin.readline().rstrip()
        value_1, value_2 = line.split()
        value_1 = int(value_1)
        value_2 = int(value_2)
        result = value_1 + value_2
        output_numbers.append(str(result))
    print('\n'.join(output_numbers))

#use main to make variables local, more efficient
if __name__ == '__main__':
    main()

# Весь код программы заключён в функцию main. Это нужно, чтобы код программы
# работал не с глобальными, а с локальными переменными функции main. Обращение
# к локальным переменным оказывается эффективнее.

# Для чтения данных подходит функция input. Но если требуется считать много данных,
# sys.stdin.readline() будет существенно эффективнее. Обратите внимание, что к
# полученной строке мы применили метод rstrip, чтобы отбросить символ перевода
# строки. Функция input это делает автоматически.

# Чтобы преобразовать данные к целым числам, можно было бы воспользоваться этой
# конструкцией:
#  value_1, value_2 = [int(x) for x in line.split()]

# Или этой:
# value_1, value_2 = map(int, line.split())

# Но такие конструкции менее эффективны: при подобной обработке данных программа
# тратит время и ресурсы на создание вспомогательных объектов — массива или объекта
# map, которые не потребуются в дальнейшей работе.

### Template for 'Make' tasks:

import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

def solution(node):
    # Your code
    # ヽ(´▽`)/
    pass

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3

# if __name__ == '__main__':
#     test()


### Example prime numbers:

def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True