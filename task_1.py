""" Красильников Илья
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists

    def __str__(self):
        res_matrix = ""
        for el in self.list_of_lists:
            res_str = ""
            for num in el:
                res_str += str(num) + " "
            res_matrix += res_str + '\n'
        return res_matrix

    def __add__(self, other):
        new_list = []
        for index, el in enumerate(self.list_of_lists):
            sum_row = []
            for i, num in enumerate(el):
                sum_row.append(num + other.list_of_lists[index][i])
            new_list.append(sum_row)
        return Matrix(new_list)


mx = Matrix([[1, 1, 2, 3], [1, 1, 1, 3], [1, 1, 2, 3]])
mc = Matrix([[2, 3, 4, 3], [3, 3, 3, 3], [1, 1, 2, 3]])
print(mx)
print(mx+mc)
