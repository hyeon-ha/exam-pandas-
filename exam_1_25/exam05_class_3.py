# -*- coding: utf-8 -*-
"""exam05_class_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19GO2yZ7ncnx3EnlaXlEg4L-0KaGhjIoq
"""

class calculator:
    def __init__(self):
        self.result = 0
        self.PI = 3.14
    def add(self, number1, number2):
        return number1 + number2
    def sub(self, number1, number2):
        return number1 - number2
    def mul(self, number1, number2):
        return number1 * number2
    def div(self, number1, number2):
        return number1 / number2

class new_calculator(calculator):
    def new_div(self, number1, number2):
        if number2 == 0:
            return 'infinity'
        else : return number1 / number2

class edited_calculator(calculator):
    def div(self, number1, number2):
        if number2 == 0:
            return 'infinity'
        else:
            return number1 / number2

if __name__ =="__main__":
    cal_1 = calculator()

    cal_1.result = cal_1.add(10, 20)
    print(cal_1.result)

    sub = cal_1.sub(4, 2)
    print(sub)

    div = cal_1.div(4, 2)
    print(div)

    cal_2 = calculator()
    cal_2.result = cal_2.add(30, 40)
    print(cal_2.result)

    cal_3 = calculator()
    print(cal_3.result)
    print(cal_1.result)



    new_cal_1 = new_calculator()
    print(new_cal_1.new_div(3,0))

    print(new_cal_1.add(10, 20))



    edited_cal_1 = edited_calculator()
    print(edited_cal_1.div(4, 0))

    class Family:
        lastname = '김'
        def __init__(self, firstname):
            self.firstname = firstname
        def print_name(self):
            print(self.firstname, end=' ')
            print(Family.lastname)

    big = Family('길동')
    big.print_name()
    print(big.lastname)

    little = Family('삿갓')
    little.print_name()
    print(little.lastname)

    print(Family.lastname)

    #print(Family.firstname)

    Family.lastname = '박'

    big.print_name()

    print(id(Family.lastname))
    print(id(big.lastname))
    print(id(little.lastname))

    big.lastname = '최'
    print(big.lastname)
    print(little.lastname)
    print(Family.lastname)

    a = 10
    b = a
    b = 20

    print(a)

    a = [1,2,3]
    b = a
    b[1] = 4
    print(a)

    a = a + [5,6,7]
    print(b)

    print(a)
    print(id(a))
    print(id(b))

    a = [1,2,3]
    b = a
    a.extend([5,6,7])
    print(b)
    print(id(a))
    print(id(b))

    b = a.extend([5,6,7])
    print(a)
    print(id(a))
    print(id(b))