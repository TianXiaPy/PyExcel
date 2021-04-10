"""
class enumerate(object):
    Return an enumerate object.

      iterable
        an object supporting iteration

    The enumerate object yields pairs containing a count (from start, which
    defaults to zero) and a value yielded by the iterable argument.

    enumerate is useful for obtaining an indexed list:
        (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
"""
path_list = ["a", "b"]
for index, path in enumerate(path_list):
    print(type(enumerate(path_list)))
    print(index, path)
