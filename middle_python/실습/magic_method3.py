# chapter special method
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(interator), 함수(Functions), 클래스(Class)
# 클래스 안에 정의할 수 있는 특별한(built in) 메소드, 이미 만들어져 있다.

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value


# 루트를 씌어줌
from math import sqrt

def distance(pt1, pt2):
    l_len = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
    return l_len

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)
print(distance(pt1, pt2))
# 네임드 튜플 사용
from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3, pt4)
print(distance(pt3, pt4))

Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # default는 false이다.

print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, 20)
p4 = Point4(10, 20, 30, 40)
p5 = Point2(**temp_dict)

print(p1)
print(p2)
print(p3)
print(p4) # Point(x=10, y=20, _2=30, _3=40) 알아서 변수를 만들어준다.
print(p5)

print(p1[0] + p2[1], p1.x + p2.y)
temp = [52, 38]

# _make() 새로운 객체를 생성
p1 = Point1._make(temp)
print(p4)

# _field 필드 네임 확인
print(p1._fields)

# _asdict(): OrderedDict를 반환
print(p1._asdict())

# 실 사용 실습
# 반 20명, 4개의 반(a, b, c, d)

Classes = namedtuple('classes', 'rank, number')
numbers = [str(i) for i in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(students)

students2 = [
    Classes(rank, number)
    for rank in 'A B C D'.split()
    for number in [ str(n)
        for n in range(1, 21)
    ]
]
print(len(students2))