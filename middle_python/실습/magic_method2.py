# chapter special method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(interator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(built in) 메소드, 이미 만들어져 있다.

# 클래스 예제2

class Vector:
    def __init__(self, *args) -> None:
        '''
        Create a vector, example v = Vector(5, 10)
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self) -> str:
        '''
        Return the vector information
        '''
        return 'Vector(%r, %r)' % (self._x, self._y)
    
    def __add__(self, v):
        '''
        Return the vector addition of self and other
        '''
        return Vector(self._x + v._x, self._y + v._y)
    
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)
    
    def __bool__(self):
        return bool(max(self._x, self._y))
    
# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 25)
v3 = Vector()

print(Vector.__init__.__doc__)
print(v1, v2 ,v3)
print(v1 + v2)
print(v1 * 3)
print(bool(v1))
print(bool(v3))