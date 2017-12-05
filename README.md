#  白话设计模式


#### 简单工厂模式

[文章详情链接](https://github.com/GraySilver/design_patterns/tree/master/简单工厂)

**优点**：销售侧与产品没有直接建立联系，即调用者没有直接依赖于被调用，当Baoma类Benchi类修改后，不需要对其进行修改而且make_car接口的使用，体现了DIP原则。   

**缺点**：当对系统进行扩展的时候，比如增加一个Tesla类，不需要修改其他产品类，如Baoma和Benchi，貌似符合OCP原则，但实际上还是需要对工厂类进行修改，所以简单工厂模式不符合OCP原则。 

**Example：**

```python
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

