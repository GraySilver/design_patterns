## 抽象工厂模式

抽象工厂主要是有一个超级工厂来创建小工厂，超级工厂是总部，小工厂是分部。这种类型的设计模式是创建型模式，是一种创建对象的最佳方式。

在抽象工厂模式中，接口是负责创建一个相关对象的小工厂，不需要显式指定工厂类，每个小工厂都可以按照工厂模式提供对象。

### 概要

**目的**：提供一个可以跟类直接交互的接口，而不需要指定具体的类，解决接口选择问题。

**何时使用**：工厂有多条产品链，不只是工厂和产品的关系，例如腾讯有聊天软件这一产品链，旗下产品有QQ、微信等，而我们只需要工厂只生产其中一种产品。

**关键思路**：在一个工厂聚合多个同类产品。

**优点**：当一个产品链中的多个对象被设计一起工作时，它能保证客户端始终只使用同一个产品链的产品。

**缺点**：产品链要扩展很困难，要增加一个系统的某一产品，既要在抽象的接口加代码，也要在具体的产品链中加代码。

**使用场景**：新闻客户端的主题—标签—关键词的层级分类

**特点**：纵向易扩展，横向难扩展。

![](http://www.runoob.com/wp-content/uploads/2014/08/abstractfactory_pattern_uml_diagram.jpg)

### Example:

```python

# -*-coding:utf-8-*-

# 创建一个构造形状Class
# 横向扩展需要修改,纵向扩展不需要
class Shape:
    def drawRectangle(self):
        print('Rectangle')

    def drawCircle(self):
        print('Circle')

    def drawSquare(self):
        print('Square')

# 创建一个构造颜色Class
# 横向扩展需要修改,纵向扩展不需要
class Color:
    def fillRed(self):
        print('Red')

    def fillGreen(self):
        print('Green')

    def fillBlue(self):
        print('Blue')


# 形状Class接口配置
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

# 颜色Class接口配置
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

# 颜色Class和形状Class的抽象接口配置
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
```

