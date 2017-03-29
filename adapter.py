class Korean:
    """Korean speaker"""
    def __init__(self):
        self.name = "Korean"

    def speak_korean(self):
        return "An-neyong"


class British:
    """English speaker"""
    def __init__(self):
        self.name = "British"

    def speak_english(self):
        return "Hello"


class Adapter:
    """This changes the generic method name to individualized method names"""
    def __init__(self, object, **adapted_method):
        self._object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, item):
        return getattr(self._object, item)


objects = []

k = Korean()
b = British()

objects.append(Adapter(k, speak=k.speak_korean))
objects.append(Adapter(b, speak=b.speak_english))

for obj in objects:
    print("{} says '{}'\n".format(obj.name, obj.speak()))
