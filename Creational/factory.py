class ShapeInterface:
    def draw(self):
        pass


class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")


class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")


class ShapeFactory:
    @staticmethod
    def get_shape(type):
        if type == "circle":
            return Circle()
        if type == "square":
            return Square()
        assert 0, 'Could not find shape ' + type


s = ShapeFactory.get_shape('square')
s.draw()
c = ShapeFactory.get_shape('circle')
c.draw()
#e = ShapeFactory.get_shape('triangle')


