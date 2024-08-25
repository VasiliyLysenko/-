def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

    ''' Вызов функции ниже не работает, выводит ошибку NameError: name 'inner_function' is not defined.
        Did you mean: 'test_function'?
    '''
#inner_function()
    ''' Этот вариант вызова функции ниже выполняется. '''

test_function()

