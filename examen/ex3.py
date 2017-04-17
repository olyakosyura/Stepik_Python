"""
Вам нужно написать класс Difference, который можно создать либо из числа

Difference(5)
либо из двух и более объектов типа Difference :
a = Difference(5)
b = Difference(6)
c = Difference(a, b)
d = Difference(a, b, c)
Так класс должен иметь метод evaluate, который возвращает обратное число в случае, если в объекте хранится число. В случае, если объект был создан из объектов a, b, ..., x, y - результатом будет
a.evaluate() + b.evaluate() + ... + x.evaluate() - y.evaluate()

Ваш код должен выглядеть следующим образом:

class Difference:
    def __init__(self, *args):
        # Создать объект

    def evaluate(self):
        # Вычислить число

К примеру:

a = Difference(5)
print(a.evaluate()) # -5
b = Difference(12)
c = Difference(a, b)
d = Difference(a, b, c)
print(c.evaluate()) # 7
print(d.evaluate()) # -24
print(a.evaluate()) # -5
"""

class Difference:
    def __init__(self, *args):
        # Создать объект
        self.args = args
            

    def evaluate(self):
        # Вычислить число
        if len(self.args) == 1:
            return -self.args[0]
        else:
            n = 0
            
            for arg in self.args:
              
                if type(arg) == "int":
                    n += arg
                else:
                    n +=arg.evaluate()
            return n - 2*self.args[len(self.args)-1].evaluate()

a = Difference(5)

print(a.evaluate()) # -5
b = Difference(12)
c = Difference(a, b)
d = Difference(a, b, c)
print(c.evaluate()) # 7
print(d.evaluate()) # -24
print(a.evaluate()) # -5
