import types
import os
import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            log = f'{datetime.datetime.now()} called: {old_function.__name__} with args: {args} {kwargs} result {result}\n'
            file = open(path, 'a')
            file.write(log)
            file.close()
            return result
        return new_function
    return __logger

@logger('main2.log')
def flat_generator(list_of_lists):
    for items in list_of_lists:
        for i in items:
            yield i


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    