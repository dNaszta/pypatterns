class Singleton:
    __instance = None
    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


x = Singleton()
x.val = 'Burger'
y = Singleton()
y.val = 'Chips'
print(x.val)
print(x == y)
