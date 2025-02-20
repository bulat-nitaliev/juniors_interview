from functools import wraps

'''Необходимо реализовать декоратор @strict Декоратор проверяет соответствие типов
 переданных в вызов функции аргументов типам аргументов, объявленным в прототипе функции.
   (подсказка: аннотации типов аргументов можно получить из атрибута объекта функции 
   func.__annotations__ или с помощью модуля inspect) При несоответствии типов бросать исключение 
   TypeError Гарантируется, что параметры в декорируемых функциях будут следующих типов: 
   bool, int, float, str Гарантируется, что в декорируемых функциях не будет значений параметров, 
   заданных по умолчанию'''

def strict(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        dic = func.__annotations__
        a,b = [type(i) for i in args]
        if dic['a']==a and dic['b']==b:    
            return func(*args,**kwargs)
        raise TypeError('несоответствие типов')
    return wrapper





