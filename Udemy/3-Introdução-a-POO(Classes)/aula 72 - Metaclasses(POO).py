"""Metaclasses (POO)
-EM PYTHON TUDO ÉUM OBJETO: Incluído classes
-Metaclass são as "classes" que criam classes.
-type é uma Metaclasses"""


"""
class A:  # Classe/molde da classe
    attr = 'Value'


# Instancias da classes/objetos criados a partir da classe
a = A()
b = A()
c = A()
"""


class Meta(type):
    def __new__(msc, name, bases, namespace):
        if name == 'A':
            return type.__new__(msc, name, bases, namespace)
        if 'b_speak' not in namespace:
            print(f'Hi you need to create the method "b_speak" em {name}')
            # Oi você precisa criar o método b_speak
        else:
            if not callable(namespace['b_speak']):
                print(f'b_speak must be a method, not attribute in {name}')
                # b_speak precisa ser um método, não atributo em

        print(namespace)
        return type.__new__(msc, name, bases, namespace)


class A(metaclass=Meta):
    def speak(self):
        self.b_speak()


class B(A):
    test = 'Value'

    def b_speak(self):
        print('Hello')


b = B()
b.speak()
# Chamamos um método da classe pai e a classe pai chamou um método da classe filho


class Meta1(type):
    def __new__(msc1, name1, bases1, namespace1):
        if name1 == 'C':
            return type.__new__(msc1, name1, bases1, namespace1)
        if 'attr_class' in namespace1:
            del namespace1['attr_class']

        return type.__new__(msc1, name1, bases1, namespace1)


class C(metaclass=Meta1):
    attr_class = 'Value C'


class C1(C):
    attr_class = 'Value C1'


class C2(C):
    attr_class = 'Value C2'


c = C1()
print(c.attr_class)


class Father:
    name = 'Test'


A1 = type(
    'A1',  # Nome da classe
    (Father,),  # Herança
    {'attr': 'Hello World'}  # Atributo
)

a = A1()
print(a.attr)
# Type - É uma MetaClass para criar classes
print(a.name)
