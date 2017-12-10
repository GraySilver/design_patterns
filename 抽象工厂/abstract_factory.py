# -*-coding:utf-8-*-


# 形状
# 横向扩展需要修改,纵向扩展不需要
class Shape:
    def drawRectangle(self):
        print('Rectangle')

    def drawCircle(self):
        print('Circle')

    def drawSquare(self):
        print('Square')

# 颜色
# 横向扩展需要修改,纵向扩展不需要
class Color:
    def fillRed(self):
        print('Red')

    def fillGreen(self):
        print('Green')

    def fillBlue(self):
        print('Blue')


# 形状接口配置
# 横向扩展需要修改,纵向扩展不需要
class ShapeFactory:
    def getShape(self,shape):
        s = Shape()
        if shape == 'rectangle':
            s.drawRectangle()
        elif shape == 'circle':
            s.drawCircle()
        elif shape == 'square':
            s.drawSquare()
        else:
            raise ValueError('shape error')

# 颜色接口配置
# 横向扩展需要修改,纵向扩展不需要
class ColorFactory:
    def getColor(self,color):
        c = Color()
        if color == 'red':
            c.fillRed()
        elif color == 'green':
            c.fillGreen()
        elif color == 'blue':
            c.fillBlue()
        else:
            raise ValueError('color error')

# 颜色和形状的抽象接口配置
class AbstractFactory:

    def getShape(self,shape):
        sf = ShapeFactory()
        return sf.getShape(shape)

    def getColor(self,color):
        cf = ColorFactory()
        return cf.getColor(color)


# 调用接口，生产
class FactoryProducer:

    def fprint(self):
        af = AbstractFactory()
        af.getColor('blue')
        af.getShape('square')


if __name__ == '__main__':
    fp = FactoryProducer()
    fp.fprint()