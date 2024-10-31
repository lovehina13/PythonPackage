# coding: utf-8


class MyClass:

    def __init__(self, value=int()):
        self._value = value

    def __str__(self):
        return str(self.__dict__)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @staticmethod
    def read():
        import pkg_resources
        file = pkg_resources.resource_filename("PythonPackage", "MyResources/MyFile.txt")
        return open(file, "r", encoding="utf-8").readlines()
