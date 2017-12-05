


class Store:
    def sale(self,ktype):
        f = Factory()
        if isinstance(ktype,str) and ktype in f():
            return f.make_car(ktype)
        else:
            raise ValueError('ktype error')



class Factory:

    def __call__(self):
        return ['baoma','benci']

    def make_car(self,ktype):
        if ktype == 'baoma':
            return Baoma.__name__
        elif ktype == 'benci':
            return Benci.__name__
        else:
            raise ValueError('ktype error')

class Baoma:

    def __str__(self):
        return 'baoma'

class Benci:

    def __str__(self):
        return 'benci'

if __name__ == '__main__':

    s = Store()
    print(s.sale('benci'))