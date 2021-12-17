
import time

if __name__ == "__main__":
    # a = 0
    # b = 2
    #
    # if a != 0:
    #     c = b / a
    # else : c = 'infinity'
    # print(c)
    start_time = time.time()
    a = [1,2,3]
    b = 4
    try:
        print('before')
        c = b / a[3]
        print('after')

    except ZeroDivisionError:
        c = 'infinity'
    except IndexError as e:
        #c = 'infinity'
        print(e)
    finally:
        try:
            print(c)
        except NameError:
            print('c가 없습니다.')

    character = chr(97)
    print(character)

    a = [1,2,3]
    print(type(a))
    print(dir(a))
    b = 10
    print(type(b))
    enum_a = enumerate(a)
    print(enum_a)
    print(list(enum_a))

    class Person:
        pass

    a = Person()
    print(isinstance(a, Person))


    a = [1,2,3]
    b = list(a)
    print(id(a))
    print(id(b))

    def celsius_to_faherenheit(c):
        return c * 1.8 + 32
    celsius_data = [12, 23, 21, 19, 23]
    print(list(map(celsius_to_faherenheit, celsius_data)))

    print(list(map(lambda c : c * 1.8 + 32, celsius_data)))

    print(list(zip([1,2,3], [4,5,6])))
    a = [1,2,3]
    b = [4,5,6,7]
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    print(c)
    c = []
    for x, y in zip([1,2,3], [4,5,6,7]):
        c.append(x + y)
        print(x + y)
    print(c)

    import sys
    print(sys.path)

    import os
    print(os.getcwd())

    import time
    print(time.localtime(time.time()))

    print(time.ctime())
    end_time = time.time()
    print(end_time - start_time)

    import random
    print(random.randint(1,6))

    import webbrowser
    print(webbrowser.open_new('http://google.com'))