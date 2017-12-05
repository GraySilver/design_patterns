### 简单工厂模式

要讲简单工厂模式得先讲一点OO原则。

1. OCP（开闭原则，Open-Closed Principle）：一个软件的实体应当对扩展开放，对修改关闭。也就是说，对于一个已有的软件，如果需要扩展，应当在不需修改已有代码的基础上进行。


2. DIP（依赖倒转原则，Dependence Inversion Principle）：要针对接口编程，不要针对实现编程。简单点说，对于不同层次的编程，高层次暴露给低层次的应当只是接口，而不是它的具体类。


3. LoD（迪米特法则，Law of Demeter）：只与你直接的朋友通信，而避免和陌生人通信。

简单工厂模式其实很简单，就是根据工厂的不同参数来生产不同产品。举个简单的栗子，奔驰和宝马都是汽车，我开个汽车厂，调个各配件的参数就可以生产奔驰和宝马了（滑稽）。

```python
"""
利用工厂去包装产品，各个产品由工厂统一生产，然后一同分配给销售端。
"""

# 销售店
class Store:
    def sale(self,ktype):
        f = Factory()
        if isinstance(ktype,str) and ktype in f():
            return f.make_car(ktype)
        else:
            raise ValueError('ktype error')

# 工厂
class Factory:

    def __call__(self):
        return ['baoma','benchi']

    def make_car(self,ktype):
        if ktype == 'baoma':
            return Baoma.__name__
        elif ktype == 'benchi':
            return Benci.__name__
        else:
            raise ValueError('ktype error')
# 宝马
class Baoma:
    def __str__(self):
        return 'baoma'
# 奔驰
class Benchi:
    def __str__(self):
        return 'benchi'

if __name__ == '__main__':

    s = Store()
    print(s.sale('benchi'))
```

简单工厂模式有什么优点呢？如上面的例子，销售侧与产品没有直接建立联系，即调用者没有直接依赖于被调用，当Baoma类Benchi类修改后，不需要对其进行修改而且make_car接口的使用，体现了DIP原则。   

那有什么缺点呢？当对系统进行扩展的时候，比如增加一个Tesla类，不需要修改其他产品类，如Baoma和Benchi，貌似符合OCP原则，但实际上还是需要对工厂类进行修改，所以简单工厂模式不符合OCP原则。                                                            



