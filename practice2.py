__author__ = 'WangZhe'


#---------------------- generator practice -------------------#

def fibonacci():
    '''
    #purpose#   generator for infinite sequence of Fibonacci numbers
    #return#    a generator object
    #example#   a = fibonacci() => returns a generator object
                a.__next__()    => returns 0
    '''
    a1 = 0
    a2 = 1
    a3 = 0
    while True:
        yield a1
        a3 = a1 + a2
        a1 = a2
        a2 = a3

def limited_yield():
    yield 1
    yield 2
    yield 3

#---------------------- exception practice ---------------------#

def display_age(age):
    while age <= 0:
        try:
            age = int(input('please input your age'))
            if age <= 0:
                print('age must be positive')
        except (EOFError, ValueError):
            print('invalid response')
            raise
        finally:
            print('running finally')
        print('after try-except')

try:
    display_age(-1)
except ValueError:
    print('outer level catching')

open()