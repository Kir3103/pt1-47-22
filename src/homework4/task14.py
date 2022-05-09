"""
Создайте декоратор, который вызывает задекорированную функцию пока она не выполнится без исключений
(но не более n раз - параметр декоратора). Если превышено количество попыток, должно быть возбуждено
исключение типа TooManyErrors.
Т.е. если во время работы функции возникло какое-то исключение, то функция должна перезапуститься
еще раз. Количество перезапусков ограничено параметром декоратора.
"""


class TooManyErrors(Exception):
    """Exception class showing exceeding the number of tries"""
    pass


def parametrized_dec(numb_try):
    """Calls the function until it is complete without exceptions

    :param numb_try: number of attempts to restart the function
    """

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for quant_try in range(1, numb_try + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if quant_try == numb_try:
                        raise TooManyErrors(f'Number of attempts exceeded: {numb_try} ')
        return wrapper
    return my_decorator


@parametrized_dec(3)
def count(numb):
    counter = 0
    for elem in range(numb + 1):
        if elem > counter:
            counter += ''
    return counter


if __name__ == '__main__':
    print(count(6))
