# chapter special method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(interator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(built in) 메소드, 이미 만들어져 있다.

# 기본형
print(dir(int))

n = 10

print(n.__add__(100))
print(n + 10) # 같은 것

print(n * 100, n.__mul__(100))
print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price
    
    def __str__(self):
        return 'Fruit Class info: {}, {}'.format(self._name, self._price)
    
    def __add__(self, x):
        print('called __add__')
        return self._price + x._price
    
    def __sub__(self, x):
        return self._price - x._price
    
    def __le__(self, x):
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        if self._price >= x._price:
            return True
        else:
            return False      

s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

print(s1.__add__(s2), s1 + s2)
print(s1 - s2)
print(s1 >= s2)
print(s1 <= s2)
print(s1)
print(s2)