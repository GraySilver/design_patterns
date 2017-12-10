#  白话设计模式

### 简单工厂

[文章链接](https://github.com/GraySilver/design_patterns/tree/master/简单工厂)

**优点**：销售侧与产品没有直接建立联系，即调用者没有直接依赖于被调用，当Baoma类Benchi类修改后，不需要对其进行修改而且make_car接口的使用，体现了DIP原则。   

**缺点**：当对系统进行扩展的时候，比如增加一个Tesla类，不需要修改其他产品类，如Baoma和Benchi，貌似符合OCP原则，但实际上还是需要对工厂类进行修改，所以简单工厂模式不符合OCP原则。 

 ![](http://graysliver.oss-cn-shenzhen.aliyuncs.com/design_patterns/factory_pattern_uml_diagram.jpg)

### 抽象工厂

[文章链接](https://github.com/GraySilver/design_patterns/tree/master/抽象工厂)

**目的**：提供一个可以跟类直接交互的接口，而不需要指定具体的类，解决接口选择问题。

**优点**：当一个产品链中的多个对象被设计一起工作时，它能保证客户端始终只使用同一个产品链的产品。

**缺点**：产品链要扩展很困难，要增加一个系统的某一产品，既要在抽象的接口加代码，也要在具体的产品链中加代码。

![](http://graysliver.oss-cn-shenzhen.aliyuncs.com/design_patterns/abstractfactory_pattern_uml_diagram.jpg)

