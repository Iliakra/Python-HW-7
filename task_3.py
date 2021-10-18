""" Красильников Илья
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
"""


class Cell:
    def __init__(self, units):
        self.units = units

    def __str__(self):
        return f"{self.units}"

    def __add__(self, other):
        return Cell(self.units + other.units)

    def __sub__(self, other):
        if self.units - other.units > 0:
            return Cell(self.units - other.units)
        else:
            return "Вычитание невозможно"

    def __mul__(self, other):
        return Cell(self.units * other.units)

    def __floordiv__(self, other):
        return Cell(self.units // other.units)

    def make_order(self, units_row_num):
        res_str = ''
        for i in range(self.units // units_row_num):
            res_str += '*' * units_row_num + '\n'
        res_str += '*' * (self.units % units_row_num) + '\n'
        return res_str


my_cell = Cell(12)
other_cell = Cell(20)
print(my_cell + other_cell)
print(my_cell - other_cell)
print(my_cell * other_cell)
print(my_cell // other_cell)
new_cell = my_cell * other_cell
print(new_cell)

print(other_cell.make_order(7))
