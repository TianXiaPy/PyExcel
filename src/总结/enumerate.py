"""
class enumerate(object):
    Return an enumerate object.

      iterable
        an object supporting iteration

    The enumerate object yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.

    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...

第13行代码中的enumerate()是Python的内置函数，
用于将一个可遍历的数据对象（如列表、元组或字符串等）组合为一个索引序列，
可同时得到数据对象的索引及对应的值，一般用在for语句当中。
该函数的语法格式和常用参数含义如下：
enumerate(sequence, start=0)
sequence : 可遍历的数据对象，可以是列表，元组或者字符串等。
start: 索引的起始位置，如果省略，默认为0
"""
path_list = ["a", "b"]
for index, path in enumerate(path_list):
    print(type(enumerate(path_list)))
    print(index, path)
