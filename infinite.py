from collections.abc import Iterable


class InfList(list):
    class Undefined:
        pass

    __it = []  # Empty List
    __created = False  # Recursion Flag

    def __init__(self, v=Undefined):
        super().__init__()
        # Not Recursive __init__()
        if v is not self.Undefined:
            if isinstance(v, Iterable):
                self.__it = [self.__new__(type(self))] + v
            else:
                self.__it = [self.__new__(type(self)), v]
            self.__created = True  # Update Recursion Flag

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise IndexError

        if not self.__created:
            self.__created = True
            self.__it = [self.__new__(type(self))]
            return self.__it[item]
        return self.__it[item]

    def __iadd__(self, other):
        print(other, self.__created, self.__it)
        if self.__created:
            self.__it = self.__it + other
        else:
            self.__it = [self.__new__(type(self))] + other

    def __add__(self, other):
        if self.__created:
            return self.__it + other
        else:
            return [self.__new__(type(self))] + other

    def __iter__(self):
        return self.__it

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise IndexError()

        if key == 0:
            # 0s Index Is Always A Inf
            if not isinstance(value, Iterable):
                value = [value]

            if not self.__created:
                self.__created = True
                self.__it = [self.__new__(type(self))] + value
            else:
                self.__it = self.__it[0] + value
        else:
            self.__it[key] = value

    def __repr__(self):
        return f"{self.__it}"
