from copy import deepcopy


class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d" % self.__wheels[0].size)

    def clone(self):
        return deepcopy(self)


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        body = self.__builder.get_body()
        car.set_body(body)

        engine = self.__builder.get_engine()
        car.set_engine(engine)

        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)
            i += 1

        return car


class BuilderInterface:
    def get_wheel(self): pass

    def get_engine(self): pass

    def get_body(self): pass


class JeepBuilder(BuilderInterface):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body


class MazdaBuilder(BuilderInterface):
    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 109
        return engine

    def get_body(self):
        body = Body()
        body.shape = "sedan"
        return body


d = Director()
d.set_builder(MazdaBuilder())
mazda = d.get_car()
mazda.specification()

mazda2 = mazda.clone()
mazda2.specification()

